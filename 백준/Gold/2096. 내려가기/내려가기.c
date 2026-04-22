#include <stdio.h>
#include <stdlib.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int min(int a, int b) {
    return (a < b) ? a : b;
}

int main() {
    int n, i, j;
    scanf("%d", &n);
    
    int arr[n][3], maxdp[3], mindp[3];
    for(i = 0; i < n; i++) {
        for(j = 0; j < 3; j++) {
            scanf("%d", &arr[i][j]);
        }
    }
    
    for(i = 0; i < 3; i++) {
        maxdp[i] = arr[0][i];
        mindp[i] = arr[0][i];
    }
    
    for(i = 1; i < n; i++) {
        int tempMax[3], tempMin[3];
        
        tempMax[0] = arr[i][0] + max(maxdp[0], maxdp[1]);
        tempMax[1] = arr[i][1] + max(maxdp[0], max(maxdp[1], maxdp[2]));
        tempMax[2] = arr[i][2] + max(maxdp[1], maxdp[2]);
        
        tempMin[0] = arr[i][0] + min(mindp[0], mindp[1]);
        tempMin[1] = arr[i][1] + min(mindp[0], min(mindp[1], mindp[2]));
        tempMin[2] = arr[i][2] + min(mindp[1], mindp[2]);

        for(j = 0; j < 3; j++) {
            maxdp[j] = tempMax[j];
            mindp[j] = tempMin[j];
        }
    }
    
    int maxVal = maxdp[0], minVal = mindp[0];
    for(i = 1; i < 3; i++) {
        maxVal = max(maxVal, maxdp[i]);
        minVal = min(minVal, mindp[i]);
    }
    
    printf("%d %d\n", maxVal, minVal);
    
    return 0;
}
