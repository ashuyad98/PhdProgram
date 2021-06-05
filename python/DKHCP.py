#this program is used when hcp parameter 'a','c' is also temp. dependence.
#Programe for calculate temperature dependent soec and toec,VELOCITY
# attenuation, along Z-AXIS for hcp using different data of c33  .


import math

def main():
  
  comp = input(" Enter the compound's name = ")
  j = input("Enter the number of c33 data=  ")
  
  a = a0 = []
  print("Enter the value of a(basel plane distance) in 'a' 'a0' format= ")
  for i in range(j):
    x, y = input().split()
    a.append(x)
    a0.append(y)
  
  p = []
  print("Enter the value of  c/a =  ")
  for i in range(j):
    p.append(input())

  C33 = C33A = []
  print("Enter the value of C33 =  ")
  for i in range(j):
    x, y = input().split()
    C33.append(x)
    C33A.append(y)  

  T = []
  print("enter the temperature= ")
  for i in range(j):
    T.append(input())

  Cva = Cvb = []
  print("enter the value of Cv= ")
  for i in range(j):
    x, y = input().split()
    Cva.append(x)
    Cvb.append(y)  
 
  Eoa = Eob = []
  print("enter the value of Eo=")
  for i in range(j):
    x, y = input().split()
    Eoa.append(x)
    Eob.append(y) 
    
  koa = kob = []
  print("enter the value of K=")
  for i in range(j):
    x, y = input().split()
    koa.append(x)
    kob.append(y)
  
  jj = input("enter the number of frequency= ")
  F = []
  print("enter the value of frequency in MHz=")
  for i in range(j):
    F.append(input())
    
if __name__ == "__main__":
  
    main()
