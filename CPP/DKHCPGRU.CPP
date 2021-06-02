//This is program to calculate velocity, G.P.,frequency dependent attenuation in
//HCP compound using elastic constant data.
#include<stdio.h>
#include<process.h>
#include<iostream.h>
#include<conio.h>
#include<math.h>
#include<fstream.h>
#include<fstream.h>
void main()
{
char comp[10];

//Vriables to calculate velocity.

double c11,c11a,c12,c12a,c13,c13a,c33,c33a,c44,c44a,c66,c66a,c111,
       c111a,c112,c112a,c113,c113a,c123,c123a,c133,c133a,
       c344,c344a,c144,c144a,c155,c155a,c222,c222a,c333,
       c333a,v1[15],v2[15],v3[15],th[15],xx[15],yy[15],p[15],
       q[15],r[15],s[15],t[15],u[15],v11[15],v22[15],v33[15];
double tth[11]={0.0,5.0,15.0,25.0,35.0,45.0,55.0,65.0,75.0,85.0,90.0};
int    n=11;

//variables to calculate gruneisen constants.

double A,C,L,M,K,x1,x2,x3,x4,x5,x6,x6a,x6b,x7,x8,x8a,x8b,x8c,x
       ,xav,AC,XX,y1a,y1,y2,y3a,y3,y4,y5a,y5,y6,y7a,y7,y8,y9,
       y10,y,yav;

//Variables to calculate ultrasonic attenuation.

int m,T;
double  dd,Vl,Vs,V,Cv,Cva,Cvb,Eo,Eoa,Eob,ko,koa,kob,to,tl,ts,Dl,Ds,ath,al,as,
	athw[15],alw[15],asw[15],f[15];

	clrscr();
	cout<<"\n Enter the compound's name =";
	cin>>comp;
	cout<<"\n Enter the value of temperature =";
	cin>>T;
cout<<"\n Enter all data in CGS SYSTEM";
cout<<"\n enter the value of c11=";   cin>>c11>>c11a;
cout<<"\n enter the value of c12=";   cin>>c12>>c12a;
	cout<<"\n enter the value of c13=";   cin>>c13>>c13a;
	cout<<"\n enter the value of c33=";   cin>>c33>>c33a;
cout<<"\n enter the value of c44=";   cin>>c44>>c44a;
cout<<"\n enter the value of c66=";   cin>>c66>>c66a;
cout<<"\n enter the value of c111=";  cin>>c111>>c111a;
	cout<<"\n enter the value of c112=";  cin>>c112>>c112a;
	cout<<"\n enter the value of c113=";  cin>>c113>>c113a;
	cout<<"\n enter the value of c123=";  cin>>c123>>c123a;
cout<<"\n enter the value of c133=";  cin>>c133>>c133a;
cout<<"\n enter the value of c344=";  cin>>c344>>c344a;
cout<<"\n enter the value of c144=";  cin>>c144>>c144a;
	cout<<"\n enter the value of c155=";  cin>>c155>>c155a;
	cout<<"\n enter the value of c222=";  cin>>c222>>c222a;
	cout<<"\n enter the value of c333=";  cin>>c333>>c333a;
cout<<"\n enter the value of dd=";  cin>>dd;
cout<<"\n enter the value of Cv=";  cin>>Cva>>Cvb;
cout<<"\n enter the value of Eo=";  cin>>Eoa>>Eob;
cout<<"\n enter the value of K=";   cin>>koa>>kob;
cout<<"\n number of frequency have to enter";
cin>>m;
	int j;
	for(j=0;j<m;j++)
	{
	cout <<"\n enter the value of frequency in MHz= ";
	cin>>f[j];
	}
		c11=c11*pow(10,c11a);
		c12=c12*pow(10,c12a);
		c13=c13*pow(10,c13a);
	c33=c33*pow(10,c33a);
	c44=c44*pow(10,c44a);
	c66=c66*pow(10,c66a);
		c111=c111*pow(10,c111a);
		c112=c112*pow(10,c112a);
		c113=c113*pow(10,c113a);
	c123=c123*pow(10,c123a);
	c133=c133*pow(10,c133a);
	c344=c344*pow(10,c344a);
		c144=c144*pow(10,c144a);
		c155=c155*pow(10,c155a);
		c222=c222*pow(10,c222a);
		c333=c333*pow(10,c333a);

//This is formulation for velocity at different theeta.

for(int i=0;i<n;i++)
	{
	th[i]=(tth[i]*22)/(180*7);

	xx[i]=sin(th[i]);

	yy[i]=cos(th[i]);

	p[i]=pow(xx[i],2.0);

	q[i]=pow(yy[i],2.0);

	r[i]=c11*p[i]-c33*q[i]+c44*(q[i]-p[i]);

	s[i]=pow(r[i],2);

	t[i]=4.0*p[i]*q[i]*pow( (c13+c44), 2);

	u[i]=pow( (s[i]+t[i]),0.5);

	v11[i]=(c33*q[i]+c11*p[i]+c44+u[i])/2;
	v1[i]=sqrt(v11[i]/dd);

	v22[i]=(c33*q[i]+c11*p[i]+c44-u[i])/2;
	v2[i]=sqrt(v22[i]/dd);

	v33[i]=c44*q[i]+((c11-c12)/2.0)*p[i];
	v3[i]=sqrt(v33[i]/dd);

	}


	A=c11-2*c44-c13;
	C=c33-2*c44-c13;
	L=C/(A+C);
	M=A/(A+C);
	K=1.0/1.414;
	XX=A*C;
	if (XX<0)
	AC=-XX;
	else
	AC=XX;
  //This is formulation for Gruneisen constant.
 //along theeta zero i.e. for longitudinal wave.
  x1=1.0+( (c13+c113)/(2.0*c33) );
  x2=(c13+c113)/(2.0*c11);
  x3=(c13+c344)/(2.0*c44);
  x4=(c13+0.5*(c113-c123) )/(2.0*c44);
  x5=1.0+( (c13+c344)/(2.0*c44) );
  x6a=((A+C)*c13)/(2.0*(C*c11+A*(2.0*c44+c13)));
  x6b=( pow(C,2.0)*c113+pow(A,2.0)*c333
	    +2.0*A*C*(c133+2.0*c344) ) / pow( (A+C), 3.0);
  x6=M+x6a+x6b;
  x7=( (A+C)*c13+0.5*C*(c113-c123)+A*c344 )/
	   (C*(c11-c12)+2.0*A*c44);
  x8a=(A+C)/( 2.0*(C*c44+A*(c33-c44-c13)) );
  x8b=c13+(A*C/pow( (A+C), 2.0))*(c113+c333-c113);
  x8c=pow( ((C-A)/(C+A)),2.0)*c344;
  x8=M+x8a*(x8b+x8c);
  x=(x1*x1+x2*x2+x3*x3+x4*x4+x5*x5+x6*x6+x7*x7+x8*x8)/41.0;
double xav1=(x1+x2+x3+x4+x5+x6+x7+x8)/41.0;
  xav=pow(xav1,2.0);

 //This is formulation for Gruneisen constant.
 //along theeta zero i.e. for shear wave.
   y1a=(A*(c44+2.0*c344)+C*(c44+2.0*c155))/
	    (C*c11+A*(2.0*c44+c13));
  y1=L*M*( 1+y1a);
  y2=-L*M*( 1+y1a);
  y3a=(A*(c44+2.0*c344)+C*(c44+2.0*c155))/
	    (C*c11+A*(2.0*c44+c13));
  y3=K*L*M*(1+y3a);
  y4=-K*L*M*(1+y3a);
  y5a=(c155+2.0*c44-c144)/(C*(c11-c12)+2.0*A*c44);
  y5=-pow(AC,0.5)*y5a;
  y6=pow(AC,0.5)*y5a;
  y7a=( (A-C)*(c344-c155)-(A+C)*c44)/(C*c44+A*(c33-c44-c13));
  y7=-(pow(AC,0.5)/(A+C))*(1+y7a);
  y8=(pow(AC,0.5)/(A+C))*(1+y7a);
  y9=-(1.0/1.414)*(pow(AC,0.5)/(A+C))*(1+y7a);
  y10=(1.0/1.414)*(pow(AC,0.5)/(A+C))*(1+y7a);
  y=(y1*y1+y2*y2+y3*y3+y4*y4+y5*y5+y6*y6+y7*y7+y8*y8+y9*y9+
  y10*y10)/16.0;
double  yav1=(y1+y2+y3+y4+y5+y6+y7+y8+y9+y10)/16.0;
  yav=pow(yav1,2.0);

 //calculation of attenuation
   Vl=sqrt(c33/dd);
   Vs=sqrt(c44/dd);
   V=pow(3,0.333)*pow((1/pow(Vl,3)+2/pow(Vs,3)),-0.333);
   Cv=Cva*pow(10,Cvb);
   Eo=Eoa*pow(10,Eob);
   ko=koa*pow(10,kob);
   to=3*ko/(Cv*V*V);
   tl=2*to; ts=to;
   Dl=9*x-( (3*xav*Cv*T)/Eo);
   Ds=9*y;
   ath=(4.0*3.14*3.14*xav*ko*T)/(2*dd*pow(Vl,5));
   al=4*3.14*3.14*tl*Eo*Dl/(3*dd*pow(Vl,3));
   as=4*3.14*3.14*ts*Eo*Ds/(3*dd*pow(Vs,3));

   for(j=0;j<m;j++)
	      {
     f[j]=f[j]*pow(10,6);

     athw[j]=ath*pow(f[j],2.0);

     alw[j]=al*pow(f[j],2.0);

     asw[j]=as*pow(f[j],2.0);
	      }


 clrscr();
 int J;
 while(1)
{
cout<<" Enter 1 to see velocity""\n";
cout<<" Enter 2 to see Gruneisen constants and DL, DS ""\n";
cout<<" Enter 3 to see attenuation values""\n";
cout<<" Enter 4 to Print all data""\n";
cout<<" Enter 5 for EXIT""\n";
cout<<" What is your choice=";
cin>>J;
 clrscr();
 switch(J)
 {
 case 1:
 cout<<"Table of velocity for hcp compound-""\n\n";
 cout<<"Compound name="<<comp<<"\n\n";

 cout<<"----------------------------------------------------------""\n";
 cout<<"theeta""\t\t""v1 " "\t\t"<<"v2 " "\t\t"<<"v3 " "\n";
 cout<<"----------------------------------------------------------""\n";
  for(i=0;i<11;i++)
	{
 cout<<""<<tth[i]<<"\t"<<""<<v1[i]<<"\t"<<""<<v2[i]<<"\t"<<""<<v3[i]<<"\n";
       }
  cout<<"----------------------------------------------------------""\n";
	   getch();
	   clrscr();
	   break;
  case 2:
	cout<<"Value of relaxation time="<<to<<"\n\n";
	cout<<"Value of long.relax.time="<<tl<<"\n\n";
	cout<<"Value of shearrelax.time="<<ts<<"\n\n";

	cout<<"Value of Gruneisen contants are as follow:-""\n";
	cout<<"Along Z-axis for lonitudinal wave""\n";
	cout<<"Average of Gamma="<<xav1<<"\n\n";
	cout<<"Average of square Gamma="<<x<<"\n\n";
	cout<<"Square of average Gamma="<<xav<<"\n\n";
	cout<<"DL="<<Dl<<"\n\n";
	cout<<"Along Z-axis for shear wave""\n";
	cout<<"Average of Gamma="<<yav1<<"\n\n";
	cout<<"Average of square Gamma="<<y<<"\n\n";
	cout<<"Square of average Gamma="<<yav<<"\n\n";
	cout<<"Ds="<<Ds<<"\n\n";
	   getch();
	   clrscr();
	   break;
case 3:
cout<<"Table of ultrasonic attenuation:-""\n\n";
cout<<"Compound name="<<comp<<"\n\n";

cout<<"----------------------------------------------------------""\n";
cout<<"frequency""\t""alpha(th)""\t""alpha(L)""\t""alpha(s)" "\n";
cout<<"----------------------------------------------------------""\n";
for(j=0;j<m;j++)
	{
cout<<""<<f[j]<<"\t"<<""<<athw[j]<<"\t"""<<alw[j]<<"\t"""<<asw[j]<<"\n";
       }
cout<<"----------------------------------------------------------""\n";
	   getch();
	   clrscr();
	   break;

  case 4:
	   fstream fout;
	   fout.open("PRN",ios::out);
  fout<<"Compound name="<<comp<<"\n\n";
 fout<<"c11="<<c11<<"\n\n";
 fout<<"c12="<<c12<<"\n\n";
 fout<<"c13="<<c13<<"\n\n";
 fout<<"c33="<<c33<<"\n\n";
 fout<<"c44="<<c44<<"\n\n";
 fout<<"c66="<<c66<<"\n\n";
 fout<<"c111="<<c111<<"\n\n";
 fout<<"c112="<<c112<<"\n\n";
 fout<<"c113="<<c113<<"\n\n";
 fout<<"c123="<<c123<<"\n\n";
 fout<<"c133="<<c133<<"\n\n";
 fout<<"c144="<<c144<<"\n\n";
 fout<<"c155="<<c155<<"\n\n";
 fout<<"c222="<<c222<<"\n\n";
 fout<<"c333="<<c333<<"\n\n";
 fout<<"c344="<<c344<<"\n\n";
 fout<<"Table of velocity for hcp compound-""\n\n";
 fout<<"----------------------------------------------------------""\n";
 fout<<"theeta""\t\t""v1 " "\t\t"<<"v2 " "\t\t"<<"v3 " "\n";
 fout<<"----------------------------------------------------------""\n";
  for(i=0;i<11;i++)
	{
 fout<<""<<tth[i]<<"\t"<<""<<v1[i]<<"\t"<<""<<v2[i]<<"\t"<<""<<v3[i]<<"\n";
       }
 fout<<"----------------------------------------------------------""\n";
 fout<<"Value of relaxation time="<<to<<"\n\n";
 fout<<"Value of long.relax.time="<<tl<<"\n\n";
 fout<<"Value of shearrelax.time="<<ts<<"\n\n";
 fout<<"Value of Gruneisen contants are as follow:-""\n";
 fout<<"Along Z-axis for lonitudinal wave""\n";
 fout<<"Average of Gamma="<<xav1<<"\n\n";
 fout<<"Average of square Gamma="<<x<<"\n\n";
 fout<<"Square of average Gamma="<<xav<<"\n\n";
 fout<<"DL="<<Dl<<"\n\n";
 fout<<"Along Z-axis for shear wave""\n";
 fout<<"Average of Gamma="<<yav1<<"\n\n";
 fout<<"Average of square Gamma="<<y<<"\n\n";
 fout<<"Square of average Gamma="<<yav<<"\n\n";
 fout<<"Ds="<<Ds<<"\n\n";
 fout<<"Table of ultrasonic attenuation:-""\n\n";
fout<<"Compound name="<<comp<<"\n\n";
fout<<"----------------------------------------------------------""\n";
fout<<"frequency""\t""alpha(th)""\t""alpha(L)""\t""alpha(s)" "\n";
fout<<"----------------------------------------------------------""\n";
for(j=0;j<m;j++)
	{
fout<<""<<f[j]<<"\t"""<<athw[j]<<"\t"""<<alw[j]<<"\t"""<<asw[j]<<"\n";
       }
fout<<"----------------------------------------------------------""\n";

 getch();
 clrscr();
 break;
 case 5:
	exit (1);
 default:
	cout<<" You have entered wrong choice, please correct it.";
	getch();
	clrscr();
	break;
	}
	}
	}
