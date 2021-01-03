# 692. Top K Frequent Words

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        friquency = {word: words.count(word) for word in words}
        friquency = sorted(friquency.items(), key=lambda x: (-x[1], x[0]), reverse=False)
        return [friquency[i][0] for i in range(k)]