#this program is used when hcp parameter 'a','c' is also temp. dependence.
#Programe for calculate temperature dependent soec and toec,VELOCITY
# attenuation, along Z-AXIS for hcp using different data of c33  .


import math

def main():
  #a,a0 is basal plane distance.    p is c/a value for hcp materials.
  #k2 is contants calculated by C33.
  #k3 is contants calculated by k2,a,m,n. 
  m, n = 1.0, 2.0
  a, a0, p, va, C33, C33A, k2, k3 = ([0.0 for x in range(15)] for i in range(8))
  c11, c12, c13, c33, c44, c66, c111, c112, c113, c123, c133, c344, c144, c155, c222, c333 = ([0.0 for x in range(15)] for i in range(16))
  
  #variables to calculate gruneisen constants.
  A,C,L,M,K,x1,x2,x3,x4,x5,x6,x6a,x6b,x7,x8,x8a,x8b,x8c,x,xav,xav1,AC,XX,y1a,y1,y2,y3a,y3,y4,y5a,y5,y6,y7a,y7,y8,y9,y10,y,yav,yav1 = ([0.0 for x in range(15)] for i in range(40))
  
  #Variables to calculate ultrasonic attenuation.
  T = [0.0 for x in range(15)]
  dd, Vl, Vs, V, Cv, Cva, Cvb ,Eo, Eoa, Eob, ko, koa, kob, to, tl, ts, Dl, Ds, ath, al, as1 = ([0.0 for x in range(15)] for i in range(21))
  
  #variables for frequency dependent
  alth, all, als = ([[0.0 for x in range(15)] for y in range(15)] for i in range(3))
  F,FF = ([0 for x in range(15)] for i in range(2))
  
  comp = input(" Enter the compound's name = ")
  j = int(input("Enter the number of c33 data=  "))
  
  print("Enter the value of a(basel plane distance) in 'a' 'a0' format= ")
  for i in range(j):
    a[i], a0[i] = (float(k) for k in (input().split()))
  
  print("Enter the value of  c/a =  ")
  for i in range(j):
    p[i] = (float(input()))

  print("Enter the value of C33 =  ")
  for i in range(j):
    C33[i], C33A[i] = (float(k) for k in (input().split()))

  print("enter the value of dd= ")
  for i in range(j):
    dd[i] = (float(input()))

  print("enter the temperature= ")
  for i in range(j):
    T[i] = (float(input()))

  print("enter the value of Cv= ")
  for i in range(j):
    Cva[i], Cvb[i] = (float(k) for k in (input().split())) 

  print("enter the value of Eo=")
  for i in range(j):
    Eoa[i], Eob[i] = (float(k) for k in (input().split()))
    
  print("enter the value of K=")
  for i in range(j):
    koa[i], kob[i] = (float(k) for k in (input().split()))
  
  jj = int(input("enter the number of frequency= "))

  print("enter the value of frequency in MHz=")
  for i in range(j):
    F[i] = (float(input()))
    
  K = 1.0/1.414
  
  for i in range(j):
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
    x1[i]=1.0+( (c13[i]+c113[i])/(2.0*c33[i]) )
    x2[i]=(c13[i]+c113[i])/(2.0*c11[i])
    x3[i]=(c13[i]+c344[i])/(2.0*c44[i])
    x4[i]=(c13[i]+0.5*(c113[i]-c123[i]) )/(2.0*c44[i])
    x5[i]=1.0+( (c13[i]+c344[i])/(2.0*c44[i]) )
    x6a[i]=((A[i]+C[i])*c13[i])/(2.0*(C[i]*c11[i]+A[i]*(2.0*c44[i]+c13[i])))
    x6b[i]=( pow(C[i],2.0)*c113[i]+pow(A[i],2.0)*c333[i]+2.0*A[i]*C[i]*(c133[i]+2.0*c344[i]))/pow((A[i]+C[i]), 3.0)
    x6[i]=M[i]+x6a[i]+x6b[i]
    x7[i]=( (A[i]+C[i])*c13[i]+0.5*C[i]*(c113[i]-c123[i])+A[i]*c344[i] )/(C[i]*(c11[i]-c12[i])+2.0*A[i]*c44[i])
    x8a[i]=(A[i]+C[i])/( 2.0*(C[i]*c44[i]+A[i]*(c33[i]-c44[i]-c13[i])) )
    x8b[i]=c13[i]+(A[i]*C[i]/pow( (A[i]+C[i]), 2.0))*(c113[i]+c333[i]-c113[i])
    x8c[i]=pow( ((C[i]-A[i])/(C[i]+A[i])),2.0)*c344[i]
    x8[i]=M[i]+x8a[i]*(x8b[i]+x8c[i])
    x[i]=(x1[i]*x1[i]+x2[i]*x2[i]+x3[i]*x3[i]+x4[i]*x4[i]+x5[i]*x5[i]+x6[i]*x6[i]+x7[i]*x7[i]+x8[i]*x8[i])/41.0
    xav1[i]=(x1[i]+x2[i]+x3[i]+x4[i]+x5[i]+x6[i]+x7[i]+x8[i])/41.0
    xav[i]=pow(xav1[i],2.0)
    
    #This is formulation for Gruneisen constant.
    #along theeta zero i.e. for shear wave.
    y1a[i]=(A[i]*(c44[i]+2.0*c344[i])+C[i]*(c44[i]+2.0*c155[i]))/(C[i]*c11[i]+A[i]*(2.0*c44[i]+c13[i]))
    y1[i]=L[i]*M[i]*(1+y1a[i])
    y2[i]=-L[i]*M[i]*(1+y1a[i])
    y3a[i]=(A[i]*(c44[i]+2.0*c344[i])+C[i]*(c44[i]+2.0*c155[i]))/(C[i]*c11[i]+A[i]*(2.0*c44[i]+c13[i]))
    y3[i]=K*L[i]*M[i]*(1+y3a[i])
    y4[i]=-K*L[i]*M[i]*(1+y3a[i])
    y5a[i]=(c155[i]+2.0*c44[i]-c144[i])/(C[i]*(c11[i]-c12[i])+2.0*A[i]*c44[i])
    y5[i]=-pow(AC[i],0.5)*y5a[i]
    y6[i]=pow(AC[i],0.5)*y5a[i]
    y7a[i]=( (A[i]-C[i])*(c344[i]-c155[i])-(A[i]+C[i])*c44[i])/(C[i]*c44[i]+A[i]*(c33[i]-c44[i]-c13[i]))
    y7[i]=-(pow(AC[i],0.5)/(A[i]+C[i]))*(1+y7a[i])
    y8[i]=(pow(AC[i],0.5)/(A[i]+C[i]))*(1+y7a[i])
    y9[i]=-(1.0/1.414)*(pow(AC[i],0.5)/(A[i]+C[i]))*(1+y7a[i])
    y10[i]=(1.0/1.414)*(pow(AC[i],0.5)/(A[i]+C[i]))*(1+y7a[i])
    y[i]=(y1[i]*y1[i]+y2[i]*y2[i]+y3[i]*y3[i]+y4[i]*y4[i]+y5[i]*y5[i]+y6[i]*y6[i]+y7[i]*y7[i]+y8[i]*y8[i]+y9[i]*y9[i]+y10[i]*y10[i])/16.0
    yav1[i]=(y1[i]+y2[i]+y3[i]+y4[i]+y5[i]+y6[i]+y7[i]+y8[i]+y9[i]+
    y10[i])/16.0
    yav[i]=pow(yav1[i],2.0)
    
    #calculation of attenuation
    Vl[i]=math.sqrt(c33[i]/dd[i])
    Vs[i]=math.sqrt(c44[i]/dd[i])
    V[i]=pow(3,0.333)*pow((1/pow(Vl[i],3)+2/pow(Vs[i],3)),-0.333)
    Cv[i]=Cva[i]*pow(10,Cvb[i])
    Eo[i]=Eoa[i]*pow(10,Eob[i])
    ko[i]=koa[i]*pow(10,kob[i])
    to[i]=3*ko[i]/(Cv[i]*V[i]*V[i])
    tl[i]=2*to[i]
    ts[i]=to[i]
    Dl[i]=9*x[i]-( (3*xav[i]*Cv[i]*T[i])/Eo[i])
    Ds[i]=9*y[i]
    ath[i]=(4.0*3.14*3.14*xav[i]*ko[i]*T[i])/(2*dd[i]*pow(Vl[i],5))
    al[i]=4*3.14*3.14*tl[i]*Eo[i]*Dl[i]/(3*dd[i]*pow(Vl[i],3))
    as1[i]=4*3.14*3.14*ts[i]*Eo[i]*Ds[i]/(3*dd[i]*pow(Vs[i],3))
    
  for ii in range(jj):
    FF[ii]=F[ii]*pow(10,6)
    
  for i in range(j):
    for ii in range(jj):
      alth[i][ii]=ath[i]*pow(FF[ii],2.0)
      all[i][ii]=al[i]*pow(FF[ii],2.0)
      als[i][ii]=as1[i]*pow(FF[ii],2.0)
  
  
  while(1):
    print(" Enter 1 to see elastic constants""\n")
    print(" Enter 2 to see Cv,Eo,density,thermalconductivity""\n")
    print(" Enter 3 to see vel and relaxtion time""\n")
    print(" Enter 4 to see gruneisen const. and DL, DS values""\n")
    print(" Enter 5 to see temp. depend. attenuation values""\n")
    print(" Enter 6 to see frequency depencent attenuation values""\n")
    print(" Enter 7 to Print all data""\n")
    print(" Enter 8 for EXIT""\n")
    print(" What is your choice= ")
    
    J = input()
    if J ==  '1':
      print("This result is for HCP compound="+comp)
      print("----------------------------------------------------------")
      print("Temp""\t\t""a""\t\t""c/a ""\n")
      print("----------------------------------------------------------")
      for i in range(j):
        print(""+str(T[i])+"\t"+str(a[i])+"\t"+""+str(p[i]))
      print("----------------------------------------------------------")
      print(" This is table for second order elastic constant. ")
      print("----------------------------------------------------------")
      print("temp""\t""c11""\t\t""c12 " "\t\t"+"c13 " "\n")
      print("----------------------------------------------------------")
      for i in range(j):
        print(""+str(T[i])+"\t"+str(c11[i])+"\t"+""+str(c12[i])+"\t"+""+str(c13[i]))
      print("----------------------------------------------------------")
      print("temp""c33""\t\t""c44 " "\t\t"+"c66 ")
      print("----------------------------------------------------------")
      for i in range(j):
        print(""+str(T[i])+"\t"+str(c33[i])+"\t"+""+str(c44[i])+"\t"+""+str(c66[i]))
      print("----------------------------------------------------------")
      print(" This is table for third order elastic constant. ")
      print("----------------------------------------------------------")
      print("temp""c111""\t\t""c112 " "\t\t"+"c113 " "\t\t"+"C123 ")
      print("----------------------------------------------------------")
      for i in range(j):
        print(""+str(T[i])+"\t"+str(c111[i])+"\t"+str(c112[i])+"\t"+str(c113[i])+"\t"+str(c123[i]))
      print("----------------------------------------------------------")
      print("temp""c133""\t\t""c344 " "\t\t"+"c144 ")
      print("----------------------------------------------------------")
      for i in range(j):
        print(""+str(T[i])+"\t"+str(c133[i])+"\t"+str(c344[i])+"\t"+str(c144[i]))
      print("----------------------------------------------------------")
      print("temp""c155""\t\t""c222 " "\t\t""c333 ")
      print("----------------------------------------------------------")
      print(""+str(T[i])+"\t"+str(c155[i])+"\t"+str(c222[i])+"\t"+str(c333[i]))
      print("----------------------------------------------------------")
    
    elif J == '2':
      print("This is table for Cv,Eo,Density and thermal cond.""\n")
      print("----------------------------------------------------------""\n")
      print("temp""\t""density""\t""Cv""\t""E0""\t""K""\n")
      print("----------------------------------------------------------""\n")
      for i in range(j):
        print(""+str(T[i])+"\t"+str(dd[i])+"\t"+str(Cv[i])+"\t"+str(Eo[i])+"\t"+str(ko[i]))
      print("----------------------------------------------------------")
    
    elif J == '3':
      print(" This is table for velocity. ")
      print("----------------------------------------------------------")
      print("Temp.""\t\t""Vl""\t\t""Vs")
      print("----------------------------------------------------------")
      for i in range(j):
        print(""+str(T[i])+"\t"+""+str(Vl[i])+"\t"+""+str(Vs[i]))
      print("----------------------------------------------------------")
      print(" This is table for debye avg.velocity and relax. time. ")
      print("----------------------------------------------------------")
      
      print("Temp.""\t\t""V""\t\t""Relax. time")
      print("----------------------------------------------------------")
      for i in range(j):
        print(""+str(T[i])+"\t"+""+str(V[i])+"\t"+""+str(to[i])+"\n")
      print("----------------------------------------------------------")
    
    elif J == '4':
      print("Value of Gruneisen contants are as follow:-")
      print("Along Z-axis for lonitudinal wave")
      print("Average of Gamma=xav1")
      print("Average of square Gamma=x")
      print("Square of average Gamma=xav")
      print("----------------------------------------------------------""\n")
      print("Temp.""\t""xav1""\t\t""xav""\t""x""\t\t""DL""\n")
      print("----------------------------------------------------------""\n")
      for i in range(j):
        print(""+str(T[i])+"\t"+str(xav1[i])+"\t"+str(xav[i])+"\t"+str(x[i])+"\t"+str(Dl[i])+"\n")
      print("----------------------------------------------------------""\n")
      print("Along Z-axis for shear wave""\n")
      print("Average of Gamma =yav1""\n")
      print("Average of square Gamma=y""\n")
      print("Square of average Gamma=yav""\n")
      print("----------------------------------------------------------""\n")
      print("Temp.""\t""yav1""\t\t""y""\t""Ds""\n")
      print("----------------------------------------------------------""\n")
      for i in range(j):
        print(""+str(T[i])+"\t"+str(yav1[i])+"\t"+str(y[i])+"\t"+str(Ds[i])+"\n")
    
      print("----------------------------------------------------------""\n")
    
    elif J == '5':
      print("Table of ultrasonic attenuation:-""\n\n")
      print("Compound name="+comp+"\n\n")
    
      print("----------------------------------------------------------""\n")
      print("temp""\t""alpha(th)""\t""alpha(L)""\t""alpha(s)" "\n")
      print("----------------------------------------------------------""\n")
      for i in range(j):
        print(""+str(T[i])+"\t"+str(ath[i])+"\t"+str(al[i])+"\t"+str(as1[i])+"\n")
      print("----------------------------------------------------------""\n")
    
    elif J == '6':
      for i in range(j):
        print("At the temperature="+T[i]+"\n")
        print("----------------------------------------------------------""\n")
        print("frequency""\t""alpha(th)""\t""alpha(L)""\t""alpha(s)" "\n")
        print("----------------------------------------------------------""\n")
        for ii in range(jj):
          print(""+str(F[ii])+"\t"+str(alth[i][ii])+"\t"+str(all[i][ii])+"\t"+str(als[i][ii]))
        print("----------------------------------------------------------""\n")
    
    elif J == '7':
      file1 = open("PRN", "a")
      file1.write("Compound name="+comp+"\n\n")
      file1.write("This result is for HCP compound="+comp+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Temp""\t\t""a""\t\t""c/a ""\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
        file1.write(""+str(T[i])+"\t"+str(a[i])+"\t"+""+str(p[i])+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write(" This is table for second order elastic constant. ""\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Temp""\t\t""c11""\t\t""c12 " "\t\t"+"c13 " "\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
        file1.write(""+str(T[i])+"\t"+str(c11[i])+"\t"+""+str(c12[i])+"\t"+""+str(c13[i])+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Temp""\t\t""c33""\t\t""c44 " "\t\t"+"c66 " "\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
        file1.write(""+str(T[i])+"\t"+str(c33[i])+"\t"+""+str(c44[i])+"\t"+""+str(c66[i])+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write(" This is table for third order elastic constant. ""\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Temp""\t\t""c111""\t\t""c112 " "\t\t""c113 " "\t\t""C123 " "\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
        file1.write(""+str(T[i])+"\t"+str(c111[i])+"\t"+str(c112[i])+"\t"+str(c113[i])+"\t"+str(c123[i])+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Temp""\t\t""c133""\t\t""c344 " "\t\t"+"c144 " "\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
        file1.write(""+str(T[i])+"\t"+str(c133[i])+"\t"+str(c344[i])+"\t"+str(c144[i])+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Temp""\t\t""c155""\t\t""c222 " "\t\t""c333 " "\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
        file1.write(""+str(T[i])+"\t"+str(c155[i])+"\t"+str(c222[i])+"\t"+str(c333[i])+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("This is table for Cv,Eo,Density and thermal cond.""\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("temp""\t""density""\t""Cv""\t""E0""\t""K""\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
        file1.write(""+str(T[i])+"\t"+str(dd[i])+"\t"+str(Cv[i])+"\t"+str(Eo[i])+"\t"+str(ko[i])+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write(" This is table for velocity. ""\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Temp.""\t\t""Vl""\t\t""Vs" "\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
        file1.write(""+str(T[i])+"\t"+""+str(Vl[i])+"\t"+""+str(Vs[i])+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write(" This is table for debye avg.velocity and relax. time. ""\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Temp.""\t\t""V""\t\t""Relax. time" "\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
        file1.write(""+str(T[i])+"\t"+""+str(V[i])+"\t"+""+str(to[i])+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Value of Gruneisen contants are as follow:-""\n")
      file1.write("Along Z-axis for lonitudinal wave""\n")
      file1.write("Average of Gamma=xav1""\n")
      file1.write("Average of square Gamma=x""\n")
      file1.write("Square of average Gamma=xav""\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Temp.""\t""xav1""\t\t""xav""\t""x""\t\t""DL""\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
       file1.write(""+str(T[i])+"\t"+str(xav1[i])+"\t"+str(xav[i])+"\t"+str(x[i])+"\t"+str(Dl[i])+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Along Z-axis for shear wave""\n")
      file1.write("Average of Gamma =yav1""\n")
      file1.write("Average of square Gamma=y""\n")
      file1.write("Square of average Gamma=yav""\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Temp.""\t""yav1""\t\t""y""\t""Ds""\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
        file1.write(""+str(T[i])+"\t"+str(yav1[i])+"\t"+str(y[i])+"\t"+str(Ds[i])+"\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("Table of ultrasonic attenuation:-""\n\n")
      file1.write("Compound name="+comp+"\n\n")
      file1.write("----------------------------------------------------------""\n")
      file1.write("temp""\t""alpha(th)""\t""alpha(L)""\t""alpha(s)" "\n")
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
        file1.write(""+str(T[i])+"\t"+str(ath[i])+"\t"+str(al[i])+"\t"+str(as1[i])+"\n")   
      file1.write("----------------------------------------------------------""\n")
      for i in range(j):
        file1.write("At the temperature="+str(T[i])+"\n")
        file1.write("----------------------------------------------------------""\n")
        file1.write("frequency""\t""alpha(th)""\t""alpha(L)""\t""alpha(s)" "\n")
        file1.write("----------------------------------------------------------""\n")
        for ii in range(jj):
          file1.write(""+str(F[ii])+"\t"+str(alth[ii])+"\t"+str(all[ii])+"\t"+str(als[ii])+"\n")
          file1.write("----------------------------------------------------------""\n")
    elif J == '8':
      exit()
    else:
      print(" You have entered wrong choice, please correct it.")


if __name__ == "__main__":
  
    main()
