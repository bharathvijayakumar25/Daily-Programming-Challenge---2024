def a(height):
    units = 0
    n = len(height)
    for i in range(1, n - 1):
        left_max = max(height[:i]) if i > 0 else 0
        right_max = max(height[i+1:]) if i >0 else 0
        water_at_i = min(left_max, right_max) - height[i]
        if water_at_i > 0:
            units += water_at_i
    return units
height = input("Height[]: ").strip()
height = [int(x) for x in height.split(",")]
print(f"Output: {a(height)}")
