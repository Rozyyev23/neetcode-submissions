class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse = True)
        fleet = []

        for pos, spd in pairs:
            res = (target - pos) / spd
            if not fleet or  res > fleet[-1]:
                fleet.append(res)

        return len(fleet)