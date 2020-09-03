#include <stdio.h>
#include <math.h>
int main()
{
long long int a[5],i,min,max,mins,maxs,sum;
for(i=0;i<5;i++){
    scanf("%lld",&a[i]);
}
min=a[0];

for(i=0;i<5;i++){
    if(a[i]<min)
    min=a[i];
    
}
max=a[0];
for(i=0;i<5;i++){
    if(a[i]>max)
    max=a[i];
}
sum=0;
for(i=0;i<5;i++){
    sum+=a[i];
}
maxs=sum-min;
mins=sum-max;
printf("%lld %lld",mins,maxs);
    return 0;
}
