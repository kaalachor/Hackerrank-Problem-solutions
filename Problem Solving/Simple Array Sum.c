#include <stdio.h>
#include<math.h>
int main()
{
int a[1000],i,n,sum;
scanf("%d",&n);
for(i=0;i<n;i++)
{
    scanf("%d",&a[i]);
}
sum=0;
for(i=0;i<n;i++)
{
    sum += a[i];
}
printf("%d",sum);

return 0;
}
