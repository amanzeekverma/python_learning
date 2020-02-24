"""
### using template version 1

https://leetcode.com/problems/palindrome-number/

CODE  STRUCTURE AND ALGO
Attempt 1 is string manipulation
Attempt 2 is a int based manipulation

TEST DETAILS
Tested with Python3.8

TAKE AWAYS:
int/float division
print formatting.
Hate PEP8 for not letting me use CamelCase variables.

"""


class Solution(object):
    def self_not_used(self):
        pass

    def isPalindrome1(self, x: int) -> bool:
        self.self_not_used()  # NICE HACK! THIS COULD HAVE BEEN A STATIC METHOD
        # ATTEMPT 1
        x_str = str(x)
        start_ix = 0
        last_ix = len(x_str) - 1
        while start_ix < last_ix:
            if x_str[start_ix] != x_str[last_ix]:
                return False
            start_ix += 1
            last_ix -= 1
        return True

    def isPalindrome2(self, x: int) -> bool:
        self.self_not_used()  # NICE HACK! THIS COULD HAVE BEEN A STATIC METHOD
        if x < 0:
            return False
        newNumber = 0
        originalNumber = x
        index = 0
        rem = -1
        while x > 0:
            rem = x % 10
            newNumber = newNumber*10 + rem
            x = x // 10    # We use "//" for int division otherwise its a float one.
            index += 1
            print("Current Status REM: {0}, NEW_NUM: {1}, x: {2}, index = {3}".format(rem, newNumber, x, index))
        print("Oring = {0} AND New = {1}".format(originalNumber, newNumber))
        if originalNumber == newNumber:
            return True
        return False


class Main:
    if __name__ == "__main__":
        s = Solution()
        x = int(input())
        print(s.isPalindrome2(x))
        # CALLER
