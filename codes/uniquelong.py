def uniquelong(s,k):
    if len(s)<k or k==0:
        return ""
    char_freq = {}
    start =0
    max_length = 0
    longest_substring = ""
    for end in range(len(s)):
        char = s[end]
        char_freq[char] = char_freq.get(char,0)+1
        while len(char_freq)>k:
            left_char = s[start]
            char_freq[left_char]-=1
            if char_freq[left_char]==0:
                del char_freq[left_char]
            start+=1
        if end-start+1 >max_length and len(char_freq)==k:
            max_length = end-start+1
            longest_substring = s[start:end+1]
    return longest_substring
s = "aabacbebebe"
k = 3
print(uniquelong(s,k))


def withoutrepeat(s):
    char_freq = {}
    start = 0
    max_len = 0
    longest_substring = ""
    for end in range(len(s)):
        char = s[end]
        if char in char_freq and char_freq[char]>=start:
            start = char_freq[char]+1
        char_freq[char] = end
        if end-start+1> max_len:
            max_len = end-start+1
            longest_substring = s[start:end+1]
    return longest_substring
print(withoutrepeat(s = "abcabcbb"))

def toys(s,k):
    toys_freq = {}
    start = 0
    maxlen = 0
    for end in range(len(s)):
        char  = s[end]
        toys_freq[char] = toys_freq.get(char,0)+1
        while len(toys_freq)>k:
            left_toy= s[start]
            toys_freq[left_toy]-=1
            if toys_freq[left_toy]==0:
                del toys_freq[left_toy]
            start+=1
        maxlen = max(maxlen,end-start+1)
    return maxlen
print(toys("abaccab",2))

