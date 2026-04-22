#include <cmath>
#include <iostream>

using namespace std;

int main() {
    int n;
    double a = 1;
    cin >> n;
    for (int i = 0; i < n; i++) {
        a /= 2;
    }
    printf("%.*f", n, a);
}