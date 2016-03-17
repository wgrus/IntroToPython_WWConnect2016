from __future__ import print_function #(only enter this line if you are using python 2)

fo = open('data/produce.txt', 'rb')
produce_price={}
for line in fo:
    if not line.startswith('#'):
        columns = line.split("\t")
        #print columns
        if not produce_price.get(columns[1]):
            produce_price[columns[1]] = {}
        produce_price[columns[1]]['unit'] = columns[2]
        produce_price[columns[1]]['unit_price'] = columns[3].rstrip()
for produce in produce_price:
    print("A ", produce, " is ", produce_price[produce]['unit_price'], " per ", produce_price[produce]['unit'])