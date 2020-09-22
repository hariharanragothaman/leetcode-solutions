#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) 
    {
        if (strs.size() == 0) return "";
        for (int i = 0; i < strs[0].size(); i++)
            for (int j = 1; j <strs.size(); j++)
            // Basically the first one is for - comparing strings of different length
            // Second one, to check the actual prefix value, if they are same or not.
                if (i >= strs[j].size() || strs[j][i] != strs[j-1][i])
                    return strs[0].substr(0,i);
        return strs[0];
    }
};