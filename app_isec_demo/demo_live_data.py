from breeze_deploy.breeze_auth import BzAuth
from pprint import pprint

app_creds = BzAuth._get_api_creds()

isec_auth = BzAuth(api_key=app_creds['demo_app']['api_key'],
                       secret_key=app_creds['demo_app']['secret_key'],
                       )

bz_conn = isec_login._isec_login()
bz_live = isec_login._conn_to_live_data()





bz_disconn = isec_login._disconnect_live_data()

