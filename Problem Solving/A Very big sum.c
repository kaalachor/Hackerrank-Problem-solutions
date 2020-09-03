#include <stdio.h>
#include<math.h>
int main()
{
long long int a[10],sum;
int n,i;
scanf("%d",&n);
for(i=0;i<n;i++)
{
    scanf("%lld",&a[i]);
}
sum=0;
for(i=0;i<n;i++)
{
    sum += a[i];
}
printf("%lld",sum);
return 0;
}
