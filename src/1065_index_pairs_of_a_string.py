"""
Given a text string and words (a list of strings),
return all index pairs [i, j] so that the substring text[i]...text[j] is in the list of words.

# Note" 'substring' is the most important part of this.

Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation:
Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].

Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]

"""

def index_pairs(text, words):
    output = []
    for w in words:
        idx = text.find(w)
        while idx != -1:
            output.append([idx, idx+len(w)-1])
            idx = text.find(w, idx+1)
    return output.sort()