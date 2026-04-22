#include <cctype>
#include <cstdio>
#include <cstdlib>

int main() {
    char x[10];
    char y[10];
    scanf("%s %s", x, y);
    bool is_x_nan = false;
    bool is_y_nan = false;
    for (int i = 0; x[i] != '\0'; i++) {
        if (!isdigit(x[i])) {
            is_x_nan = true;
            break;
        }
    }
    for (int i = 0; y[i] != '\0'; i++) {
        if (!isdigit(y[i])) {
            is_y_nan = true;
            break;
        }
    }

    if (is_x_nan || is_y_nan) {
        printf("NaN\n");
    } else {
        int result = atoi(x) - atoi(y);
        printf("%d\n", result);
    }

    return 0;
}