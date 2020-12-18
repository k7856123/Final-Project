#kennedy becher
#problem 1

all_sum = 0 #setting sum to zero
for i in range(1000): #setting range and for statement
    if (i%3 ==0 or i%5 ==0): # finding multiples of 3 & 5
        all_sum = all_sum + i 
print(all_sum)


#problem 2
def Fibonacci(p1):
    p1 = input
    if ((p1==0) or (p1==1)):
        return 1
    else:
        return ((Fibonacci(p1-1))+(Fibonacci(p1-2)))
a =0
all_sum = 0
while (Fibonacci(a))<4000000:
    if (((Fibonacci(a))%2)==0):
        all_sum+= Fibonacci(a)
print(all_sum)

Fibonacci()
