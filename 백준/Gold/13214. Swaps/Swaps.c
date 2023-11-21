#include <stdio.h>
#include <stdlib.h>

int minSwaps(int *A, int *B, int N) {
    int pos[N+1], visited[N], i, j, ans = 0;

    // Create a mapping from elements to their positions in B
    for (i = 0; i < N; i++) {
        pos[B[i]] = i;
    }

    // Initialize visited array
    for (i = 0; i < N; i++) {
        visited[i] = 0;
    }

    // Find cycles and count swaps
    for (i = 0; i < N; i++) {
        if (visited[i] || pos[A[i]] == i)
            continue;

        int cycle_size = 0;
        j = i;

        while (!visited[j]) {
            visited[j] = 1;
            j = pos[A[j]];
            cycle_size++;
        }

        if (cycle_size > 0) {
            ans += (cycle_size - 1);
        }
    }

    return ans;
}

int main() {
    int N;
    scanf("%d", &N);

    int A[N], B[N], i;
    for (i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }

    for (i = 0; i < N; i++) {
        scanf("%d", &B[i]);
    }

    printf("%d\n", minSwaps(A, B, N));

    return 0;
}
