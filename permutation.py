# calculate all the permutaions
# permutations if "abc": [abc, acb, bac, bca, cab, cba]


# Without dynamic programming
# Pure recursive calls. Space used O(1)
def permute(key, input):
    if input == "":
        print(key)
        return
    for idx, letter in enumerate(list(input)):
        k = key + letter
        i = input[:idx] + input[idx+1:]
        permute(k, i)

def permutation(input):
    permute("", input)


# Recursive with Dynamic Programming
def permute_dp(input, kv={}, use_dp=True):
    if len(input) == 1:
        return [input], 1
    res = []
    count = 0
    for idx, letter in enumerate(list(input)):
        i = input[:idx] + input[idx+1:]
        if i in kv and use_dp:
            prm = kv[i]
        else:
            prm, cnt = permute_dp(i, kv=kv, use_dp=use_dp)
            count += cnt
        for p in prm:
            res.append(letter + p)
    kv[input] = res
    return res, count


def permutation_dp(input, use_dp=True):
    hh = {}
    result, counter = permute_dp(input, kv=hh, use_dp=use_dp)
    for res in result:
        print (res)
    print("Number of recursive call: %d, used DP: %s" % (counter, str(use_dp)))


print("Recursive without using space")
permutation("abcd")
print("Recursive DP and using a hash")
permutation_dp("abcd")
permutation_dp("abcd", use_dp=False)

