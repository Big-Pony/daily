class LFUCache:

    def __init__(self, capacity):
        self.capacity=capacity
        #key:[value,p,t],p是被操作的次数,t是加入时的时间
        self.storage={}
        self.time=0
    def leng(self):
        return len(self.storage)
    def find_min(self,i):
        min_val=float('inf')
        for k in self.storage:
            if self.storage[k][i]<min_val:
                min_val=self.storage[k][i]
        return min_val
    def get(self, key) :
        if key in self.storage:
            self.time+= 1
            self.storage[key][1]+=1
            print(self.storage[key][0])
            return self.storage[key][0]
        else:
            print(-1)
            return -1
    def put(self, key, value):
        self.time += 1
        if self.leng()<self.capacity:
            self.storage[key]=[value,1,self.time]
        else:

            min_val=self.find_min(1)
            min_list_key=[]
            for i in self.storage:
                if self.storage[i][1]<=min_val:
                    min_list_key.append(i)

            if len(min_list_key)>1:
                min_time=self.find_min(2)
                for i in self.storage:
                    if self.storage[i][2] <= min_time:
                        self.storage.pop(i)
                        break
            else:
                self.storage.pop(min_list_key[0])
            self.storage[key]=[value,1,self.time]


cache=LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
print(cache.storage)
cache.get(2)
cache.get(3)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)


