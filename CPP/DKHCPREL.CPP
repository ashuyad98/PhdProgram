//This is program to calculate direction dependent velocity,relx.time in
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
double  dd,V[15],Cv,Cva,Cvb,Eo,Eoa,Eob,ko,koa,kob,to[15];

	clrscr();
	cout<<"\n Enter the compound's name =";
	cin>>comp;
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
cout<<"\n enter the value of c144=";  cin>>c144>>c144a;
cout<<"\n enter the value of c155=";  cin>>c155>>c155a;
	cout<<"\n enter the value of c222=";  cin>>c222>>c222a;
	cout<<"\n enter the value of c333=";  cin>>c333>>c333a;
	cout<<"\n enter the value of c344=";  cin>>c344>>c344a;
cout<<"\n enter the value of dd=";  cin>>dd;
cout<<"\n enter the value of Cv=";  cin>>Cva>>Cvb;
cout<<"\n enter the value of Eo=";  cin>>Eoa>>Eob;
cout<<"\n enter the value of K=";   cin>>koa>>kob;

	       Cv=Cva*pow(10,Cvb);
		Eo=Eoa*pow(10,Eob);
		ko=koa*pow(10,kob);
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
	V[i]=pow(3,0.333)*pow((1/pow(v1[i],3)+1/pow(v3[i],3)+
		1/pow(v2[i],3)),-0.333);
	to[i]=3*ko/(Cv*V[i]*V[i]);
	}

 clrscr();
 int J;
 while(1)
{
cout<<" Enter 1 to see velocity""\n";
cout<<" Enter 2 to see debye avg.velocity and relx.time using V1,V2&V3 ""\n";
cout<<" Enter 3 to Print all data""\n";
cout<<" Enter 4 for EXIT""\n";
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
  cout<<"Table of debye velocity and relax.time using V1,V2&V3-""\n\n";
 cout<<"Compound name="<<comp<<"\n\n";

 cout<<"----------------------------------------------------------""\n";
 cout<<"theeta""\t\t""V""\t\t""RELAX.TIME""\n";
 cout<<"----------------------------------------------------------""\n";
  for(i=0;i<11;i++)
	{
 cout<<""<<tth[i]<<"\t\t"<<V[i]<<"\t"<<""<<to[i]<<"\n";
       }
  cout<<"----------------------------------------------------------""\n";

	   getch();
	   clrscr();
	   break;

  case 3:
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
 fout<<"Cv="<<Cv<<"\n\n";
 fout<<"Eo="<<Eo<<"\n\n";
 fout<<"K="<<ko<<"\n\n";
 fout<<"density="<<dd<<"\n\n";
 fout<<"Table of velocity for hcp compound-""\n\n";
 fout<<"----------------------------------------------------------""\n";
 fout<<"theeta""\t\t""v1 " "\t\t"<<"v2 " "\t\t"<<"v3 " "\n";
 fout<<"----------------------------------------------------------""\n";
  for(i=0;i<11;i++)
	{
 fout<<""<<tth[i]<<"\t"<<""<<v1[i]<<"\t"<<""<<v2[i]<<"\t"<<""<<v3[i]<<"\n";
       }
 fout<<"----------------------------------------------------------""\n";
 fout<<"Table of debye velocity and relax.time using V1,V2&V3-""\n\n";
 fout<<"Compound name="<<comp<<"\n\n";
 fout<<"----------------------------------------------------------""\n";
 fout<<"theeta""\t\t""V""\t\t""RELAX.TIME""\n";
 fout<<"----------------------------------------------------------""\n";
  for(i=0;i<11;i++)
	{
 fout<<""<<tth[i]<<"\t\t"<<V[i]<<"\t"<<""<<to[i]<<"\n";
       }
 fout<<"----------------------------------------------------------""\n";

 getch();
 clrscr();
 break;
 case 4:
	exit (1);
 default:
	cout<<" You have entered wrong choice, please correct it.";
	getch();
	clrscr();
	break;
	}
	}
	}





