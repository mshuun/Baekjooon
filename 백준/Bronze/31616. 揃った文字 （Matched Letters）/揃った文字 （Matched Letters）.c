main() {
    int N;char S[101];scanf("%d",&N);scanf("%s",S);int M=1;
    for(int i=1;i<N;i++){if(S[i]!=S[0]){M=0;break;}}

    if(M)printf("Yes\n");
    else printf("No\n");
    
}