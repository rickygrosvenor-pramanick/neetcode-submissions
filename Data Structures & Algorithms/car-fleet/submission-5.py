class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # zip the cars and sort in descending order
        zipped = zip(position, speed)
        sorted_zipped = sorted(zipped, key= lambda x: x[0], reverse=True)

        # the front car maintains the fleet
        # so if the finishing time of the subsequent cars is less than
        # the front car, we join the same fleet
        # if its greater than the front car, we make a new fleet and push that
        # as the head of the stack

        stack = [sorted_zipped[0]]
        for i in range(1, len(position)):
            curr_pos, curr_speed = sorted_zipped[i]
            dist_to_tar = target - curr_pos
            time_to_tar = dist_to_tar / curr_speed

            # time_to_tar for fleet lead
            fleet_pos, fleet_speed = stack[-1]
            fleet_dist_tar = target - fleet_pos
            fleet_time_tar = fleet_dist_tar / fleet_speed

            if fleet_time_tar >= time_to_tar:
                continue
            else:
                stack.append(sorted_zipped[i])
        
        return len(stack)

        
