from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        for i in range(len(rating)-2):
            for j in range(i+1,len(rating)):
                for k in range(j,len(rating)):
                    if rating[i]<rating[j]<rating[k]:
                        # print(rating[i], rating[j],rating[k],sep=' ')
                        teams+=1
                    elif rating[i]>rating[j]>rating[k]:
                        # print(rating[i], rating[j],rating[k],sep=' ')
                        teams+=1
        return teams