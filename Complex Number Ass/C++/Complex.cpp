#include "Complex.h"
using namespace std;

Complex::Complex(double re, double im)
{
    real = re;
    imag = im;
}

Complex::Complex()
{
    real = 0;
    imag = 0;
}

// Print complex number
ostream& operator<<(ostream& out, const Complex& c)
{
    if ((c.imag > 0 && c.real > 0) || (c.imag > 0 && c.real < 0)) {
        out << "" << c.real << "+" << c.imag << "i";
    } else if (c.imag == 0) {
        out << c.real;
    } else if (c.real == 0) {
        out << c.imag << "i";
    } else {
        out << c.real << "" << c.imag << "i";
    }
    return out;
}

// Add complex numbers
Complex Complex::add(Complex a) {
		return *this + a;
}

Complex operator+(Complex a, const Complex& b)
{
    a.real += b.real;
    a.imag += b.imag;
    return a;
}

// Subtract complex numbers
Complex Complex::subtract(Complex a) {
		return *this - a;
}

Complex operator-(Complex a, const Complex& b)
{
    a.real -= b.real;
    a.imag -= b.imag;
    return a;
}

// multiply complex numbers
Complex Complex::multiply(Complex a) {
		return *this * a;
}
Complex operator*(Complex a, const Complex& b)
{
    double x, y;
    x = a.real * b.real - a.imag * b.imag;
    y = a.real * b.imag + a.imag * b.real;
    a.real = x;
    a.imag = y;
    return a;
}

// divide complex numbers
Complex Complex::divide(Complex a) {
		return *this / a;
}

Complex operator/(Complex a, const Complex& b)
{
    double x, y;
    x = (a.real * b.real + a.imag * b.imag) / (pow(b.real, 2) + pow(b.imag, 2));
    y = (a.imag * b.real - a.real * b.imag) / (pow(b.real, 2) + pow(b.imag, 2));
    a.real = x;
    a.imag = y;
    return a;
}

