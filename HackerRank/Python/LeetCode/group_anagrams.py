
from collections import defaultdict
from typing import List

'''
FAILED ATTEMPT
def groupAnagramsfailed(strs: List[str]) -> List[List[str]]:
    res = []
    wordmap = {}

    for i in strs: 
        if sorted(word): 
            res # here to stop err
    
    # after having a hashmap of original words to sorted strings 
    # i wanted to get all words which had the same value 
    # append all matching words into a list if there were no matching words append it to a list on its own 
    # append that to the res list and retulrn it
    return res

'''

# this is O(m * n) where m is the size of the array and n is the average size of the words, but it is not as efficient as the other solution because the words do not get big enough. 
def groupAnagrams2(strs: List[str]) -> List[List[str]]: 
    res = defaultdict(list) # storing character count to anagrams list because anagrams  have the same frequency of words

    for word in strs: 
        count = [0] * 26 # same as count = [0, 0, 0, .... 0] 26 times

        for char in word: 
            count[ord(char) - ord("a")] += 1
        res[tuple(count)].append(word)  

        print(count)
    print(res.keys())
    

    return res.values()

    # if you don't want to use default dict 
    res = {}

    
    for word in strs:
        count = [0] * 26  # Count frequency of each character (a-z)

        for char in word:
            count[ord(char) - ord('a')] += 1

        key = tuple(count)  

        if key not in res:
            res[key] = []  

        res[key].append(word)

# O(m * n log n) n log n for the sorting alg, but since strings <= 100 and the length of the whole array is <= 10^4 this is faster
def groupAnagrams1(strs: List[str]) -> List[List[str]]:
    
    groups = defaultdict(list) 
    
    # had to watch vids and chatgpt before figuring this out
    for word in strs: 
        sorted_word = "".join(sorted(word))
        groups[sorted_word].append(word)
    
    return list(groups.values())

    # if not wanting to use default dict 
    groups = {}

    for word in strs: 
        sorted_word = "".join(sorted(word))

        if sorted_word not in groups: 
            groups[sorted_word] = []
        
        groups[sorted_word].append(word)

    return groups.values()


strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

print(groupAnagrams2(strs1))

