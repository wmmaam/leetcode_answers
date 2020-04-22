''' #这摘录是来自leetcode编辑器里help(ListNode)
Help on class ListNode in module precompiled.listnode:

class ListNode(builtins.object)
 |  ListNode(val=0, next=None)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, val=0, next=None)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  __str__(self)
 |      Return str(self).
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  serialize(head) from builtins.type
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  deserialize(s)
 |  
 |  has_cycle(head)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
'''


class Solution:
    '''
    这个不是leetcode里要的解法，leetcode里需要用到ListNode
    '''
    def addTwoNumbers(self, l1: list, l2: list) -> list:
        '''
        给出两个 非空 的链表用来表示两个非负的整数。
        其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
        如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
        您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
        示例：
        输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
        输出：7 -> 0 -> 8
        原因：342 + 465 = 807
        '''

        l1.reverse()
        l2.reverse()
        l1_num = ""
        l2_num = ""
        for n in l1:
            l1_num += str(n)
        for n in l2:
            l2_num += str(n)
        s = int(l1_num) + int(l2_num)
        s = str(s)
        rst = []
        for c in s:
            rst.append(c)
        rst.reverse()
        return rst


# test
# sol: Solution = Solution()
# print(sol.addTwoNumbers([3, 4, 5], [6, 7, 8]))


# Definition for singly-linked list. 来自leetcode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        should_add = False
        rst = []
        while l1 or l2:
            if l1:
                n1 = l1.val
            else:
                n1 = 0
            if l2:
                n2 = l2.val
            else:
                n2 = 0
            s = n1 + n2
            if should_add:
                s += 1
                should_add = False
            if s >= 10: should_add = True
            rst.append(s % 10)
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        if should_add: rst.append(1)

        # rst.reverse()
        # print(rst)

        head: ListNode = ListNode(rst[0])
        r = head
        e = head
        for n in rst[1::]:
            # print(n)
            node = ListNode(n)
            e.next = node
            e = e.next

        return r


#TEST
'''
输入
[2,4,3]
[5,6,4]
输出
[7,0,8]
预期结果
[7,0,8]
'''
sol2: Solution2 = Solution2()
#构建l1 [2,4,3]

# l1=ListNode(2)
# l1.next=ListNode(4)
# l1.next.next=ListNode(3) #2b方法
list = [2, 4, 3]
l1_head = ListNode(list[0])
l1 = l1_head
temp = l1_head
print("l1_head id is {}".format(id(l1_head)))
print("l1 id is {}".format(id(l1)))
print("temp id is {}".format(id(temp)))
for n in list[1::]:
    temp.next = ListNode(n)
    temp = temp.next
# after this for, the l1 has been built from list

#构建l2 [5,6,4]
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result = sol2.addTwoNumbers(l1, l2)

# print(result) can not be printed
while result is not None:
    print(result.val)
    result = result.next
