// 변수
#include <iostream>
using namespace std;

int main()
{
    int i;
    i = 2222;
    cout << "integar : " << i << endl; // 화면에 출력하는 객체에(cout) i를 넣어서 출력, endl = "\n"

    string s {"2domi"};
    cout << "string : " << s << endl;

    bool boolean {(1000 == 10000)};
    cout << "boolean : " << boolean << endl;

    const double pi = 3.1415926535897932384626433832795028841971693993751058209749445923;
    cout << "const, double, pi : " << pi << endl; // cout에서 기본 소수점 5자리까지밖에 없어서 5자리까지만 출력됨(나중에 배움)

    return 0; // 프로그램이 종료됨을 알림
}

/*
1. 정수형 : short(2byte), int(4byte), long(4byte), long long(8byte)
2. 문자형(열) : char(1byte), string(unlimited, 성능에 따라 다름)
3. 불린형 : bool(1byte, [true,false])
4. 부동소수점형 : float(4byte), double(8byte), long double(8byte)
5. 기호 상수(변경되지 않음) : const [자료형] [이름]
*/