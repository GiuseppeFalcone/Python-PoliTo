
def main():
    sales, customers = list(), list()
    flag = True
    while flag:
        print("Inserting the names of the customers and their purchase amount \nTo stop insert \'basta\"")
        name = input("Enter the Name of the customer: ")
        if name.lower() == 'basta':
            flag = False
        else:
            purchase = float(input("Enter the amount of purchase: "))
            sales.append(purchase)
            customers.append(name)
    name_of_the_best_customer(sales, customers)

def name_of_the_best_customer(sales, customers):
    largest = max(sales)
    ind_largest = sales.index(largest)
    print(f"Best customer is: {customers[ind_largest]} with {max(sales)} of purchases")

if __name__ == '__main__':
    main()
