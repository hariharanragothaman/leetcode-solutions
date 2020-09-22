#include <iostream>
#include <vector>
using namespace std;

vector<int> shuffleArray(vector<int>& nums, int n)
{
    int i = 0;
    int j = nums.size() / 2;
    vector<int> result;

    while( i < nums.size() / 2 or j < 2*n)
    {
        result.push_back(nums[i]);
        result.push_back(nums[j]);
        i++;
        j++;
    }
    return result;
}

int main()
{
    vector<int> nums = {2, 5, 1, 3, 4, 7};
    vector<int> output;
    int n = 3;
    output = shuffleArray(nums, n);

    for(auto it: output)
    {
        cout << it;
    }
}