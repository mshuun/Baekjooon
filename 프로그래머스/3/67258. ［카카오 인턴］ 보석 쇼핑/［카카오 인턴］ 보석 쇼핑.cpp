#include <bits/stdc++.h>
using namespace std;

vector<int> solution(vector<string> gems) {
    int target = unordered_set<string>(gems.begin(), gems.end()).size();
    unordered_map<string, int> counts;

    int left = 0;
    vector<int> answer = {0, (int)gems.size() - 1};

    for (int right = 0; right < gems.size(); right++) {
        counts[gems[right]]++;

        while (counts.size() == target) {
            if (right - left < answer[1] - answer[0])
                answer = {left, right};

            counts[gems[left]]--;
            if (counts[gems[left]] == 0)
                counts.erase(gems[left]);

            left++;
        }
    }

    return {answer[0] + 1, answer[1] + 1};
}
