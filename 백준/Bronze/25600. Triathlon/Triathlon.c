#include <stdio.h>
int main() {
    int scores[1000];
    int num;
    scanf("%d", &num);

    for (int i = 0; i < num; i++) {
        int a, d, g;
        scanf("%d %d %d", &a, &d, &g);

        if (a == d + g) {
            scores[i] = 2 * (a * (d + g));
        } else {
            scores[i] = a * (d + g);
        }
    }

    int maxScore = scores[0];
    for (int i = 1; i < num; i++) {
        if (scores[i] > maxScore) {
            maxScore = scores[i];
        }
    }

    printf("%d\n", maxScore);

    return 0;
}
