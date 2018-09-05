# -*- coding: utf-8 -*-

# Dictionary for mapping ALK values to Building USE (Residential Buildings (RB) or
# Non Residential Buildings (NRB)) and TYPE (Wohngebaeude, Buerogebaeude, etc.)

# Inputvalue (*xin)
def get(*xin):

    from PyQt4.QtCore import QVariant

    # Dictionary from ALKIS®- Grunddatenbestand und länderspezifische Inhalte
    ALKUSAGE = {
    "1000":"RB",
    "1010":"RB",
    "1020":"RB",
    "1021":"RB",
    "1022":"RB",
    "1023":"RB",
    "1024":"RB",
    "1025":"RB",
    "1100":"RB",
    "1110":"RB",
    "1120":"RB",
    "1121":"RB",
    "1122":"RB",
    "1123":"RB",
    "1130":"RB",
    "1131":"RB",
    "1210":"RB",
    "1220":"RB",
    "1221":"RB",
    "1222":"RB",
    "1223":"RB",
    "1310":"RB",
    "1311":"RB",
    "1312":"RB",
    "1313":"RB",
    "2000":"NRB",
    "2010":"NRB",
    "2020":"NRB",
    "2030":"NRB",
    "2040":"NRB",
    "2050":"NRB",
    "2051":"NRB",
    "2052":"NRB",
    "2053":"NRB",
    "2054":"NRB",
    "2055":"NRB",
    "2056":"NRB",
    "2060":"NRB",
    "2070":"NRB",
    "2071":"NRB",
    "2072":"NRB",
    "2073":"NRB",
    "2074":"NRB",
    "2080":"NRB",
    "2081":"NRB",
    "2082":"NRB",
    "2083":"NRB",
    "2090":"NRB",
    "2091":"NRB",
    "2092":"NRB",
    "2093":"NRB",
    "2094":"NRB",
    "2100":"NRB",
    "2110":"NRB",
    "2111":"NRB",
    "2112":"NRB",
    "2113":"NRB",
    "2114":"NRB",
    "2120":"NRB",
    "2121":"NRB",
    "2130":"NRB",
    "2131":"NRB",
    "2140":"NRB",
    "2141":"NRB",
    "2142":"NRB",
    "2143":"NRB",
    "2150":"NRB",
    "2160":"NRB",
    "2170":"NRB",
    "2171":"NRB",
    "2172":"NRB",
    "2180":"NRB",
    "2200":"NRB",
    "2210":"NRB",
    "2211":"NRB",
    "2212":"NRB",
    "2213":"NRB",
    "2220":"NRB",
    "2310":"NRB",
    "2320":"NRB",
    "2400":"NRB",
    "2410":"NRB",
    "2411":"NRB",
    "2412":"NRB",
    "2420":"NRB",
    "2421":"NRB",
    "2422":"NRB",
    "2423":"NRB",
    "2424":"NRB",
    "2430":"NRB",
    "2431":"NRB",
    "2440":"NRB",
    "2441":"NRB",
    "2442":"NRB",
    "2443":"NRB",
    "2444":"NRB",
    "2450":"NRB",
    "2451":"NRB",
    "2460":"NRB",
    "2461":"NRB",
    "2462":"NRB",
    "2463":"NRB",
    "2464":"NRB",
    "2465":"NRB",
    "2500":"NRB",
    "2501":"NRB",
    "2510":"NRB",
    "2511":"NRB",
    "2512":"NRB",
    "2513":"NRB",
    "2520":"NRB",
    "2521":"NRB",
    "2522":"NRB",
    "2523":"NRB",
    "2527":"NRB",
    "2528":"NRB",
    "2529":"NRB",
    "2540":"NRB",
    "2560":"NRB",
    "2570":"NRB",
    "2571":"NRB",
    "2580":"NRB",
    "2590":"NRB",
    "2591":"NRB",
    "2600":"NRB",
    "2610":"NRB",
    "2611":"NRB",
    "2612":"NRB",
    "2620":"NRB",
    "2621":"NRB",
    "2622":"NRB",
    "2623":"NRB",
    "2700":"NRB",
    "2720":"NRB",
    "2721":"NRB",
    "2723":"NRB",
    "2724":"NRB",
    "2726":"NRB",
    "2727":"NRB",
    "2728":"NRB",
    "2729":"NRB",
    "2732":"NRB",
    "2735":"NRB",
    "2740":"NRB",
    "2741":"NRB",
    "2742":"NRB",
    "3000":"NRB",
    "3010":"NRB",
    "3011":"NRB",
    "3012":"NRB",
    "3013":"NRB",
    "3014":"NRB",
    "3015":"NRB",
    "3016":"NRB",
    "3017":"NRB",
    "3018":"NRB",
    "3019":"NRB",
    "3020":"NRB",
    "3021":"NRB",
    "3022":"NRB",
    "3023":"NRB",
    "3024":"NRB",
    "3030":"NRB",
    "3031":"NRB",
    "3032":"NRB",
    "3033":"NRB",
    "3034":"NRB",
    "3035":"NRB",
    "3036":"NRB",
    "3037":"NRB",
    "3038":"NRB",
    "3040":"NRB",
    "3041":"NRB",
    "3042":"NRB",
    "3043":"NRB",
    "3044":"NRB",
    "3045":"NRB",
    "3046":"NRB",
    "3047":"NRB",
    "3048":"NRB",
    "3050":"NRB",
    "3051":"NRB",
    "3052":"NRB",
    "3053":"NRB",
    "3060":"NRB",
    "3061":"NRB",
    "3062":"NRB",
    "3063":"NRB",
    "3064":"NRB",
    "3065":"NRB",
    "3066":"NRB",
    "3070":"NRB",
    "3071":"NRB",
    "3072":"NRB",
    "3073":"NRB",
    "3074":"NRB",
    "3075":"NRB",
    "3080":"NRB",
    "3081":"NRB",
    "3082":"NRB",
    "3090":"NRB",
    "3091":"NRB",
    "3092":"NRB",
    "3094":"NRB",
    "3095":"NRB",
    "3097":"NRB",
    "3098":"NRB",
    "3100":"NRB",
    "3200":"NRB",
    "3210":"NRB",
    "3211":"NRB",
    "3212":"NRB",
    "3220":"NRB",
    "3221":"NRB",
    "3222":"NRB",
    "3230":"NRB",
    "3240":"NRB",
    "3241":"NRB",
    "3242":"NRB",
    "3260":"NRB",
    "3261":"NRB",
    "3262":"NRB",
    "3263":"NRB",
    "3264":"NRB",
    "3270":"NRB",
    "3271":"NRB",
    "3272":"NRB",
    "3273":"NRB",
    "3280":"NRB",
    "3281":"NRB",
    "3290":"NRB"
    }


    #Output Name and Use is defined
    bui_use = ALKUSAGE.get(xin[0],"no USAGE specified")

    return (bui_use.encode('utf8'))
