#include<stdio.h>
int main()
{
    char c1;
    scanf("%c",&c1);
    c1=(c1>'A' && c1<'z')?(c1+32):c1;
    printf("%c",c1);
    return 0;
}