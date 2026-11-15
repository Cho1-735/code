#include <stdio.h>
#include <math.h>
int main()
{
    double a,b,c,disc,x1,x2,p,q;
    scanf("%lf%lf%lf",&a,&b,&c);
    disc=b*b-4*a*c;
    p=-b/(2*a);
    q=sqrt(disc)/(2*a);
    x1=p+q;
    x2=p-q;
    printf("x1=%7.2lf\nx2=%7.2lf",x1,x2);
    return 0;
}
