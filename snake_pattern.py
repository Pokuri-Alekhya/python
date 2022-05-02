num=int(input())
n=0
for i in range(1,num+1):
    if i%2==1:
         for j in range(num):
             n=n+1
             print(n,end=' ')
          
         print()
    else:
         n=n+num
         n1=n
         for j in range(num):
             
             print(n1,end=' ')
             n1=n1-1
         print()   
