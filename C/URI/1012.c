#include<stdio.h>
int main()
{
 float a,b,c;
 scanf("%f %f %f",&a,&b,&c);
 printf("TRIANGULO: %.3f\nCIRCULO: %.3f\n",(a*c)/2,(3.14159*c*c));
 printf("TRAPEZIO: %.3f\nQUADRADO: %.3f\n",((a+b)/2)*c,b*b);
 printf("RETANGULO: %.3f\n",a*b);
 return 0;
}
