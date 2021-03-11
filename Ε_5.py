def catalan(n):
  ans = 1
  for i in range(2,n+1):
     ans = ans *(n+i)/i
  return ans



number_n = input("give the n number")
answer = 1
while(answer != 0):
    print(catalan(int(number_n)))
    answer = input("if you want to find an othe number give 1 else give 0")
    if int(answer) == 1:
        number_n = input("give a new n number")
