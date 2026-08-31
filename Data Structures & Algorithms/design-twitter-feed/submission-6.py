import heapq

class Twitter:

    def __init__(self):
        self.followMap=defaultdict(set)
        self.postMap=defaultdict(list)
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap=[]
        res=[]
        self.followMap[userId].add(userId)
        for follower in self.followMap[userId]:
            if follower in self.postMap:
                index=len(self.postMap[follower])-1
                count, tweetid=self.postMap[follower][index]
                minheap.append([count,tweetid,index-1,follower])
        heapq.heapify(minheap)
        while minheap and len(res)<10:
            count,Id,index,follower=heapq.heappop(minheap)
            res.append(Id)
            if index>=0:
                count, tweetid=self.postMap[follower][index]
                heapq.heappush(minheap,[count,tweetid, index-1,follower])
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
