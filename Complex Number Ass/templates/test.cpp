#include <iostream>
#include "Complex.cpp"
using namespace std;

typedef complex<double> dcmplx;
typedef complex<float>  fcmplx;

int main(){
  dcmplx a, b, sum;
  
  cout << "Enter Re(a) and Im(a)\n";
  cin >> a.re >> a.im;
  cout << "Enter Re(b) and Im(b)\n";
  cin >> b.re >> b.im;
  
  
  cout << "a + b: " << add(a, b) << "\n";
  cout << "a - b: " << subtract(a, b) << "\n";
  cout << "a * b: " << multiply(a, b) << "\n";
  cout << "a / b: " << divide(a, b) << "\n";
}
