# 953. Verifying an Alien Dictionary

 class Solution:
     def isAlienSorted(self, words: List[str], order: str) -> bool:
         order_dict = {o: i for i, o in enumerate(order)}
         i=1
         while True:
             j=1
             while True:
                 if (order_dict[words[i-1][j-1]] < order_dict[words[i][j-1]]):
                     break
                 if (order_dict[words[i-1][j-1]] > order_dict[words[i][j-1]]):
                     return False
                 if j == min(len(words[i-1]), len(words[i])):
                     if len(words[i-1]) > len(words[i]):
                         return False
                     break
                 j+=1    
             if i == len(words)-1:
                 return True
             i+=1
            



#class Solution:
#    def isAlienSorted(self, words: List[str], order: str) -> bool:
#        return words==sorted(words, key=lambda x: [order.find(i) for i in x])