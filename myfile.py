#kennedy becher
#problem 1

all_sum = 0 #setting sum to zero
for i in range(1000): #setting range and for statement
    if (i%3 ==0 or i%5 ==0): # finding multiples of 3 & 5
        all_sum = all_sum + i 
print(all_sum)
