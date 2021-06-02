//this program is used when hcp parameter 'a','c' is also temp. dependence.
//Programe for calculate temperature dependent soec and toec,VELOCITY
// attenuation, along Z-AXIS for hcp using different data of c33  .
#include<process.h>
#include<iostream.h>
#include<conio.h>
#include<math.h>
#include<fstream.h>
void main()
{
  //a,a0 is basal plane distance.    p is c/a value for hcp materials.
  //k2 is contants calculated by C33.
 //k3 is contants calculated by k2,a,m,n.
	char comp[10];
	double a[15],a0[15],p[15],va[15],C33[15],C33A[15],k2[15],k3[15],m=1.0,n=2.0;
	double c11[15],c12[15],c13[15],c33[15],c44[15],c66[15],
		c111[15],c112[15],c113[15],c123[15],c133[15],c344[15],
		c144[15],c155[15],c222[15],c333[15];
	int i=0,j;
 //variables to calculate gruneisen constants.

double A[15],C[15],L[15],M[15],K,x1[15],x2[15],x3[15],x4[15],
	x5[15],x6[15],x6a[15],x6b[15],x7[15],x8[15],x8a[15],x8b[15],
	x8c[15],x[15],xav[15],xav1[15],AC[15],XX[15],y1a[15],y1[15],y2[15],y3a[15]
	,y3[15],y4[15],y5a[15],y5[15],y6[15],y7a[15],y7[15],y8[15],y9[15],
       y10[15],y[15],yav[15],yav1[15];
//Variables to calculate ultrasonic attenuation.
int T[15];
double  dd[15],Vl[15],Vs[15],V[15],Cv[15],Cva[15],Cvb[15],Eo[15],Eoa[15],
	Eob[15],ko[15],koa[15],kob[15],to[15],tl[15],ts[15],Dl[15],Ds[15],
	ath[15],al[15],as[15];
//variables for frequency dependent
 double alth[15][15],all[15][15],als[15][15],F[15],FF[15];
 int ii=0,jj;

	clrscr();
	cout<<"\n Enter the compound's name =";
	cin>>comp;
	cout<<"\n Enter the number of c33 data=  ";
	cin>>j;
		for(i=0;i<j;i++)
	{
	cout<<"\n Enter the value of a(basel plane distance) =  ";
	cin>>a[i]>>a0[i];
	}
		for(i=0;i<j;i++)
	{
	cout<<"\n Enter the value of  c/a =  ";
	cin>>p[i];
	}
	for(i=0;i<j;i++)
	{
	cout<<"\n Enter the value of C33 =  ";
	cin>>C33[i]>>C33A[i];
	}
	for(i=0;i<j;i++)
	{
	cout<<"\n enter the temperature=";  cin>>T[i];
	}
	for(i=0;i<j;i++)
	{
	cout<<"\n enter the value of dd=";  cin>>dd[i];
	}
	for(i=0;i<j;i++)
	{
	cout<<"\n enter the value of Cv=";  cin>>Cva[i]>>Cvb[i];
	}
	for(i=0;i<j;i++)
	{
	cout<<"\n enter the value of Eo=";  cin>>Eoa[i]>>Eob[i];
	}
	for(i=0;i<j;i++)
	{
	cout<<"\n enter the value of K=";   cin>>koa[i]>>kob[i];
	}
	cout<<"\n enter the number of frequency=";   cin>>jj;
	for(ii=0;ii<jj;ii++)
	{
	cout<<"\n enter the value of frequency in MHz=";   cin>>F[ii];
	}

	K=1.0/1.414;
 for(i=0;i<j;i++)
 {
 a[i]=a[i]*pow(10,a0[i]);
 va[i]=1.732*pow(a[i],3.0)*p[i]/2.0;
 C33[i]=C33[i]*pow(10,C33A[i]);
 k2[i]=(C33[i]*va[i])/(pow(a[i],4.0)*pow(p[i],4.0)*3.0);
 k3[i]=-(k2[i]*(m+n+6.0))/(6.0*pow(a[i],2.0));
 c11[i]=(167.0*pow(a[i],4.0)*k2[i])/(8.0*va[i]);
 c12[i]=(41.0*pow(a[i],4.0)*k2[i])/(8.0*va[i]);
 c13[i]=(5.0*pow(a[i],4.0)*pow(p[i],2.0)*k2[i])/(3.0*va[i]);
 c33[i]=(3.0*pow(a[i],4.0)*pow(p[i],4.0)*k2[i])/(va[i]);
 c44[i]=(2.0*pow(a[i],4.0)*pow(p[i],2.0)*k2[i])/(va[i]);
 c66[i]=(63.0*pow(a[i],4.0)*k2[i])/(8.0*va[i]);
 c111[i]=((1099.0*pow(a[i],6.0)*k3[i])/(10.0*va[i]))+
	((23.0*pow(a[i],4.0)*k2[i])/(3.0*va[i]));
 c112[i]=((83.0*pow(a[i],6.0)*k3[i])/(5.0*va[i]))-
	((7.0*pow(a[i],4.0)*k2[i])/(5.0*va[i]));
 c113[i]=((5.0*pow(a[i],6.0)*pow(p[i],2.0)*k3[i])/(3.0*va[i]))+
	((pow(a[i],4.0)*pow(p[i],2.0)*k2[i])/(va[i]));
 c123[i]=((7.0*pow(a[i],6.0)*pow(p[i],2.0)*k3[i])/(5.0*va[i]))-
	((pow(a[i],4.0)*pow(p[i],2.0)*k2[i])/(va[i]));
 c133[i]=(16.0*pow(a[i],6.0)*pow(p[i],4.0)*k3[i])/(5.0*va[i]);
 c344[i]=(3.0*pow(a[i],6.0)*pow(p[i],4.0)*k3[i])/(va[i]);
 c144[i]=(2.0*pow(a[i],6.0)*pow(p[i],2.0)*k3[i])/(va[i]);
 c155[i]=(4.0*pow(a[i],6.0)*pow(p[i],2.0)*k3[i])/(3.0*va[i]);
 c222[i]=((175.0*pow(a[i],6.0)*k3[i])/(2.0*va[i]))+
	((39.0*pow(a[i],4.0)*k2[i])/(5.0*va[i]));
 c333[i]=(9.0*pow(a[i],6.0)*pow(p[i],6.0)*k3[i])/(2.0*va[i]);
 //condituional expression
	A[i]=c11[i]-2*c44[i]-c13[i];
	C[i]=c33[i]-2*c44[i]-c13[i];
	L[i]=C[i]/(A[i]+C[i]);
	M[i]=A[i]/(A[i]+C[i]);
	XX[i]=A[i]*C[i];
	if (XX[i]<0)
	AC[i]=-XX[i];
	else
	AC[i]=XX[i];
  //This is formulation for Gruneisen constant.
 //along theeta zero i.e. for longitudinal wave.
  x1[i]=1.0+( (c13[i]+c113[i])/(2.0*c33[i]) );
  x2[i]=(c13[i]+c113[i])/(2.0*c11[i]);
  x3[i]=(c13[i]+c344[i])/(2.0*c44[i]);
  x4[i]=(c13[i]+0.5*(c113[i]-c123[i]) )/(2.0*c44[i]);
  x5[i]=1.0+( (c13[i]+c344[i])/(2.0*c44[i]) );
  x6a[i]=((A[i]+C[i])*c13[i])/(2.0*(C[i]*c11[i]+A[i]*(2.0*c44[i]+c13[i])));
  x6b[i]=( pow(C[i],2.0)*c113[i]+pow(A[i],2.0)*c333[i]
	    +2.0*A[i]*C[i]*(c133[i]+2.0*c344[i]))/pow((A[i]+C[i]), 3.0);
  x6[i]=M[i]+x6a[i]+x6b[i];
  x7[i]=( (A[i]+C[i])*c13[i]+0.5*C[i]*(c113[i]-c123[i])+A[i]*c344[i] )/
	   (C[i]*(c11[i]-c12[i])+2.0*A[i]*c44[i]);
  x8a[i]=(A[i]+C[i])/( 2.0*(C[i]*c44[i]+A[i]*(c33[i]-c44[i]-c13[i])) );
  x8b[i]=c13[i]+(A[i]*C[i]/pow( (A[i]+C[i]), 2.0))*(c113[i]+c333[i]-c113[i]);
  x8c[i]=pow( ((C[i]-A[i])/(C[i]+A[i])),2.0)*c344[i];
  x8[i]=M[i]+x8a[i]*(x8b[i]+x8c[i]);
  x[i]=(x1[i]*x1[i]+x2[i]*x2[i]+x3[i]*x3[i]+x4[i]*x4[i]+x5[i]*x5[i]+
	x6[i]*x6[i]+x7[i]*x7[i]+x8[i]*x8[i])/41.0;
 xav1[i]=(x1[i]+x2[i]+x3[i]+x4[i]+x5[i]+x6[i]+x7[i]+x8[i])/41.0;
  xav[i]=pow(xav1[i],2.0);
 //This is formulation for Gruneisen constant.
 //along theeta zero i.e. for shear wave.
   y1a[i]=(A[i]*(c44[i]+2.0*c344[i])+C[i]*(c44[i]+2.0*c155[i]))/
	    (C[i]*c11[i]+A[i]*(2.0*c44[i]+c13[i]));
  y1[i]=L[i]*M[i]*(1+y1a[i]);
  y2[i]=-L[i]*M[i]*(1+y1a[i]);
  y3a[i]=(A[i]*(c44[i]+2.0*c344[i])+C[i]*(c44[i]+2.0*c155[i]))/
	    (C[i]*c11[i]+A[i]*(2.0*c44[i]+c13[i]));
  y3[i]=K*L[i]*M[i]*(1+y3a[i]);
  y4[i]=-K*L[i]*M[i]*(1+y3a[i]);
  y5a[i]=(c155[i]+2.0*c44[i]-c144[i])/(C[i]*(c11[i]-c12[i])+2.0*A[i]*c44[i]);
  y5[i]=-pow(AC[i],0.5)*y5a[i];
  y6[i]=pow(AC[i],0.5)*y5a[i];
  y7a[i]=( (A[i]-C[i])*(c344[i]-c155[i])-(A[i]+C[i])*c44[i])/
	 (C[i]*c44[i]+A[i]*(c33[i]-c44[i]-c13[i]));
  y7[i]=-(pow(AC[i],0.5)/(A[i]+C[i]))*(1+y7a[i]);
  y8[i]=(pow(AC[i],0.5)/(A[i]+C[i]))*(1+y7a[i]);
  y9[i]=-(1.0/1.414)*(pow(AC[i],0.5)/(A[i]+C[i]))*(1+y7a[i]);
  y10[i]=(1.0/1.414)*(pow(AC[i],0.5)/(A[i]+C[i]))*(1+y7a[i]);
  y[i]=(y1[i]*y1[i]+y2[i]*y2[i]+y3[i]*y3[i]+y4[i]*y4[i]+y5[i]*y5[i]+
	y6[i]*y6[i]+y7[i]*y7[i]+y8[i]*y8[i]+y9[i]*y9[i]+y10[i]*y10[i])/16.0;
 yav1[i]=(y1[i]+y2[i]+y3[i]+y4[i]+y5[i]+y6[i]+y7[i]+y8[i]+y9[i]+
	y10[i])/16.0;
  yav[i]=pow(yav1[i],2.0);
  //calculation of attenuation
   Vl[i]=sqrt(c33[i]/dd[i]);
   Vs[i]=sqrt(c44[i]/dd[i]);
   V[i]=pow(3,0.333)*pow((1/pow(Vl[i],3)+2/pow(Vs[i],3)),-0.333);
   Cv[i]=Cva[i]*pow(10,Cvb[i]);
   Eo[i]=Eoa[i]*pow(10,Eob[i]);
   ko[i]=koa[i]*pow(10,kob[i]);
   to[i]=3*ko[i]/(Cv[i]*V[i]*V[i]);
   tl[i]=2*to[i]; ts[i]=to[i];
   Dl[i]=9*x[i]-( (3*xav[i]*Cv[i]*T[i])/Eo[i]);
   Ds[i]=9*y[i];
   ath[i]=(4.0*3.14*3.14*xav[i]*ko[i]*T[i])/(2*dd[i]*pow(Vl[i],5));
   al[i]=4*3.14*3.14*tl[i]*Eo[i]*Dl[i]/(3*dd[i]*pow(Vl[i],3));
   as[i]=4*3.14*3.14*ts[i]*Eo[i]*Ds[i]/(3*dd[i]*pow(Vs[i],3));
   }
		for (ii=0;ii<jj;ii++)
			{
		FF[ii]=F[ii]*pow(10,6);
			}
	 for(i=0;i<j;i++)
		{
	 for (ii=0;ii<jj;ii++)
		{
		alth[i][ii]=ath[i]*pow(FF[ii],2.0);
		all[i][ii]=al[i]*pow(FF[ii],2.0);
		als[i][ii]=as[i]*pow(FF[ii],2.0);
		}
		}


 clrscr();
 int J;
 while(1)
{
cout<<" Enter 1 to see elastic constants""\n";
cout<<" Enter 2 to see Cv,Eo,density,thermalconductivity""\n";
cout<<" Enter 3 to see vel and relaxtion time""\n";
cout<<" Enter 4 to see gruneisen const. and DL, DS values""\n";
cout<<" Enter 5 to see temp. depend. attenuation values""\n";
cout<<" Enter 6 to see frequency depencent attenuation values""\n";
cout<<" Enter 7 to Print all data""\n";
cout<<" Enter 8 for EXIT""\n";
cout<<" What is your choice=";
cin>>J;
 clrscr();
 switch(J)
 {
 case 1:
  clrscr();
  cout<<"This result is for HCP compound="<<comp<<"\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"Temp""\t\t""a""\t\t""c/a ""\n";
 cout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 cout<<""<<T[i]<<"\t"<<a[i]<<"\t"<<""<<p[i]<<"\n";
 }
 cout<<"----------------------------------------------------------""\n";
 getch();
 clrscr();
 cout<<" This is table for second order elastic constant. ""\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"temp""\t""c11""\t\t""c12 " "\t\t"<<"c13 " "\n";
 cout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 cout<<""<<T[i]<<"\t"<<c11[i]<<"\t"<<""<<c12[i]<<"\t"<<""<<c13[i]<<"\n";
 }
  getch();
 clrscr();
 cout<<"----------------------------------------------------------""\n";
 cout<<"temp""c33""\t\t""c44 " "\t\t"<<"c66 " "\n";
 cout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 cout<<""<<T[i]<<"\t"<<c33[i]<<"\t"<<""<<c44[i]<<"\t"<<""<<c66[i]<<"\n";
 }
 cout<<"----------------------------------------------------------""\n";
 getch();
 clrscr();
 cout<<" This is table for third order elastic constant. ""\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"temp""c111""\t\t""c112 " "\t\t"<<"c113 " "\t\t"<<"C123 " "\n";
 cout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 cout<<""<<T[i]<<"\t"<<c111[i]<<"\t"<<c112[i]<<"\t"<<c113[i]<<"\t"<<c123[i]<<"\n";
  }
  getch();
 clrscr();
  cout<<"----------------------------------------------------------""\n";
 cout<<"temp""c133""\t\t""c344 " "\t\t"<<"c144 " "\n";
 cout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 cout<<""<<T[i]<<"\t"<<c133[i]<<"\t"<<c344[i]<<"\t"<<c144[i]<<"\n";
  }
  getch();
 clrscr();
 cout<<"----------------------------------------------------------""\n";
 cout<<"temp""c155""\t\t""c222 " "\t\t""c333 " "\n";
 cout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 cout<<""<<T[i]<<"\t"<<c155[i]<<"\t"<<c222[i]<<"\t"<<c333[i]<<"\n";
  }
  cout<<"----------------------------------------------------------""\n";

	   getch();
	   clrscr();
	   break;
  case 2:
 cout<<"This is table for Cv,Eo,Density and thermal cond.""\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"temp""\t""density""\t""Cv""\t""E0""\t""K""\n";
 cout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 cout<<""<<T[i]<<"\t"<<dd[i]<<"\t"<<Cv[i]<<"\t"<<Eo[i]<<"\t"<<ko[i]<<"\n";
  }
  cout<<"----------------------------------------------------------""\n";
   getch();
   clrscr();
   break;
  case 3:
 cout<<" This is table for velocity. ""\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"Temp.""\t\t""Vl""\t\t""Vs" "\n";
 cout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 cout<<""<<T[i]<<"\t"<<""<<Vl[i]<<"\t"<<""<<Vs[i]<<"\n";
 }
 cout<<"----------------------------------------------------------""\n";
  getch();
