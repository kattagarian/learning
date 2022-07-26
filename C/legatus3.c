#include <stdio.h>

int main(){
    int g1=0, g2=0, g3=0;
    int Df1 = 0, Df2 = 0, Dft=0;
    scanf("%d",&g1);
    scanf("%d",&g2);
    scanf("%d",&g3);
    Df1 = g2-g1;
    Df2 = g3-g2;
    Dft = Df1 -Df2;
    
    if (g3<0){
        printf("esses dados nao valem");
        return 0;
    }
    if (Df2>Df1){
    printf(":)");
    
    }
    if (Df1 > Df2 && Dft > 0){
        printf(":(");
    }
    
    return 0;
}