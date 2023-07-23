from breeze_connect import BreezeConnect
from breeze_deploy.bzutils import BzUtils

bzutils = BzUtils()

# creds dict
creds = bzutils.get_api_creds()
breeze = BreezeConnect(api_key=creds['api_key'])
breeze.generate_session(api_secret=creds['app_secret'],
                        session_token=creds['session_token'])

print(breeze.get_customer_details(api_session=creds['session_token']))

