from breeze_deploy.breeze_auth import BzAuth
import yaml
from yaml.loader import BaseLoader

def get_api_creds():
    _secret_file = '/home/mohan/icicidirect-api-keys/app_secrets.yaml'
    app_secrets_dict = ''
    with open(_secret_file, 'r') as stream:

        try:
            # Converts yaml document to python object
            app_secrets_dict = yaml.load(stream, Loader=BaseLoader)
            for key, val in app_secrets_dict.items():
               print(key, " : ", val, "\n")
        except yaml.YAMLError as e:
            LOG.info(e)

    return app_secrets_dict

def login_to_isec():

    app_creds = get_api_creds()
    app_key = app_creds['myapp']['api_key']
    app_secret = app_creds['myapp']['secret_key']

    isec_auth = BzAuth(api_key=app_key, secret_key=app_secret)

    isec_auth.get_session_token()


if __name__ == '__main__':

    login_to_isec()