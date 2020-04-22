'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1
示例 2:
输入: [4,1,2,1,2]
输出: 4
'''


class Solution:
    '''
    执行用时 :4196 ms, 在所有 Python3 提交中击败了5.55%的用户
    内存消耗 :15.4 MB, 在所有 Python3 提交中击败了5.26%的用户
    '''
    def singleNumber(self, nums: list) -> int:
        for i in range(len(nums)):
            n = nums[i]
            if i == 0:
                if n not in nums[i + 1:]:
                    return n
            elif i == len(nums) - 1:
                return n
            else:
                if n not in nums[i + 1:] and n not in nums[:i]:
                    return n


sol = Solution()
print(sol.singleNumber([2, 2, 1]))
print(sol.singleNumber([4, 1, 2, 1, 2]))
