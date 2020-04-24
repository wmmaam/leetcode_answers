'''
统计所有小于非负整数 n 的质数的数量。
示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''


class Solution:
    def countPrimes(self, n: int) -> int:
        pass


def getPrimes(n) -> list:
    '''
    求解小于n的质数，如果没有反馈空列表[]
    '''
    if n < 3:
        return []

    rst = {}
    for i in range(1, n):  # 从1 到 n-1
        rst[i] = True  #在rst中先存入数和是否是质数的bool值，默认true
    rst[1] = False  #1不是质数

    for num in range(2, (int(n**0.5) + 1)):
        # 从2开始，遍历到根号n取整，因为range是左包含，右不包含，所以是int(n**0.5) + 1
        if rst[num] == True:
            # 如果num是质数，从num的平方开始（包含），遍历num的倍数num+1，倍数num+2.....直到大于n
            start = num
            step = num  #倍数
            checking_num = start * num  #其实就是num*num
            while checking_num < n:
                rst[checking_num] = False
                step += 1
                checking_num = num * step

    # print(rst)
    # use "python lise comprehension" to get the list
    # can also use for loop
    return [k for k in rst.keys() if rst[k] == True]


def getPrimes2(n) -> list:
    '''
    求解小于n的质数，如果没有反馈空列表[]
    '''
    if n < 3:
        return []

    # rst = {}
    # for i in range(1, n): # 从1 到 n-1
    #     rst[i] = True  #在rst中先存入数和是否是质数的bool值，默认true
    # rst[1] = False  #1不是质数

    #用存bool值的list代替
    rst = [1] * (n - 1)  #构建一个全是1值的数组
    rst[0] = 0  #第一个数，1，不是质数

    for num in range(2, (int(n**0.5) + 1)):
        # 从2开始，遍历到根号n取整，因为range是左包含，右不包含，所以是int(n**0.5) + 1
        if rst[num - 1] == 1:  #这是index是num-1，
            # 如果num是质数，从num的平方开始（包含），遍历num的倍数num+1，倍数num+2.....直到大于n
            # start = num #去掉start，用num代替
            step = num  #倍数
            checking_num = num * num  #其实就是num*num
            while checking_num < n:
                rst[checking_num - 1] = 0
                step += 1
                checking_num = num * step

    # print(rst)
    # use "python lise comprehension" to get the list
    # can also use for loop
    return [idx + 1 for idx in range(n - 1) if rst[idx] == 1]


def getPrimes3(n) -> list:
    '''
    求解小于n的质数，如果没有反馈空列表[]
    '''
    if n < 3:
        return []

    #用存bool值的list代替
    rst = [1] * n  #构建一个全是1值的数组
    # 直接将index看成对应的数，只是包含一个初始的0
    rst[0] = rst[1] = 0  #第一个数0和第二个数1都不是质数

    for num in range(2, (int(n**0.5) + 1)):
        # 从2开始，遍历到根号n取整，因为range是左包含，右不包含，所以是int(n**0.5) + 1
        if rst[num] == 1:
            # 如果num是质数，从num的平方开始（包含），遍历num的倍数num+1，倍数num+2.....直到大于n
            # start = num #去掉start，用num代替
            # step = num  #倍数
            # checking_num = num * num  #其实就是num*num
            # while checking_num < n:
            #     rst[checking_num - 1] = 0
            #     step += 1
            #     checking_num = num * step

            #切片赋值
            rst[num**2:n:num] = [0] * (((n - 1 - num**2) // num) + 1)

    # print(rst)
    # use "python lise comprehension" to get the list
    # can also use for loop
    return [idx for idx in range(n) if rst[idx] == 1]


primes = getPrimes3(10)
print(primes)
print("Total primes' count is: {}".format(len(primes)))
