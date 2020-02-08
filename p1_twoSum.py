"""
https://leetcode.com/problems/two-sum/

I am a java guy trying to move onto python. This is first code I wrote to get started

This was initially to really learn python. Instead of clever compliment solution
Start with nested O(n^2) solution to understand basics of python.
Later improve "algo" by using compliment hashing algo, which will introduce you to dict.

Following code is tested in python3.6 (should be workable with 2.7 and 3.8)

Learn about:
__main__ and "self"
static/none staic method.
Calling function and what not.

Ofcourse, dont forget to indent! 


"""
class Solution(object):
    def self_not_used(self):
        pass

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.self_not_used()  # The function was defined as "self" but "self" was not used in function, well, this could be a static function in that case.
        compliment_dict = {}  # compliment map "compliment number" --> index
        for i in range(0, len(nums)):
            compliment = target - nums[i]
            if compliment_dict.get(compliment) is None:
                compliment_dict[nums[i]] = i
            else:
                return [compliment_dict.get(compliment), i]



class Main:
    if __name__ == "__main__":
        s = Solution()
        nums = [7, 11, 2, 15]
        target = 9
        print("answer = ", s.twoSum(nums, target))
