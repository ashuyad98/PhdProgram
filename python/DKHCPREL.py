#This is program to calculate direction dependent velocity,relx.time in
#HCP compound using elastic constant data.
import math

def main():
  comp = input(" Enter the compound's name = ")

  #Vriables to calculate velocity.
  c11,c11a,c12,c12a,c13,c13a,c33,c33a,c44,c44a,c66,c66a,c111,c111a,c112,c112a,c113,c113a,c123,c123a,c133,c133a,c344,c344a,c144,c144a,c155,c155a,c222,c222a,c333,c333a = (0.0 for i in range(34))
  v1,v2,v3,th,xx,yy,p,q,r,s,t,u,v11,v22,v33 = ([0.0 for x in range(15)] for i in range(15))
  tth =[0.0,5.0,15.0,25.0,35.0,45.0,55.0,65.0,75.0,85.0,90.0]
  n = 11
  V, to = ([0.0 for x in range(15)] for i in range(2))


  print("\n Enter all data in CGS SYSTEM")

  c11, c11a = (float(i) for i in (input("enter the value of c11=").split()))
  c12, c12a = (float(i) for i in (input("enter the value of c12=").split()))
  c13, c13a = (float(i) for i in (input("enter the value of c13=").split()))
  c33, c33a = (float(i) for i in (input("enter the value of c33=").split()))
  c44, c44a = (float(i) for i in (input("enter the value of c44=").split()))
  c66, c66a = (float(i) for i in (input("enter the value of c66=").split()))
  c111, c111a = (float(i) for i in (input("enter the value of c111=").split()))
  c112, c112a = (float(i) for i in (input("enter the value of c112=").split()))
  c113, c113a = (float(i) for i in (input("enter the value of c113=").split()))
  c123, c123a = (float(i) for i in (input("enter the value of c123=").split()))
  c133, c133a = (float(i) for i in (input("enter the value of c133=").split()))
  c344, c344a = (float(i) for i in (input("enter the value of c344=").split()))
  c144, c144a = (float(i) for i in (input("enter the value of c144=").split()))
  c155, c155a = (float(i) for i in (input("enter the value of c155=").split()))
  c222, c222a = (float(i) for i in (input("enter the value of c222=").split()))
  c333, c333a = (float(i) for i in (input("enter the value of c333=").split()))
  c344, c344a = (float(i) for i in (input("enter the value of c344=").split()))
  dd = (float(input("enter the value of dd=")))
  Cva, Cvb = (float(i) for i in (input("enter the value of Cv=").split()))
  Eoa, Eob = (float(i) for i in (input("enter the value of Eo=").split()))
  koa, kob = (float(i) for i in (input("enter the value of K=").split()))

  Cv=Cva*pow(10,Cvb)
  Eo=Eoa*pow(10,Eob)
  ko=koa*pow(10,kob)
  c11=c11*pow(10,c11a)
  c12=c12*pow(10,c12a)
  c13=c13*pow(10,c13a)
  c33=c33*pow(10,c33a)
  c44=c44*pow(10,c44a)
  c66=c66*pow(10,c66a)
  c111=c111*pow(10,c111a)
  c112=c112*pow(10,c112a)
  c113=c113*pow(10,c113a)
  c123=c123*pow(10,c123a)
  c133=c133*pow(10,c133a)
  c344=c344*pow(10,c344a)
  c144=c144*pow(10,c144a)
  c155=c155*pow(10,c155a)
  c222=c222*pow(10,c222a)
  c333=c333*pow(10,c333a)

  #This is formulation for velocity at different theeta.

  for i in range(n):
    th[i]=(tth[i]*22)/(180*7)
    xx[i]=math.sin(th[i])
    yy[i]=math.cos(th[i])
    p[i]=pow(xx[i],2.0)
    q[i]=pow(yy[i],2.0)
    r[i]=c11*p[i]-c33*q[i]+c44*(q[i]-p[i])
    s[i]=pow(r[i],2)
    t[i]=4.0*p[i]*q[i]*pow( (c13+c44), 2)
    u[i]=pow( (s[i]+t[i]),0.5)
    v11[i]=(c33*q[i]+c11*p[i]+c44+u[i])/2
    v1[i]=math.sqrt(v11[i]/dd)
    v22[i]=(c33*q[i]+c11*p[i]+c44-u[i])/2
    v2[i]=math.sqrt(v22[i]/dd)
    v33[i]=c44*q[i]+((c11-c12)/2.0)*p[i]
    v3[i]=math.sqrt(v33[i]/dd)
    V[i]=pow(3,0.333)*pow((1/pow(v1[i],3)+1/pow(v3[i],3)+1/pow(v2[i],3)),-0.333)
    to[i]=3*ko/(Cv*V[i]*V[i])

  print(" Enter 1 to see velocity""\n")
  print(" Enter 2 to see debye avg.velocity and relx.time using V1,V2&V3 ""\n")
  print(" Enter 3 to Print all data""\n")
  print(" Enter 4 for EXIT""\n")
  print(" What is your choice=")
  J = int(input())

  if J == 1:
    print("Table of velocity for hcp compound-""\n\n")
    print("Compound name="+comp+"\n\n")
  
    print("----------------------------------------------------------""\n")
    print("theeta""\t\t""v1 " "\t\t"+"v2 " "\t\t"+"v3 " "\n")
    print("----------------------------------------------------------""\n")
    for i in range(11):
      print(""+tth[i]+"\t"+""+v1[i]+"\t"+""+v2[i]+"\t"+""+v3[i]+"\n")
    print("----------------------------------------------------------""\n")
  
  elif J == 2:
    print("Table of debye velocity and relax.time using V1,V2&V3-""\n\n")
    print("Compound name="+comp+"\n\n")
  
    print("----------------------------------------------------------""\n")
    print("theeta""\t\t""V""\t\t""RELAX.TIME""\n")
    print("----------------------------------------------------------""\n")
    for i in range(11):
      print(""+tth[i]+"\t\t"+V[i]+"\t"+""+to[i]+"\n")
    print("----------------------------------------------------------""\n")
  
  elif J == 3:
    file1 = open("PRN", "w")
    print("Compound name="+comp+"\n\n")
    print("c11="+c11+"\n\n")
    print("c12="+c12+"\n\n")
    print("c13="+c13+"\n\n")
    print("c33="+c33+"\n\n")
    print("c44="+c44+"\n\n")
    print("c66="+c66+"\n\n")
    print("c111="+c111+"\n\n")
    print("c112="+c112+"\n\n")
    print("c113="+c113+"\n\n")
    print("c123="+c123+"\n\n")
    print("c133="+c133+"\n\n")
    print("c144="+c144+"\n\n")
    print("c155="+c155+"\n\n")
    print("c222="+c222+"\n\n")
    print("c333="+c333+"\n\n")
    print("c344="+c344+"\n\n")
    print("Cv="+Cv+"\n\n")
    print("Eo="+Eo+"\n\n")
    print("K="+ko+"\n\n")
    print("density="+dd+"\n\n")
    print("Table of velocity for hcp compound-""\n\n")
    print("----------------------------------------------------------""\n")
    print("theeta""\t\t""v1 " "\t\t"+"v2 " "\t\t"+"v3 " "\n")
    print("----------------------------------------------------------""\n")
    for i in range(11):
      print(""+tth[i]+"\t"+""+v1[i]+"\t"+""+v2[i]+"\t"+""+v3[i]+"\n")
    print("----------------------------------------------------------""\n")
    print("Table of debye velocity and relax.time using V1,V2&V3-""\n\n")
    print("Compound name="+comp+"\n\n")
    print("----------------------------------------------------------""\n")
    print("theeta""\t\t""V""\t\t""RELAX.TIME""\n")
    print("----------------------------------------------------------""\n")
    for i in range(11):
      print(""+tth[i]+"\t\t"+V[i]+"\t"+""+to[i]+"\n")
    print("----------------------------------------------------------""\n")
  
   elif J == 4:
  	exit())
   else:
  	print(" You have entered wrong choice, please correct it.")

if __name__ == "__main__":
  
    main()
  