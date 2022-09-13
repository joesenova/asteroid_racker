"""
Test fixtures
"""

API_RESPONSE_400_ERROR = {
    'code': 400,
    'http_error': 'BAD_REQUEST',
    'error_message': 'Date Format Exception - Expected format (yyyy-mm-dd) - The Feed date limit is only 7 Days',
    'request': 'http://www.neowsapp.com/rest/v1/feed?start_date=2016-04-01&end_date=2016-05-11',
}


API_RESPONSE_2021_01_01_TO_2021_01_02_SUCCESS = {
  "links": {
    "next": "http://api.nasa.gov/neo/rest/v1/feed?start_date=2021-01-02&end_date=2021-01-03&detailed=False&api_key=DEMO_KEY",
    "previous": "http://api.nasa.gov/neo/rest/v1/feed?start_date=2020-12-31&end_date=2021-01-01&detailed=False&api_key=DEMO_KEY",
    "self": "http://api.nasa.gov/neo/rest/v1/feed?start_date=2021-01-01&end_date=2021-01-02&detailed=False&api_key=DEMO_KEY"
  },
  "element_count": 31,
  "near_earth_objects": {
    "2021-01-02": [
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3471590?api_key=DEMO_KEY"
        },
        "id": "3471590",
        "neo_reference_id": "3471590",
        "name": "(2009 TK12)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3471590",
        "absolute_magnitude_h": 20.6,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.2016299194,
            "estimated_diameter_max": 0.4508582062
          },
          "meters": {
            "estimated_diameter_min": 201.6299194428,
            "estimated_diameter_max": 450.8582061718
          },
          "miles": {
            "estimated_diameter_min": 0.1252869847,
            "estimated_diameter_max": 0.2801502144
          },
          "feet": {
            "estimated_diameter_min": 661.5155049046,
            "estimated_diameter_max": 1479.1936371367
          }
        },
        "is_potentially_hazardous_asteroid": True,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 21:38",
            "epoch_date_close_approach": 1609623480000,
            "relative_velocity": {
              "kilometers_per_second": "13.1554373998",
              "kilometers_per_hour": "47359.5746393772",
              "miles_per_hour": "29427.397919673"
            },
            "miss_distance": {
              "astronomical": "0.252794391",
              "lunar": "98.337018099",
              "kilometers": "37817502.44154717",
              "miles": "23498706.367684146"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3477945?api_key=DEMO_KEY"
        },
        "id": "3477945",
        "neo_reference_id": "3477945",
        "name": "(2009 WN8)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3477945",
        "absolute_magnitude_h": 25.2,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0242412481,
            "estimated_diameter_max": 0.0542050786
          },
          "meters": {
            "estimated_diameter_min": 24.2412481101,
            "estimated_diameter_max": 54.2050786336
          },
          "miles": {
            "estimated_diameter_min": 0.0150628086,
            "estimated_diameter_max": 0.0336814639
          },
          "feet": {
            "estimated_diameter_min": 79.5316564495,
            "estimated_diameter_max": 177.8381901842
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 16:51",
            "epoch_date_close_approach": 1609606260000,
            "relative_velocity": {
              "kilometers_per_second": "9.1999417302",
              "kilometers_per_hour": "33119.7902286523",
              "miles_per_hour": "20579.3496562423"
            },
            "miss_distance": {
              "astronomical": "0.2383741552",
              "lunar": "92.7275463728",
              "kilometers": "35660265.880969424",
              "miles": "22158261.7261850912"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3703247?api_key=DEMO_KEY"
        },
        "id": "3703247",
        "neo_reference_id": "3703247",
        "name": "(2014 YD42)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3703247",
        "absolute_magnitude_h": 22.2,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.096506147,
            "estimated_diameter_max": 0.2157943048
          },
          "meters": {
            "estimated_diameter_min": 96.5061469579,
            "estimated_diameter_max": 215.7943048444
          },
          "miles": {
            "estimated_diameter_min": 0.059966121,
            "estimated_diameter_max": 0.134088323
          },
          "feet": {
            "estimated_diameter_min": 316.6212271853,
            "estimated_diameter_max": 707.9865871058
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 23:27",
            "epoch_date_close_approach": 1609630020000,
            "relative_velocity": {
              "kilometers_per_second": "22.5532909862",
              "kilometers_per_hour": "81191.8475503297",
              "miles_per_hour": "50449.4566070368"
            },
            "miss_distance": {
              "astronomical": "0.3537272571",
              "lunar": "137.5999030119",
              "kilometers": "52916844.223102377",
              "miles": "32881002.2878997226"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3756788?api_key=DEMO_KEY"
        },
        "id": "3756788",
        "neo_reference_id": "3756788",
        "name": "(2016 PN)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3756788",
        "absolute_magnitude_h": 20.3,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.2315021222,
            "estimated_diameter_max": 0.5176544822
          },
          "meters": {
            "estimated_diameter_min": 231.5021222103,
            "estimated_diameter_max": 517.6544821978
          },
          "miles": {
            "estimated_diameter_min": 0.1438487052,
            "estimated_diameter_max": 0.3216554833
          },
          "feet": {
            "estimated_diameter_min": 759.5214226325,
            "estimated_diameter_max": 1698.3415313737
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 20:26",
            "epoch_date_close_approach": 1609619160000,
            "relative_velocity": {
              "kilometers_per_second": "18.0459712584",
              "kilometers_per_hour": "64965.4965302929",
              "miles_per_hour": "40367.0331079478"
            },
            "miss_distance": {
              "astronomical": "0.3769637839",
              "lunar": "146.6389119371",
              "kilometers": "56392979.138580293",
              "miles": "35040972.3652343234"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3766183?api_key=DEMO_KEY"
        },
        "id": "3766183",
        "neo_reference_id": "3766183",
        "name": "(2016 YS8)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3766183",
        "absolute_magnitude_h": 21.4,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.1394938229,
            "estimated_diameter_max": 0.3119176705
          },
          "meters": {
            "estimated_diameter_min": 139.4938229344,
            "estimated_diameter_max": 311.9176705226
          },
          "miles": {
            "estimated_diameter_min": 0.0866774163,
            "estimated_diameter_max": 0.1938165949
          },
          "feet": {
            "estimated_diameter_min": 457.6569140361,
            "estimated_diameter_max": 1023.3519701574
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 00:00",
            "epoch_date_close_approach": 1609545600000,
            "relative_velocity": {
              "kilometers_per_second": "18.3816843515",
              "kilometers_per_hour": "66174.0636653809",
              "miles_per_hour": "41117.9897258585"
            },
            "miss_distance": {
              "astronomical": "0.4768126868",
              "lunar": "185.4801351652",
              "kilometers": "71330162.334257116",
              "miles": "44322507.6125195608"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3787068?api_key=DEMO_KEY"
        },
        "id": "3787068",
        "neo_reference_id": "3787068",
        "name": "(2017 US)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3787068",
        "absolute_magnitude_h": 26.2,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0152951935,
            "estimated_diameter_max": 0.0342010925
          },
          "meters": {
            "estimated_diameter_min": 15.2951935344,
            "estimated_diameter_max": 34.201092472
          },
          "miles": {
            "estimated_diameter_min": 0.0095039897,
            "estimated_diameter_max": 0.021251567
          },
          "feet": {
            "estimated_diameter_min": 50.1810827555,
            "estimated_diameter_max": 112.2083122258
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 07:31",
            "epoch_date_close_approach": 1609572660000,
            "relative_velocity": {
              "kilometers_per_second": "2.7745743607",
              "kilometers_per_hour": "9988.4676986372",
              "miles_per_hour": "6206.4453875226"
            },
            "miss_distance": {
              "astronomical": "0.2137735061",
              "lunar": "83.1578938729",
              "kilometers": "31980061.174992007",
              "miles": "19871488.5609714166"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3825828?api_key=DEMO_KEY"
        },
        "id": "3825828",
        "neo_reference_id": "3825828",
        "name": "(2018 OZ)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3825828",
        "absolute_magnitude_h": 24.9,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0278326768,
            "estimated_diameter_max": 0.0622357573
          },
          "meters": {
            "estimated_diameter_min": 27.8326768072,
            "estimated_diameter_max": 62.2357573367
          },
          "miles": {
            "estimated_diameter_min": 0.0172944182,
            "estimated_diameter_max": 0.0386714948
          },
          "feet": {
            "estimated_diameter_min": 91.3145593761,
            "estimated_diameter_max": 204.1855621004
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 01:14",
            "epoch_date_close_approach": 1609550040000,
            "relative_velocity": {
              "kilometers_per_second": "7.4805361545",
              "kilometers_per_hour": "26929.9301560494",
              "miles_per_hour": "16733.2113239075"
            },
            "miss_distance": {
              "astronomical": "0.209123019",
              "lunar": "81.348854391",
              "kilometers": "31284358.21036953",
              "miles": "19439198.784298314"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3837718?api_key=DEMO_KEY"
        },
        "id": "3837718",
        "neo_reference_id": "3837718",
        "name": "(2019 AU6)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3837718",
        "absolute_magnitude_h": 26.61,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0126635356,
            "estimated_diameter_max": 0.0283165265
          },
          "meters": {
            "estimated_diameter_min": 12.6635356293,
            "estimated_diameter_max": 28.3165265026
          },
          "miles": {
            "estimated_diameter_min": 0.0078687538,
            "estimated_diameter_max": 0.0175950684
          },
          "feet": {
            "estimated_diameter_min": 41.547034234,
            "estimated_diameter_max": 92.9019928107
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 07:29",
            "epoch_date_close_approach": 1609572540000,
            "relative_velocity": {
              "kilometers_per_second": "18.298856739",
              "kilometers_per_hour": "65875.8842605134",
              "miles_per_hour": "40932.7126395396"
            },
            "miss_distance": {
              "astronomical": "0.3114598591",
              "lunar": "121.1578851899",
              "kilometers": "46593731.511860117",
              "miles": "28952002.2392869346"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3959223?api_key=DEMO_KEY"
        },
        "id": "3959223",
        "neo_reference_id": "3959223",
        "name": "(2019 YB4)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3959223",
        "absolute_magnitude_h": 26.8,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0116025908,
            "estimated_diameter_max": 0.0259441818
          },
          "meters": {
            "estimated_diameter_min": 11.6025908209,
            "estimated_diameter_max": 25.9441817907
          },
          "miles": {
            "estimated_diameter_min": 0.0072095135,
            "estimated_diameter_max": 0.0161209622
          },
          "feet": {
            "estimated_diameter_min": 38.066244069,
            "estimated_diameter_max": 85.1187093863
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 09:25",
            "epoch_date_close_approach": 1609579500000,
            "relative_velocity": {
              "kilometers_per_second": "7.153241485",
              "kilometers_per_hour": "25751.6693460303",
              "miles_per_hour": "16001.0858778153"
            },
            "miss_distance": {
              "astronomical": "0.043132941",
              "lunar": "16.778714049",
              "kilometers": "6452596.10043567",
              "miles": "4009457.295805446"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3972419?api_key=DEMO_KEY"
        },
        "id": "3972419",
        "neo_reference_id": "3972419",
        "name": "(2020 AT)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3972419",
        "absolute_magnitude_h": 25.2,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0242412481,
            "estimated_diameter_max": 0.0542050786
          },
          "meters": {
            "estimated_diameter_min": 24.2412481101,
            "estimated_diameter_max": 54.2050786336
          },
          "miles": {
            "estimated_diameter_min": 0.0150628086,
            "estimated_diameter_max": 0.0336814639
          },
          "feet": {
            "estimated_diameter_min": 79.5316564495,
            "estimated_diameter_max": 177.8381901842
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 18:55",
            "epoch_date_close_approach": 1609613700000,
            "relative_velocity": {
              "kilometers_per_second": "8.5075527924",
              "kilometers_per_hour": "30627.1900524988",
              "miles_per_hour": "19030.5448412319"
            },
            "miss_distance": {
              "astronomical": "0.1444564912",
              "lunar": "56.1935750768",
              "kilometers": "21610383.391193744",
              "miles": "13428069.5714279072"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54051064?api_key=DEMO_KEY"
        },
        "id": "54051064",
        "neo_reference_id": "54051064",
        "name": "(2020 PE3)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54051064",
        "absolute_magnitude_h": 24.3,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0366906138,
            "estimated_diameter_max": 0.0820427065
          },
          "meters": {
            "estimated_diameter_min": 36.6906137531,
            "estimated_diameter_max": 82.0427064882
          },
          "miles": {
            "estimated_diameter_min": 0.0227984834,
            "estimated_diameter_max": 0.0509789586
          },
          "feet": {
            "estimated_diameter_min": 120.3760332259,
            "estimated_diameter_max": 269.1689931548
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 20:30",
            "epoch_date_close_approach": 1609619400000,
            "relative_velocity": {
              "kilometers_per_second": "13.5483820297",
              "kilometers_per_hour": "48774.1753070258",
              "miles_per_hour": "30306.3757623017"
            },
            "miss_distance": {
              "astronomical": "0.4646162157",
              "lunar": "180.7357079073",
              "kilometers": "69505596.236180559",
              "miles": "43188774.8110633542"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54073358?api_key=DEMO_KEY"
        },
        "id": "54073358",
        "neo_reference_id": "54073358",
        "name": "(2020 TT7)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54073358",
        "absolute_magnitude_h": 22.27,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0934447651,
            "estimated_diameter_max": 0.2089488469
          },
          "meters": {
            "estimated_diameter_min": 93.4447650924,
            "estimated_diameter_max": 208.9488468882
          },
          "miles": {
            "estimated_diameter_min": 0.0580638671,
            "estimated_diameter_max": 0.1298347539
          },
          "feet": {
            "estimated_diameter_min": 306.5773231058,
            "estimated_diameter_max": 685.5277348245
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 03:59",
            "epoch_date_close_approach": 1609559940000,
            "relative_velocity": {
              "kilometers_per_second": "3.5909109866",
              "kilometers_per_hour": "12927.2795518881",
              "miles_per_hour": "8032.5087860051"
            },
            "miss_distance": {
              "astronomical": "0.1862160888",
              "lunar": "72.4380585432",
              "kilometers": "27857530.244210856",
              "miles": "17309866.6245715728"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54095182?api_key=DEMO_KEY"
        },
        "id": "54095182",
        "neo_reference_id": "54095182",
        "name": "(2020 WA5)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54095182",
        "absolute_magnitude_h": 21.78,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.1170994827,
            "estimated_diameter_max": 0.2618424035
          },
          "meters": {
            "estimated_diameter_min": 117.09948272,
            "estimated_diameter_max": 261.8424034921
          },
          "miles": {
            "estimated_diameter_min": 0.0727622227,
            "estimated_diameter_max": 0.1627012761
          },
          "feet": {
            "estimated_diameter_min": 384.1846668872,
            "estimated_diameter_max": 859.0630310729
          }
        },
        "is_potentially_hazardous_asteroid": True,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 09:40",
            "epoch_date_close_approach": 1609580400000,
            "relative_velocity": {
              "kilometers_per_second": "7.398100272",
              "kilometers_per_hour": "26633.1609791791",
              "miles_per_hour": "16548.8104984238"
            },
            "miss_distance": {
              "astronomical": "0.0776759235",
              "lunar": "30.2159342415",
              "kilometers": "11620152.705882945",
              "miles": "7220428.075736841"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54097969?api_key=DEMO_KEY"
        },
        "id": "54097969",
        "neo_reference_id": "54097969",
        "name": "(2020 XR)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54097969",
        "absolute_magnitude_h": 19.9,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.2783267681,
            "estimated_diameter_max": 0.6223575734
          },
          "meters": {
            "estimated_diameter_min": 278.3267680719,
            "estimated_diameter_max": 622.3575733667
          },
          "miles": {
            "estimated_diameter_min": 0.1729441822,
            "estimated_diameter_max": 0.3867149477
          },
          "feet": {
            "estimated_diameter_min": 913.1455937611,
            "estimated_diameter_max": 2041.8556210042
          }
        },
        "is_potentially_hazardous_asteroid": True,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 04:47",
            "epoch_date_close_approach": 1609562820000,
            "relative_velocity": {
              "kilometers_per_second": "19.9007980199",
              "kilometers_per_hour": "71642.8728715846",
              "miles_per_hour": "44516.0950906799"
            },
            "miss_distance": {
              "astronomical": "0.3280661448",
              "lunar": "127.6177303272",
              "kilometers": "49077996.481191576",
              "miles": "30495652.9111967088"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54099344?api_key=DEMO_KEY"
        },
        "id": "54099344",
        "neo_reference_id": "54099344",
        "name": "(2020 XP2)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54099344",
        "absolute_magnitude_h": 22.12,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.1001278698,
            "estimated_diameter_max": 0.2238927232
          },
          "meters": {
            "estimated_diameter_min": 100.1278697699,
            "estimated_diameter_max": 223.8927232478
          },
          "miles": {
            "estimated_diameter_min": 0.0622165546,
            "estimated_diameter_max": 0.1391204453
          },
          "feet": {
            "estimated_diameter_min": 328.503520256,
            "estimated_diameter_max": 734.5562021403
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 17:09",
            "epoch_date_close_approach": 1609607340000,
            "relative_velocity": {
              "kilometers_per_second": "13.3199923498",
              "kilometers_per_hour": "47951.9724592296",
              "miles_per_hour": "29795.4908872363"
            },
            "miss_distance": {
              "astronomical": "0.0594498495",
              "lunar": "23.1259914555",
              "kilometers": "8893570.857020565",
              "miles": "5526208.676851197"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54099601?api_key=DEMO_KEY"
        },
        "id": "54099601",
        "neo_reference_id": "54099601",
        "name": "(2020 XW2)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54099601",
        "absolute_magnitude_h": 25,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.02658,
            "estimated_diameter_max": 0.0594346868
          },
          "meters": {
            "estimated_diameter_min": 26.58,
            "estimated_diameter_max": 59.4346868419
          },
          "miles": {
            "estimated_diameter_min": 0.0165160412,
            "estimated_diameter_max": 0.0369309908
          },
          "feet": {
            "estimated_diameter_min": 87.2047272,
            "estimated_diameter_max": 194.9956979785
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 02:10",
            "epoch_date_close_approach": 1609553400000,
            "relative_velocity": {
              "kilometers_per_second": "2.7818373464",
              "kilometers_per_hour": "10014.6144470117",
              "miles_per_hour": "6222.6919601446"
            },
            "miss_distance": {
              "astronomical": "0.1054561095",
              "lunar": "41.0224265955",
              "kilometers": "15776009.359686765",
              "miles": "9802757.656196757"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54104551?api_key=DEMO_KEY"
        },
        "id": "54104551",
        "neo_reference_id": "54104551",
        "name": "(2021 AQ1)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54104551",
        "absolute_magnitude_h": 25.07,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0257368254,
            "estimated_diameter_max": 0.0575492912
          },
          "meters": {
            "estimated_diameter_min": 25.7368254194,
            "estimated_diameter_max": 57.5492911629
          },
          "miles": {
            "estimated_diameter_min": 0.0159921169,
            "estimated_diameter_max": 0.0357594606
          },
          "feet": {
            "estimated_diameter_min": 84.4384063091,
            "estimated_diameter_max": 188.8100164188
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 07:34",
            "epoch_date_close_approach": 1609572840000,
            "relative_velocity": {
              "kilometers_per_second": "13.9754625815",
              "kilometers_per_hour": "50311.6652935224",
              "miles_per_hour": "31261.7122486334"
            },
            "miss_distance": {
              "astronomical": "0.0151278165",
              "lunar": "5.8847206185",
              "kilometers": "2263089.126150855",
              "miles": "1406218.375777599"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54104841?api_key=DEMO_KEY"
        },
        "id": "54104841",
        "neo_reference_id": "54104841",
        "name": "(2021 AJ2)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54104841",
        "absolute_magnitude_h": 23.26,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0592318063,
            "estimated_diameter_max": 0.1324463452
          },
          "meters": {
            "estimated_diameter_min": 59.2318062676,
            "estimated_diameter_max": 132.4463452445
          },
          "miles": {
            "estimated_diameter_min": 0.0368049267,
            "estimated_diameter_max": 0.082298318
          },
          "feet": {
            "estimated_diameter_min": 194.330079275,
            "estimated_diameter_max": 434.5352673318
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 07:12",
            "epoch_date_close_approach": 1609571520000,
            "relative_velocity": {
              "kilometers_per_second": "9.7976821443",
              "kilometers_per_hour": "35271.6557194673",
              "miles_per_hour": "21916.4351885768"
            },
            "miss_distance": {
              "astronomical": "0.2429619405",
              "lunar": "94.5121948545",
              "kilometers": "36346588.789866735",
              "miles": "22584723.006501543"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54104906?api_key=DEMO_KEY"
        },
        "id": "54104906",
        "neo_reference_id": "54104906",
        "name": "(2021 AR3)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54104906",
        "absolute_magnitude_h": 25.89,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0176422908,
            "estimated_diameter_max": 0.0394493615
          },
          "meters": {
            "estimated_diameter_min": 17.6422908113,
            "estimated_diameter_max": 39.4493615328
          },
          "miles": {
            "estimated_diameter_min": 0.0109624079,
            "estimated_diameter_max": 0.0245126892
          },
          "feet": {
            "estimated_diameter_min": 57.8815333853,
            "estimated_diameter_max": 129.4270432914
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 23:26",
            "epoch_date_close_approach": 1609629960000,
            "relative_velocity": {
              "kilometers_per_second": "14.0595990557",
              "kilometers_per_hour": "50614.5566004534",
              "miles_per_hour": "31449.9171276539"
            },
            "miss_distance": {
              "astronomical": "0.0238890416",
              "lunar": "9.2928371824",
              "kilometers": "3573749.739701392",
              "miles": "2220625.1164955296"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54106086?api_key=DEMO_KEY"
        },
        "id": "54106086",
        "neo_reference_id": "54106086",
        "name": "(2021 AN7)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54106086",
        "absolute_magnitude_h": 20.8,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.1838886721,
            "estimated_diameter_max": 0.411187571
          },
          "meters": {
            "estimated_diameter_min": 183.8886720703,
            "estimated_diameter_max": 411.1875710413
          },
          "miles": {
            "estimated_diameter_min": 0.1142630881,
            "estimated_diameter_max": 0.2555000322
          },
          "feet": {
            "estimated_diameter_min": 603.309310875,
            "estimated_diameter_max": 1349.040630575
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 23:01",
            "epoch_date_close_approach": 1609628460000,
            "relative_velocity": {
              "kilometers_per_second": "8.8682713585",
              "kilometers_per_hour": "31925.7768906314",
              "miles_per_hour": "19837.4362018481"
            },
            "miss_distance": {
              "astronomical": "0.4318998104",
              "lunar": "168.0090262456",
              "kilometers": "64611291.689243848",
              "miles": "40147594.9869791824"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54144273?api_key=DEMO_KEY"
        },
        "id": "54144273",
        "neo_reference_id": "54144273",
        "name": "(2021 JD3)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54144273",
        "absolute_magnitude_h": 26.09,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0160899605,
            "estimated_diameter_max": 0.0359782453
          },
          "meters": {
            "estimated_diameter_min": 16.089960451,
            "estimated_diameter_max": 35.9782453236
          },
          "miles": {
            "estimated_diameter_min": 0.0099978348,
            "estimated_diameter_max": 0.0223558383
          },
          "feet": {
            "estimated_diameter_min": 52.7885858459,
            "estimated_diameter_max": 118.0388663876
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-02",
            "close_approach_date_full": "2021-Jan-02 10:28",
            "epoch_date_close_approach": 1609583280000,
            "relative_velocity": {
              "kilometers_per_second": "6.6483101168",
              "kilometers_per_hour": "23933.9164204277",
              "miles_per_hour": "14871.6049002374"
            },
            "miss_distance": {
              "astronomical": "0.3139298344",
              "lunar": "122.1187055816",
              "kilometers": "46963234.555692728",
              "miles": "29181600.7840985264"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      }
    ],
    "2021-01-01": [
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3735686?api_key=DEMO_KEY"
        },
        "id": "3735686",
        "neo_reference_id": "3735686",
        "name": "(2015 XP54)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3735686",
        "absolute_magnitude_h": 24,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0421264611,
            "estimated_diameter_max": 0.0941976306
          },
          "meters": {
            "estimated_diameter_min": 42.1264610556,
            "estimated_diameter_max": 94.1976305719
          },
          "miles": {
            "estimated_diameter_min": 0.0261761612,
            "estimated_diameter_max": 0.0585316759
          },
          "feet": {
            "estimated_diameter_min": 138.2101784897,
            "estimated_diameter_max": 309.0473542854
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-01",
            "close_approach_date_full": "2021-Jan-01 11:41",
            "epoch_date_close_approach": 1609501260000,
            "relative_velocity": {
              "kilometers_per_second": "11.354735448",
              "kilometers_per_hour": "40877.0476129732",
              "miles_per_hour": "25399.4077237388"
            },
            "miss_distance": {
              "astronomical": "0.3036640215",
              "lunar": "118.1253043635",
              "kilometers": "45427490.812034205",
              "miles": "28227333.871733829"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3797688?api_key=DEMO_KEY"
        },
        "id": "3797688",
        "neo_reference_id": "3797688",
        "name": "(2018 AE12)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3797688",
        "absolute_magnitude_h": 22.3,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0921626549,
            "estimated_diameter_max": 0.2060819612
          },
          "meters": {
            "estimated_diameter_min": 92.1626548503,
            "estimated_diameter_max": 206.0819612321
          },
          "miles": {
            "estimated_diameter_min": 0.057267201,
            "estimated_diameter_max": 0.1280533543
          },
          "feet": {
            "estimated_diameter_min": 302.370924539,
            "estimated_diameter_max": 676.1219416887
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-01",
            "close_approach_date_full": "2021-Jan-01 23:01",
            "epoch_date_close_approach": 1609542060000,
            "relative_velocity": {
              "kilometers_per_second": "26.865235514",
              "kilometers_per_hour": "96714.8478503813",
              "miles_per_hour": "60094.845321255"
            },
            "miss_distance": {
              "astronomical": "0.0783065301",
              "lunar": "30.4612402089",
              "kilometers": "11714490.110050887",
              "miles": "7279046.6205087606"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3838033?api_key=DEMO_KEY"
        },
        "id": "3838033",
        "neo_reference_id": "3838033",
        "name": "(2019 BF3)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3838033",
        "absolute_magnitude_h": 25.1,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0253837029,
            "estimated_diameter_max": 0.0567596853
          },
          "meters": {
            "estimated_diameter_min": 25.3837029364,
            "estimated_diameter_max": 56.7596852866
          },
          "miles": {
            "estimated_diameter_min": 0.0157726969,
            "estimated_diameter_max": 0.0352688224
          },
          "feet": {
            "estimated_diameter_min": 83.279867942,
            "estimated_diameter_max": 186.2194458756
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-01",
            "close_approach_date_full": "2021-Jan-01 10:04",
            "epoch_date_close_approach": 1609495440000,
            "relative_velocity": {
              "kilometers_per_second": "11.931504927",
              "kilometers_per_hour": "42953.4177371687",
              "miles_per_hour": "26689.5833711868"
            },
            "miss_distance": {
              "astronomical": "0.2658826503",
              "lunar": "103.4283509667",
              "kilometers": "39775478.154834861",
              "miles": "24715336.0600526418"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/3892775?api_key=DEMO_KEY"
        },
        "id": "3892775",
        "neo_reference_id": "3892775",
        "name": "(2019 VB5)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3892775",
        "absolute_magnitude_h": 31.7,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0012149404,
            "estimated_diameter_max": 0.0027166893
          },
          "meters": {
            "estimated_diameter_min": 1.214940408,
            "estimated_diameter_max": 2.7166893409
          },
          "miles": {
            "estimated_diameter_min": 0.0007549287,
            "estimated_diameter_max": 0.001688072
          },
          "feet": {
            "estimated_diameter_min": 3.9860250882,
            "estimated_diameter_max": 8.9130230572
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-01",
            "close_approach_date_full": "2021-Jan-01 13:03",
            "epoch_date_close_approach": 1609506180000,
            "relative_velocity": {
              "kilometers_per_second": "4.919669084",
              "kilometers_per_hour": "17710.8087022821",
              "miles_per_hour": "11004.8077739263"
            },
            "miss_distance": {
              "astronomical": "0.1460419418",
              "lunar": "56.8103153602",
              "kilometers": "21847563.423943966",
              "miles": "13575446.4098240908"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54100579?api_key=DEMO_KEY"
        },
        "id": "54100579",
        "neo_reference_id": "54100579",
        "name": "(2020 XQ6)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54100579",
        "absolute_magnitude_h": 22.79,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0735453089,
            "estimated_diameter_max": 0.1644523102
          },
          "meters": {
            "estimated_diameter_min": 73.545308935,
            "estimated_diameter_max": 164.452310205
          },
          "miles": {
            "estimated_diameter_min": 0.0456989222,
            "estimated_diameter_max": 0.1021858964
          },
          "feet": {
            "estimated_diameter_min": 241.2903913664,
            "estimated_diameter_max": 539.5417174129
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-01",
            "close_approach_date_full": "2021-Jan-01 10:46",
            "epoch_date_close_approach": 1609497960000,
            "relative_velocity": {
              "kilometers_per_second": "18.8332933357",
              "kilometers_per_hour": "67799.8560086122",
              "miles_per_hour": "42128.1938626846"
            },
            "miss_distance": {
              "astronomical": "0.1006789411",
              "lunar": "39.1641080879",
              "kilometers": "15061355.142415457",
              "miles": "9358692.1171770266"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54101660?api_key=DEMO_KEY"
        },
        "id": "54101660",
        "neo_reference_id": "54101660",
        "name": "(2020 YQ1)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54101660",
        "absolute_magnitude_h": 23.27,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0589596608,
            "estimated_diameter_max": 0.1318378096
          },
          "meters": {
            "estimated_diameter_min": 58.9596608383,
            "estimated_diameter_max": 131.8378095647
          },
          "miles": {
            "estimated_diameter_min": 0.0366358234,
            "estimated_diameter_max": 0.0819201916
          },
          "feet": {
            "estimated_diameter_min": 193.4372136647,
            "estimated_diameter_max": 432.5387591324
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-01",
            "close_approach_date_full": "2021-Jan-01 23:22",
            "epoch_date_close_approach": 1609543320000,
            "relative_velocity": {
              "kilometers_per_second": "11.6936656039",
              "kilometers_per_hour": "42097.1961739597",
              "miles_per_hour": "26157.560589314"
            },
            "miss_distance": {
              "astronomical": "0.1119471256",
              "lunar": "43.5474318584",
              "kilometers": "16747051.542382472",
              "miles": "10406135.2895312336"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54103879?api_key=DEMO_KEY"
        },
        "id": "54103879",
        "neo_reference_id": "54103879",
        "name": "(2021 AA)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54103879",
        "absolute_magnitude_h": 26.98,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0106795998,
            "estimated_diameter_max": 0.023880311
          },
          "meters": {
            "estimated_diameter_min": 10.6795997524,
            "estimated_diameter_max": 23.8803110188
          },
          "miles": {
            "estimated_diameter_min": 0.0066359936,
            "estimated_diameter_max": 0.0148385327
          },
          "feet": {
            "estimated_diameter_min": 35.0380580515,
            "estimated_diameter_max": 78.3474796028
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-01",
            "close_approach_date_full": "2021-Jan-01 13:16",
            "epoch_date_close_approach": 1609506960000,
            "relative_velocity": {
              "kilometers_per_second": "22.2152685842",
              "kilometers_per_hour": "79974.9669032557",
              "miles_per_hour": "49693.3342960813"
            },
            "miss_distance": {
              "astronomical": "0.0015855962",
              "lunar": "0.6167969218",
              "kilometers": "237201.814200094",
              "miles": "147390.3727615372"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54104553?api_key=DEMO_KEY"
        },
        "id": "54104553",
        "neo_reference_id": "54104553",
        "name": "(2021 AS1)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54104553",
        "absolute_magnitude_h": 24.21,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0382432662,
            "estimated_diameter_max": 0.0855145429
          },
          "meters": {
            "estimated_diameter_min": 38.24326621,
            "estimated_diameter_max": 85.5145429273
          },
          "miles": {
            "estimated_diameter_min": 0.0237632566,
            "estimated_diameter_max": 0.0531362571
          },
          "feet": {
            "estimated_diameter_min": 125.4700375125,
            "estimated_diameter_max": 280.5595330175
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-01",
            "close_approach_date_full": "2021-Jan-01 06:58",
            "epoch_date_close_approach": 1609484280000,
            "relative_velocity": {
              "kilometers_per_second": "23.2064190724",
              "kilometers_per_hour": "83543.1086606764",
              "miles_per_hour": "51910.4388230742"
            },
            "miss_distance": {
              "astronomical": "0.0328728466",
              "lunar": "12.7875373274",
              "kilometers": "4917707.832196742",
              "miles": "3055721.9512173596"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54104718?api_key=DEMO_KEY"
        },
        "id": "54104718",
        "neo_reference_id": "54104718",
        "name": "(2021 AZ1)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54104718",
        "absolute_magnitude_h": 24.74,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0299609084,
            "estimated_diameter_max": 0.0669946278
          },
          "meters": {
            "estimated_diameter_min": 29.9609083851,
            "estimated_diameter_max": 66.9946278168
          },
          "miles": {
            "estimated_diameter_min": 0.0186168396,
            "estimated_diameter_max": 0.0416285189
          },
          "feet": {
            "estimated_diameter_min": 98.2969466663,
            "estimated_diameter_max": 219.7986547266
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-01",
            "close_approach_date_full": "2021-Jan-01 11:00",
            "epoch_date_close_approach": 1609498800000,
            "relative_velocity": {
              "kilometers_per_second": "11.3411969891",
              "kilometers_per_hour": "40828.309160747",
              "miles_per_hour": "25369.1235449097"
            },
            "miss_distance": {
              "astronomical": "0.0802024851",
              "lunar": "31.1987667039",
              "kilometers": "11998120.939666737",
              "miles": "7455286.6456734906"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      },
      {
        "links": {
          "self": "http://api.nasa.gov/neo/rest/v1/neo/54105488?api_key=DEMO_KEY"
        },
        "id": "54105488",
        "neo_reference_id": "54105488",
        "name": "(2021 AF5)",
        "nasa_jpl_url": "http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=54105488",
        "absolute_magnitude_h": 24.82,
        "estimated_diameter": {
          "kilometers": {
            "estimated_diameter_min": 0.0288771931,
            "estimated_diameter_max": 0.0645713667
          },
          "meters": {
            "estimated_diameter_min": 28.8771930757,
            "estimated_diameter_max": 64.5713667167
          },
          "miles": {
            "estimated_diameter_min": 0.0179434503,
            "estimated_diameter_max": 0.0401227747
          },
          "feet": {
            "estimated_diameter_min": 94.7414501306,
            "estimated_diameter_max": 211.848322779
          }
        },
        "is_potentially_hazardous_asteroid": False,
        "close_approach_data": [
          {
            "close_approach_date": "2021-01-01",
            "close_approach_date_full": "2021-Jan-01 21:31",
            "epoch_date_close_approach": 1609536660000,
            "relative_velocity": {
              "kilometers_per_second": "3.3704632079",
              "kilometers_per_hour": "12133.6675483178",
              "miles_per_hour": "7539.3891496756"
            },
            "miss_distance": {
              "astronomical": "0.0321894156",
              "lunar": "12.5216826684",
              "kilometers": "4815468.010304772",
              "miles": "2992193.0717669736"
            },
            "orbiting_body": "Earth"
          }
        ],
        "is_sentry_object": False
      }
    ]
  }
}
