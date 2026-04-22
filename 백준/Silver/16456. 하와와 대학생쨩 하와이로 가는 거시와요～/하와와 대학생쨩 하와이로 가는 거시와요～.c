#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int dp[1000000];
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;

    for (int i = 3; i < n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 3]) % 1000000009;
    }

    printf("%d\n", dp[n - 1] % 1000000009);
    return 0;
}
