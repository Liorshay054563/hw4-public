# start

slices: float = int(input('who many pizza slices:'))
slices_each = (slices // 4)
slices_left = (slices % 4)
print(f"{slices_each} slices per one and {slices_left} sliced left")

# end

# start

friends: int = int(input('how many friends come:'))
slices: int = int(input('how many slices order:'))

slices_each = (slices // friends)
slices_left = (slices % friends)

print(f"each friend eat {slices_each} and they left {slices_left}")

# end
