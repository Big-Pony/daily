'''
1367. 二叉树中的列表
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head, root):
        self.head=head
        self.res=0
        def dfs(root,head):
            if root==None:
                return
            if root.val==head.val:
                if head.next==None:
                    self.res=1
                else:
                    dfs(root.left, head.next)
                    dfs(root.right, head.next)
            elif head!=self.head:
                dfs(root,self.head)
            else:

                dfs(root.left,self.head)
                dfs(root.right,self.head)
        dfs(root,head)
        if self.res==0:
            return False
        else:
            return True