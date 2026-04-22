
w = {
    "Red": (620, 780),
    "Orange": (590, 619),
    "Yellow": (570, 589),
    "Green": (495, 569),
    "Blue": (450, 494),
    "Indigo": (425, 449),
    "Violet": (380, 424)
}

l = int(input().strip())
color_output = next((color for color, (lb, ub) in w.items() if lb <= l <= ub), "")

print(color_output)
