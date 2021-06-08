#This is program to calculate velocity, G.P.,frequency dependent attenuation in
#HCP compound using elastic constant data.
import math

def main():
  comp = input(" Enter the compound's name = ")

  #Vriables to calculate velocity.
  c11,c11a,c12,c12a,c13,c13a,c33,c33a,c44,c44a,c66,c66a,c111,c111a,c112,c112a,c113,c113a,c123,c123a,c133,c133a,c344,c344a,c144,c144a,c155,c155a,c222,c222a,c333,c333a = (0.0 for i in range(34))
  v1,v2,v3,th,xx,yy,p,q,r,s,t,u,v11,v22,v33 = ([0.0 for x in range(15)] for i in range(15))
  tth =[0.0,5.0,15.0,25.0,35.0,45.0,55.0,65.0,75.0,85.0,90.0]
  n = 11

  #variables to calculate gruneisen constants.
  A,C,L,M,K,x1,x2,x3,x4,x5,x6,x6a,x6b,x7,x8,x8a,x8b,x8c,x,xav,AC,XX,y1a,y1,y2,y3a,y3,y4,y5a,y5,y6,y7a,y7,y8,y9,y10,y,yav = (0.0 for i in range(38))

  #Variables to calculate ultrasonic attenuation.
  m,T = 0, 0
  dd,Vl,Vs,V,Cv,Cva,Cvb,Eo,Eoa,Eob,ko,koa,kob,to,tl,ts,Dl,Ds,ath,al,as1 = (0.0 for i in range(21))
  athw,alw,asw,f = ([0.0 for x in range(15)] for i in range(4))

  T = int(input("Enter the value of temperature ="))
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
  dd = (float(input("enter the value of dd=")))
  Cva, Cvb = (float(i) for i in (input("enter the value of Cv=").split()))
  Eoa, Eob = (float(i) for i in (input("enter the value of Eo=").split()))
  koa, kob = (float(i) for i in (input("enter the value of K=").split()))
  c11, c11a = (float(i) for i in (input("enter the value of c11=").split()))
  m = int(input("number of frequency have to enter"))

  print("enter the value of frequency in MHz= ")
  for j in range(m):
    f[j] = float(input())
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
  A=c11-2*c44-c13
  C=c33-2*c44-c13
  L=C/(A+C)
  M=A/(A+C)
  K=1.0/1.414
  XX=A*C
  if XX<0:
    AC=-XX
  else:
    AC=XX

  #This is formulation for Gruneisen constant.
  #along theeta zero i.e. for longitudinal wave.

  x1=1.0+( (c13+c113)/(2.0*c33) )
  x2=(c13+c113)/(2.0*c11)
  x3=(c13+c344)/(2.0*c44)
  x4=(c13+0.5*(c113-c123) )/(2.0*c44)
  x5=1.0+( (c13+c344)/(2.0*c44) )
  x6a=((A+C)*c13)/(2.0*(C*c11+A*(2.0*c44+c13)))
  x6b=( pow(C,2.0)*c113+pow(A,2.0)*c333+2.0*A*C*(c133+2.0*c344) ) / pow( (A+C), 3.0)
  x6=M+x6a+x6b
  x7=( (A+C)*c13+0.5*C*(c113-c123)+A*c344 )/(C*(c11-c12)+2.0*A*c44)
  x8a=(A+C)/( 2.0*(C*c44+A*(c33-c44-c13)) )
  x8b=c13+(A*C/pow( (A+C), 2.0))*(c113+c333-c113)
  x8c=pow( ((C-A)/(C+A)),2.0)*c344
  x8=M+x8a*(x8b+x8c)
  x=(x1*x1+x2*x2+x3*x3+x4*x4+x5*x5+x6*x6+x7*x7+x8*x8)/41.0

  xav1=(x1+x2+x3+x4+x5+x6+x7+x8)/41.0
  xav=pow(xav1,2.0)

  #This is formulation for Gruneisen constant.
  #along theeta zero i.e. for shear wave.

  y1a=(A*(c44+2.0*c344)+C*(c44+2.0*c155))/(C*c11+A*(2.0*c44+c13))
  y1=L*M*( 1+y1a)
  y2=-L*M*( 1+y1a)
  y3a=(A*(c44+2.0*c344)+C*(c44+2.0*c155))/(C*c11+A*(2.0*c44+c13))
  y3=K*L*M*(1+y3a)
  y4=-K*L*M*(1+y3a)
  y5a=(c155+2.0*c44-c144)/(C*(c11-c12)+2.0*A*c44)
  y5=-pow(AC,0.5)*y5a
  y6=pow(AC,0.5)*y5a
  y7a=( (A-C)*(c344-c155)-(A+C)*c44)/(C*c44+A*(c33-c44-c13))
  y7=-(pow(AC,0.5)/(A+C))*(1+y7a)
  y8=(pow(AC,0.5)/(A+C))*(1+y7a)
  y9=-(1.0/1.414)*(pow(AC,0.5)/(A+C))*(1+y7a)
  y10=(1.0/1.414)*(pow(AC,0.5)/(A+C))*(1+y7a)
  y=(y1*y1+y2*y2+y3*y3+y4*y4+y5*y5+y6*y6+y7*y7+y8*y8+y9*y9+y10*y10)/16.0
  yav1=(y1+y2+y3+y4+y5+y6+y7+y8+y9+y10)/16.0
  yav=pow(yav1,2.0)

  #calculation of attenuation
  Vl=math.sqrt(c33/dd) 
  Vs=math.sqrt(c44/dd)
  V=pow(3,0.333)*pow((1/pow(Vl,3)+2/pow(Vs,3)),-0.333)
  Cv=Cva*pow(10,Cvb)
  Eo=Eoa*pow(10,Eob)
  ko=koa*pow(10,kob)
  to=3*ko/(Cv*V*V)
  tl=2*to 
  ts=to
  Dl=9*x-( (3*xav*Cv*T)/Eo)
  Ds=9*y
  ath=(4.0*3.14*3.14*xav*ko*T)/(2*dd*pow(Vl,5))
  al=4*3.14*3.14*tl*Eo*Dl/(3*dd*pow(Vl,3))
  as1=4*3.14*3.14*ts*Eo*Ds/(3*dd*pow(Vs,3))

  for j in range(m):
    f[j]=f[j]*pow(10,6)
    athw[j]=ath*pow(f[j],2.0)
    alw[j]=al*pow(f[j],2.0)
    asw[j]=as1*pow(f[j],2.0)

  while 1:
    print(" Enter 1 to see velocity""\n")
    print(" Enter 2 to see Gruneisen constants and DL, DS ""\n")
    print(" Enter 3 to see attenuation values""\n")
    print(" Enter 4 to Print all data""\n")
    print(" Enter 5 for EXIT""\n")

    J = int(input(" What is your choice="))

    if J == 1:
      print("Table of velocity for hcp compound-""\n\n";
      print("Compound name="+comp+"\n\n";

      print("----------------------------------------------------------""\n";
      print("theeta""\t\t""v1 " "\t\t"+"v2 " "\t\t"+"v3 " "\n";
      print("----------------------------------------------------------""\n";
      for i in range(11):
        print(""+str(tth[i])+"\t"+""+str(v1[i])+"\t"+""+str(v2[i])+"\t"+""+str(v3[i])+"\n";
      print("----------------------------------------------------------""\n";
    elif J == 2:
	  print("Value of relaxation time="+str(to)+"\n\n";
	  print("Value of long.relax.time="+str(tl)+"\n\n";
	  print("Value of shearrelax.time="+str(ts)+"\n\n";
	  print("Value of Gruneisen contants are as follow:-""\n";
	  print("Along Z-axis for lonitudinal wave""\n";
	  print("Average of Gamma="+str(xav1)+"\n\n";
	  print("Average of square Gamma="+str(x)+"\n\n";
	  print("Square of average Gamma="+str(xav)+"\n\n";
	  print("DL="+str(Dl)+"\n\n";
	  print("Along Z-axis for shear wave""\n";
	  print("Average of Gamma="+str(yav1)+"\n\n";
	  print("Average of square Gamma="+str(y)+"\n\n";
	  print("Square of average Gamma="+str(yav)+"\n\n";
	  print("Ds="+str(Ds)+"\n\n";
    elif J == 3:
      print("Table of ultrasonic attenuation:-""\n\n";
      print("Compound name="+comp+"\n\n";
      print("----------------------------------------------------------""\n";
      print("frequency""\t""alpha(th)""\t""alpha(L)""\t""alpha(s)" "\n";
      print("----------------------------------------------------------""\n";
      for j in range(m):
        print(""+str(f[j])+"\t"+""+str(athw[j])+"\t"""+str(alw[j])+"\t"""+str(asw[j])+"\n";
      print("----------------------------------------------------------""\n";
    elif J == 4:
	  file1 = open("PRN", "a")
      file1.write("Compound name="+comp+"\n\n")
      file1.write("c11="+str(c11)+"\n\n")
      file1.write("c12="+str(c12)+"\n\n")
      file1.write("c13="+str(c13)+"\n\n")
      file1.write("c33="+str(c33)+"\n\n")
      file1.write("c44="+str(c44)+"\n\n")
      file1.write("c66="+str(c66)+"\n\n")
      file1.write("c111="+str(c111)+"\n\n")
      file1.write("c112="+str(c112)+"\n\n")
      file1.write("c113="+str(c113)+"\n\n")
      file1.write("c123="+str(c123)+"\n\n")
      file1.write("c133="+str(c133)+"\n\n")
      file1.write("c144="+str(c144)+"\n\n")
      file1.write("c155="+str(c155)+"\n\n")
      file1.write("c222="+str(c222)+"\n\n")
      file1.write("c333="+str(c333)+"\n\n")
      file1.write("c344="+str(c344)+"\n\n")
      file1.write("Table of velocity for hcp compound-""\n\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("theeta""\t\t""v1 " "\t\t"+"v2 " "\t\t"+"v3 " "\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(11):
        file1.write(""+str(tth[i])+"\t"+""+str(v1[i])+"\t"+""+str(v2[i])+"\t"+""+str(v3[i])+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Value of relaxation time="+str(to)+"\n\n")
      file1.write("Value of long.relax.time="+str(tl)+"\n\n")
      file1.write("Value of shearrelax.time="+str(ts)+"\n\n")
      file1.write("Value of Gruneisen contants are as follow:-""\n")
      file1.write("Along Z-axis for lonitudinal wave""\n")
      file1.write("Average of Gamma="+str(xav1)+"\n\n")
      file1.write("Average of square Gamma="+str(x)+"\n\n")
      file1.write("Square of average Gamma="+str(xav)+"\n\n")
      file1.write("DL="+str(Dl)+"\n\n")
      file1.write("Along Z-axis for shear wave""\n")
      file1.write("Average of Gamma="+str(yav1)+"\n\n")
      file1.write("Average of square Gamma="+str(y)+"\n\n")
      file1.write("Square of average Gamma="+str(yav)+"\n\n")
      file1.write("Ds="+str(Ds)+"\n\n")
      file1.write("Table of ultrasonic attenuation:-""\n\n")
      file1.write("Compound name="+comp+"\n\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("frequency""\t""alpha(th)""\t""alpha(L)""\t""alpha(s)" "\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(m):
        file1.write(""+str(f[j])+"\t"""+str(athw[j])+"\t"""+str(alw[j])+"\t"""+str(asw[j])+"\n")
      file1.write("----------------------------------------------------------""\n")

    elif J == 5:
      exit()
    else:
      print(" You have entered wrong choice, please correct it.")



if __name__ == "__main__":
  
    main()
