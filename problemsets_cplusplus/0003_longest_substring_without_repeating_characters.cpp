#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int longest_substring_without_repeating_characters(string s)
{
    vector<int> dict(256, -1);
    int max_length = 0;
    int start = -1;

    for(int i = 0; i < s.length(); i++)
    {
        if (dict[s[i]] > start)
        {
            start = dict[s[i]];
        }

        dict[s[i]] = i;
        max_length = max(max_length, i - start);
    }
    return max_length;


}

int main()
{
    string s = "ababab";
    int length = 0;
    length = longest_substring_without_repeating_characters(s);
    cout << "The length is:" << length;
    return 0;
}