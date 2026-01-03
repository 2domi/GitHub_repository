// 숫자 2개 받아서 더 큰거 출력
#include <iostream>
#include <random>
using namespace std;

int main()
{
    int num1; int num2;
    
    cout << "num1 : "; cin >> num1;
    cout << "num2 : "; cin >> num2;

    if (num1 > num2) { // num1이 num2보다 크다면
        cout << "num1(" << num1 << ") is bigger than num2(" << num2 << ")." << endl;
    }
    else if (num1 < num2) { // num2이 num1보다 크다면
        cout << "num2(" << num2 << ") is bigger than num1(" << num1 << ")." << endl;
    }
    else {
        cout << "num1(" << num1 << ") and num2(" << num2 << ") is same.";
    }
    return 0;
}