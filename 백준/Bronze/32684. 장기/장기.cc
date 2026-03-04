#include <iostream>

using namespace std;

int main() {
    double scores[6] = {13, 7, 5, 3, 3, 2};

    double chuk_score = 0;
    double eun_score = 1.5;

    int count;

    for (int i = 0; i < 6; i++) {
        cin >> count;
        chuk_score += count * scores[i];
    }

    for (int i = 0; i < 6; i++) {
        cin >> count;
        eun_score += count * scores[i];
    }

    cout << (chuk_score > eun_score ? "cocjr0208" : "ekwoo") << endl;

    return 0;
}