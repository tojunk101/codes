

# S1 = "ABCDGH" and S2 = "AEDFHR", lcs => "ADH"
def lcs(s1, s2, res):
    res['counter'] += 1
    if len(s1) <= 0 or len(s2) <= 0:
        return ""
    if s1[0] == s2[0]:
        return s1[0] + lcs(s1[1:], s2[1:], res)
    s1_ret = lcs(s1[1:], s2, res)
    s2_ret = lcs(s1, s2[1:], res)
    if len(s1_ret) > len(s2_ret):
        return s1_ret
    return s2_ret


print "Without Dynamic Programming"
res = {'counter': 0}
s1 = "ABCDGH"
s2 = "AEDFHR"
print "s1 = %s, s2 = %s, lcs => %s, recursive calls: %d" % (s1, s2, lcs(s1, s2, res), res['counter'])

res['counter'] = 0
s1 = "AGGTAB"
s2 = "GXTXAYB"
print "s1 = %s, s2 = %s, lcs => %s, recursive calls: %d" % (s1, s2, lcs(s1, s2, res), res['counter'])



# use dp with a hash to store the info
# The recursion will start from the back

def lcs_dp(s1, s2, res, i, j, dp):
    if 'counter' not in res:
        res['counter'] = 0
    res['counter'] += 1

    if i < 0 or j < 0:
        return ""
    idx = "{}_{}".format(i, j)
    if idx in dp:
        return dp[idx]
    if s1[i] == s2[j]:
        dp[idx] = lcs_dp(s1, s2, res, i-1, j-1, dp) + s1[i]
        return dp[idx]
    s1_ret = lcs_dp(s1, s2, res, i-1, j, dp)
    s2_ret = lcs_dp(s1, s2, res, i, j-1, dp)
    if len(s1_ret) > len(s2_ret):
        dp[idx] = s1_ret
    else:
        dp[idx] = s2_ret
    return dp[idx]

print "With Dynamic Programming"
dp = {}
res = {'counter': 0}
s1 = "ABCDGH"
s2 = "AEDFHR"
print "s1 = %s, s2 = %s, lcs => %s, recursive calls: %d" % (s1, s2, lcs_dp(s1, s2, res, len(s1) - 1, len(s2) - 1, dp), res['counter'])
dp = {}
res = {'counter': 0}
s1 = "AGGTAB"
s2 = "GXTXAYB"
print "s1 = %s, s2 = %s, lcs => %s, recursive calls: %d" % (s1, s2, lcs_dp(s1, s2, res, len(s1) - 1, len(s2) - 1, dp), res['counter'])

