class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        sorted_pairs = sorted(pairs, key=lambda x: x[0], reverse=True)
        stack = []

        for pair in sorted_pairs:
            pos, spd = pair[0], pair[1]
            time_to_target = (target - pos)/spd
            stack.append(time_to_target)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            