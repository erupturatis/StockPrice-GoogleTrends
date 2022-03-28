import json
from sqlite3 import paramstyle
from urllib import request
import requests
import urllib3 

class GoogleTrendsRequest(object):

    STANDARD_URL = "https://trends.google.com/trends/api/explore"
    HL = "en-US"
    TZ = -120
    def __init__(self,) -> None:
        pass

    def request_trends(self) -> object:

        return self




    def test_request(self):
        s = requests.session()
        payload = dict()
      
        payload = {
            'hl':'en-US',
            'tz':'-180',
            'req':{'comparisonItem':[{'keyword':'ukraine','geo':'','time':'today 12-m'}],'category':0,'property':''},
        }

        element = open("textfile.txt","w",encoding="utf-8")
        payload['req'] = json.dumps(payload['req'])

        payload2 = {
            'hl':'en-US',
            'tz':'-120'
        }

        url = 'https://trends.google.com/trends/api/explore'
        url2 = 'https://trends.google.com/trends/api/explore/pickers/category'

        headers = {
            "cookie": "CONSENT=YES+yt.431552762.en+FX+765; SEARCH_SAMESITE=CgQI7ZQB; OGPC=19028269-1:; SID=IggLaXv1gyaaP7Dz6kzO_F-R2ShntSVee-Wpg_0hpG9ikjS1MX8uvmHzBUMlFNbjNQfG6w.; __Secure-1PSID=IggLaXv1gyaaP7Dz6kzO_F-R2ShntSVee-Wpg_0hpG9ikjS1lK80swmLvvRixXLMPo2WlA.; __Secure-3PSID=IggLaXv1gyaaP7Dz6kzO_F-R2ShntSVee-Wpg_0hpG9ikjS1Tm0h6ww29dskATel-7OJEw.; HSID=Ajc_1gDnS_Lcfkg-b; SSID=ATm7uOy04l-PgRaHj; APISID=mxjcbP6VqFtJvwGe/Arv_d63FN5rmaBDRp; SAPISID=PzsC36JbpwqLvTEI/AVOBYP9TteCsitk-8; __Secure-1PAPISID=PzsC36JbpwqLvTEI/AVOBYP9TteCsitk-8; __Secure-3PAPISID=PzsC36JbpwqLvTEI/AVOBYP9TteCsitk-8; NID=511=cc3H-APEmwVARjLy4bVD1d738ZoGW5unnwPgUpIFRXKzUoaOQUq7hLxrW4XYTuOw8T3ozFCprfDDcx-OM4Aw2LGcPNFoOJeLgcxy_mIf6zLrnh4wAm5iVy-7yq5BQYE5NIOA5mDqMcTcOa-EshpKT5i2nwEue-1oz8xlrHvcf3PBm6dgL8U6DdAsb5oshO5FBb7gevAtbd-CuCmZAj7APjweyNQyWLaN_tgZbyrFsFNLYLBwF3MFp1GWuWmZkU4vHWsQkaeSEL7QzZ92hwLNzyit_t77fCh3-B3R2XvSWfFPOa-bMsbpnJxeYUW9LgxIJGhj2o_IHAbrVWL7lDWemYa8WDoy_wMR9BbCTnPwsRl3T85EA-H9Q9LTMsyD29T-vvXRBUMxB9wGa5yy5XC4-G2po6u4DbZ2expWsE6_aTUMSZ1kXvNqNdtujlH1jYpnhuop7kkV78-yh_LPt4PrbebRUiMnQtDs; AEC=AVQQ_LBmsmBmvfrJ7c48BssjEJAxdvKafO_jZY1-TRxAgzeEU_IEFOyoGw; 1P_JAR=2022-03-28-17; SIDCC=AJi4QfHo-AJiKoRnEqj1IJRX-UWP7cTGISADgMfUJUI1TTreYyZyDRS7aHX_5HTLwu6RKgEypA; __Secure-3PSIDCC=AJi4QfEnyLopC7lz10cBLHTKqXOC_zlOeFpgpsD0rkWkDhDaiVk6MPIuQObpUkCbcAb8hDmpEQ",
        }

        get_request = s.get(url, params = payload, headers= headers )

        #element.write(json.dumps(payload) + '\n')
        element.write(get_request.text)
        print(get_request.text)
        element.close()


        return


trends_requester = GoogleTrendsRequest()
trends_requester.test_request()