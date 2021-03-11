def perm_length(n):
    if int(n) == 0 :
        print("It doesnt exist bracuse there is only one value")
    else:
        print("The length of the permutation is",+ int(n))

def find_opposite(n,list):
    list_2 = []
    list_3 = []
    for i in range(0, int(n)+1):
        j = 0
        while list[int(j)] != int(i):
           j = int(j) + 1
        if int(j) == int(n):
            list_2.insert(list[0])
        else:
            list_2.insert(int(i), list[int(j)]) #+1
    for a in range(0, int(n+1)):
        j = 0
        while list_2[int(j)] != int(a):
            j = int(j) + 1
        if int(j) == int(n):
            list_3.insert(int(a), list_2[0])
        else:
            list_3.insert(int(a), list_2[int(j)]) #+1
    print("The opposite is:",  list_3)
    print("The last is:", list_3[int(n)])
    return list_3

def product_perm(list,n):
    for i in range(1,int(n)+1):
        if ( int(i) == int(n)):
            print(i);
        else:
         print(i,"<-");





n = input("give the n number")   #θεωρω οτι θα δοθει αριθμος ακεραιος >0
list = []
print("give the numbers of the permutation in order")
for i in range(1, int(n)+1):
    perm_num = int(input())
    list.append(perm_num)
    print("number is:", perm_num, "and the index is:", list.index(perm_num))
print(find_opposite(int(n),list))

































