#include <iostream>
using namespace std;

int main(){
    long long n,a=1,b=1,s=1,c=0;
    cin>>n;
    while(a<=n){
        if(s<n) s+=++b;
        else if(s>n) s-=a++;
        else c++,s-=a++;
    }
    cout<<c;
}