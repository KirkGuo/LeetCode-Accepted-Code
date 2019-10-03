class Solution {
public:
    bool is_grouped(vector<int> &boss, unsigned int a, unsigned int b){
        if(a>=boss.size() || b>=boss.size())
            return false;
        if(a==b)
            return true;
        if(boss[a]==a && boss[b]==b)
            return false;
        return find_boss(boss, a)==find_boss(boss, b);
    }
    int find_boss(vector<int> &boss, unsigned int a){
        if(a>=boss.size())
            return -1;
        if(boss[a]==a)
            return a;
        return boss[a] = find_boss(boss, boss[a]);
    }
    int set_boss(vector<int> &boss, unsigned int a, unsigned int b){
        if(a>=boss.size() || b>=boss.size())
            return -1;
        int boss_a = find_boss(boss, a);
        int boss_b = find_boss(boss, b);
        return boss_a==boss_b ? boss_a : boss[a]=boss[boss_a]=boss_b;
    }
    
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<int> boss(n);
        for(int i=0; i<n; i++)
            boss[i] = i;
        for(int i=0; i<edges.size(); i++)
            set_boss(boss, edges[i][0], edges[i][1]);
        int ans = 0;
        for(int i=0; i<n; i++)
            if(boss[i]==i)
                ans++;
        return ans;
    }
};
