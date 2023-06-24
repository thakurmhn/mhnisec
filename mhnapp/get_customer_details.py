from pprint import pprint
from breeze_connect import BreezeConnect
from mhnapp_login import get_session_creds

secret_dict = get_session_creds()
app_key = secret_dict['api_key']
app_secret = secret_dict['app_secret']
api_session_token = secret_dict['session_token']

breeze = BreezeConnect(api_key=app_key)
bz_session = breeze.generate_session(api_secret=app_secret, session_token=api_session_token)


customer_details = breeze.get_customer_details(api_session=api_session_token)
pprint(customer_details)
