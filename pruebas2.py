import requests
from lxml import html

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

headers = {
    'authority': 'www.portalinmobiliario.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://www.portalinmobiliario.com/venta/departamento/propiedades-usadas',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-419,es;q=0.9',
    'cookie': '_d2id=30bd47eb-42c3-41b2-a962-13078e2034d4-n; _ga=GA1.1.1912636198.1561734910; _fbp=fb.1.1561734910733.628405043; uniqueID=08800a8f-0051-4b24-9799-e9b1d805c097; _hjid=f23ba57d-3024-487f-b630-b5172398d089; PI=hluvrif21rawp4jyk3kx504l; __RequestVerificationToken=UyshJZtYwdUzN9lyEh1bZ6q1wCmO2JB77-Sowtekq8Gmu43xV1eUMMH8R4y1lS5ni041J-U8ddnBtf7mtJ8hjgpaV_U1; AWSELB=7517F7ED0C3C5C3E0C8743D6A3E725F2C642132534377F9EF06CAF69A7F774FA8A907829A9DA8CEB557EF21D08E73AEAFB4646D1A7649FA1F5173424833A26103960BEA6D7; ASPSESSIONIDSCSRQTSC=KOFDBIPBBJCMEDNJHNCJIAGP; idDepartamento=13; _pi_ci=396901228.1568044422; orguseridp=29350808; orgid=CS-090911-b4ddf2b70041d50a99bef014e4879ddd10e242e00d3b5fd587459dcdb9c93fa8-29350808; ssid=ghy-090911-cpGjwTsAlVcEeqhf9EsaIk4DAUIps4-__-29350808-__-1662652440738--RRR_0-RRR_0; orghash=090911-MLCB4f0utHWKdmOTKwbzU84FKbD7kX__RRR_0__RRR_0-29350808; orguserid=ZZ4ZHT9d7d7; ftid=JXGzIa2raXc2pVMEIfWYmpxG4AO3zgSq-1568044404358; orgapi=CS-090911-12b4d2c9f203026d7dfe9e40cbef3f52605a1528836e32f04b2271db07bdce092596fc3a4f5858eb5c34dd47c2733f2ad1eae425d9e7af34e7e7452aa03f9039-29350808; orgnickp=SERGEI.SCHKOLNIK; ml_retry=; ml_regblock=; _gac_UA-20245975-1=1.1568044464.CjwKCAjw9dboBRBUEiwA7VrrzT4bbMOtibrXPtw_4HuNaFb5MH7OO3Mz9uI7nqTsG70AV5ZwXy0sZxoCrhAQAvD_BwE; _gac_UA-30712667-1=1.1568044464.CjwKCAjw9dboBRBUEiwA7VrrzT4bbMOtibrXPtw_4HuNaFb5MH7OO3Mz9uI7nqTsG70AV5ZwXy0sZxoCrhAQAvD_BwE; _gac_UA-46085697-8=1.1568044464.CjwKCAjw9dboBRBUEiwA7VrrzT4bbMOtibrXPtw_4HuNaFb5MH7OO3Mz9uI7nqTsG70AV5ZwXy0sZxoCrhAQAvD_BwE; ASPSESSIONIDSCQTRTSD=DLJLMJDDKPPCHAJANOJFMAMI; ASPSESSIONIDSCTSQTTC=DKJJOAHALDLAGPGFHKDCJLAO; Buscador=Region=356&IDBusquedaUnidadGeopolitica=356&TipoPropiedad=Casa; IdUsuarioASP=48yl396Ra4sd%2b1pDBRmdgg%3d%3d; _ga=GA1.2.1912636198.1561734910; _gac_UA-46085697-8=1.1568044464.CjwKCAjw9dboBRBUEiwA7VrrzT4bbMOtibrXPtw_4HuNaFb5MH7OO3Mz9uI7nqTsG70AV5ZwXy0sZxoCrhAQAvD_BwE; PORTAL=7389B772973A8BCB9C99024FF5F4D0CE2537C4B5CBFDE03B4C6266EEB1F62E309D3DC2E12DF554B57F4C2CE4CFDE1B0531F954911E7B40DF7D5A5AA10AD72DEC55E36AD21E0BF344389FB23F33A68405DA7C0C168BA5EA0F40884AD95C72F8EB5ECA4F6D2AB79B66756B5C541D3D2F1308F8B9CA14569DA6254BA7DC229CD8D6C08DB23AA001891296AA16D1912E00C2F59FA367; _mlt=247ff446-ef36-4309-af2e-4bf06c8f3c29; pin_d2id=30bd47eb-42c3-41b2-a962-13078e2034d4-n; _pi_ga=GA1.2.396901228.1568044422; _d2id=30bd47eb-42c3-41b2-a962-13078e2034d4; __gads=ID=3997df86c1b3ec93:T=1569701571:S=ALNI_MZQ4vo7xng4ZcCT-I178S5nKn5R6w; _hjIncludedInSample=1; _csrf=2fyS9xSl36jtOFfQpCK9oJbX; pin_exp=new; _pi_ga_gid=GA1.2.721703724.1571176961; _hjShownFeedbackMessage=true; c_home=0.0.6-redirect-circular-ref%7C5.2.0; searchbox-currentSearch=eyJvcGVyYXRpb25zIjp7ImxhYmVsIjoiVmVudGEiLCJzZWxlY3RlZCI6InZlbnRhIn0sImNhdGVnb3JpZXMiOnsibGFiZWwiOiJEZXBhcnRhbWVudG9zIiwic2VsZWN0ZWQiOiJ2ZW50YV9kZXBhcnRhbWVudG8ifSwibG9jYXRpb24iOnsidmFsdWUiOiIiLCJzZWxlY3RlZCI6IiJ9LCJmaWx0ZXItbmV3Ijp7ImNoZWNrZWQiOmZhbHNlLCJkaXNhYmxlZCI6ZmFsc2V9fQ==; JSESSIONID=9296F82668DA6347736CCCFA2A7097A1; pmsctx=******IMLC508946895%7C%7CIMLC462815533%7C%7C%7C**; navigation_items=MLC508946895%7C15102019220519-MLC462815533%7C15102019220239-MLC503477416%7C09102019153959-MLC508111572%7C09102019153949-MLC507403795%7C09102019152518',
}

link="https://www.portalinmobiliario.com/venta/sitio/las-condes-metropolitana/5536262-los-dominicos-camino-otonal-la-fuente-uda"

request = requests.get(link, headers3)
print(request)
# headerIndex += 1
# headerIndex = headerIndex % len(headerList)

tree = html.fromstring(request.content)


comunaPath = '//*[@id="productInfo"]/fieldset/span/span[1]'

comuna=tree.xpath(comunaPath)
print(comuna)
