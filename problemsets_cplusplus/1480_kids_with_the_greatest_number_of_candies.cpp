#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<bool> kidswithCandies(vector<int>& candies, int extraCandies)
{
    vector<bool> result(candies.size());
    fill(result.begin(), result.end(), false);

    int max_value;
    max_value = *max_element(candies.begin(), candies.end());

    for(int j=0; j < candies.size(); j++)
    {
        if(candies[j] + extraCandies >= max_value)
        {
            result[j] = true;
        }
    }
    return result;
}