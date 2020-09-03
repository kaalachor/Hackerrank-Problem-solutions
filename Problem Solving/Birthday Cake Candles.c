#include <stdio.h>

int main()
{
int a[100000],i,n,max,b;
scanf("%d",&n);
for(i=0;i<n;i++){
    scanf("%d",&a[i]);
}
max=a[0];
for(i=0;i<n;i++){
    if(max<a[i]){
        max=a[i];
    }
}
b=0;
for(i=0;i<n;i++){
    if((max) == (a[i])){
        b++;
    }
}
printf("%d\n",b);

return 0;
}
