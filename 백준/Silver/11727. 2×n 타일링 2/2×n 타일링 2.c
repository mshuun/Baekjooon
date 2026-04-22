#include <stdio.h>
#include <string.h>

int main() {
    int n = 0;
    scanf("%d", &n);
    int dp[n];
    dp[0] = 1;
    dp[1] = 3;
    dp[2] = 5;

    for (int i = 3; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2] * 2)%10007;
    } 
    printf("%d\n", dp[n-1]%10007);
    return 0;
}
