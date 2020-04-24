'''
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。
示例：
输入：19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
# 注意以上^是幂次运算， 不是位异或运算
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        trycount = 10000
        ct = 0
        while ct < trycount:
            n = toH(n)
            if n == 1:
                return True
            ct += 1
        return False


def toH(n):
    strn = str(n)
    r = 0
    for i in strn:
        r += (int(i)**2)
    return r


sol = Solution()
print(sol.isHappy(19))
