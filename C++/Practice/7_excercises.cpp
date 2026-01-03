#include <iostream>
#include <cmath> //수학 계산 라이브러리
#include <string>
#include <iomanip> //출력 포맷
using namespace std;

int main()
{   
    cout << "========================================================\n";

    // 주어 동사 목적어 합치기
    string S; string V; string O;

    cout << "Subject : " ; cin >> S;
    cout << "Verb : " ; cin >> V;
    cout << "Object : " ; cin >> O;

    cout << S << " " << V << " a(an) " << O << endl;
    cout << "========================================================\n";

    // 나이 + 10
    int age;
    cout << "age : "; cin >> age;
    cout << "age after 10 years : " << age + 10 << endl;
    cout << "========================================================\n";

    // 직각삼각형의 빗변 구하기 (a^2 + b^2 = C^2)
    double a; double b; double c;
    cout << "base : "; cin >> a;
    cout << "height : "; cin >> b;
    
    c = sqrt(a*a + b*b);
    cout << "hypotenuse : " << c << endl;
    cout << "========================================================\n";

    // 상자의 부피, 표면적
    double length; double weight; double height;
    cout << "length : "; cin >> length;
    cout << "weight : "; cin >> weight;
    cout << "height : "; cin >> height;

    cout << "volume : " << length * weight * height << endl;
    cout << "surface area : " << 2 * ((length * weight) + (weight * height) + (length * height)) << endl;

    // 평 -> m^2
    const float pyeong_unit {3.3058};
    double pyeong;

    cout << "Pyeong : "; cin >> pyeong;
    cout << "Square Meter : " << pyeong * pyeong_unit << endl;

    // 시간  단위 변환
    double hour; double minute; double second;

    cout << "hour : "; cin >> hour;
    cout << "minute : "; cin >> minute;
    cout << "second : "; cin >> second;

    cout << (hour * 3600 + minute * 60 + second) << endl;

    // 구의 겉넓이, 부피
    const double pi = 3.141592;
    double r;

    cout << "r : "; cin >> r;
    cout << "volume : " << (4.0/3.0) * pi * r * r * r << endl;
    cout << "surface : " << 4 * r * r * pi << endl;

    return 0;
}