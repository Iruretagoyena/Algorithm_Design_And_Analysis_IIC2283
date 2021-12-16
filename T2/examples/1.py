/*#include<stdio.h>
#include<iostream>
#include<math.h>
using namespace std;
struct complex
{
	double r,i;
	complex(double R=0.0,double I=0.0) { r=R,i=I;}
};
complex operator +(complex a,complex b) { return complex(a.r+b.r,a.i+b.i);}
complex operator -(complex a,complex b) { return complex(a.r-b.r,a.i-b.i);}
complex operator *(complex a,complex b) { return complex(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r);}
const int N=600000;
const double pi=acos(-1);
complex a[N],b[N];
char s[N],t[N];
int p[N];
int n,m,k;
void fft(complex *a,int n,int x)
{
	for (int i=1,j=n/2;i<n-1;i++)
	{
		if (i<j) swap(a[i],a[j]);
		int p=n/2;
		while (j>=p) j-=p,p/=2;
		j+=p;
	}
	for (int j=2;j<=n;j*=2)
	{
		complex wn(cos(2*pi/j*x),sin(2*pi/j*x));
		for (int i=0;i<n;i+=j)
		{
			complex w(1,0);
			for (int k=i;k<i+j/2;k++)
			{
				complex u=a[k],t=a[k+j/2]*w;
				a[k]=u+t;a[k+j/2]=u-t;
				w=w*wn;
			}
		}
	}
	if (x==-1)
	for (int i=0;i<n;i++) a[i].r/=n;
}
void work(char ch)
{
	int cnt=0;
	int nn=1;
	while (nn<=n+m) nn*=2;
	for (int i=0;i<nn;i++) a[i].r=a[i].i=b[i].r=b[i].i=0;
	for (int i=1;i<=k&&i<=n;i++) cnt+=s[i]==ch;
	for (int i=1;i<=n;i++)
	{
		if (i+k<=n) cnt+=s[i+k]==ch;
		if (cnt) a[i].r=1;
		if (i>k) cnt-=s[i-k]==ch;
	}
	for (int i=1;i<=m;i++) b[i].r=t[m+1-i]==ch;
	fft(a,nn,1);fft(b,nn,1);
	for (int i=0;i<nn;i++) a[i]=a[i]*b[i];
	fft(a,nn,-1);
	for (int i=0;i<nn;i++) p[i]+=(int)(a[i].r+0.5);
}
int main()
{
    //freopen("input.txt", "r", stdin);
   // freopen("output.txt", "w", stdout);
	return 0;
} */
#include<stdio.h>
#include<iostream>
#include<math.h>
using namespace std;
struct complex
{
	double r,i;
	complex(double R=0.0,double I=0.0) { r=R,i=I;}
};
complex operator +(complex a,complex b) { return complex(a.r+b.r,a.i+b.i);}
complex operator -(complex a,complex b) { return complex(a.r-b.r,a.i-b.i);}
complex operator *(complex a,complex b) { return complex(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r);}
const int N=600000;
const double pi=acos(-1);
complex a[N],b[N];
char s[N],t[N];
int res[N],n,m,k;
void reverseBIT(complex *a,int n)
{
    for (int i=1,j=n/2;i<n-1;i++)
	{
		if (i<j) swap(a[i],a[j]);
		int p=n/2;
		while (j>=p) j-=p,p/=2;
		j+=p;
	}
}
void fft(complex *a,int n,int x)
{
    reverseBIT(a,n);
	for (int j=2;j<=n;j*=2)
	{
		complex wn(cos(2*pi/j*x),sin(2*pi/j*x));
		for (int i=0;i<n;i+=j)
		{
			complex w(1,0);
			for (int k=i;k<i+j/2;k++)
			{
				complex u=a[k],t=a[k+j/2]*w;
				a[k]=u+t;a[k+j/2]=u-t;
				w=w*wn;
			}
		}
	}
	if (x==-1)
	for (int i=0;i<n;i++) a[i].r/=n;
}
void setStringtobinary(char ch)
{   int cnt=0 ;
    for (int i=1;i<=k;i++) cnt+=s[i]==ch;
	for (int i=1;i<=n;i++)
	{
		if (i+k<=n) cnt+=s[i+k]==ch;
		if (cnt) a[i].r=1;
		if (i>k) cnt-=s[i-k]==ch;
	}
	for (int i=1;i<=m;i++) b[i].r=t[m+1-i]==ch;
}
void multiplePoly(char ch)
{
	int nn=1;
	while (nn<=n+m) nn*=2;
	for (int i=0;i<nn;i++) a[i].r=a[i].i=b[i].r=b[i].i=0;
    setStringtobinary(ch);
	fft(a,nn,1);fft(b,nn,1);
	for (int i=0;i<nn;i++) a[i]=a[i]*b[i];
	fft(a,nn,-1);
	for (int i=0;i<nn;i++) res[i]+=(int)(a[i].r+0.1);
}
void input()
{
   // freopen("input.txt", "r", stdin);
    scanf("%d%d%d",&n,&m,&k);
    scanf("%s",s+1);scanf("%s",t+1);
}
void solve()
{  // freopen()
	multiplePoly('A');multiplePoly('C');
	multiplePoly('G');multiplePoly('T');
	long long ans=0;
	for (int i=m+1;i<=n+1;i++)
	if (res[i]==m) ans+=1;
	//printf("Chuoi S : %s\n",s+1);
	//printf("Chuoi T : %s\n",t+1);
	//printf("n=%d,m=%d,K =%d\n",n,m,k);
	//cout << "So lan xuat hien chuoi T trong chuoi S la :";
	cout<<ans<<endl;
}
int main()
{
   /* cout << "+------------------------------------------------------------------------------------------------------------------+" << endl;
    cout << "|                                                     DO LAP TRINH TINH TOAN                                       |" << endl;
    cout << "|                             TIM CHUOI DNA VOI PHUONG PHAP MO (FUZZY) SU DUNG BIEN DOI FOURIER NHANH (FFT)        |" << endl;
    cout << "+------------------------------------------------------------------------------------------------------------------+" << endl;
    cout << "|                                                                                                                  |" << endl;
    cout << "|       THANH VIEN NHOM : NGUYEN MINH QUANG                                                                        |" << endl;
    cout << "|                         HO BA THANH                                                                              |" << endl ;
    cout << "|       LOP       : 19TCLC_NHAT1                                                                                   |" << endl;
    cout << "|       GIAO VIEN HUONG DAN     : PHAM MINH TUAN                                                                   |" << endl;
    cout << "|                                                                                                                  |" << endl;
    cout << "+------------------------------------------------------------------------------------------------------------------+" << endl;*/
    input();
    solve();

}
 