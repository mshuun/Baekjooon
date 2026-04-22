#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    if (1 <= N && N < 10) {
    }
    else if (N < 100) {
        N = 2 * (N - 9) + 9;
    }
    else if (N < 1000) {
        N = 3 * (N - 99) + 189;
    }
    else if (N < 10000) {
        N = 4 * (N - 999) + 2889;
    }
    else if (N < 100000) {
        N = 5 * (N - 9999) + 38889;
    }
    else if (N < 1000000) {
        N = 6 * (N - 99999) + 488889;
    }
    else if (N < 10000000) {
        N = 7 * (N - 999999) + 5888889;
    }
    else if (N < 100000000) {
        N = 8 * (N - 9999999) + 68888889;
    }
    else if (N == 100000000) {
        N = 788888898;
    }

    printf("%d\n", N);
    return 0;
}
