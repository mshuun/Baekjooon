#include <bits/stdc++.h>
using namespace std;

static const int BUFSZ = 1 << 20;
static unsigned char buf[BUFSZ];
static int bi = 0, bn = 0;

static inline int gc() {
    if (bi >= bn) { bn = fread(buf, 1, BUFSZ, stdin); bi = 0; }
    return bn ? buf[bi++] : -1;
}
static inline long long rd() {
    int c; do c = gc(); while (c <= 32);
    long long x = 0;
    for (; c > 32; c = gc()) x = x * 10 + (c - '0');
    return x;
}

int main() {
    int N = (int)rd();
    long long M = rd();

    vector<uint32_t> a(N);
    uint32_t mx = 0;
    for (int i = 0; i < N; ++i) {
        uint32_t v = (uint32_t)rd();
        a[i] = v;
        if (v > mx) mx = v;
    }

    uint32_t lo = 0, hi = mx, ans = 0;
    while (lo <= hi) {
        uint32_t mid = lo + ((hi - lo) >> 1);
        unsigned long long s = 0;

        const uint32_t *p = a.data();
        for (int i = 0; i < N; ++i) {
            uint32_t v = p[i];
            if (v > mid) {
                s += (unsigned long long)(v - mid);
                if (s >= (unsigned long long)M) break;
            }
        }

        if (s >= (unsigned long long)M) ans = mid, lo = mid + 1;
        else hi = mid - 1;
    }

    printf("%u\n", ans);
    return 0;
}