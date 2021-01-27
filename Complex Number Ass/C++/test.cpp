#include "Complex.h"
#include <array>
using namespace std;


int main()
{
    std::array<Complex, 2> cx;
    double x, y;
    
    for (int i = 0; i < 2; i++) {
        cout << "Enter complex number " << i + 1 << endl;
        cout << "Real part" << endl;
        cin >> x;
        cout << "Imaginary part" << endl;
        cin >> y;
        cx[i] = Complex(x, y);
        cout << endl;
    }
    
    cout << "c1: " << cx[0] << endl;
    cout << "c2: " << cx[1] << endl << endl;
    
    cout << "c1 + c2: " << cx[0].add(cx[1]) << endl;
    cout << "c1 - c2: " << cx[0].subtract(cx[1]) << endl << endl;
    
    cout << "c1 / c2 : " << cx[0].divide(cx[1]) << endl;
    cout << "c1 * c2 : " << cx[0].multiply(cx[1]) << endl << endl;  
}

