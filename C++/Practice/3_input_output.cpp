// 자동 팁 계산기

#include <iostream>
using namespace std;

int main()
{
    int price;
    double tip_rate;

    cout << "Price : "; cin >> price;
    cout << "tip rate : "; cin >> tip_rate;

    auto tip = price * tip_rate;
    cout << tip << endl;

    return 0;
}