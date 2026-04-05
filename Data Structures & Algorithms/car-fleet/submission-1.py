class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse = True)
        fleet = [0]

        for pos, spd in pairs:
            res = (target - pos) / spd

            if res > fleet[-1]:
                fleet.append(res)

        return len(fleet)-1