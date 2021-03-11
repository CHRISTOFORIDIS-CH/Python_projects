n = input("pls give a number n")   #περιμενω θετικο ακεραιο αριθμο
a = 0
b = 1

if int(n) == int(a):
    print("an Euler road doesnt exist")
elif int(n) == int(b):
    print(" V 1->V 1")           #τα V συμβολιζουν τους κομβους
else:
    for i in range( 1 , int(n) + 1):
        if int(i) == int(n):
            print("V", i, "-> V 1")
        else:
            print("V",  i,  "->", end = " ")




