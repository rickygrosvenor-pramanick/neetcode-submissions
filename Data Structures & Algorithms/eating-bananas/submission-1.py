class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # O(nlogm), meaning we are searching over values as opposed to indices
        # The values we are searching over are bananas-per-hour eating rate k
        # These values range from 1 to max(piles)
        # we want the min value over these range such that we can eat all the
        # bananas in h hours.

        def doesEatInTime(eating_speed: int) -> bool:
            
            time_taken = 0
            for i in range(len(piles)):
                current_pile = piles[i]
                # need to add ceiling of divided time, so remainder adds another hour
                time_taken += (current_pile + eating_speed - 1) // eating_speed
            
            if time_taken > h:
                return False
            else:
                return True
        
        min_so_far = max(piles)

        def findMin(a, b):

            midpoint = (a + b) // 2

            # base case: we are at the minimum only when 
            # we eat in time at midpoint, but any value lower than this
            # takes too long to eat.

            # base case 1.2: if midpoint is 1, and we eat in time with 1
            # return 1
            if midpoint == 1 and doesEatInTime(1):
                return 1
            
            if doesEatInTime(midpoint) and not doesEatInTime(midpoint - 1):
                return midpoint
            elif doesEatInTime(midpoint):
                return findMin(a, midpoint - 1)
            else:
                return findMin(midpoint + 1, b)
        
        minimum = findMin(1, max(piles))

        return minimum



