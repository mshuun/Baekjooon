#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    int left = 0;
    int right = n - 1;
    int ans = abs(arr[left] + arr[right]);
    int a = arr[left];
    int b = arr[right];

    while (left < right) {
        int now = arr[left] + arr[right];
        if (abs(now) <= ans) {
            a = arr[left];
            b = arr[right];
            ans = abs(now);
        }
        if (now < 0) {
            left++;
        }
        else {
            right--;
        }
    }

    printf("%d %d\n", a, b);
    return 0;
}
