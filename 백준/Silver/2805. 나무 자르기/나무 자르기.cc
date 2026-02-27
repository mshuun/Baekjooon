#include <stdio.h>
#include <sys/stat.h>
#include <sys/mman.h>

int a[1000000];

int main() {

    struct stat st; fstat(0, &st);
    char* p = (char*)mmap(0, st.st_size, PROT_READ, MAP_SHARED, 0, 0);
    
    auto get = [&]() {
        int n = 0;
        while (*p < '0') p++;
        while (*p >= '0') n = n * 10 + *p++ - '0';
        return n;
    };
    
    int n = get(), m = get(), r = 0;
    
    for (int i = 0; i < n; ++i) {
        if ((a[i] = get()) > r) r = a[i];
    }
    
    int l = 0, ans = 0;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        long long sum = 0;
        
        for (int i = 0; i < n; ++i) 
            if (a[i] > mid) sum += a[i] - mid;
        
        if (sum >= m) {
            ans = mid;
            l = mid + 1; 
        } else {
            r = mid - 1;
        }
    }
    
    printf("%d", ans);
}