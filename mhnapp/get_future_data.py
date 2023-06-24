import pandas as pd

scrip = pd.read_csv("Data/FONSEScripMaster.txt")
scrip = scrip[['Token', 'InstrumentName', 'ShortName', 'Series','ExpiryDate', 'StrikePrice', 'OptionType', 'ExchangeCode']]
print(scrip.head())
