# Exercise 1 - Given two integer numbers return their product. If the product is greater than 1000, then return their sum.

x = 500
y = 502
if x + y > 1000:
	print(x + y)

# Exercise 2 - Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration print the sum of the current number and previous number

a = 1
b = 11
c = 111
d = 1111
e = 1000
f = 1001
g = 1011
h = 2
i = 22
j = 222
print(a+b, b+c, c+d, d+e, e+f, f+g, g+h, h+i, i+j)

# Exercise 3 - Given a string, display only those characters which are present at an even index number.

str = "Amazon Web Server"
modified_string = str[::2]
print(modified_string)

#Exercise 4 - Given a list of numbers, return True if first and last number of a list is same

def isFirst_And_Last_Same(numberList):
  firstElement = numberList[0]
  lastElement =  numberList[-1]
  if(firstElement == lastElement):
    return True
  else:
    return False
numList = [10, 20, 30, 40, 10]
print("The first and last number of a list is same")
print("result is", isFirst_And_Last_Same(numList))

# Exercise 5 - Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

def findDivisible(numberList):
    print("Given list is ", numberList)
    print("Divisible of 5 in a list")
    for num in numberList:
        if (num % 5 == 0):
            print(num)
numList = [10, 20, 33, 46, 55]
findDivisible(numList)

# Exercise 6 - Return the count of sub-string “Emma” appears in the given string

