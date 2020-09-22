/* Remove element from an array -in place and return the length of the resultant array */
class Solution {
public:
    int removeElement(vector<int>& nums, int val) 
    {
        int index = 0;
        for(int i=0; i < nums.size(); i++)
        {
            if(nums[i] != val)
            {
                nums[index] = nums[i];
                index++;
            }
        }
        
        for(auto i : nums)
            cout << i;
        
        return index;
    }
};

/*  The other smart way to do it using STL is: 
class Solution {
public:
    int removeElement(vector<int>& nums, int val) 
    {
        nums.erase(remove(nums.begin(), nums.end(), val), nums.end());
        return nums.size();
    }
};

*/

