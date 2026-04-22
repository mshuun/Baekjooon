#include <stdio.h>
#include <string.h>

int main() {
    char a[9];
    scanf("%s", a);
    
    if (strcmp(a, "fdsajkl;") == 0 || strcmp(a, "jkl;fdsa") == 0)
        printf("in-out\n");
    else if (strcmp(a, "asdf;lkj") == 0 || strcmp(a, ";lkjasdf") == 0)
        printf("out-in\n");
    else if (strcmp(a, "asdfjkl;") == 0)
        printf("stairs\n");
    else if (strcmp(a, ";lkjfdsa") == 0)
        printf("reverse\n");
    else
        printf("molu\n");
    
    return 0;
}
