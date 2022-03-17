// math.cpp

#include <iostream>
#include "math.h"

int main()
{
    double a = 7.4;
    int b = 99;

    std::cout << "a + b = " <<
        math::Arithmetic::Add(a, b) << std::endl;
    std::cout << "a - b = " <<
        math::Arithmetic::Subtract(a, b) << std::endl;
    std::cout << "a * b = " <<
        math::Arithmetic::Multiply(a, b) << std::endl;
    std::cout << "a / b = " <<
        math::Arithmetic::Divide(a, b) << std::endl;

    return 0;
}
