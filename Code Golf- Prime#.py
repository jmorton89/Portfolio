# Print all the prime numbers from 1 to 100 inclusive, each on their own line.
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

for n in range(2,98):
 for i in range(2,n):
  if n%i==0:break 
 else:print(n)