cout<<" This is table for debye avg.velocity and relax. time. ""\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"Temp.""\t\t""V""\t\t""Relax. time" "\n";
 cout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 cout<<""<<T[i]<<"\t"<<""<<V[i]<<"\t"<<""<<to[i]<<"\n";
 }
 cout<<"----------------------------------------------------------""\n";
 getch();
   clrscr();
   break;
   case 4:
	cout<<"Value of Gruneisen contants are as follow:-""\n";
	cout<<"Along Z-axis for lonitudinal wave""\n";
	cout<<"Average of Gamma=xav1""\n";
	cout<<"Average of square Gamma=x""\n";
	cout<<"Square of average Gamma=xav""\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"Temp.""\t""xav1""\t\t""xav""\t""x""\t\t""DL""\n";
 cout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 cout<<""<<T[i]<<"\t"<<xav1[i]<<"\t"<<xav[i]<<"\t"<<x[i]<<"\t"<<Dl[i]<<"\n";
 }
 cout<<"----------------------------------------------------------""\n";
	getch();
	cout<<"Along Z-axis for shear wave""\n";
	cout<<"Average of Gamma =yav1""\n";
	cout<<"Average of square Gamma=y""\n";
	cout<<"Square of average Gamma=yav""\n";
  cout<<"----------------------------------------------------------""\n";
 cout<<"Temp.""\t""yav1""\t\t""y""\t""Ds""\n";
 cout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 cout<<""<<T[i]<<"\t"<<yav1[i]<<"\t"<<y[i]<<"\t"<<Ds[i]<<"\n";
 }
 cout<<"----------------------------------------------------------""\n";
 getch();
 clrscr();
 break;
