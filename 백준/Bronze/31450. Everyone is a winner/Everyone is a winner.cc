#include <iostream>

int main() {
    int num1, num2;

    std::cin >> num1 >> num2;
    
    if (num1 % num2 == 0) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }

    return 0;
}
