/Programe for calculate soec and toec for hcp at room temperature.
#include<process.h>
#include<iostream.h>
#include<conio.h>
#include<math.h>
#include<fstream.h>
void main()
{
  //a,a0 is basal plane distance.    p is c/a value for hcp materials.
 // si is sigma and ap is appsilan. b is hcp constant.
 //b is calculated by si and ap.    M is mass of atom.(in formula cancelled)
 //et is eta (a constant) and calculated by n,m,b,M,a.
 //k2 is contants calculated by et,M,a.
 //k3 is contants calculated by k2,a,m,n.
	char comp[10];
	double a,a0,p,C33,C33A,k2,k3,m=6.0,n=7.0,B,cp;
	double c11,c12,c13,c33,c44,c66,c111,c112,c113,c123,c133,c344;
	double c144,c155,c222,c333;
	double e111,e112,e113,e123,e133,e344,e144,e155,e222,e333,cc,va;
	double e11,e12,e13,e33,e44,e66;
	double f111,f112,f113,f123,f133,f344,f144,f155,f222,f333;
	clrscr();
	cout<<"\n Enter the compound's name =";
	cin>>comp;
	cout<<"\n Enter the value of a(basel plane distance) =  ";
	cin>>a>>a0;
	cout<<"\n Enter the value of  c/a =  ";
	cin>>p;
	cout<<"\n Enter the value of C33 =  ";
	cin>>C33>>C33A;
	a=a*pow(10,a0);
	C33=C33*pow(10,C33A);
	cc=p*a;
	va=1.732*pow(a,2.0)*cc/2.0;
	k2=(C33*va)/(pow(a,4.0)*pow(p,4.0)*3.0);
	k3=-(k2*(m+n+6.0))/(6.0*pow(a,2.0));
	//B is constants calculated by a,p,k3.
	//cp is cprim constants calculated by k2,a,p.
	B=(pow(a,3.0)/pow(p,3.0))*k3;
	cp=(k2*a)/pow(p,5.0);
	//all elastic constants is calculated by B,cp,c.

 c11=24.1*pow(p,4.0)*cp;
 e11=(167.0*pow(a,4.0)*k2)/(8.0*va);
	c12=5.918*pow(p,4.0)*cp;
	e12=(41.0*pow(a,4.0)*k2)/(8.0*va);
 c13=1.925*pow(p,6.0)*cp;
 e13=(5.0*pow(a,4.0)*pow(p,2.0)*k2)/(3.0*va);
	c33=3.464*pow(p,8.0)*cp;
	e33=(3.0*pow(a,4.0)*pow(p,4.0)*k2)/(va);
 c44=2.309*pow(p,6.0)*cp;
 e44=(2.0*pow(a,4.0)*pow(p,2.0)*k2)/(va);
	c66=9.451*pow(p,4.0)*cp;
	e66=(63.0*pow(a,4.0)*k2)/(8.0*va);
 c111=(126.9*pow(p,2.0)*B+8.853*pow(p,4.0)*cp);
 e111=((1099.0*pow(a,6.0)*k3)/(10.0*va))+((23.0*pow(a,4.0)*k2)/(3.0*va));

	c112=19.168*pow(p,2.0)*B-1.61*pow(p,4.0)*cp;
	e112=((83.0*pow(a,6.0)*k3)/(5.0*va))-((7.0*pow(a,4.0)*k2)/(5.0*va));

 c113=(1.924*pow(p,4.0)*B+1.155*pow(p,6.0)*cp);
 e113=((5.0*pow(a,6.0)*pow(p,2.0)*k3)/(3.0*va))+((pow(a,4.0)*pow(p,2.0)*k2)/
	(va));

c123=1.617*pow(p,4.0)*B-1.155*pow(p,6.0)*cp;
e123=((7.0*pow(a,6.0)*pow(p,2.0)*k3)/(5.0*va))-((pow(a,4.0)*pow(p,2.0)*k2)/
	(va));

 c133=(3.695*pow(p,6.0)*B);
 e133=(16.0*pow(a,6.0)*pow(p,4.0)*k3)/(5.0*va);

	c344=(3.464*pow(p,6.0)*B);
	e344=(3.0*pow(a,6.0)*pow(p,4.0)*k3)/(va);

  c144=2.309*pow(p,4.0)*B;
  e144=(2.0*pow(a,6.0)*pow(p,2.0)*k3)/(va);

	c155=1.539*pow(p,4.0)*B;
	e155=(4.0*pow(a,6.0)*pow(p,2.0)*k3)/(3.0*va);

  c222=(101.039*pow(p,2.0)*B+9.007*pow(p,4.0)*cp);
  e222=((175.0*pow(a,6.0)*k3)/(2.0*va))+((39.0*pow(a,4.0)*k2)/(5.0*va));

	c333=(5.196*pow(p,8.0)*B);
	e333=(9.0*pow(a,6.0)*pow(p,6.0)*k3)/(2.0*va);


     clrscr();
  cout<<"This result is for HCP compound="<<comp<<"\n";
  cout<<"Basal planedistance(a)="<<a<<"\n";
  cout<<"value of c/a="<<p<<"\n";
   cout<<"value of K2="<<k2<<"\n";
  cout<<" This is table for second order elastic constant. ""\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"c11""\t\t""c12 " "\t\t"<<"c13 " "\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<""<<c11<<"\t"<<""<<c12<<"\t"<<""<<c13<<"\n";
 cout<<""<<e11<<"\t"<<""<<e12<<"\t"<<""<<e13<<"\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"c33""\t\t""c44 " "\t\t"<<"c66 " "\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<""<<c33<<"\t"<<""<<c44<<"\t"<<""<<c66<<"\n";
 cout<<""<<e33<<"\t"<<""<<e44<<"\t"<<""<<e66<<"\n";
  cout<<"----------------------------------------------------------""\n";
  getch();
 clrscr();
 cout<<" This is table for third order elastic constant. ""\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"c111""\t\t""c112 " "\t\t"<<"c113 " "\t\t"<<"C123 " "\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<""<<c111<<"\t"<<""<<c112<<"\t"<<""<<c113<<"\t"<<""<<c123<<"\n";
 cout<<""<<e111<<"\t"<<""<<e112<<"\t"<<""<<e113<<"\t"<<""<<e123<<"\n";
  cout<<"----------------------------------------------------------""\n";
 cout<<"c133""\t\t""c344 " "\t\t"<<"c144 " "\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<""<<c133<<"\t"<<""<<c344<<"\t"<<""<<c144<<"\n";
 cout<<""<<e133<<"\t"<<""<<e344<<"\t"<<""<<e144<<"\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"c155""\t\t""c222 " "\t\t"<<"c333 " "\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<""<<c155<<"\t"<<""<<c222<<"\t"<<""<<c333<<"\n";
 cout<<""<<e155<<"\t"<<""<<e222<<"\t"<<""<<e333<<"\n";
 cout<<"----------------------------------------------------------""\n";
 getch();
   }
