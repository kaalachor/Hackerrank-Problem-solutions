#include <stdio.h>
int main()
{
int a[100][100],i,j,n,d1,d2,td;
scanf("%d",&n);
for(i=0;i<n;i++){
    for(j=0;j<n;j++){
        scanf("%d",&a[i][j]);
    }
}
d1=0;
d2=0;
for(i=0;i<n;i++){
    for(j=0;j<n;j++){
        if(i==j)
        d1+=a[i][j];
        if((i+j)==(n-1))
        d2+=a[i][j];
    }
}
td=(d1-d2);
td=abs(td);
printf("%d",td);
    return 0;
}
