main(X,N){int c=0;scanf("%d%d",&X,&N);while(X<N)c++,X=X%3==2?3*X:X%3?2*X:X+1;printf("%d\n",c);}