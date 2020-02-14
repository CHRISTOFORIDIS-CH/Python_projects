
def sum_digits(num):
    l = len(num)
    sum = 0
    for i in range(int(l)):
        if num[i] != ".":
            sum = int(sum) + int(num[i])
    return sum


num = input("give the number")    # θεωρω οτι θα δοθει αριθμος δεν κανω ελεγχο εγκυροτητας εφοσον δεν ζητιεται απο την εκφωνηση
if float(num) < 0:
    num = float(num) * -1
c = len(str(num))
while int(c) > 1:
    num = float(num) * 3
    num = float(num) + 1
    num = sum_digits(str(num))
    c = len(str((num)))
print(num)











