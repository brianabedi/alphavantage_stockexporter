from alpha_vantage.timeseries import TimeSeries
import pandas as pd

api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'

ts = TimeSeries(key=api_key, output_format='pandas')

def fetch_ohlc_data(symbol):
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
    return data

# Can use any symbol here
voo_data = fetch_ohlc_data('VOO')

def transform_data(data):
    transformed = []
    data = data.sort_index()

    for i in range(2, len(data)):
        row = {}
        for j in range(3):
            day = data.iloc[i - j]
            row[f'Open{j+1}'] = day['1. open']
            row[f'High{j+1}'] = day['2. high']
            row[f'Low{j+1}'] = day['3. low']
            row[f'Close{j+1}'] = day['4. close']
            row[f'Volume{j+1}'] = day['5. volume']
        transformed.append(row)
    
    return pd.DataFrame(transformed)

transformed_voo = transform_data(voo_data)

transformed_voo.to_csv('transformed_voo.csv', index=False)
