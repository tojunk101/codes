# Find the longest substring without repeating characters
# "abcabcbb" => "abc"
# "bbbb" => "b"
# "pwwkew" => "wke"
# Complexity: O(n^2) => n = length of arg

def lc_substring(arg):
    max_cur = max_gbl = []
    for c in arg:
        if c not in max_cur:
            max_cur.append(c)
        else:
            max_cur = [c]
        if len(max_cur) > len(max_gbl):
            max_gbl = max_cur
    return max_gbl


print "Input: \"abcabbb\", Output: %s" % "".join(lc_substring("abcabbb"))
print "Input: \"bbb\", Output: %s" % "".join(lc_substring("bbb"))
print "Input: \"pwwkew\", Output: %s" % "".join(lc_substring("pwwkew"))

