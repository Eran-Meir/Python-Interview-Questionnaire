#############################
#    Name:     Eran Meir    #
#    Question:     3        #
#############################

# Main function. defines the products, checks the lists and prints the number of errors
def main():
    number = 2347623
    print(getSum(number))


# For each digit return the sum of the least significant digit and call recursively divided by 10 without the remainder
# Note: negative numbers will return the same sum of digits regardless to their negativity
def getSum(number):
    if number < 0:
        return getSum(abs(number))
    elif number == 0:
        return 0
    else:
        return number % 10 + getSum(number // 10)


# All the code that is at indentation level 0 gets executed thus, we know that only main() will get executed
if __name__ == '__main__':
    main()