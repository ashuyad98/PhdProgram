#Programe for calculate soec and toec for hcp at room temperature.


import math

def main():
  comp = input(" Enter the compound's name = ")

  #a,a0 is basal plane distance.    p is c/a value for hcp materials.
  # si is sigma and ap is appsilan. b is hcp constant.
  #b is calculated by si and ap.    M is mass of atom.(in formula cancelled)
  #et is eta (a constant) and calculated by n,m,b,M,a.
  #k2 is contants calculated by et,M,a.
  #k3 is contants calculated by k2,a,m,n.

  m,n = 6.0,7.0

  a, a0 = (float(i) for i in (input("Enter the value of a(basel plane distance) =  ").split()))
  p = float(input("Enter the value of  c/a =  "))
  C33, C33A = (float(i) for i in (input("Enter the value of C33 =  ").split()))

  a=a*pow(10,a0)
  C33=C33*pow(10,C33A)
  cc=p*a
  va=1.732*pow(a,2.0)*cc/2.0
  k2=(C33*va)/(pow(a,4.0)*pow(p,4.0)*3.0)
  k3=-(k2*(m+n+6.0))/(6.0*pow(a,2.0))
  #B is constants calculated by a,p,k3.
  #cp is cprim constants calculated by k2,a,p.
  B=(pow(a,3.0)/pow(p,3.0))*k3
  cp=(k2*a)/pow(p,5.0)
  #all elastic constants is calculated by B,cp,c.
  
  c11=24.1*pow(p,4.0)*cp
  e11=(167.0*pow(a,4.0)*k2)/(8.0*va)
  c12=5.918*pow(p,4.0)*cp
  e12=(41.0*pow(a,4.0)*k2)/(8.0*va)
  c13=1.925*pow(p,6.0)*cp
  e13=(5.0*pow(a,4.0)*pow(p,2.0)*k2)/(3.0*va)
  c33=3.464*pow(p,8.0)*cp
  e33=(3.0*pow(a,4.0)*pow(p,4.0)*k2)/(va)
  c44=2.309*pow(p,6.0)*cp
  e44=(2.0*pow(a,4.0)*pow(p,2.0)*k2)/(va)
  c66=9.451*pow(p,4.0)*cp
  e66=(63.0*pow(a,4.0)*k2)/(8.0*va)
  c111=(126.9*pow(p,2.0)*B+8.853*pow(p,4.0)*cp)
  e111=((1099.0*pow(a,6.0)*k3)/(10.0*va))+((23.0*pow(a,4.0)*k2)/(3.0*va))
  
  c112=19.168*pow(p,2.0)*B-1.61*pow(p,4.0)*cp
  e112=((83.0*pow(a,6.0)*k3)/(5.0*va))-((7.0*pow(a,4.0)*k2)/(5.0*va))
  
  c113=(1.924*pow(p,4.0)*B+1.155*pow(p,6.0)*cp)
  e113=((5.0*pow(a,6.0)*pow(p,2.0)*k3)/(3.0*va))+((pow(a,4.0)*pow(p,2.0)*k2)/(va))
  
  c123=1.617*pow(p,4.0)*B-1.155*pow(p,6.0)*cp
  e123=((7.0*pow(a,6.0)*pow(p,2.0)*k3)/(5.0*va))-((pow(a,4.0)*pow(p,2.0)*k2)/(va))
  
  c133=(3.695*pow(p,6.0)*B)
  e133=(16.0*pow(a,6.0)*pow(p,4.0)*k3)/(5.0*va)
  
  c344=(3.464*pow(p,6.0)*B)
  e344=(3.0*pow(a,6.0)*pow(p,4.0)*k3)/(va)
  
  c144=2.309*pow(p,4.0)*B
  e144=(2.0*pow(a,6.0)*pow(p,2.0)*k3)/(va)
  
  c155=1.539*pow(p,4.0)*B
  e155=(4.0*pow(a,6.0)*pow(p,2.0)*k3)/(3.0*va)
  
  c222=(101.039*pow(p,2.0)*B+9.007*pow(p,4.0)*cp)
  e222=((175.0*pow(a,6.0)*k3)/(2.0*va))+((39.0*pow(a,4.0)*k2)/(5.0*va))
  
  c333=(5.196*pow(p,8.0)*B)
  e333=(9.0*pow(a,6.0)*pow(p,6.0)*k3)/(2.0*va)
  
  print("This result is for HCP compound="+comp+"\n")
  print("Basal planedistance(a)="+str(a)+"\n")
  print("value of c/a="+str(p)+"\n")
  print("value of K2="+str(k2)+"\n")
  print(" This is table for second order elastic constant. ""\n")
  print("----------------------------------------------------------""\n")
  print("c11""\t\t""c12 " "\t\t"+"c13 " "\n")
  print("----------------------------------------------------------""\n")
  print(""+str(c11)+"\t"+""+str(c12)+"\t"+""+str(c13)+"\n")
  print(""+str(e11)+"\t"+""+str(e12)+"\t"+""+str(e13)+"\n")
  print("----------------------------------------------------------""\n")
  print("c33""\t\t""c44 " "\t\t"+"c66 " "\n")
  print("----------------------------------------------------------""\n")
  print(""+str(c33)+"\t"+""+str(c44)+"\t"+""+str(c66)+"\n")
  print(""+str(e33)+"\t"+""+str(e44)+"\t"+""+str(e66)+"\n")
  print("----------------------------------------------------------""\n")
  
  print(" This is table for third order elastic constant. ""\n")
  print("----------------------------------------------------------""\n")
  print("c111""\t\t""c112 " "\t\t"+"c113 " "\t\t"+"C123 " "\n")
  print("----------------------------------------------------------""\n")
  print(""+str(c111)+"\t"+""+str(c112)+"\t"+""+str(c113)+"\t"+""+str(c123)+"\n")
  print(""+str(e111)+"\t"+""+str(e112)+"\t"+""+str(e113)+"\t"+""+str(e123)+"\n")
  print("----------------------------------------------------------""\n")
  print("c133""\t\t""c344 " "\t\t"+"c144 " "\n")
  print("----------------------------------------------------------""\n")
  print(""+str(c133)+"\t"+""+str(c344)+"\t"+""+str(c144)+"\n")
  print(""+str(e133)+"\t"+""+str(e344)+"\t"+""+str(e144)+"\n")
  print("----------------------------------------------------------""\n")
  print("c155""\t\t""c222 " "\t\t"+"c333 " "\n")
  print("----------------------------------------------------------""\n")
  print(""+str(c155)+"\t"+""+str(c222)+"\t"+""+str(c333)+"\n")
  print(""+str(e155)+"\t"+""+str(e222)+"\t"+""+str(e333)+"\n")
  print("----------------------------------------------------------""\n")



if __name__ == "__main__":

  main()