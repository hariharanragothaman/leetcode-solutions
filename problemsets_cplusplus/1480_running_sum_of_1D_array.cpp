#include <iostream>
#include <vector>

#include <numeric>  // std:: partial_sum
#include <functional> // std:: multiplies

using namespace std;


vector<int> runningSum(vector<int>& nums)
{
    for(int i=1; i < nums.size(); i++)
    {
        nums[i] = nums[i] + nums[i-1];
    }
    return nums;
}

vector<int> runningSum_stl(vector<int>& nums)
{
    partial_sum(nums.begin(), nums.end(), nums.begin());
    return nums;
}


int main()
{
    vector<int> nums = {1, 2, 3, 4};
    vector<int> op;
    op = runningSum_stl(nums);

    for(auto it: op)
    {
        cout << it << endl;
    }
}