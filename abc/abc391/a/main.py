from collections import defaultdict

D = input()
direction = defaultdict(str)
direction["N"] = "S"
direction["S"] = "N"
direction["E"] = "W"
direction["W"] = "E"
direction["NE"] = "SW"
direction["SW"] = "NE"
direction["NW"] = "SE"
direction["SE"] = "NW"
print(direction[D])