#This is program to calculate direction dependent velocity,relx.time in
#HCP compound using c33 elastic constant data.

import math

def main():
  comp = input(" Enter the compound's name = ")

  #a,a0 is basal plane distance.    p is c/a value for hcp materials.
  #k2 is contants calculated by C33.
  #k3 is contants calculated by k2,a,m,n.
  a,a0,p,va = 0.0, 0.0, 0.0, 0.0
  m, n = 1.0, 2.0
  C33,C33A,k2,k3,c11,c12,c13,c33,c44,c66,c111,c112,c113,c123,c133,c344,c144,c155,c222,c333,T = ([0.0 for x in range(15)] for i in range(21))
  i, j = 0, 0
  
  #Variables to calculate velocity.
  th,xx,yy,p1,q = ([0.0 for x in range(15)] for i in range(5))
  r,s,t,u,v11,v22,v33,v1,v2,v3 = ([[0.0 for x in range(15)] for y in range(15)] for i in range(10))
  tth=[0.0,5.0,15.0,25.0,35.0,45.0,55.0,65.0,75.0,85.0,90.0]
  ii=0
  dd,Cv,Cva,Cvb,Eo,Eoa,Eob,ko,koa,kob = ([0.0 for x in range(15)] for i in range(10))  
  V,to = ([[0.0 for x in range(15)] for y in range(15)] for i in range(2))

  a, a0 = input("Enter the value of a(basel plane distance) in 'a' 'a0' format= ").split()

  p = float(input("Enter the value of  c/a =  "))

  j = int(input("Enter the number of c33 data=  "))
  print("Enter the value of C33 =  ")
  for i in range(j):
    C33[i], C33A[i] = input().split() 
  
  print("enter the temperature= ")
  for i in range(j):
    T[i] = input()
  
  print("enter the value of dd=")
  for i in range(j):
    dd[i] = input()

  print("enter the value of Cv= ")
  for i in range(j):
    Cva[i], Cvb[i] = input().split() 

  print("enter the value of Eo=")
  for i in range(j):
    Eoa[i], Eob[i] = input().split()

  print("enter the value of K=")
  for i in range(j):
    koa[i], kob[i] = input().split()

  a=a*pow(10,a0)
  va=1.732*pow(a,3.0)*p/2.0

  for i in range(j):
    C33[i]=C33[i]*pow(10,C33A[i])
    k2[i]=(C33[i]*va)/(pow(a,4.0)*pow(p,4.0)*3.0)
    k3[i]=-(k2[i]*(m+n+6.0))/(6.0*pow(a,2.0))
    c11[i]=(167.0*pow(a,4.0)*k2[i])/(8.0*va)
    c12[i]=(41.0*pow(a,4.0)*k2[i])/(8.0*va)
    c13[i]=(5.0*pow(a,4.0)*pow(p,2.0)*k2[i])/(3.0*va)
    c33[i]=(3.0*pow(a,4.0)*pow(p,4.0)*k2[i])/(va)
    c44[i]=(2.0*pow(a,4.0)*pow(p,2.0)*k2[i])/(va)
    c66[i]=(63.0*pow(a,4.0)*k2[i])/(8.0*va)
    c111[i]=((1099.0*pow(a,6.0)*k3[i])/(10.0*va))+((23.0*pow(a,4.0)*k2[i])/(3.0*va))
    c112[i]=((83.0*pow(a,6.0)*k3[i])/(5.0*va))-((7.0*pow(a,4.0)*k2[i])/(5.0*va))
    c113[i]=((5.0*pow(a,6.0)*pow(p,2.0)*k3[i])/(3.0*va))+((pow(a,4.0)*pow(p,2.0)*k2[i])/(va))
    c123[i]=((7.0*pow(a,6.0)*pow(p,2.0)*k3[i])/(5.0*va))-((pow(a,4.0)*pow(p,2.0)*k2[i])/(va))
    c133[i]=(16.0*pow(a,6.0)*pow(p,4.0)*k3[i])/(5.0*va)
    c344[i]=(3.0*pow(a,6.0)*pow(p,4.0)*k3[i])/(va)
    c144[i]=(2.0*pow(a,6.0)*pow(p,2.0)*k3[i])/(va)
    c155[i]=(4.0*pow(a,6.0)*pow(p,2.0)*k3[i])/(3.0*va)
    c222[i]=((175.0*pow(a,6.0)*k3[i])/(2.0*va))+((39.0*pow(a,4.0)*k2[i])/(5.0*va))
    c333[i]=(9.0*pow(a,6.0)*pow(p,6.0)*k3[i])/(2.0*va)
    Cv[i]=Cva[i]*pow(10,Cvb[i])
    Eo[i]=Eoa[i]*pow(10,Eob[i])
    ko[i]=koa[i]*pow(10,kob[i])

  for ii in range(11):
    th[ii]=(tth[ii]*22)/(180*7)
    xx[ii]=math.sin(th[ii])
    yy[ii]=math.cos(th[ii])
    p1[ii]=pow(xx[ii],2.0)
    q[ii]=pow(yy[ii],2.0)

  for i in range(j):
    for ii in range(11):
      r[i][ii]=c11[i]*p1[ii]-c33[i]*q[ii]+c44[i]*(q[ii]-p1[ii])
      s[i][ii]=pow(r[i][ii],2)
      t[i][ii]=4.0*p1[ii]*q[ii]*pow( (c13[i]+c44[i]), 2)
      u[i][ii]=pow( (s[i][ii]+t[i][ii]),0.5)
      v11[i][ii]=(c33[i]*q[ii]+c11[i]*p1[ii]+c44[i]+u[i][ii])/2
      v1[i][ii]=math.sqrt(v11[i][ii]/dd[i])
      v22[i][ii]=(c33[i]*q[ii]+c11[i]*p1[ii]+c44[i]-u[i][ii])/2
      v2[i][ii]=math.sqrt(v22[i][ii]/dd[i])
      v33[i][ii]=c44[i]*q[ii]+((c11[i]-c12[i])/2.0)*p1[ii]
      v3[i][ii]=math.sqrt(v33[i][ii]/dd[i])
      V[i][ii]=pow(3,0.333)*pow((1/pow(v1[i][ii],3)+1/pow(v3[i][ii],3)+1/pow(v2[i][ii],3)),-0.333)
      to[i][ii]=3*ko[i]/(Cv[i]*V[i][ii]*V[i][ii])

  while 1:
    print(" Enter 1 to see velocity""\n")
    print(" Enter 2 to see debye avg.velocity and relx.time using V1&V3 ""\n")
    print(" Enter 3 to Print all data""\n")
    print(" Enter 4 for EXIT""\n")
    J = int(input(" What is your choice="))

    if J == 1:
      for i in range(j):
        print("Table of velocity for hcp compound-""\n\n")
        print("Compound name="+comp+"\n\n")
        print("temperature="+T[i]+"\n")
        print("----------------------------------------------------------""\n")
        print("theeta""\t\t""v1 " "\t\t"+"v2 " "\t\t"+"v3 " "\n")
        print("----------------------------------------------------------""\n")
        for ii in range(11):
          print(""+tth[ii]+"\t"+v1[i][ii]+"\t"+v2[i][ii]+"\t"+v3[i][ii]+"\n")
        print("----------------------------------------------------------""\n")

    elif J == 2:     
      for i in range(j):
        print("Table of debye velocity and relax.time using V1&V3-""\n\n")
        print("Compound name="+comp+"\n\n")
        print("temperature="+T[i]+"\n")
        print("----------------------------------------------------------""\n")
        print("theeta""\t\t""V""\t\t""RELAX.TIME""\n")
        print("----------------------------------------------------------""\n")
        for ii in range(11):
          print(""+tth[ii]+"\t\t"+V[i][ii]+"\t"+""+to[i][ii]+"\n")
        print("----------------------------------------------------------""\n")

    elif J == 3:
      file1 = open("PRN", "w")
      for i in range(j):
        file1.append("Table of velocity for hcp compound-""\n\n")
        file1.append("Compound name="+comp+"\n\n")
        file1.append("temperature="+T[i]+"\n")
        file1.append("----------------------------------------------------------""\n")
        file1.append("theeta""\t\t""v1 " "\t\t"+"v2 " "\t\t"+"v3 " "\n")
        file1.append("----------------------------------------------------------""\n")
        for ii in range(11):
          file1.append(""+tth[ii]+"\t"+v1[i][ii]+"\t"+v2[i][ii]+"\t"+v3[i][ii]+"\n")
        file1.append("----------------------------------------------------------""\n")
      for i in range(j):
        file1.append("Table of debye velocity and relax.time using V1&V3-""\n\n")
        file1.append("Compound name="+comp+"\n\n")
        file1.append("temperature="+T[i]+"\n")
        file1.append("----------------------------------------------------------""\n")
        file1.append("theeta""\t\t""V""\t\t""RELAX.TIME""\n")
        file1.append("----------------------------------------------------------""\n")
        for ii in range(11):
          file1.append(""+tth[ii]+"\t\t"+V[i][ii]+"\t"+to[i][ii]+"\n")
        file1.append("----------------------------------------------------------""\n")

    elif J == 4:
      exit()
    else:
      print(" You have entered wrong choice, please correct it.")


if __name__ == "__main__":

  main()
