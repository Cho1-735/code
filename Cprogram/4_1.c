#include<stdio.h>
#include<math.h>
int main()
{
    double a,b,c,disc,x1,x2,q,p;
    scanf("%lf%lf%lf",&a,&b,&c);
    disc=b*b-4*a*c;
    if(disc<0)
    {
        printf("This equation has no real roots.");
        return 0;      
    }
    else
    {
        p=-b/(2*a);
        q=sqrt(disc)/(2*a);
        x1=p+q;
        x2=p-q;
        printf("real roots:\nx1=%.2lf\nx2=%.2lf",x1,x2);
    }
    return 0;
}