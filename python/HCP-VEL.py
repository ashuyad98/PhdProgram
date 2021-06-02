import math

def main():
      
  v1 ,v2 ,v3 = ([] for i in range(3))
  
  tth = [0.0, 5.0, 15.0, 25.0, 35.0, 45.0, 55.0, 65.0, 75.0, 85.0, 90.0]
  
  comp = input(" Enter the compound's name = ")
  c11 = float(input(" Enter the value of c11 =  "))
  c12 = float(input(" Enter the value of c12 =  "))
  c13 = float(input(" Enter the value of c13 =  "))
  c33 = float(input(" Enter the value of c33 =  "))
  c44 = float(input(" Enter the value of c44 =  "))
  print()
  
  for tthValue in tth:
    
    th = (tthValue*22)/(180*7)
    
    p = pow(math.sin(th),2.0)
    q = pow(math.cos(th), 2.0)
    
    r = c11*p-c33*q+c44*(q-p)
    s = pow(r, 2.0);
    
    t = 4.0*p*q*pow((c13+c44), 2)
    u = pow((s+t),0.5)
    
    v1.append((c33*q+c11*p+c44+u)/2)
    v2.append((c33*q+c11*p+c44-u)/2)
    v3.append((c44*q+((c11-c12)/2.0)*p))
    
  print("Table of velocity for hcp compound-")         
  print("Compound name="+ comp+"\n")

  print("{:<18} {:<18} {:<18} {:<18}".format("Theeta", "v1", "v2", "v3"))
  print("{:<18} {:<18} {:<18} {:<18}".format("---------", "---------", "---------", "---------"))
 
  for tthValue, v1Value, v2Value, v3Value in zip(tth, v1, v2, v3):
    
    print("{:<18} {:<18.10f} {:<18.10f} {:<18.10f}".format(tthValue, v1Value, v2Value, v3Value))
  
  print()

    
if __name__ == "__main__":
  
    main()
