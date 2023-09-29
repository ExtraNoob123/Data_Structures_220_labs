#Lab Assignment 1
#Done by Ms Rodsy Tahmid (Id: 20101021)


############################################################################
#Linear Arrays


#Ans1)
#left shifting an array by k places


def shiftLeft(a, k):
    i = 0# pointer at the first index of source


    while (i<k):
        source[i] = source[i+k] #shift elements k places to the left


        i = i+1
        
    while (i>=k):
        source[i] = 0 # setting last k values to 0
        i = i+1
        if i == len(a):
            break




source = [10, 20, 30, 40, 50, 60]
shiftLeft(source, 3)
print(source)
############################################################################


#Ans2)
#left rotating an array by k place
def rotateLeft(a, k):
    temp = a.copy() #copying array in temp


    i = 0
    while (i<k):
        a[len(a)-k+i] = temp[i]  #setting first k values to last values
        
        i = i+1


    i=0
    if len(a)%2==0:
        while(i < k):
            a[i] = temp[i+k] #setting last k values to first values
            i = i+1
        
    else:
        while(i < k-1):
            a[i] = temp[i+k] #setting last k values to first values
            i = i+1


source = [10, 20, 30, 40, 50, 60]
rotateLeft(source, 3) #k =3
print(source)
############################################################################


#Ans3)
#removing a value in an array(in index 2)
def insert(s, size, index):
    if(size == len(s)):
        print('no space in array!')
        return
    if (index <0 or index > size):
        print('wrong index!')
        return
    i = size - 1
  
    s.remove(s[index])
    s.append(0)


source = [10, 20, 30, 40, 50, 0, 0]
insert(source, 5, 2)
print(source)
############################################################################


#Ans4)
#removing a value in an array(in index 2)
def insert(s, size, element):
    if(size == len(s)):
        print('no space in array!')
        return
    
    for i in range(0, size, 1):
        if s[i] == s[i+1] and s[i]==element:
            s.remove(s[i+1])
            s.append(0)
        if s[i]==element:
            s.remove(element)
            s.append(0)




source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
insert(source, 5, 2)
print(source)
############################################################################


