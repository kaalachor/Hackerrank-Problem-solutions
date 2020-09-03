#include <stdio.h>
#include <math.h>
int main()
{
int a[100],n,i,x,y,z;
float p,q,r;

scanf("%d",&n);

for(i=0;i<n;i++){
    scanf("%d",&a[i]);
}
x=0;
y=0;
z=0;
for(i=0;i<n;i++){
    if(a[i]>0)
    x++;
    if(a[i]<0)
    y++;
    if(a[i]==0)
    z++;
}
p=(float)x/(float)n;
q=(float)y/(float)n;
r=(float)z/(float)n;
printf("%f\n%f\n%f",p,q,r);

    return 0;
}
