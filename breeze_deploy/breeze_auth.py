from breeze_connect import BreezeConnect
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import json
import urllib.parse


import logging
LOG = logging.getLogger(__name__)


class BzAuth:
    """
    Class to create login to Isec breeze API
    :param api_key
    :param secret_token
    """

    def __init__(self, api_key, secret_key):

        self.api_key = api_key
        self.secret_key = secret_key
        self.encoded_api_key = self._get_encoded_api_key()
        self.session_token_gen_url = 'https://api.icicidirect.com/apiuser/login?api_key=' + self.encoded_api_key
        self.session_token = self._get_session_token()


    def _isec_login(self):
        _bz_conn = BreezeConnect(api_key=self.api_key)
        _bz_conn.generate_session(api_secret=self.secret_key, session_token=self.session_token)

        return _bz_conn

    def _get_encoded_api_key(self):
        encoded_api_key = urllib.parse.quote(self.api_key)
        return encoded_api_key

    def _get_session_token(self):

        _session_token = ''
        _caps = DesiredCapabilities.CHROME
        _caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        _driver = webdriver.Chrome(desired_capabilities=_caps)

        _driver.get(self.session_token_gen_url)
        sleep(60)
        _logs_raw = _driver.get_log('performance')
        _logs = [json.loads(lr["message"])["message"] for lr in _logs_raw]

        _nw_logs = _logs
        _r_lines = []
        for entry in range(len(_nw_logs)):
            if _nw_logs[entry]["method"] == "Page.frameScheduledNavigation" and "url" in _nw_logs[entry]["params"]:
                # print(_nw_logs[i]['params']['url'])
                _r_lines.append(_nw_logs[entry]['params']['url'])

                for line in _r_lines:
                    if 'apisession' in line:
                        _session_token = line.split('=')[1]
                        _driver.quit()

        _session_token = int(_session_token)
        return _session_token


