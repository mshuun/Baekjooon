#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int start;
    int end;
} Meeting;

int compare(const void* a, const void* b) {
    Meeting m1 = *(Meeting*)a;
    Meeting m2 = *(Meeting*)b;
    
    if (m1.end == m2.end) {
        return m1.start - m2.start;
    }
    return m1.end - m2.end;
}

int main() {
    int n, e = 0, c = 0;
    scanf("%d", &n);
    
    Meeting* meetings = (Meeting*)malloc(sizeof(Meeting) * n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &meetings[i].start, &meetings[i].end);
    }
    
    qsort(meetings, n, sizeof(Meeting), compare);
    
    for (int i = 0; i < n; i++) {
        if (meetings[i].start >= e) {
            c++;
            e = meetings[i].end;
        }
    }
    
    printf("%d\n", c);
    free(meetings);
    return 0;
}
