#include <string>
#include <vector>

using namespace std;

int solution(vector<int> bandage, int max_hp, vector<vector<int>> attacks) {
    int t = bandage[0];
    int heal = bandage[1];
    int bonus = bandage[2];
    int hp = max_hp;
    int prev = 0;
    
    for(int i=0; i<attacks.size(); i++){
        int time = attacks[i][0];
        int damage = attacks[i][1];
        
        int gap = time - prev - 1;
        int new_hp = hp + gap * heal + gap/t * bonus;
        if(new_hp > max_hp)
            hp = max_hp;
        else
            hp = new_hp;
        hp -= damage;
        
        if(hp<=0)
            return -1;
        
        prev = time;
    }
    return hp;
}