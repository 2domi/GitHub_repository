#include <iostream>
using namespace std;

int main()
{
    double F_degree;
    double S_degree;

    cout << "Fahrenheit degree : "; cin >> F_degree;

    S_degree = (5.0/9.0) * (F_degree - 32);
    cout << "= Fahrenheit degree : " << S_degree;

    return 0;
}
