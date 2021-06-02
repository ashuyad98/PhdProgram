import math


def main():
      
  v1 ,v2 ,v3 = ([] for i in range(3))
  
  tth = [0.0, 5.0, 15.0, 25.0, 35.0, 45.0, 55.0, 65.0, 75.0, 85.0, 90.0]
  
  comp = input("\n Enter the compound's name =")
  c11 = input("\n Enter the value of c11 =  ")
  c12 = input("\n Enter the value of c12 =  ")
  c13 = input("\n Enter the value of c13 =  ")
  c33 = input("\n Enter the value of c33 =  ")
  c44 = input("\n Enter the value of c44 =  ")
  
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
    v3.append.((c44*q+((c11-c12)/2.0)*p))
    
    print("Table of velocity for hcp compound-""\n")         
    print("Compound name="<<comp<<"\n")

cout<<"----------------------------------------------------------""\n";
 cout<<"theeta""\t\t""v1 " "\t\t"<<"v2 " "\t\t"<<"v3 " "\n";
 cout<<"----------------------------------------------------------""\n";
    
  
if __name__ == "__main__":
  
    main()
