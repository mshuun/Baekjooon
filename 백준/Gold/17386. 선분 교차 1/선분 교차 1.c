#include <stdio.h>

long long ccw(int ax, int ay, int bx, int by, int cx, int cy) {
    long long result = (long long)ax * by + (long long)bx * cy + (long long)cx * ay - (long long)bx * ay - (long long)cx * by - (long long)ax * cy;
    if(result>0){
        return 1;
    }
    else{
        if(result<0){
            return -1;
        }
        else{
            return 0;
        }
    }
}

int main() {
    int x1, y1, x2, y2;
    int x3, y3, x4, y4;
    long long ccw123, ccw124, ccw341, ccw342;

    scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
    scanf("%d %d %d %d", &x3, &y3, &x4, &y4);

    ccw123 = ccw(x1, y1, x2, y2, x3, y3);
    ccw124 = ccw(x1, y1, x2, y2, x4, y4);
    ccw341 = ccw(x3, y3, x4, y4, x1, y1);
    ccw342 = ccw(x3, y3, x4, y4, x2, y2);

    // 두 선분이 한 직선 위에 있는 경우
    if (ccw123 * ccw124 == 0 && ccw341 * ccw342 == 0) {
        // 두 선분의 x좌표가 겹치는지 확인하여 겹치면 1, 아니면 0을 출력
        if (x1 > x2) { int temp = x1; x1 = x2; x2 = temp; }
        if (x3 > x4) { int temp = x3; x3 = x4; x4 = temp; }
        printf("%d\n", (x1 <= x4 && x3 <= x2) ? 1 : 0);
    } else {
        // 두 선분이 서로 교차하는지 확인하여 교차하면 1, 아니면 0을 출력
        printf("%d\n", (ccw123 * ccw124 <= 0 && ccw341 * ccw342 <= 0) ? 1 : 0);
    }

    return 0;
}
