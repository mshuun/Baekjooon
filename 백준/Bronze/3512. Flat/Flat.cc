 #include <bits/stdc++.h>
using namespace std;

map <string, double> s;
double n, c, t, sz;
string type;

int main(){
  cin >> n >> c;

  while(n--){
    cin >> sz >> type;
    s[type] += sz;
    t += sz;
  }
  
  cout << t << '\n' << s["bedroom"] << '\n';
  printf("%.6f\n", c * (t - s["balcony"]/2));
}