/This programe is to calculate lenard jones potential constants//
#include<process.h>
#include<iostream.h>
#include<conio.h>
#include<math.h>
#include<fstream.h>
void main()
{
       /*	char comp[10];
	double a,a0,n,q,si,ap,apn;
	clrscr();
	cout<<"\n Enter the compound's name =";
	cin>>comp;
	cout<<"\n Enter the value of a(basel plane distance) =  ";
	cin>>a>>a0;
	cout<<"\n The number of electrons giving charge on atom =  ";
	cin>>n;
	a=a*pow(10,a0);
	si=a/1.092;
	q=n*4.8*pow(10,-10);
	ap=1.17795*pow(10,-3)*pow(q,2.0)/a;				          //(6.0*1.74*0.9*pow(q,2.0))/(2.15*4.0*12.0*a);
	apn=0.09*pow(q,2.0)/a;
	cout<<"Lenard Jones potential constants are as follows-""\n";
	cout<<"Compound name="<<comp<<"\n";
	cout<<"Sigma="<<si<<"\n";
	cout<<"apsilan (energy constant value)="<<ap<<"\n";
	cout<<"apsilan(new)="<<apn<<"\n";     */
		char comp[10];
	double a,a0,b,b0,b12,si,ap,apn,p;
	clrscr();
	cout<<"\n Enter the compound's name =";
	cin>>comp;
	cout<<"\n Enter the value of a(basel plane distance) =  ";
	cin>>a>>a0;
	cout<<"\n Enter the value of c/a =  ";
	cin>>p;
	cout<<"\n The bulk modulous =  ";
	cin>>b>>b0;
	a=a*pow(10,a0);
	si=a/1.092;
	b=b*pow(10,b0);
	ap=(b*p*pow(si,3.0))/(3.953*36.0);
	b12=4.0*ap*pow(si,12.0);
	cout<<"\n"" Lenard Jones potential constants are as follows-""\n\n";
	cout<<" Compound name="<<comp<<"\n\n";
	cout<<" Sigma="<<si<<"\n\n";
	cout<<" apsilan (energy constant value)="<<ap<<"\n\n";
	cout<<" b="<<b12<<"\n";
	  getch();
	  }
