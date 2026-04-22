#include <stdio.h>
#include <math.h>

int cnt(int n) {
    int count = 0;
    int i = 2;
    while (i * i <= n) {
        if (n % i == 0) {
            while (n % i == 0) {
                n /= i;
                count += 1;
            }
        }
        i += 1;
    }
    if (n > 1) {
        count += 1;
    }
    return count;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", (int)ceil(log2(cnt(n))));
    return 0;
}
