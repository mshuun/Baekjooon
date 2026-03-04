#include <iostream>
#include <string>

using namespace std;

int main() {
    int max_num = 0;
    string max_name;
    for (int i = 0; i < 7; i++) {
        string name;
        int num;
        cin >> name >> num;
        if (max_num < num) {
            max_name = name;
            max_num = num;
        }
    }
    cout << max_name;
    return 0;
}