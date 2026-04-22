 #include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    int can[100]; 
    for (int i = 0; i < a; i++) scanf("%d", &can[i]);

    int c = 1;
    int r;
    while (c) {
        for (int i = 0; i < a; i++) {
            if (can[i] < b) {
                c = 0;
                r = i;
                break;
            } else b += 1;
        }
    }

    printf("%d\n", r + 1);

    return 0;
}