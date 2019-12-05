### Euro XREF Currency Lookup ###
from requests import get
from bs4 import BeautifulSoup
import argparse


gru = get("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml").text
soup = BeautifulSoup(gru, features="html.parser")

cdate = soup.cube.find("cube").attrs.get("time")
cc = soup.cube.cube.find_all("cube")


def currList(data=cc):
    _l = []
    for x in cc:
        x = list(x.attrs.values())[0]
        _l.append(x)
    return _l


def returnRate(my_curr="CZK", data=cc):
    for x in cc:
        if x.attrs.get("currency") == my_curr:
            print(
                "\n1 EUR = {} {} ({})\n".format(
                    list(x.attrs.values())[1], my_curr, cdate
                )
            )


def main():
    my_curr = input("Please type the currency shorthand or press Enter to continue")
    if len(my_curr) <= 1:
        currList()
    returnRate(my_curr)
    print(
        "\n\nSource: ECB (European Central Bank Euro Exchange Referral - https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml )\n"
    )


if __name__ == "__main__":
    main()