#Ans5)
def sumEqual(a):
    y=(len(a)//2)+1
    z = 0
    for x in range(0, y, 1):
        sum1 = 0
        sum2 = 0
        for i in range (len(a)-1, x, -1):
            sum2=sum2 + a[i]
    
        for j in range(0, i, 1):
            sum1 = sum1 + a[j]


        if sum1 == sum2:
            print("true")
            z = z + 1
        else:
            x = x + 1 
    if z == 0:
        print("false")
        
Input1 = [1, 1, 1, 2, 1]
Input2 = [2, 1, 1, 2, 1]
Input3 = [10, 3, 1, 2, 10]
sumEqual(Input1)
sumEqual(Input2)
sumEqual(Input3)
############################################################################


#Ans6)
def arraySeries(n):
    a = [0]*(n*n)
    w=n*n #16
    for i in range(w-1, (w-1)-n, -1):
        # 15 # 11
        a[i]=w-i #4


    x =n*(n-1) #12
    for i in range(x-1, (x-1)-(n-1), -1):
        # 11 # 8
        a[i]=x-i #3
    
    y =n*(n-2) #8    
    for i in range(y-1,(y-1)-(n-2), -1):
        # 7 # 5
        a[i] = y-i #2
    
    z =n*(n-3) #4    
    for i in range(z-1,(z-1)-(n-3), -1):
        # 3 # 2
        a[i] = z-i #1
    print(a)
    
N2 = 2
N3 = 3
N4 = 4
arraySeries(N2)
arraySeries(N3)
arraySeries(N4)
############################################################################


#Ans7)
def bunch(a):
    b = []
    c = []
    if len(a)%2==0:
        for i in range(0, len(a)-2, 1):
            if a[i]==a[i+1]:
                b.append(a[i])
                b.append(a[i])     
    else:
        for i in range(0, len(a)-2, 1):
            if i == len(a)-3:
                b.append(a[i])
                b.append(a[i])
                b.append(a[i])              
            else:
                if a[i]==a[i+1]:
                    b.append(a[i])
                    b.append(a[i])
    for i in range(0, len(b), 1):
        max=0
        if max==4 and i==len(b)-3:
            break
        if max==3 and i == len(b)-2:
            break
        if i+3 == len(b):
            b.append(0)
        if b[i]==b[i+1] and b[i] == b[i+2] and b[i] == b[i+3]:
            max=max+4
            c.append(max)
        elif b[i]==b[i+1] and b[i] == b[i+2]:
            max=max+3
            c.append(max)
        elif b[i]==b[i+1] and i!=3:
            max=max+2
            c.append(max)  
            
    largest = 0
    for i in range(1, len(c), 1):
        if c[i] > c[i-1]:
            largest = c[i]
    print(largest)


a1 = [1,2,2,3,4,4,4]
a2 = [1,1,2,2,1,1,1,1]
bunch(a1)
bunch(a2)
############################################################################


#Ans8)
def repitition(a):
    b=[]
    for i in range(0, len(a), 1):
        for j in range(i+1, len(a), 1):
            if a[i] == a[j]:
                b.append(a[i])
                b.append(a[j])
                a[i]=0
                a[j]=0
    for i in range(0,len(a)):
        i=0
        if i < len(a):
            if a[i] <= 0:
                del a[i]
        else:
            break
    for i in range(len(a)-1,0,-1):
        i=len(a)-1
        if i < len(a):
            if a[i] <= 0:
                del a[i]
        else:
            break
    for i in range(0,len(b)):
        if i < len(b):
            if b[i] <= 0:
                del b[i]
        else:
            break 
    for i in a:
        if i==0:
            a.remove(0)
    for i in b:
        if i==0:
            b.remove(0)
    for i in b:
        if i==0:
            b.remove(0) 
    for i in a:
        if i in b:
            b.insert(i,i) 
    b.sort()
    c1=1
    c2=1
    c3=1
    for i in range(0, len(b), 1):
        if b[i]==b[i+1]:
            c1=c1+1
        else:
            break
    for j in range(i+1, len(b), 1):
        if j == len(b)-1:
            break
        if b[j]==b[j+1]:
            c2=c2+1
        else:
            break
    for k in range(j+1, len(b), 1):
        if k == len(b)-1:
            break
        if b[k]==b[k+1]:
            c3=c3+1
        else:
            break
    if c1==c2 or c1==c3 or c2==c3:
        print("True")
    else:
        print("False")
    
a1 = [4,5,6,6,4,3,6,4]
a2 = [3,4,6,3,4,7,4,6,8,6,6]


repitition(a1)
repitition(a2)
############################################################################
############################################################################


#Circular Arrays
#Ans1)
def palindromeCheck(c,start,size):   
    a = []
    index = start
    i = 0


    while (i < size):
        a.append(c[index])
        index = (index + 1) % len(c)


        i = i + 1
        #print(a)
    p=0
    f=0
    for i in range(0, len(a), 1):
        if i == (len(a)+1)/2:
            break
        if a[i]==a[len(a)-1-i]:
            p=p+1
        else:
            f=f+1
    if p==(len(a)+1)/2:
        print("True")
    else:
        print("False")


Input1 = [20,10,0,0,0,10,20,30]
Input2 = [10,20,0,0,0,10,20,30]
palindromeCheck(Input1, 5, 5)
palindromeCheck(Input2, 5, 5)
#print(pal)
############################################################################


#Ans2)
def intersection(c,start,size):
    a = []
    index = start
    i = 0


    while (i < size):
        a.append(c[index])
        index = (index + 1) % len(c)


        i = i + 1
    return a




temp1 = [40, 50, 0, 0, 0, 10, 20, 30]
temp2 = [10, 20, 5, 0, 0, 0, 0, 0, 5, 40, 15, 25]


a3 = intersection(temp1,5,5)
a4 = intersection(temp2,8,7)


def common(a1,a2):
    b=[]
    if len(a2)>len(a1):
        for i in range(0, len(a1), 1):
            for j in range(0, len(a2),1):
                if a1[i]==a2[j]:
                    b.append(a1[i])
    else:
        for i in range(0, len(a2), 1):
            for j in range(0, len(a1),1):
                if a2[i]==a1[j]:
                    b.append(a2[i])
    return b
com = common(a3, a4)
print(com)
############################################################################


#Ans3)
arr1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
n = int(len(arr1))
for j in range(0,n+1,1):
    n = int(len(arr1))
    for i in range(0, 3+1, 1):
        if i == 1:
            arr1.remove(arr1[int(n/2)])
        if n == 2 and i == 1:
            break
    if n == 2 and i == 1:
        break
    
print(arr1[0])