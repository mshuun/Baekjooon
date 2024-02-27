#include <iostream>
#include <string>

int main() {
    int N;
    std::cin >> N;

    for (int i = 0; i < N; ++i) {
        std::string K;
        std::cin >> K;

        if ((K.back() - '0') % 2 == 0) {
            std::cout << "even" << std::endl;
        } else {
            std::cout << "odd" << std::endl;
        }
    }

    return 0;
}
