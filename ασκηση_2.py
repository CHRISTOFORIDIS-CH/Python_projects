file = input("Enter the pathway of the file")  #δεν χρειαζεται ελεγχο εγκυροτητας για το φακελο
with open(file) as f:
    flat_list=[word for line in f for word in line.split()]
with open(file) as f:
    for line in f:
        for flat_list in line.split():
            c_word = 0
            g_word = 0
            r = len(flat_list)
            for i in range(int(r)):
                if flat_list[i] == "f" or flat_list[i] == "r" or flat_list[i] == "c" or flat_list[i] == "k":
                    c_word = c_word + 1
                else:
                    g_word = g_word + 1
            if int(c_word) > int(g_word):
               print(flat_list,"is a bad word")
            else:
                print(flat_list,"is good word")