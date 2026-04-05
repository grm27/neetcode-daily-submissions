from sortedcontainers import SortedDict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = SortedDict()
        for card in hand:
            count[card] = count.get(card, 0) + 1
        
        for i in range(len(hand) // groupSize):
            start = next(iter(count))
            for j in range(groupSize):
                if start not in count:
                    return False
                count[start] -= 1
                if count[start] == 0:
                    del count[start]
                start += 1
        
        return True