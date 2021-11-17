### Written in PYthon 3.7 #########################################
from bs4 import BeautifulSoup , element
from requests import get
import argparse
import sys

url = 'https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html'

def get_list():
    target = get(url).text
    soup = BeautifulSoup(target, features="html.parser")
    table = soup.table.tbody
    return [[x.td.attrs.get('id'), x.span.string] for x in table.find_all('tr') if isinstance(x, element.Tag)]


def main(curlist):
    a = parser.parse_intermixed_args() 
    if len(sys.argv) <= 1:
        parser.print_help()
        return
    if a.search != False:
        c = a.search
        for x in curlist:
            if c in x[0]:
                print(f'\n 1 EUR = {x[1]} {x[0]} \n')
                return
    elif a.list !=False:
        print(curlist)
        return 
    else:
        return "No action"


if __name__ == "__main__":
    curlist = get_list()
    curname = [x[0] for x in curlist]
    parser = argparse.ArgumentParser(prog='Euro XREF Currency Lookup Tool', epilog=f"Source: ECB Euro Exchange Reference - {url} - No rights can be derived from this information.",add_help=True)
    parser.add_argument('search' ,nargs="?",help='Type a currency shorthand to get its value', default=False,type=str,choices=curname)
    parser.add_argument("-l", "--list", help="Returns list of currencies", action="store_true", default=False)
    args = parser.parse_args()
    main(curlist)

