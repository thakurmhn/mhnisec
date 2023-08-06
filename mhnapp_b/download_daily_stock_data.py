import pandas as pd
import urllib.request
import zipfile
import warnings
warnings.filterwarnings('ignore')

# Download Instrument for URL
def dowonload_instruments():
    url = 'https://directlink.icicidirect.com/NewSecurityMaster/SecurityMaster.zip'
    urllib.request.urlretrieve(url, "Data/SecurityMaster.zip")
    with zipfile.ZipFile("Data/SecurityMaster.zip", 'r') as zip_ref:
        zip_ref.extractall('Data')
    print('instruments downloaded')

dowonload_instruments()


