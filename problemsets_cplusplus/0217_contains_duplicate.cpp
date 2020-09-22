// Contain duplicates - just to check if array has duplicates

#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) 
    {
        unordered_map<int, int> hmap;
        for(auto &n: nums)
        {
            hmap[n]++;
        }
        
        for(auto pair: hmap)
        {
            if(pair.second > 1)
            {
                return true;
            }
        }

        return false;
    }
};

int main()
{
    vector<int> nums = {2, 7, 11, 15};
    Solution sol;
    bool result;
    result = sol.containsDuplicate(nums);
    return 0;
}