import investpy
import sys
from datetime import datetime

today = datetime.today().strftime('%d/%m/%Y')

for pair in sys.argv[1:]:
    df = investpy.get_currency_cross_historical_data(currency_cross=pair, from_date='01/01/2010', to_date=today)[
        ['Close', 'Currency']]
    pair = pair.replace('/', '_')
    tod = today.replace('/', '-')
    print('\n scraping {}'.format(pair))
    df.to_csv('database\{}  {}  Until  {}.csv'.format(pair, '01-01-2010', tod))

print("\nFinished scraping all the data!")