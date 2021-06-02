//This programe is to direction dependent velocity//
#include<process.h>
#include<iostream.h>
#include<conio.h>
#include<math.h>
#include<fstream.h>
void main()
{
	char comp[10];

	double c11,c12,c13,c33,c44,v1[15],v2[15],v3[15],th[15],
	       x[15],y[15],p[15],q[15],r[15],s[15],t[15],u[15],n=11;

	double tth[11]={0.0,5.0,15.0,25.0,35.0,45.0,55.0,65.0,75.0,85.0,90.0};

	//clrscr();

	cout<<"\n Enter the compound's name =";
	cin>>comp;
	cout<<"\n Enter the value of c11 =  ";
	cin>>c11;
	cout<<"\n Enter the value of c12 =  ";
	cin>>c12;
	cout<<"\n Enter the value of c13 =  ";
	cin>>c13;
	cout<<"\n Enter the value of c33 =  ";
	cin>>c33;
	cout<<"\n Enter the value of c44 =  ";
	cin>>c44;

	for(int i=0;i<n;i++)
	{
	th[i]=(tth[i]*22)/(180*7);

	x[i]=sin(th[i]);

	y[i]=cos(th[i]);

	p[i]=pow(x[i],2.0);

	q[i]=pow(y[i],2.0);

	r[i]=c11*p[i]-c33*q[i]+c44*(q[i]-p[i]);

	s[i]=pow(r[i],2);

	t[i]=4.0*p[i]*q[i]*pow( (c13+c44), 2);

	u[i]=pow( (s[i]+t[i]),0.5);

	v1[i]=(c33*q[i]+c11*p[i]+c44+u[i])/2;

	v2[i]=(c33*q[i]+c11*p[i]+c44-u[i])/2;

	v3[i]=c44*q[i]+((c11-c12)/2.0)*p[i];

	}

	cout<<"Table of velocity for hcp compound-""\n";
	cout<<"Compound name="<<comp<<"\n";

 cout<<"----------------------------------------------------------""\n";
 cout<<"theeta""\t\t""v1 " "\t\t"<<"v2 " "\t\t"<<"v3 " "\n";
 cout<<"----------------------------------------------------------""\n";
  for(i=0;i<11;i++)
	{
 cout<<""<<tth[i]<<"\t"<<""<<v1[i]<<"\t"<<""<<v2[i]<<"\t"<<""<<v3[i]<<"\n";
       }
  cout<<"----------------------------------------------------------""\n";
  getch();
	  }
