#include <iostream>
#include <string>
using namespace std;

int main()
{
    // 비밀 코드 맞추기
    string secret_code {'h'};
    string code;
    cout << "input secret code : " ; cin >> code;
    if (code > secret_code) {
        cout << "Secret Code is back to " << code << endl;
    }
    else if (code < secret_code) {
        cout << "Secret Code is in front of " << code << endl;
    }
    else {
        cout << "Secret Code is " << code << endl;
    }

    cout << "==================================================" << endl;

    // 세 개의 정수 중에서 큰 수 찾기
    int num1, num2, num3, largest;

    cout << "num1 : "; cin >> num1;
    cout << "num2 : "; cin >> num2;
    cout << "num3 : "; cin >> num3;

    if (num1 > num2 && num2 > num3) {
        largest = num1;
    }
    
    else if (num2 > num1 && num2 > num3) {
        largest = num2;
    }
    else {
        largest = num3;
    }   
    cout << largest << " is the Largest of 3";

    return 0;
}