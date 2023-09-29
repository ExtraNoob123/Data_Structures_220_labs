#Lab Assignment 5
#Done by Ms Rodsy Tahmid (Id: 20101021)




############################################################################
#Recursion (Lecture-9)

#Task-1:
#1(a)
#function fact which takes n as argument
def fact(n):
    # if n == 0
    if n == 0:
        return 0
    elif n == 1:
        # return 1
        return 1
    else:
        return n*fact(n-1)

#ask user to enter n
n = int(input("Enter n: "))
#printing factorial of n
print("Factorial of",n,':',fact(n))
#################################################

#1(b)
#function fib which takes n
def fib(n):
   #if n == 0 or n == 1
   if n == 0:
       #return n
       return n
   elif n == 1:
       return n
   #else
   else:
       return fib(n - 1) + fib(n - 2)
   
#ask user to enter n
n = int(input("Enter n: "))

#printing nth fibonacci number
print(n,'th fibonacci number: ', fib(n))
#################################################

#1(c)
#function printElements which takes array and n
def printElements(array, n):
   #if n == 0
   if(n == 0):
       #print array[n]
       print(array[n], end=' ')
   #else
   else:
       #calling printElements(array,n-1)
       printElements(array, n - 1)
       #print array[n]
       print(array[n], end=' ')

#Tester
array1 = [1, 2, 3, 4, 5]
#calling printElements with array and len(array)-1
printElements(array1, len(array1) - 1)
#################################################

#1(d)
#exponentiation
#function powerN which takes base and n
def powerN(base, n):
  if (n == 0):
    return 1
  else:
    # return base*powerN(base,n-1)
    m=powerN(base,n-1)
    return base*m

#Tester
print(powerN(3, 1))
print(powerN(3, 2))
print(powerN(3, 3))
# calling powerN with 3 and 3
# printing return value

############################################################################


#Task-2:
#2(a)
#Decimal to Binary Converter

def deci_bin(n):
    if (n==0):
        return 0
    else:
        deci_bin(int(n / 2))
        print(n % 2, end="")
#Tester
deci_bin(15)
#################################################

#2(b)
#sum of elements in a non-dummy headed singly linked list

class Node():
    def __init__(self, items=None, link=None):
        self.items = items
        self.link = link


class Singly_linkedL:
    def __init__(self):
        self.Start_Node = Node()

        self.sum = 0
        pass


    def add_last(self, this_item):
        New_Node = Node(this_item)

        if (self.Start_Node.items == None):  # first node
            self.Start_Node = New_Node
        else:
            temp = self.Start_Node
            while temp.link != None:
                temp = temp.link
                # pass
            # temp = the last node
            temp.link = New_Node

    def add_list(self, list):
        for i in list:
            V = str(i)
            self.add_last(V)

    # print
    def print_(self):
        Print_Node = self.Start_Node
        # print(Print_Node.items, end=" ")
        sum = int(Print_Node.items)
        while Print_Node.link != None:
            Print_Node = Print_Node.link
            # print(Print_Node.items, end=" ")
            sum = sum + int(Print_Node.items)
        print()
        print(sum)

    def recursion_print(self, Start_Node):
        sum = 0
        if Start_Node == None:
            return 0
        else:
            return int(Start_Node.items) + int(self.recursion_print(Start_Node.link))


input = Singly_linkedL()
input.add_list(([10, 20, 30, 40, 150]))
# print("Hello",input.Start_Node.items)
# print("Hello",input.Start_Node.next.items)
# input.print_()
print(input.recursion_print(input.Start_Node))
#################################################

#2(c)
#non-dummy headed singly linked list in reverse order
#recursive algo

class Node():
    def __init__(self, items=None, link=None):
        self.items = items
        self.link = link


