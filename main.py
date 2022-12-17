import requests
from bs4 import BeautifulSoup
import re
import numpy as np

ebay_url = "https://www.ebay.co.uk/sch/i.html?_dcat=74469&_fsrp=1&rt=nc&_nkw=Electric+bikes&Bike%2520Type=E%252DCity%2520Bike&_sop=10&_udlo=100"
#response = requests.get(ebay_url)





def price():

    print(response)

    soup = BeautifulSoup(response.text, "html.parser")

    price_find = str(soup.findAll("span", class_ = "s-item__price"))
    a = price_find.split(",")
    #a = price_find.split(",")
    #print(price_find)
    #print(a)
    first_price = a[1]
    
    print(first_price)
    
   
    get_price = re.findall(r"[+-]?\d*\.\d+|\d+", first_price)
    convert_to_string = "".join(get_price)  # перевести з списка в string з join
    
    #b = list(np.float_(get_price))  # перевести дані в списку з string в float з numpy.float__(list_name)
    #print(b)
    price = int(convert_to_string)  # перевести дані з string ("") в int (1, 2, 3, 111, 23452) з int()
    print(price)
    #number = [print(i) for i in first_price.split() if i.isdigit()]
    #print(number)

    if price > 100 and price < 500:
        print("working")
#price()

run = True
while run:
    response = requests.get(ebay_url)
    price()



#if __name__ == "__main__":

