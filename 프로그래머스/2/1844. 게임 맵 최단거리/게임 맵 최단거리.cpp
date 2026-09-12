#include <bits/stdc++.h>
using namespace std;

int solution(vector<vector<int> > maps)
{
    int dx[] = {-1,1,0,0};
    int dy[] = {0,0,-1,1};
    
    int n = maps.size();
    int m = maps[0].size();
    
    if (n == 1 && m == 1)
        return 1;
    
    vector<vector<int>> dist(n,vector<int>(m,-1));
    
    queue<pair<int,int>> q;
    q.push({0,0});
    dist[0][0] = 1;
    
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
            
        for (int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (0 <= nx && nx < n && 0 <= ny && ny < m){
                if(maps[nx][ny] == 1 && dist[nx][ny] == -1){
                    dist[nx][ny] = dist[x][y] + 1;
                    q.push({nx,ny});
                    
                    if(nx == n-1 && ny == m-1)
                        return dist[nx][ny];
                }
            }
        }
    }
    return -1;
}