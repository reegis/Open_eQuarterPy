import pandas as pd
import numpy as np

from mole.stat_corr import window_wall_ratio_AVG_by_building_age_lookup
from mole.stat_corr import common_walls_by_population_density_corr
from mole.stat_corr import present_base_uvalue_AVG_by_building_age_lookup
from mole.stat_corr import contemporary_base_uvalue_by_building_age_lookup
from mole.stat_corr import present_wall_uvalue_AVG_by_building_age_lookup
from mole.stat_corr import contemporary_wall_uvalue_by_building_age_lookup
from mole.stat_corr import present_window_uvalue_AVG_by_building_age_lookup
from mole.stat_corr import contemporary_window_uvalue_by_building_age_lookup
from mole.stat_corr import present_roof_uvalue_AVG_by_building_age_lookup
from mole.stat_corr import contemporary_roof_uvalue_by_building_age_lookup


def add_col(df, colname):
    if colname not in df:
        df[colname] = None
    return df


def evaluate_building(data, **kwargs):
    """Calculating the heat demand of a building based on the calculations of
    the Open_eQuarter qgis plugin.

    Parameters
    ----------
    data : pandas.DataFrame
        Containing the known values as columns.

    Returns
    -------
    pandas.DataFrame
        Containing the calculated values as columns.
    """
    p = pd.DataFrame()

    # Set default values
    p.ratio_solar_available = kwargs.get('ratio_solar_available', 0.5)
    p.ratio_solar_installable = kwargs.get('ratio_solar_installable', 0.5)
    p.solar_earnings_per_sqm = kwargs.get('solar_earnings_per_sqm', 300)
    p.average_heat_demand_per_sqm = kwargs.get(
        'average_heat_demand_per_sqm', 120)
    p.heating_degree_days = kwargs.get('heating_degree_days', 2750)
    p.default_average_build_year = kwargs.get(
        'default_average_build_year', 1950)
    p.default_population_density = kwargs.get(
        'default_population_density', 10000)
    p.default_accumulated_heating_hours = kwargs.get(
        'default_accumulated_heating_hours', 66000)
    p.fraction_living_area = kwargs.get('fraction_living_area', 0.8)

    # TODO: Default floors by "stadtstrukturatlas"
    p.default_floors = kwargs.get('default_floors', 5)

    # Create missing columns
    add_col(data, 'width')
    add_col(data, 'length')
    add_col(data, 'height')
    add_col(data, 'window_ratio')
    add_col(data, 'common_walls')
    add_col(data, 'year_of_construction')
    add_col(data, 'accumulated_heating_hours')

    # Set non values to zero for column 'length'
    data.length.fillna(0, inplace=True)

    # If length not set and building is not a square
    sub1 = (data.length == 0) & ((data.perimeter / 4) ** 2 > data.area)
    data.loc[sub1, 'length'] = data.loc[sub1, 'perimeter'] / 4 + ((
        ((data.loc[sub1, 'perimeter'] / -4) ** 2) -
        data.loc[sub1, 'area']) ** 0.5)

    # If length is not set but building is not a square
    # Normally (data.perimeter / 4) ** 2 can't be smaller than data.area but
    # due to measurement mismatches we should catch this case.
    sub2 = (data.length == 0) & ((data.perimeter / 4) ** 2 <= data.area)
    data.loc[sub2, 'length'] = data.loc[sub2, 'perimeter'] / 4

    # If length < width exchange values
    data.width.fillna(data.area / data.length, inplace=True)
    l_max = data[['width', 'length']].max(axis=1)
    l_min = data[['width', 'length']].min(axis=1)
    data.width = l_min
    data.length = l_max

    # Set default values for None values
    data.fillna(value={
        'floors': p.default_floors,
        'year_of_construction': p.default_average_build_year,
        'population_density': p.default_population_density,
        'accumulated_heating_hours': p.default_accumulated_heating_hours,
        }, inplace=True)

    data.loc[data.population_density <= 0, 'population_density'] = (
        p.default_population_density)

    data['height'].fillna(data['floors'] * 3.3, inplace=True)

    # Get window ratio by age
    data['window_ratio'] = window_wall_ratio_AVG_by_building_age_lookup.get(
        data.year_of_construction)

    # Share of non-tilted roofs
    add_col(data, 'share_non_tilted_roof')
    len_data = len(data)
    roof_h = pd.Series(np.zeros(len_data), index=data.index)
    roof_a = pd.Series(np.zeros(len_data), index=data.index)
    height_interv = (data.height <= 33) & (data.height >= 8)
    roof_h[height_interv] = 1/25 * (data.height[height_interv] - 8)
    roof_h[data.height > 33] = 1
    age_interv = ((data.year_of_construction <= 1960) &
                  (data.year_of_construction >= 1860))
    roof_a[age_interv] = 1/100 * (data.year_of_construction[age_interv] - 1860)
    roof_a[data.year_of_construction > 1960] = 1
    data.flatroof_ratio = (roof_h + roof_a) / 2

    # ***** GEOMETRY *****
    # Statistical number of common walls
    data['common_walls'] = common_walls_by_population_density_corr.get(
        data.population_density)

    # Area of the walls
    data['wall_area_gross'] = data.perimeter * data.height
    data['wall_area'] = ((data.perimeter - data.common_walls * data.width) *
                         data.height * (1 - data.window_ratio))

    # Area of windows
    data['window_area'] = ((data.perimeter - data.common_walls * data.width) *
                           data.height * data.window_ratio)

    # Area of the roof
    data['roof_area'] = data.area
    data['flatroof_area'] = data.area * data.flatroof_ratio

    # Base area
    data['base_area'] = data.area

    # Area of active envelope
    data['a_envelope'] = (data.wall_area + data.window_area + data.roof_area +
                          data.base_area)

    # Volume of building
    data['volume'] = data.area * data.height

    # Volume-Area-Relation
    data['a_v_relation'] = data.a_envelope / data.volume

    # Living area
    data['living_area'] = data.area * data.floors * p.fraction_living_area

    # Heating hours
    p['heating_hours'] = p.heating_degree_days * 24

    # transmission heat losses (QT) of the base
    data['base_uvalue_pres'] = (
        present_base_uvalue_AVG_by_building_age_lookup.get(
            data.year_of_construction))
    data['base_uvalue_contemp'] = (
        contemporary_base_uvalue_by_building_age_lookup.get(
            data.year_of_construction))
    data['base_loss_pres'] = (data.base_area * data.base_uvalue_pres *
                              data.accumulated_heating_hours / 1000 * 0.35)
    data['base_loss_contemp'] = (data.base_area * data.base_uvalue_contemp *
                                 data.accumulated_heating_hours / 1000 * 0.35)
    data['base_spec_loss_contemp'] = data.base_loss_contemp / data.base_area
    data['base_spec_loss_pres'] = data.base_loss_pres / data.base_area

    # transmission heat losses (QT) of the walls
    data['wall_uvalue_pres'] = (
        present_wall_uvalue_AVG_by_building_age_lookup.get(
            data.year_of_construction))
    data['wall_uvalue_contemp'] = (
        contemporary_wall_uvalue_by_building_age_lookup.get(
            data.year_of_construction))
    data['wall_loss_pres'] = (data.wall_area * data.wall_uvalue_pres *
                              data.accumulated_heating_hours / 1000)
    data['wall_loss_contemp'] = (data.wall_area * data.wall_uvalue_contemp *
                                 data.accumulated_heating_hours / 1000)
    data['wall_spec_loss_contemp'] = data.wall_loss_contemp / data.wall_area
    data['wall_spec_loss_pres'] = data.wall_loss_pres / data.wall_area

    # transmission heat losses (QT) of the windows
    data['window_uvalue_pres'] = (
        present_window_uvalue_AVG_by_building_age_lookup.get(
            data.year_of_construction))
    data['window_uvalue_contemp'] = (
        contemporary_window_uvalue_by_building_age_lookup.get(
            data.year_of_construction))
    data['window_loss_pres'] = (data.window_area * data.window_uvalue_pres *
                                data.accumulated_heating_hours / 1000)
    data['window_loss_contemp'] = (data.window_area *
                                   data.window_uvalue_contemp *
                                   data.accumulated_heating_hours / 1000)
    data['window_spec_loss_contemp'] = (data.window_loss_contemp /
                                        data.window_area)
    data['window_spec_loss_pres'] = (data.window_loss_pres /
                                     data.window_area)

    # transmission heat losses (QT) of the  roof
    data['roof_uvalue_pres'] = (
        present_roof_uvalue_AVG_by_building_age_lookup.get(
            data.year_of_construction))
    data['roof_uvalue_contemp'] = (
        contemporary_roof_uvalue_by_building_age_lookup.get(
            data.year_of_construction))
    data['roof_loss_pres'] = (data.roof_area * data.roof_uvalue_pres *
                              data.accumulated_heating_hours / 1000)
    data['roof_loss_contemp'] = (data.roof_area * data.roof_uvalue_contemp *
                                 data.accumulated_heating_hours / 1000)
    data['roof_spec_loss_contemp'] = data.roof_loss_contemp / data.roof_area
    data['roof_spec_loss_pres'] = data.roof_loss_pres / data.roof_area

    # Air change heat loss
    data['air_change_heat_loss'] = 40 * data.living_area

    # Total transmission heat losses (QT total)
    data['total_loss_pres'] = (data.base_loss_pres +
                               data.wall_loss_pres +
                               data.window_loss_pres * 1.2 +
                               data.roof_loss_pres)

    data['total_loss_contemp'] = (data.base_loss_contemp +
                                  data.wall_loss_contemp +
                                  data.window_loss_contemp * 1.2 +
                                  data.roof_loss_contemp)

    # Specific heat losses
    data['HLAC'] = data.total_loss_contemp / data.living_area
    data['HLAP'] = data.total_loss_pres / data.living_area
    data['AHDC'] = data.HLAC + 40.0 * p.fraction_living_area
    data['AHDP'] = data.HLAP + 40.0 * p.fraction_living_area

    return data
