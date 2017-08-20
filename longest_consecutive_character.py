# Complexity: O(n)
# Tag: string
def longest_consecutive_character(arg):
    max_cur = max_gbl = [arg[0]]
    for c in arg[1:]:
        if c == max_cur[0]:
            max_cur.append(c)
        else:
            max_cur = [c]
        if len(max_cur) > len(max_gbl):
            max_gbl = max_cur
    return max_gbl

input = "aabsbbbcbccb"
print "Input: %s, Output: %s" % (input, "".join(longest_consecutive_character(input)))
input = "aabsbbcbccb"
print "Input: %s, Output: %s" % (input, "".join(longest_consecutive_character(input)))

