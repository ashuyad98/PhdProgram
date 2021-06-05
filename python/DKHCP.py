#this program is used when hcp parameter 'a','c' is also temp. dependence.
#Programe for calculate temperature dependent soec and toec,VELOCITY
# attenuation, along Z-AXIS for hcp using different data of c33  .


import math

def main():
  #a,a0 is basal plane distance.    p is c/a value for hcp materials.
  #k2 is contants calculated by C33.
  #k3 is contants calculated by k2,a,m,n. 
  m, n = 1.0, 2.0
  a, a0, p, va, C33, C33A, k2, k3 = ([0 for x in range(15)] for i in range(8))
  c11, c12, c13, c33, c44, c66, c111, c112, c113, c123, c133, c344, c144, c155, c222, c333 = ([0 for x in range(15)] for i in range(16))
  
  #variables to calculate gruneisen constants.
  A,C,L,M,K,x1,x2,x3,x4,x5,x6,x6a,x6b,x7,x8,x8a,x8b,x8c,x,xav,xav1,AC,XX,y1a,y1,y2,y3a,y3,y4,y5a,y5,y6,y7a,y7,y8,y9,y10,y,yav,yav1 = ([0 for x in range(15)] for i in range(39))
  
  #Variables to calculate ultrasonic attenuation.
  T = []
  dd,Vl,Vs,V,Cv,Cva,Cvb,Eo,Eoa,Eob,ko,koa,kob,to,tl,ts,Dl,Ds,ath,al,as = ([0 for x in range(15)] for i in range(20))
  
  #variables for frequency dependent
  alth, all, als = ([[0 for x in range(15)] for y in range(15)] for i in range(3))
  
  comp = input(" Enter the compound's name = ")
  j = input("Enter the number of c33 data=  ")
  
  print("Enter the value of a(basel plane distance) in 'a' 'a0' format= ")
  for i in range(j):
    a[i], a0[i] = input().split()
  
  print("Enter the value of  c/a =  ")
  for i in range(j):
    p[i] = input()

  print("Enter the value of C33 =  ")
  for i in range(j):
    C33[i], C33A[i] = input().split() 

  print("enter the temperature= ")
  for i in range(j):
    T[i] = input()

  print("enter the value of Cv= ")
  for i in range(j):
    Cva[i], Cvb[i] = input().split() 

  print("enter the value of Eo=")
  for i in range(j):
    Eoa[i], Eob[i] = input().split()
    
  print("enter the value of K=")
  for i in range(j):
    koa[i], kob[i] = input().split()
  
  jj = input("enter the number of frequency= ")

  print("enter the value of frequency in MHz=")
  for i in range(j):
    F[i] = input()
    
  K = 1.0/1.414
  
  for in in range(j):
    a[i]=a[i]*pow(10,a0[i])
    va[i]=1.732*pow(a[i],3.0)*p[i]/2.0
    C33[i]=C33[i]*pow(10,C33A[i])
    k2[i]=(C33[i]*va[i])/(pow(a[i],4.0)*pow(p[i],4.0)*3.0)
    k3[i]=-(k2[i]*(m+n+6.0))/(6.0*pow(a[i],2.0))
    c11[i]=(167.0*pow(a[i],4.0)*k2[i])/(8.0*va[i])
    c12[i]=(41.0*pow(a[i],4.0)*k2[i])/(8.0*va[i])
    c13[i]=(5.0*pow(a[i],4.0)*pow(p[i],2.0)*k2[i])/(3.0*va[i])
    c33[i]=(3.0*pow(a[i],4.0)*pow(p[i],4.0)*k2[i])/(va[i])
    c44[i]=(2.0*pow(a[i],4.0)*pow(p[i],2.0)*k2[i])/(va[i])
    c66[i]=(63.0*pow(a[i],4.0)*k2[i])/(8.0*va[i])
    c111[i]=((1099.0*pow(a[i],6.0)*k3[i])/(10.0*va[i]))+((23.0*pow(a[i],4.0)*k2[i])/(3.0*va[i]))
    c112[i]=((83.0*pow(a[i],6.0)*k3[i])/(5.0*va[i]))-((7.0*pow(a[i],4.0)*k2[i])/(5.0*va[i]))
    c113[i]=((5.0*pow(a[i],6.0)*pow(p[i],2.0)*k3[i])/(3.0*va[i]))+((pow(a[i],4.0)*pow(p[i],2.0)*k2[i])/(va[i]))
    c123[i]=((7.0*pow(a[i],6.0)*pow(p[i],2.0)*k3[i])/(5.0*va[i]))-((pow(a[i],4.0)*pow(p[i],2.0)*k2[i])/(va[i]))
    c133[i]=(16.0*pow(a[i],6.0)*pow(p[i],4.0)*k3[i])/(5.0*va[i])
    c344[i]=(3.0*pow(a[i],6.0)*pow(p[i],4.0)*k3[i])/(va[i])
    c144[i]=(2.0*pow(a[i],6.0)*pow(p[i],2.0)*k3[i])/(va[i])
    c155[i]=(4.0*pow(a[i],6.0)*pow(p[i],2.0)*k3[i])/(3.0*va[i])
    c222[i]=((175.0*pow(a[i],6.0)*k3[i])/(2.0*va[i]))+((39.0*pow(a[i],4.0)*k2[i])/(5.0*va[i]))
    c333[i]=(9.0*pow(a[i],6.0)*pow(p[i],6.0)*k3[i])/(2.0*va[i])
    
    #condituional expression
    A[i]=c11[i]-2*c44[i]-c13[i]
    C[i]=c33[i]-2*c44[i]-c13[i]
    L[i]=C[i]/(A[i]+C[i])
    M[i]=A[i]/(A[i]+C[i])
    XX[i]=A[i]*C[i]
    
    if XX[i]<0:
      AC[i]=-XX[i]
    else:
      AC[i]=XX[i]
      
    #This is formulation for Gruneisen constant.
    #along theeta zero i.e. for longitudinal wave.
    
    
if __name__ == "__main__":
  
    main()
