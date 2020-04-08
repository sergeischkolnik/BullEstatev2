import requests
from lxml import html
import math
import agentCreator
import time
import random
from bs4 import BeautifulSoup
import datetime
import pymysql as mysql
import uf

headers1 = {
    'authority': 'www.portalinmobiliario.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'none',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-US,es;q=0.9,es-419;q=0.8,en;q=0.7',
    'cookie': '_d2id=10753c94-136c-426d-b536-52f4bdc9ad06-n; PI=d50qlpmdqz1qdv4lynbllh0w; __RequestVerificationToken=NK9YOkOtc3k6bUsfzF0OyZa_kYCBJlPtdTSyYK97lihubPSwAGhZp8pigJ1j5S6LOPG3PlvaiaCMpSoomr7Ez00OFHw1; uniqueID=4df06d9b-bd2e-4565-bff5-9d30c15ea7b2; _ga=GA1.1.434386957.1551705638; _hjid=f5243996-1bed-4c3a-9d9b-0468976dd33e; Buscador=Region=356&IDBusquedaUnidadGeopolitica=356&TipoPropiedad=Departamento; AWSELB=7517F7ED0C3C5C3E0C8743D6A3E725F2C6421325348258AB2B2B6C24C55B97E7B421F62FEDE1E3B33663FE99C845602640543858273DAF905910FD5E38A1B2D3F9329B42B1; _mlt=d8ec613f-94d1-479b-9224-07a09b8ecc69; pin_d2id=10753c94-136c-426d-b536-52f4bdc9ad06-n; _pi_ga=GA1.2.901507403.1570560325; _pi_ci=901507403.1570560325; _d2id=10753c94-136c-426d-b536-52f4bdc9ad06; _csrf=wiPGYePC-rZQJpMMJMEqYZv_; searchbox-currentSearch=eyJvcGVyYXRpb25zIjp7ImxhYmVsIjoiVmVudGEiLCJzZWxlY3RlZCI6InZlbnRhIn0sImNhdGVnb3JpZXMiOnsibGFiZWwiOiJEZXBhcnRhbWVudG9zIiwic2VsZWN0ZWQiOiJ2ZW50YV9kZXBhcnRhbWVudG8ifSwibG9jYXRpb24iOnsidmFsdWUiOiJwcm92aWRlbmNpYSIsInNlbGVjdGVkIjoiIn0sImZpbHRlci1uZXciOnsiY2hlY2tlZCI6ZmFsc2UsImRpc2FibGVkIjpmYWxzZX19; JSESSIONID=4EE983A7EB482E20624672E4E17AF4E8; pmsctx=******IMLC507223027%7C%7CIMLC507775718%7CIMLC508093497%7C%7C**; navigation_items=MLC507223027%7C14102019125752-MLC507775718%7C14102019125042-MLC508093497%7C08102019190408-MLC507769027%7C08102019184813-MLC507748684%7C08102019184550; c_home=0.0.6-redirect-circular-ref%7C5.2.0; pin_exp=new; _pi_ga_gid=GA1.2.1582383825.1571164864',
}

headers2 = {
    'authority': 'www.google.com',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'dpr': '1',
    'viewport-width': '1920',
    'rtt': '100',
    'downlink': '4.35',
    'ect': '4g',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'sec-fetch-mode': 'nested-navigate',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'cross-site',
    'referer': 'https://www.portalinmobiliario.com/MLC-509232849-sn-martin575-vistamar-2d-lado-playacasino-cestacionamient-_JM',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-US,es;q=0.9,es-419;q=0.8,en;q=0.7',
    'cookie': 'NID=189=d1T2vt5csSsrUd5KBdpdFAFv6Etc2ggAwQC5hSdVVPg_x0VGNrkl8Qxw6Pgyleov_j7CXq0qncsjCMtjOwniOpJ__p5_OmGwev7LBVyMc4o9Vw8Lsw2et0j-gFbv5l8MyIA-F9Em4w_2wFMFJVhtIT4Hewe6bybpVureG_4keJA',
    'Sec-Fetch-Mode': 'no-cors',
    'Referer': 'https://www.google.com/recaptcha/api2/webworker.js?hl=es-419&v=xw1jR43fRSpRG88iDviKn3qM',
    'Origin': 'https://www.google.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Content-Type': 'text/plain',
    'Upgrade-Insecure-Requests': '1',
}

headers3 = {
    'authority': 'www.portalinmobiliario.com',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'dpr': '1',
    'viewport-width': '1920',
    'rtt': '50',
    'downlink': '10',
    'ect': '4g',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'none',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-US,es;q=0.9,es-419;q=0.8,en;q=0.7',
    'cookie': '_d2id=6f449319-f0db-4852-b6e6-4473d31fff5d-n; _mlt=6a76c9f9-c776-47f0-bf16-8e3bf8ea1091; uniqueID=15965c7c-9edb-43df-9c85-f4dac69268ea; _pi_ga=GA1.2.2067791864.1571058095; _pi_ci=2067791864.1571058095; _d2id=6f449319-f0db-4852-b6e6-4473d31fff5d; _hjid=eb71f50e-8d3c-489e-9792-11a7f5617768; _csrf=WaWxAUx6HMKTob31r4cf-3mz; c_home=0.0.6-redirect-circular-ref%7C5.2.0; pin_d2id=6f449319-f0db-4852-b6e6-4473d31fff5d; pin_exp=new; _pi_ga_gid=GA1.2.996463285.1571231021; JSESSIONID=FFF44D40DDF915344000286569A64337; pmsctx=******IMLC509232849%7C%7CIMLC507223027%7C%7C%7C**; navigation_items=MLC509232849%7C16102019130355-MLC507223027%7C14102019130557; _pi_dc=1',
}


headerList = [headers1,headers2,headers3]


dormitorios = ["sin-dormitorios",
                "1-dormitorio",
                "2-dormitorios",
                "3-dormitorios",
                "mas-de-4-dormitorios"]
banos = ["_Banos_1",
          "_Banos_2",
          "_Banos_3",
          "_Banos_4",
          "_Banos_5-o-mas"]