main() {
    int N;
    char S[101];

    scanf("%d", &N); 
    scanf("%s", S); 

    int is_same = 1;
    for (int i = 1; i < N; i++) {
        if (S[i] != S[0]) { 
            is_same = 0;
            break;
        }
    }

    if (is_same) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
}
