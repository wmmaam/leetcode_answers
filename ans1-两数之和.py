class Solution:
    def twoSum(self, nums: list, target: int) -> list:

        for start_index in range(0, len(nums)):
            diff = target - nums[start_index]
            if diff in nums and nums.index(diff) != start_index:
                # 使用数组的查找功能，引入哈希表的优势，减少遍历次数，比暴力算法更快
                return [start_index, nums.index(diff)]

        return [-1, -1]


class Solution2():
    def twoSum(self, nums: list, target: int) -> list:

        #从原数组中遍历值，算差diff，如果temp_list中包含diff，就return结果
        #如果temp_list中没有diff，就把原值放入temp_list
        #这样1.避免了差和原值是同一个数的情况
        #2.而且利用temp_list数组比较，能减少比较量
        temp_list = []
        for start_index in range(0, len(nums)):
            diff = target - nums[start_index]
            if diff in temp_list:
                return [start_index, temp_list.index(diff)]
            temp_list.append(nums[start_index])

        return [-1, -1]


sol: Solution2 = Solution2()
ans = sol.twoSum([3, 4, 5, 6, 7, 8], 12)
print(ans)
