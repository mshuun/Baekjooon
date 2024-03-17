int G(int a,int b){return b?G(b,a%b):a;}
int R(const char *s, const char *P, int T){int Z=strlen(s);if(Z%T!=0)return 0;for(int i=0;i<Z;i++){if(s[i]!=P[i%T])return 0;}return 1;}
main(){char S[51],T[51];scanf("%s%s",S,T);int X=strlen(S), Y=strlen(T);int e=G(X, Y);for (int i=1; i <= e; i++){if(e%i==0&&R(S,S,i)&&R(T,S,i)){S[i]='\0';printf("%s",S);return 0;}}printf("No solution");}