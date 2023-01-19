#############################
#    Name:     Eran Meir    #
#    Question:     1        #
#############################
import itertools


# Main function. defines the products, checks the lists and prints the number of errors
def main():
    products = ['eggs', 'milk', 'cheese']
    productPrices = [2.89, 3.29, 5.79]
    productSold = ['eggs', 'eggs', 'cheese', 'milk', 'milk']
    soldPrice = [2.89, 2.99, 5.97, 3.29, 3]
    checkListsLength(products, productPrices)
    checkListsLength(productSold, soldPrice)
    numOfErrors = priceCheck(products, productPrices, productSold, soldPrice)
    printErrors(numOfErrors)


# Determines the number of errors in selling prices and returns it.
def priceCheck(products, productPrices, productSold, soldPrice):
    priceDic = createDictionary(products, productPrices)
    return getErrors(productSold, soldPrice, priceDic)


# Receiving a sold products, their selling price and a dictionary of the prices
def getErrors(productSold, soldPrice, priceDic):
    sum = 0
    for (product, price) in itertools.zip_longest(productSold, soldPrice):
        if price != priceDic.get(product):
            sum = sum + 1
    return sum


# Printing the number of errors
def printErrors(numOfErrors):
    print("Total number of errors is: ", numOfErrors)


# Checking that the length of the lists is the same
def checkListsLength(products, prices):
    if len(products) != len(prices):
        print("There was a problem with matching the products and the prices, "
              "please check again the length of the lists you've entered!")
        exit()


# Creating a dictionary from the two lists, there is a assumption that the lengths were checked and are the same.
def createDictionary(products, productPrices):
    return {products[i]: productPrices[i] for i in range(len(products))}


# All the code that is at indentation level 0 gets executed thus, we know that only main() will get executed
if __name__ == '__main__':
    main()