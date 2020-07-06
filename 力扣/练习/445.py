class Node():
    def __init__(self,val):
        self.val=val
        self.next=None
class Slink():
    def __init__(self):
        self.head=None
    def add_tail(self,val):
        node=Node(val)
        if self.head==None:
            self.head=node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    def travel(self):
        print('链表',end=':')
        cur=self.head
        while cur!=None:
            print(cur.val,end=',')
            cur=cur.next
        print('')

class Solution:
    def addTwoNumbers(self, l1, l2):

        def travel(node):
            cur=node
            res=[]
            while cur!=None:
                res.append(cur.val)

                cur=cur.next
            return res
        ls1=travel(l1)
        ls2=travel(l2)
        n=len(ls1)
        m=len(ls2)
        res=[0 for i in range(max(n,m)+1)]
        print('00',res,ls1,ls2)
        i=0
        min_val=-min(n,m)

        while i>min_val:

            i-=1
            r=ls1[i]+ls2[i]
            print('aa',ls1[i],ls2[i])
            res[i]=r%10
            if n>m:
                ls1[i-1]+=r//10
            else:
                ls2[i-1] += r // 10

        print(i,res)


if __name__=='__main__':
    l1=Slink()
    l2 = Slink()
    l1.add_tail(7)
    l1.add_tail(2)
    l1.add_tail(4)
    l1.add_tail(3)
    l2.add_tail(5)
    l2.add_tail(6)
    l2.add_tail(4)
    l1.travel()
    l2.travel()

    a=Solution()
    a.addTwoNumbers(l1.head,l2.head)