#include <stdio.h>

double func1(double p1, int p2)
{
    int v1 = 0;
    double v2 = 1;
    if (0 <= p2) {
        while (v1 < p2) {
            v2 = v2 * p1;
            v1 = v1 - 1;
        }
    } else if (p2 < 0) {
        while (p2 < v1) {
            v2 = v2 / p1;
            v1 = v1 - 1;
        }
    }
    return v2;
}

int main(void){
double p1;
int p2;
p1=1.1; p2=2;
printf("%f^%d = %f\n", p1, p2, func1(p1, p2));
p1=1.1; p2=1;
printf("%f^%d = %f\n", p1, p2, func1(p1, p2));
p1=1.1; p2=0;
printf("%f^%d = %f\n", p1, p2, func1(p1, p2));
p1=1.1; p2=-1;
printf("%f^%d = %f\n", p1, p2, func1(p1, p2));
p1=1.1; p2=-2;
printf("%f^%d = %f\n", p1, p2, func1(p1, p2));
return 0;
}
