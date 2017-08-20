#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).
#

# The logic can be cleaned up a little
def isMatch(arg, regex):
    if len(regex) <= 0:
        return len(arg) == 0
    if len(arg) > 0 and arg[0] == regex[0] and (len(regex) <= 1 or (len(regex) > 1 and regex[1] != "*")):
        return isMatch(arg[1:], regex[1:])
    if regex[0] == "." and regex[1] and regex[1] != "*":
        return len(arg) > 0 and isMatch(arg[1:], regex[1:])
    if regex[0] == "." and regex[1] and regex[1] == "*":
        return (len(arg) == 0) or (len(arg) > 0 and isMatch(arg[1:], regex)) or (len(regex) > 2 and len(arg) > 1 and isMatch(arg[1:], regex[2:]))
    if len(regex) > 1 and regex[1] == "*":
        return (len(arg) == 0) or (arg[0] != regex[0] and isMatch(arg[1:], regex[2:])) or isMatch(arg[1:], regex)


inp = "aa"
reg = "a"
print "input: %s, regex: %s, result: %s" % (inp, reg, isMatch(inp, reg))
inp = "aa"
reg = "aa"
print "input: %s, regex: %s, result: %s" % (inp, reg, isMatch(inp, reg))
inp = "aaa"
reg = "aa"
print "input: %s, regex: %s, result: %s" % (inp, reg, isMatch(inp, reg))
inp = "aa"
reg = "a*"
print "input: %s, regex: %s, result: %s" % (inp, reg, isMatch(inp, reg))
inp = "aa"
reg = ".*"
print "input: %s, regex: %s, result: %s" % (inp, reg, isMatch(inp, reg))
inp = "ab"
reg = ".*"
print "input: %s, regex: %s, result: %s" % (inp, reg, isMatch(inp, reg))
inp = "aab"
reg = "c*a*b"
print "input: %s, regex: %s, result: %s" % (inp, reg, isMatch(inp, reg))

