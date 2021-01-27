#include <stdio.h>
#include <string.h>
#include <cmath>

struct complex
{
   int real, img;
};

void printComplex(complex c);
void sum(complex a, complex b);
void subtract(complex a, complex b);
void divide(complex a, complex b);
void multiply(complex a, complex b);

int main()
{
   struct complex a, b, c;

   printf("Enter a and b where a + bi is the first complex number: C1.\n");
   scanf("%d%d", &a.real, &a.img);
   printf("Enter c and d where c + di is the second complex number: C2.\n");
   scanf("%d%d", &b.real, &b.img);

	 printf("\n");
	 
	 printf("C1: "); printComplex(a);	 
	 printf("C2: "); printComplex(b);
	 
	 printf("\n");
	 
   sum(a, b);
   subtract(a, b);
   divide(a, b);
   multiply(a, b);
   
   return 0;
}

void multiply(complex a, complex b) {
	 struct complex c;
		
   c.real = a.real * b.real - a.img * b.img;
   c.img = a.real * b.img + a.img * b.real;
    
   printf("C1 * C2: ");
   printComplex(c);
}

void divide(complex a, complex b) {
	 struct complex c;
    
   c.real = (a.real * b.real + a.img * b.img) / (pow(b.real, 2) + pow(b.img, 2));
   c.img = (a.img * b.real - a.real * b.img) / (pow(b.real, 2) + pow(b.img, 2));
    
   printf("C1 / C2: ");
   printComplex(c);
}

void subtract(complex a, complex b) {
	 struct complex c;
	 
	 c.real = a.real - b.real;
   c.img = a.img - b.img;

   printf("C1 - C2: ");
   printComplex(c);
}

void sum(complex a, complex b) {
	 struct complex c;
	 
	 c.real = a.real + b.real;
   c.img = a.img + b.img;

   printf("C1 + C2: ");
   printComplex(c);
}

void printComplex(complex c) {
		if ((c.img > 0 && c.real > 0) || (c.img > 0 && c.real < 0)) {
        printf("%d + %di\n", c.real, c.img);
    } else if (c.img == 0) {
        printf("%d\n", c.real);
    } else if (c.real == 0) {
        printf("%di\n", c.img);
    } else {
        printf("%d %di\n", c.real, c.img);
    }
}
