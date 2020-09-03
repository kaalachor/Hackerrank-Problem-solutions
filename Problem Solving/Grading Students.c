#include <stdio.h>
#include <math.h>
int main()
{
int a[100],n,i;
scanf("%d",&n);
for(i=0;i<n;i++){
    scanf("%d",&a[i]);
}
for(i=0;i<n;i++){
    if(a[i]>=38){
        if(a[i]%5==3)
        printf("%d\n",a[i]+2);
        else if(a[i]%5==4)
        printf("%d\n",a[i]+1);
        else
        printf("%d\n",a[i]);
    }
    else
    printf("%d\n",a[i]);
}
    return 0;
}
