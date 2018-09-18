# Is a string is unique or not? using hashtable
# O(n)
def is_unique(str):
    htable = {}

    for i in range(len(str)):
        if str[i] in htable:
            return False
        else:
            htable[str[i]] = 1
    return True


str = "abcdedf"
print(is_unique(str))
