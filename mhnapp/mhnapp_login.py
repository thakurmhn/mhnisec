from breeze_deploy.breeze_auth import BzAuth
from breeze_deploy.authutils import get_api_creds
import yaml


def login_to_isec():
    # get api creds from yaml
    app_creds = get_api_creds()

    # login to breeze api using api_key and secret loaded from yaml
    app_key = app_creds['myapp']['api_key']
    app_secret = app_creds['myapp']['secret_key']
    isec_auth = BzAuth(api_key=app_key, secret_key=app_secret)

    # store session token to make subsequent requests

    token_file = 'secret_token.yaml'
    mhnapp_session_token = isec_auth.session_token
    mhnapp_app_key = app_key

    f = open(token_file, 'w')
    f.write(f"api_key: {mhnapp_app_key}\napp_secret: {app_secret}\nsession_token: {mhnapp_session_token}")
    f.close()



def get_session_creds():
    _secret_dict = ''
    with open('secret_token.yaml', 'r') as file:
        isec_secret = yaml.load(file, Loader=yaml.FullLoader)

        _secret_dict = isec_secret
    return _secret_dict




if __name__ == '__main__':
    login_to_isec()
   # print(get_session_creds())