class Singly_LinkedL:
    def __init__(self):
        self.Start_Node = Node()

        self.sum = 0
        pass

    def add_last(self, this_item):
        New_Node = Node(this_item)

        if (self.Start_Node.items == None):  # first node
            self.Start_Node = New_Node
        else:
            temp = self.Start_Node
            while temp.link != None:
                temp = temp.link
                # pass
            # temp = the last node
            temp.link = New_Node

    def add_list(self, list):
        for i in list:
            V = str(i)
            self.add_last(V)

    # print
    def print_(self):
        Print_Node = self.Start_Node
        # print(Print_Node.items, end=" ")
        sum = int(Print_Node.items)
        while Print_Node.link != None:
            Print_Node = Print_Node.link
            # print(Print_Node.items, end=" ")
            sum = sum + int(Print_Node.items)
        print()
        print(sum)

    def recursion_print(self, Start_Node):
        sum = 0
        if Start_Node == None:
            return 0
        else:
            return int(Start_Node.items) + int(self.recursion_print(Start_Node.link))

    def Forward_Node(self, Start_Node):  # return as string, all element of nodues in forward manner
        if Start_Node == None:
            return
        else:
            return str(Start_Node.items) + str(self.Forward_Node(Start_Node.link))

    def reverse_S_recur(self, S):
        if len(S) == 0:
            return S
        else:
            return self.reverse_S_recur(S[1:]) + S[0]

    def Reverse_Node_Print(self, Start_Node):  # takes Start_Node and try to reverse print all data as a S

        S = str(self.Forward_Node(Start_Node))
        New_List = list(S)
        New_List = New_List[:-1]
        New_List = New_List[:-1]
        New_List = New_List[:-1]
        New_List = New_List[:-1]
        S = ""
        for i in New_List:
            S = S + str(i)
        print(S)
        print(self.reverse_S_recur(S))


input = Singly_LinkedL()
input.add_list(([10, 20, 30, 40]))

input.Reverse_Node_Print(input.Start_Node)

############################################################################


#Task-3:
def hocBuilder(n):
    if n == 0:
        return 0
    elif n == 1:
        return 8
    elif n == 2:
        return 5 + hocBuilder(n-1)
    else:
        return 5*(n-2) + hocBuilder(n-1)

##################################################
#Tester Class

L1 = hocBuilder(1)
L2 = hocBuilder(2)
L3 = hocBuilder(3)

print(L1)
print(L2)
print(L3)


############################################################################


#Task-4:
#4(a)
#Left Right-Angled Triangle
# function print_ which prints row
def print_(n, index): #row printing
    if (n == 0): # base case
        return

    print(index, end=" ")
    index += 1

    # recursively calling function print_
    print_(n - 1, index)


# this function is to to print the pattern/ column
def Line(n, index):
    # this is the base case
    if (n == 0):
        return
    print_(index, 1)  # calls function print_ which prints row of the pattern
    print("\n", end="")

    # recursively calling Line()
    Line(n - 1, index + 1)


n = 5
Line(n, 1)  # calls function Line()
#################################################

#4(b)
#Left Right-Angled Triangle
# this function is to print spaces of the left side of the triangle
def Space_print(gap):
    # this is the base case
    if (gap == 0):
        return

    print(" ", end=" ")

    # this below line recursively calls  printSpace
    Space_print(gap - 1)


# this function is to print the row
def print_(n, index): #row printing
    # this is the base case
    if (n == 0):
        return;

    print(index, end=" ")
    index += 1

    # this below line recursively calls  print_
    print_(n - 1, index)


# this function is to to print the pattern/ column
def Line_Print(n, m):
    # this is the base case
    if (n == 0):
        return

    Space_print(n - 1)  # calls function printSpace for printing space in left side of triangle
    print_(m - n + 1, 1)  # calls function printRow for printing row of the the pattern
    print()

    # recursively calling pattern()
    Line_Print(n - 1, m)


n = 5
Line_Print(n, n)  # calls function patternPrint

############################################################################


#Task-5:
class FinalQ:
    def print(self, array, idx):
        if (idx < len(array)):
            profit = self.calcProfit(array[idx])  # calls function calcProfit
            # below lines prints the investment and profit
            print(str(idx + 1) + ". Investment: " + str(array[idx]) + "; Profit: " + str(profit))
            self.print(array, idx + 1)  # recursively calls print function

    def calcProfit(self, investment):
        if investment <= 25000:  # checks if investment is less than 25000 then 0.0 is returned
            return 0.0
        else:  # this else executes when investment is not less than 25000
            data = investment - 100000
            data = data / 100
            data = data + data + data + data + data + data + data + data
            return data + 3375.0  # returns sum of data and 3375.0


# Tester code
array = [25000, 100000, 250000, 350000]
f = FinalQ()
f.print(array, 0)