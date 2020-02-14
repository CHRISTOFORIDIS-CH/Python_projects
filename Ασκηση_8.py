from random import *
f_1 = randint(0, 100)  # πανω απο 100 αυτοκινητα ειναι αδυνατον να ειναι σε 1 φαναρι(το πιο τραβηγμενο σεναριο),τα f_.. ειναι τα φαναρια
f_2 = randint(0, 100)
f_3 = randint(0, 100)
list_1 = [1,3]
list_2 = [1,2]
list_3 = [2,3]
g = 0
print("Τα φανάρια αρχικά εχουν: f_1=", f_1, "f_2 =", f_2, "f_3=", f_3)
answ = "Yes"
while answ == "Yes":
  if int(f_1) > int(f_2):
     if int(f_1) > int(f_3):
        print("Το f_1 ειναι πρασινο και τα αλλα ειναι κοκκινα")
        g = f_1
     elif int(f_1) == int(f_3):
            g_1 =  random.choice(list_1)
            if int(g_1) == 1:
                g = f_1
            else:
                g = f_2
            print(g, "ειναι πρασινο και τα αλλα ειναι κοκκινα")
     if int(f_1) > int(f_3) and int(f_1) == int(f_2):
        g_2 = random.choice(list_2)
        if int(g_2) == 2 :
            g = f_2
        else:
            g = f_1
        print(g, "ειναι πρασινο και τα αλλα ειναι κοκκινα")
  if int(f_2) > int(f_1):
     if int(f_2) > int(f_3):
            print(" Το f_2 ειναι πρασινο και τα αλλα ειναι κοκκινα")
            g = f_2
     elif int(f_2) == int(f_3):
            g_3 =  random.choice(list_3)
            if int(g_3) == 3:
                g = f_3
            else:
                g = f_2
            print("f", g , "ειναι πρασινο και τα αλλα ειναι κοκκινα")
  if int(f_3) > int(f_1):
     if int(f_3) > int(f_2):
            print(" Το f_3 ειναι πρασινο και τα αλλα ειναι κοκκινα")
            g = f_3
  if g >= 5 :               #δηλαδη μπορω να του αφερεσω 5 αμαξια
    from random import*
    m = randint(5,10)
    if int(g) == int(f_1):
        f_1 = int(f_1) - m
        b = randint(0, 5)
        f_2 = int(f_2) + int(b)
        c = randint(0, 5)
        f_3 = int(f_3) + int(c)
        print("ηρθαν", c, "στο f_3")
        print("ηρθαν", b, "στο f_2")
        print("εφυγαν", m, "στο f_1")
    elif int(g) == int(f_2):
        f_2 = int(f_2) - m
        a = randint(0, 5)
        f_1 = int(f_1) + int(a)
        c = randint(0, 5)
        f_3 = int(f_3) + int(c)
        print("ηρθαν", c, "στο f_3")
        print("ηρθαν", a, "στο f_1")
        print("εφυγαν", m, "στο f_2")
    else:
        f_3 = int(f_3) - m
        a = randint(0, 5)
        f_1 = int(f_1) + int(a)
        b = randint(0, 5)
        f_2 = int(f_2) + int(b)
        print("ηρθαν", b, "στο f_2")
        print("ηρθαν", a, "στο f_1")
        print("εφυγαν", m, "στο f_3")
  else:
      if int(g) != f_1 and int(g) != f_2:
          m = randint(0, 5)
          f_1 = int(f_1) + int(m)
          print("ηρθαν", m, "στο f_1")
          m = randint(0, 5)
          f_2 = int(f_2) + int(m)
          print("ηρθαν", m, "στο f_2")
      elif int(g) != f_2 and int(g) != f_3:
          m = randint(0, 5)
          f_2 = int(f_2) + int(m)
          print("ηρθαν",m,"στο f_2")
          m = randint(0, 5)
          f_3 = int(f_3) + int(m)
          print("ηρθαν", m, "στο f_3")
      elif int(g) != f_1 and int(g) != f_3:
          m = randint(0, 5)
          f_1 = int(f_1) + int(m)
          print("ηρθαν", m, "στο f_2")
          m = randint(0, 5)
          f_3 = randint(0, 5)
          print("ηρθαν", m, "στο f_3")





  print("το f_1 εχει:", f_1, "to f_2 εχει", f_2, "το f_3 εχει:", f_3)
  answ = input("you want to continue Yes/No")