case 5:
cout<<"Table of ultrasonic attenuation:-""\n\n";
cout<<"Compound name="<<comp<<"\n\n";

cout<<"----------------------------------------------------------""\n";
cout<<"temp""\t""alpha(th)""\t""alpha(L)""\t""alpha(s)" "\n";
cout<<"----------------------------------------------------------""\n";
for(i=0;i<j;i++)
	{
cout<<""<<T[i]<<"\t"<<ath[i]<<"\t"<<al[i]<<"\t"<<as[i]<<"\n";
       }
cout<<"----------------------------------------------------------""\n";
	   getch();
	   clrscr();
	   break;
 case 6:
for (i=0;i<j;i++)
{
cout<<"At the temperature="<<T[i]<<"\n";
cout<<"----------------------------------------------------------""\n";
cout<<"frequency""\t""alpha(th)""\t""alpha(L)""\t""alpha(s)" "\n";
cout<<"----------------------------------------------------------""\n";
for(ii=0;ii<jj;ii++)
	{

	cout<<""<<F[ii]<<"\t"<<alth[i][ii]<<"\t"<<all[i][ii]<<"\t"<<als[i][ii]<<"\n";

       }
cout<<"----------------------------------------------------------""\n";
	   getch();
	   clrscr();
	   }
	   getch();
	   clrscr();
	   break;


  case 7:
	   fstream fout;
	   fout.open("PRN",ios::out);
  fout<<"Compound name="<<comp<<"\n\n";
  fout<<"This result is for HCP compound="<<comp<<"\n";
 fout<<"----------------------------------------------------------""\n";
 fout<<"Temp""\t\t""a""\t\t""c/a ""\n";
 fout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 fout<<""<<T[i]<<"\t"<<a[i]<<"\t"<<""<<p[i]<<"\n";
 }
 fout<<"----------------------------------------------------------""\n";
 fout<<" This is table for second order elastic constant. ""\n";
 fout<<"----------------------------------------------------------""\n";
 fout<<"Temp""\t\t""c11""\t\t""c12 " "\t\t"<<"c13 " "\n";
 fout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 fout<<""<<T[i]<<"\t"<<c11[i]<<"\t"<<""<<c12[i]<<"\t"<<""<<c13[i]<<"\n";
 }
 fout<<"----------------------------------------------------------""\n";
 fout<<"Temp""\t\t""c33""\t\t""c44 " "\t\t"<<"c66 " "\n";
 fout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 fout<<""<<T[i]<<"\t"<<c33[i]<<"\t"<<""<<c44[i]<<"\t"<<""<<c66[i]<<"\n";
 }
 fout<<"----------------------------------------------------------""\n";
 fout<<" This is table for third order elastic constant. ""\n";
 fout<<"----------------------------------------------------------""\n";
 fout<<"Temp""\t\t""c111""\t\t""c112 " "\t\t""c113 " "\t\t""C123 " "\n";
 fout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 fout<<""<<T[i]<<"\t"<<c111[i]<<"\t"<<c112[i]<<"\t"<<c113[i]<<"\t"<<c123[i]<<"\n";
  }
  fout<<"----------------------------------------------------------""\n";
 fout<<"Temp""\t\t""c133""\t\t""c344 " "\t\t"<<"c144 " "\n";
 fout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 fout<<""<<T[i]<<"\t"<<c133[i]<<"\t"<<c344[i]<<"\t"<<c144[i]<<"\n";
  }
 fout<<"----------------------------------------------------------""\n";
 fout<<"Temp""\t\t""c155""\t\t""c222 " "\t\t""c333 " "\n";
 fout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 fout<<""<<T[i]<<"\t"<<c155[i]<<"\t"<<c222[i]<<"\t"<<c333[i]<<"\n";
  }
  fout<<"----------------------------------------------------------""\n";
 fout<<"This is table for Cv,Eo,Density and thermal cond.""\n";
 fout<<"----------------------------------------------------------""\n";
 fout<<"temp""\t""density""\t""Cv""\t""E0""\t""K""\n";
 fout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 fout<<""<<T[i]<<"\t"<<dd[i]<<"\t"<<Cv[i]<<"\t"<<Eo[i]<<"\t"<<ko[i]<<"\n";
  }
  fout<<"----------------------------------------------------------""\n";
  fout<<" This is table for velocity. ""\n";
 fout<<"----------------------------------------------------------""\n";
 fout<<"Temp.""\t\t""Vl""\t\t""Vs" "\n";
 fout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 fout<<""<<T[i]<<"\t"<<""<<Vl[i]<<"\t"<<""<<Vs[i]<<"\n";
 }
 fout<<"----------------------------------------------------------""\n";
 fout<<" This is table for debye avg.velocity and relax. time. ""\n";
 fout<<"----------------------------------------------------------""\n";
 fout<<"Temp.""\t\t""V""\t\t""Relax. time" "\n";
 fout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 fout<<""<<T[i]<<"\t"<<""<<V[i]<<"\t"<<""<<to[i]<<"\n";
 }
 fout<<"----------------------------------------------------------""\n";
	fout<<"Value of Gruneisen contants are as follow:-""\n";
	fout<<"Along Z-axis for lonitudinal wave""\n";
	fout<<"Average of Gamma=xav1""\n";
	fout<<"Average of square Gamma=x""\n";
	fout<<"Square of average Gamma=xav""\n";
 fout<<"----------------------------------------------------------""\n";
 fout<<"Temp.""\t""xav1""\t\t""xav""\t""x""\t\t""DL""\n";
 fout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 fout<<""<<T[i]<<"\t"<<xav1[i]<<"\t"<<xav[i]<<"\t"<<x[i]<<"\t"<<Dl[i]<<"\n";
 }
 fout<<"----------------------------------------------------------""\n";
	fout<<"Along Z-axis for shear wave""\n";
	fout<<"Average of Gamma =yav1""\n";
	fout<<"Average of square Gamma=y""\n";
	fout<<"Square of average Gamma=yav""\n";
  fout<<"----------------------------------------------------------""\n";
 fout<<"Temp.""\t""yav1""\t\t""y""\t""Ds""\n";
 fout<<"----------------------------------------------------------""\n";
 for(i=0;i<j;i++)
 {
 fout<<""<<T[i]<<"\t"<<yav1[i]<<"\t"<<y[i]<<"\t"<<Ds[i]<<"\n";
 }
 fout<<"----------------------------------------------------------""\n";
 fout<<"Table of ultrasonic attenuation:-""\n\n";
