G(int a,int b){return b?G(b,a%b):a;}
R(char *s,char *P,int T){int Z=strlen(s);if(Z%T!=0)return 0;for(int i=0;i<Z;i++){if(s[i]!=P[i%T])return 0;}return 1;}
main(X,Y,e,i){char S[51],T[51];scanf("%s%s",S,T);X=strlen(S);Y=strlen(T);e=G(X, Y);for (i=1;i<=e;i++){if(e%i==0&&R(S,S,i)&&R(T,S,i)){S[i]='\0';printf("%s",S);return 0;}}printf("No solution");}