class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        sorted_pairs = sorted(pairs, key=lambda x: x[0], reverse=True)
        stack = []

        for pair in sorted_pairs:
            pos, spd = pair[0], pair[1]
            time_to_target = (target - pos)/spd
            if not stack:
                stack.append(time_to_target)
            elif time_to_target > stack[-1]:
                # current car's finish time is slower than
                # the current fleet's head so we need a new
                # fleet
                stack.append(time_to_target)
            else:
                # time_to_target <= stack[-1]
                # the car corresponding to time_to_target
                # eventually catches up to the front of the fleet
                # so we need to do nothing
                continue
        
        return len(stack)
            