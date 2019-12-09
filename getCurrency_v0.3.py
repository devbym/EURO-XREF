from bs4 import BeautifulSoup , element
from requests import get

target = get('https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html').text

soup = BeautifulSoup(target, features="html.parser")
table = soup.table.tbody

currlist = [[x.td.attrs.get('id'), x.span.string] for x in table.find_all('tr') if isinstance(x, element.Tag)]


for x in currlist:
    print(f' 1 EUR = {x[1]} {x[0]}')
