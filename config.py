main_url = 'https://www.kinopoisk.ru/'
cookie_string = 'yashr=8176113751727348510; my_perpages=%5B%5D; mda_exp_enabled=1; gdpr=0; _ym_uid=1728058168710601950; stars_sort_v5=01.170.10.70.181; hideBlocks=131072; yandexuid=9189060501707669232; yuidss=9189060501707669232; yp=1734200740.yu.9189060501707669232; ymex=1736706340.oyu.9189060501707669232; _csrf=xmzUgVQr5nphg7t14TkepPZa; desktop_session_key=33314f0b9344166a20dcbc9fab6f0bafa0e99ab5666e63e4821f7a9aa62af7a9aa1864ea94ae4b79f9a108156a41acbfaa77be63eede818c64c46bfb946a9e327db2e4ffaec63a49b448c7a8273a3adf8f73e809b4e82005e307d2131383d9755e8995f1f6c5bec88664e3b5404d2e95; desktop_session_key.sig=AVyQJabtoCtEf6E0o5BffrXOPFk; location=1; coockoos=17; i=jms/BGtYWOVBOAhhK0bJsi0UuCEFq9P6l2qo/S6MzSIY3PWyNnG6TUDw5FG5XqeNlhfNp63for33AfkZzaBgVJqi/jI=; PHPSESSID=86e1139863e125d13f09ad1c0d150c78; _csrf_csrf_token=m-tMNckhjxBOMK7-aDYuvieZhZ46jJXWLe2p3MeXTB0; yandex_login=sukhmad; L=YS5zXgBiXkQERkR7BwNwXm1ZUwFhQHNcPkA6H1gGNQ==.1745419017.16128.348351.d3f619b5fe13d873ccbf08dfd56596f8; uid=80195954; crookie=+J5BHhs37/7k0pdbolZfhGg63jGEBK5wB+H9tKYbELlTK6xDsJTIp0kS399aX984nZoKrEPSrIqMFU/4A4BOniaFzYA=; cmtchd=MTc0NTU5Mzg5MDY1NQ==; disable_server_sso_redirect=1; ya_sess_id=3:1745839271.5.0.1745419017952:No_5Aq8E2BSijgiEANADKg:428e.1.2:1|1162743704.0.2.3:1745419017|30:10234382.517703.y4C6BN4AqKSzy0W2MWRqzbIwKiA; sessar=1.1201.CiD5lJBhWbQqtHhvymbXQ11Tr-pPZOwWgxJu2rRJle60Mg.-6lnv_f8NhnMO6sE5nFjvgfumn7qxkDRnZMcHRdhL3k; ys=c_chck.3444873726#udn.cDrQnNCw0YDQuNGPINCR0YPQu9GL0YfQtdCy0LA%3D; mda2_beacon=1745839271579; sso_status=sso.passport.yandex.ru:synchronized; no-re-reg-required=1; kdetect=1; mobile=no; yandex_plus_metrika_cookie=true; _yasc=XNCALHMs44vwMFqQ6zyl5wbYkjXX0Ifsvpjaogkcm6ZGkUfob6IGtWxWNf3DqICBXMTB; _ym_d=1745842193; sgst=searchRequest-%D0%B0%D0%B2%D0%B0%D1%82%D0%B0%D1%80'
def parse_cookies(cookie_string):
    cookies = []
    for cookie in cookie_string.split(';'):
        name, value = cookie.strip().split('=', 1)
        cookies.append({'name': name, 'value': value, 'path': '/'})
    return cookies

cookies = parse_cookies(cookie_string)

class APIConfig:
    api_base_url = "https://api.kinopoisk.dev"
    api_token = ""

    def __init__(self):
        self.headers = {
            "X-API-KEY": self.api_token,
            "Content-Type": "application/json"
        }
