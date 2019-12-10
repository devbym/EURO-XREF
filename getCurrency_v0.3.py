from bs4 import BeautifulSoup , element
from requests import get
import argparse
import sys


parser = argparse.ArgumentParser(prog='Euro XREF Currency Lookup Tool', epilog="\n\nSource: ECB European Central Bank Euro Exchange Referral - https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml \n")
parser.add_argument('search' , nargs='?', help='Type a currency shorthand to search', default=False)
parser.add_argument("-l", "--list", help="Return list of currencies and exit", action="store_true", default=False)

args = parser.parse_args()

def get_list():
    target = get('https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html').text
    soup = BeautifulSoup(target, features="html.parser")
    table = soup.table.tbody
    return [[x.td.attrs.get('id'), x.span.string] for x in table.find_all('tr') if isinstance(x, element.Tag)]

if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

if args.search:
    c = args.search
    for x in get_list():
        if c in x[0]:
            print(f' 1 EUR = {x[1]} {x[0]}')

if args.list:
    for x in get_list():
        print(x[0])




