#############################
#    Name:     Eran Meir    #
#    Question:     4        #
#############################
import sys


# Main function, gets the input from the user and prints the result
def main():
    print(getInputFromUser())


# Here we get the input from the user and then we calculate the maximum "Going only forward"
def getInputFromUser():
    stop = False
    count = 0
    max = -sys.maxsize
    print("Please enter your sequence, numbers after 0 won't be read: ", end='')
    stream = input().split()
    while not stop:
        for s in stream:
            s = int(s)
            if s == 0:
                stop = True                 # We got a 0, stop
                if count == 0:
                    return -1               # We stopped and no numbers were given
                else:
                    return (max, count)     # We stopped and we have a maximum
            elif s > max:
                max = s                     # Got a new maximum candidate, it's the biggest so far
                count = 1                   # First time seeing this new maximum, set it's count to 1
            elif s == max:
                count = count + 1           # We got the current maximum again, increment
        stream = input().split()            # Keep reading the lines from the keyboard


# All the code that is at indentation level 0 gets executed thus, we know that only main() will get executed
if __name__ == '__main__':
    main()