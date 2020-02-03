"""
### using template version 1

https://leetcode.com/problems/reverse-integer/

Standard reversing a number logic.
String manipulation for reverse here is a cheating though, IMO, we should use:
    rev = rev*10 + remainder
Runtime was good on leet platform, so I guess the string-int conversion is not a hit.

TEST DETAILS
    works for python3 only.

TAKE AWAYS:
    import sys
    sys.maxsize and int32,64 and python!
    reverse string, string to int and vice-versa
    inline if else
    python3 special params :)


"""


class Solution:
    def self_not_used(self):
        pass

    def isInt32(self, value: int) -> bool:
        self.self_not_used()
        if -(2 ** 31) < value < (2 ** 31 - 1):
            return True

    def reverse(self, x: int) -> int:
        self.self_not_used()
        number = abs(x)
        rev_number_str = ""
        while number / 10 > 0:
            remainder = number % 10
            number = int(number / 10)
            rev_number_str += str(remainder)
            print("DEB:{0} {1} {2}", number, remainder, rev_number_str)
        rev_number = int(rev_number_str) if rev_number_str else 0
        valid = self.isInt32(rev_number)
        if not valid:
            return 0
        if x > 0:
            return rev_number
        else:
            return 0 - rev_number


class Main:
    if __name__ == "__main__":
        s = Solution()
        y = s.reverse(123)
        print(y)
        # CALLER
