//This is program to calculate direction dependent velocity,relx.time in
//HCP compound using c33 elastic constant data.
#include<stdio.h>
#include<process.h>
#include<iostream.h>
#include<conio.h>
#include<math.h>
#include<fstream.h>
#include<fstream.h>
void main()
{
 //a,a0 is basal plane distance.    p is c/a value for hcp materials.
  //k2 is contants calculated by C33.
 //k3 is contants calculated by k2,a,m,n.
	char comp[10];
	double a,a0,p,va,C33[15],C33A[15],k2[15],k3[15],m=1.0,n=2.0;
	double c11[15],c12[15],c13[15],c33[15],c44[15],c66[15],
		c111[15],c112[15],c113[15],c123[15],c133[15],c344[15],
		c144[15],c155[15],c222[15],c333[15],T[15];
	int i=0,j;
	//Vriables to calculate velocity.

double th[15],xx[15],yy[15],p1[15],q[15],r[15][15],s[15][15],t[15][15],
	u[15][15],v11[15][15],v22[15][15],v33[15][15],v1[15][15],v2[15][15],
	v3[15][15];
double tth[11]={0.0,5.0,15.0,25.0,35.0,45.0,55.0,65.0,75.0,85.0,90.0};
int    ii=0;
double  dd[15],Cv[15],Cva[15],Cvb[15],Eo[15],Eoa[15],Eob[15],ko[15],
	koa[15],kob[15],V[15][15],to[15][15];

	clrscr();
	clrscr();
	cout<<"\n Enter the compound's name =";
	cin>>comp;
	cout<<"\n Enter the value of a(basel plane distance) =  ";
	cin>>a>>a0;
	cout<<"\n Enter the value of  c/a =  ";
	cin>>p;
	cout<<"\n Enter the number of c33 data=  ";
	cin>>j;
	for(i=0;i<j;i++)
	{
	cout<<"\n Enter the value of C33 =  ";
	cin>>C33[i]>>C33A[i];
	}
		for(i=0;i<j;i++)
	{
	cout<<"\n Enter the temperature value  =  ";
	cin>>T[i];
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
	a=a*pow(10,a0);
	va=1.732*pow(a,3.0)*p/2.0;
      for(i=0;i<j;i++)
 {
 C33[i]=C33[i]*pow(10,C33A[i]);
 k2[i]=(C33[i]*va)/(pow(a,4.0)*pow(p,4.0)*3.0);
 k3[i]=-(k2[i]*(m+n+6.0))/(6.0*pow(a,2.0));
 c11[i]=(167.0*pow(a,4.0)*k2[i])/(8.0*va);
 c12[i]=(41.0*pow(a,4.0)*k2[i])/(8.0*va);
 c13[i]=(5.0*pow(a,4.0)*pow(p,2.0)*k2[i])/(3.0*va);
 c33[i]=(3.0*pow(a,4.0)*pow(p,4.0)*k2[i])/(va);
 c44[i]=(2.0*pow(a,4.0)*pow(p,2.0)*k2[i])/(va);
 c66[i]=(63.0*pow(a,4.0)*k2[i])/(8.0*va);
 c111[i]=((1099.0*pow(a,6.0)*k3[i])/(10.0*va))+((23.0*pow(a,4.0)*k2[i])/(3.0*va));
 c112[i]=((83.0*pow(a,6.0)*k3[i])/(5.0*va))-((7.0*pow(a,4.0)*k2[i])/(5.0*va));
 c113[i]=((5.0*pow(a,6.0)*pow(p,2.0)*k3[i])/(3.0*va))+
	((pow(a,4.0)*pow(p,2.0)*k2[i])/(va));
 c123[i]=((7.0*pow(a,6.0)*pow(p,2.0)*k3[i])/
	(5.0*va))-((pow(a,4.0)*pow(p,2.0)*k2[i])/(va));
 c133[i]=(16.0*pow(a,6.0)*pow(p,4.0)*k3[i])/(5.0*va);
 c344[i]=(3.0*pow(a,6.0)*pow(p,4.0)*k3[i])/(va);
 c144[i]=(2.0*pow(a,6.0)*pow(p,2.0)*k3[i])/(va);
 c155[i]=(4.0*pow(a,6.0)*pow(p,2.0)*k3[i])/(3.0*va);
 c222[i]=((175.0*pow(a,6.0)*k3[i])/(2.0*va))+((39.0*pow(a,4.0)*k2[i])/(5.0*va));
 c333[i]=(9.0*pow(a,6.0)*pow(p,6.0)*k3[i])/(2.0*va);
  Cv[i]=Cva[i]*pow(10,Cvb[i]);
   Eo[i]=Eoa[i]*pow(10,Eob[i]);
   ko[i]=koa[i]*pow(10,kob[i]);
  }

//This is formulation for velocity at different theeta.

for( ii=0;ii<11;ii++)
	{
	th[ii]=(tth[ii]*22)/(180*7);

	xx[ii]=sin(th[ii]);

	yy[ii]=cos(th[ii]);

	p1[ii]=pow(xx[ii],2.0);

	q[ii]=pow(yy[ii],2.0);
	 }
for(i=0;i<j;i++)
      {
	 for(int ii=0;ii<11;ii++)
		{
		r[i][ii]=c11[i]*p1[ii]-c33[i]*q[ii]+c44[i]*(q[ii]-p1[ii]);

		s[i][ii]=pow(r[i][ii],2);

		t[i][ii]=4.0*p1[ii]*q[ii]*pow( (c13[i]+c44[i]), 2);

		u[i][ii]=pow( (s[i][ii]+t[i][ii]),0.5);

		v11[i][ii]=(c33[i]*q[ii]+c11[i]*p1[ii]+c44[i]+u[i][ii])/2;
		v1[i][ii]=sqrt(v11[i][ii]/dd[i]);

		v22[i][ii]=(c33[i]*q[ii]+c11[i]*p1[ii]+c44[i]-u[i][ii])/2;
		v2[i][ii]=sqrt(v22[i][ii]/dd[i]);

		v33[i][ii]=c44[i]*q[ii]+((c11[i]-c12[i])/2.0)*p1[ii];
		v3[i][ii]=sqrt(v33[i][ii]/dd[i]);
V[i][ii]=pow(3,0.333)*pow((1/pow(v1[i][ii],3)+1/pow(v3[i][ii],3)+
	      1/pow(v2[i][ii],3)),-0.333);
to[i][ii]=3*ko[i]/(Cv[i]*V[i][ii]*V[i][ii]);
	 }
	}

 clrscr();
 int J;
 while(1)
{
cout<<" Enter 1 to see velocity""\n";
cout<<" Enter 2 to see debye avg.velocity and relx.time using V1&V3 ""\n";
cout<<" Enter 3 to Print all data""\n";
cout<<" Enter 4 for EXIT""\n";
cout<<" What is your choice=";
cin>>J;
 clrscr();
 switch(J)
 {
 case 1:
 for(i=0;i<j;i++)
 {
 cout<<"Table of velocity for hcp compound-""\n\n";
 cout<<"Compound name="<<comp<<"\n\n";
 cout<<"temperature="<<T[i]<<"\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"theeta""\t\t""v1 " "\t\t"<<"v2 " "\t\t"<<"v3 " "\n";
 cout<<"----------------------------------------------------------""\n";
  for(ii=0;ii<11;ii++)
	{
 cout<<""<<tth[ii]<<"\t"<<v1[i][ii]<<"\t"<<v2[i][ii]<<"\t"<<v3[i][ii]<<"\n";
       }
  cout<<"----------------------------------------------------------""\n";
	   getch();
	   clrscr();
	   }
	    getch();
	   clrscr();
	   break;
  case 2:
 for(i=0;i<j;i++)
 {
 cout<<"Table of debye velocity and relax.time using V1&V3-""\n\n";
 cout<<"Compound name="<<comp<<"\n\n";
 cout<<"temperature="<<T[i]<<"\n";
 cout<<"----------------------------------------------------------""\n";
 cout<<"theeta""\t\t""V""\t\t""RELAX.TIME""\n";
 cout<<"----------------------------------------------------------""\n";
  for(ii=0;ii<11;ii++)
	{
 cout<<""<<tth[ii]<<"\t\t"<<V[i][ii]<<"\t"<<""<<to[i][ii]<<"\n";
       }
  cout<<"----------------------------------------------------------""\n";

	   getch();
	   clrscr();
	   }
	    getch();
	   clrscr();
	   break;
 case 3:
	   fstream fout;
	   fout.open("PRN",ios::out);
   for(i=0;i<j;i++)
	{
  fout<<"Table of velocity for hcp compound-""\n\n";
  fout<<"Compound name="<<comp<<"\n\n";
  fout<<"temperature="<<T[i]<<"\n";
 fout<<"----------------------------------------------------------""\n";
 fout<<"theeta""\t\t""v1 " "\t\t"<<"v2 " "\t\t"<<"v3 " "\n";
 fout<<"----------------------------------------------------------""\n";
  for(ii=0;ii<11;ii++)
	{
 fout<<""<<tth[ii]<<"\t"<<v1[i][ii]<<"\t"<<v2[i][ii]<<"\t"<<v3[i][ii]<<"\n";
       }
 fout<<"----------------------------------------------------------""\n";
	}
 for(i=0;i<j;i++)
	{
 fout<<"Table of debye velocity and relax.time using V1&V3-""\n\n";
 fout<<"Compound name="<<comp<<"\n\n";
 fout<<"temperature="<<T[i]<<"\n";
 fout<<"----------------------------------------------------------""\n";
 fout<<"theeta""\t\t""V""\t\t""RELAX.TIME""\n";
 fout<<"----------------------------------------------------------""\n";
  for(ii=0;ii<11;ii++)
	{
 fout<<""<<tth[ii]<<"\t\t"<<V[i][ii]<<"\t"<<to[i][ii]<<"\n";
       }
 fout<<"----------------------------------------------------------""\n";
 }
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










