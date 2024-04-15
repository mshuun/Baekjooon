#include <stdio.h>
#include <stdlib.h>

int main() {
    long long N, M, i, j;
    scanf("%lld", &N);
    long long *points = (long long *)malloc(N * 3 * sizeof(long long));
    for (i = 0; i < N * 3; i++) {
        scanf("%lld", &points[i]);
    }
    
    scanf("%lld", &M);
    long long *results = (long long *)malloc(M * sizeof(long long));
    long long xq, yq, zq, rq, radius_squared, count;
    for (i = 0; i < M; i++) {
        scanf("%lld %lld %lld %lld", &xq, &yq, &zq, &rq);
        radius_squared = rq * rq;
        count = 0;
        for (j = 0; j < N; j++) {
            long long dx = points[j * 3] - xq;
            long long dy = points[j * 3 + 1] - yq;
            long long dz = points[j * 3 + 2] - zq;
            if (dx * dx + dy * dy + dz * dz <= radius_squared) {
                count++;
            }
        }
        
        results[i] = count;
    }
    for (i = 0; i < M; i++) {
        printf("%lld\n", results[i]);
    }
    free(points);
    free(results);
    
    return 0;
}
