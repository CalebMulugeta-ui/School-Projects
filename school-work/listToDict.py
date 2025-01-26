sales = [['customer1', 'bread', 5], ['customer1', 'egg', 6.75],['customer1','milk', 4.35],
['customer2', 'bread', 4.5],['customer2', 'egg', 3.6],['customer2','milk', 4.35],
['customer3', 'egg', 3.6],
['customer4', 'bread', 4.5],['customer4','milk', 4.35]]


def listToDictionary(sales):
    d = {}

    #Customer
    for i in range(0, len(sales)):
        customer = sales[i][0]
        if customer not in d:
            d[customer] = [[], 0]

    #Product
    for i in range(0, len(sales)):
        customer = sales[i][0]
        product = sales[i][1]
        d[customer][0].append(product)

    #Price
    for i in range(0,len(sales)):
        price = 0
        price += sales[i][2]
        customer = sales[i][0]
        d[customer][1] += price
    return d

def display(d):
    for i in d:
        print(f"{i} : {d[i]}")

def main():  
    d = listToDictionary(sales)
    display(d)

main()