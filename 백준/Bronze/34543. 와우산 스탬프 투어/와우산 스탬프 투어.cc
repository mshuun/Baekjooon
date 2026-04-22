#include <iostream>

using namespace std;

int main() {
    int n, w;
    cin >> n >> w;

    int visit[6] = {0, 10, 20, 50, 60, 120};
    int score = visit[n];
    if (w > 1000) {
        score -= 15;
    }
    if (score < 0) {
        score = 0;
    }
    cout << score;
}