#include <iostream>
using namespace std;

int main()
{
    int money;
    int candy_price;

    cout << "How much money do you have : "; cin >> money;
    cout << "Candy's price : "; cin >> candy_price;

    cout << "Numbers of the candy you can buy :" << money / candy_price << endl;
    cout << "Money left : " << money % candy_price;

    return 0;
}