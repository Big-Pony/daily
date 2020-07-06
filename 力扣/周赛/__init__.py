import time
lis=[i for i in range(100000000)]
def test1():
    t1=time.time()
    a=0
    for i in range(len(lis)):
        a=i
    print(time.time()-t1)

def test2():
    t2=time.time()

    for i in range(len(lis)):
        a=i
    print(time.time()-t2)

test1()
test2()