#Task 1:




def array(V):
    j = len(V)

    list1 = [0] * j

    r = 0
    m =811

    for i in V:
        if i > r:
            r = i

        elif i < m:
            m = i

    length = r - m + 1
    list2 = [0] * length

    for i in range(0, j, 1):
        list2[V[i] - m] += 1

    for i in range(1, len(list2), 1):
        list2[i] = list2[i] + list2[i - 1]

    for i in range(j - 1, -1, -1):
        list1[list2[V[i] - m] - 1] = V[i]

        list2[V[i] - m] -= 1

    return list1


def find(V, value):
    for i in V:

        if i == value:
            return True

    return False


k = [7,11,21,8,9,2,1,4]
jm = array(k)
print(jm)
jn = find(k,5)
print(jn)




#Task 2:



class hash_table:
    def __init__(self):
        self.size = 9
        self.table = list(0 for r in range(self.size))
        self.counter = 0
        self.compare = 0
    def filled(self):
        if self.counter == self.size:
            return True
        else:
            return False
    def hash_function(self,elmnt):
        val = 0
        count = 0
        total= 0
        for v in elmnt:
          if v not in ('A', 'E', 'I', 'O', 'U', '1', '2','3','4','5','6','7','8','9','0'):
            count +=1
          else:
            if v not in ('A', 'E', 'I', 'O', 'U'):
              total += ord(v)-ord('0')
        val = (count*24 + total)
        return val % self.size
    def insert(self, elmnt):
        if self.filled():
            print("Hash Table Full")
            return False
        saved = False
        jk = self.hash_function(elmnt)
        if self.table[jk] == 0:
            self.table[jk] = elmnt
            saved = True
            self.counter += 1
        else:
            while self.table[jk] != 0:
                jk += 1
                if jk >= self.size:
                    jk = 0
            self.table[jk] = elmnt
            saved = True
            self.counter += 1
        return saved
    def display(self):
        print("\n")
        for r in range(self.size):
            print(str(r) + " = " + str(self.table[r]))
        print("The no. of element in the respective table are : " + str(self.counter))
p = hash_table()
words = ["ST1E89B8A32","ST1E89B8A33","ST1E89B8A34"]
for r in words:
    p.insert(r)
p.display()