fout<<"Compound name="<<comp<<"\n\n";

fout<<"----------------------------------------------------------""\n";
fout<<"temp""\t""alpha(th)""\t""alpha(L)""\t""alpha(s)" "\n";
fout<<"----------------------------------------------------------""\n";
for(i=0;i<j;i++)
	{
fout<<""<<T[i]<<"\t"<<ath[i]<<"\t"<<al[i]<<"\t"<<as[i]<<"\n";
       }
fout<<"----------------------------------------------------------""\n";
for (i=0;i<j;i++)
{
 fout<<"At the temperature="<<T[i]<<"\n";
fout<<"----------------------------------------------------------""\n";
fout<<"frequency""\t""alpha(th)""\t""alpha(L)""\t""alpha(s)" "\n";
fout<<"----------------------------------------------------------""\n";
for(ii=i;ii<jj;ii++)
	{

	fout<<""<<F[ii]<<"\t"<<alth[ii]<<"\t"<<all[ii]<<"\t"<<als[ii]<<"\n";
       }
fout<<"----------------------------------------------------------""\n";
    }


 getch();
 clrscr();
 break;
 case 8:
	exit (1);
 default:
	cout<<" You have entered wrong choice, please correct it.";
	getch();
	clrscr();
	break;
	}
	}
	}
