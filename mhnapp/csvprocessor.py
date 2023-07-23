import pandas as pd
import os


class CsvProcessor:

    def __init__(self):

        self.csv_file = f"{os.getcwd()}/Data/NSEScripMaster.txt"

    def get_icici_stock_codes(self):
        exchange_codes = []
        df = pd.read_csv(self.csv_file)
        #print(df.loc)

        # remove extra "" from column names
        df = df[[' "ShortName"', ' "CompanyName"', ' "ExchangeCode"', ' "Series"']]
        column1 = [' "ShortName"', ' "CompanyName"', ' "ExchangeCode"', ' "Series"']
        column2 = ['ShortName', 'CompanyName', 'ExchangeCode', 'Series']
        rename_col = dict(zip(column1, column2))
        df.rename(columns=rename_col, inplace=True)
        column_series = df.Series
        column_exchangecode = df.ExchangeCode
        column_company = df.CompanyName

        for ex_code, series in zip(column_exchangecode, column_series):
            if series == 'EQ':
                exchange_codes.append(ex_code)


        icic_codes = []
        
        
        for i in range(0, len(exchange_codes)):
            s = df.loc[df.ExchangeCode == exchange_codes[i]]
            icic_codes.append(s.iloc[0, 0])
            i = i + 1
            
        return icic_codes

   

if __name__ == '__main__':

    csv = CsvProcessor()
    stock_codes = csv.get_icici_stock_codes()

    print(stock_codes)
