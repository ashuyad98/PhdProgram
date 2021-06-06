#This programe is to calculate lenard jones potential constants



def main():
  comp = input(" Enter the compound's name = ")

  a, a0 = (float(i) for i in (input("Enter the value of a(basel plane distance) =  ").split()))
  p = float(input("Enter the value of  c/a =  "))
  b, b0 = (float(i) for i in (input(" The bulk modulous =  ").split()))

  a=a*pow(10,a0)
  si=a/1.092
  b=b*pow(10,b0)
  ap=(b*p*pow(si,3.0))/(3.953*36.0)
  b12=4.0*ap*pow(si,12.0)

  print("\n"" Lenard Jones potential constants are as follows-""\n\n")
  print(" Compound name="+comp+"\n\n")
  print(" Sigma="+si+"\n\n")
  print(" apsilan (energy constant value)="+ap+"\n\n")
  print(" b="+b12+"\n")



if __name__ == "__main__":

  main()



