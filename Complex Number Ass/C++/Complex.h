#ifndef COMPLEX__H__
#define COMPLEX__H__

#include <string>
#include <cmath>
#include <iostream>

class Complex {
	public:
		Complex();
		Complex(double re, double im);
		
		Complex add(Complex a);
		Complex subtract(Complex a);
		Complex multiply(Complex a);
		Complex divide(Complex a);
		
		friend Complex operator+(Complex a, const Complex &b);
		friend Complex operator-(Complex a, const Complex &b);
		friend Complex operator*(Complex a, const Complex &b);
		friend Complex operator/(Complex a, const Complex &b);
		friend std::ostream &operator<<(std::ostream &out, const Complex &c);
	
	private:
		double real;
		double imag;
};
#endif
