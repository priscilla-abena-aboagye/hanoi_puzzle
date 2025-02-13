number_of_disks = 3
number_of_moves = 2 ** number_of_disks - 1

rods = {
    "A": list(range(number_of_disks, 0, -1)),
    "B": [],
    "C": []
}

def move(n, source, auxiliary, target):
    # display starting configuration
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            print(f"Move {i + 1} allowed between {source} and {target}")
            forward = False
            if not rods[target]:
                forward = True
        elif remainder == 2:
            print(f"Move {i + 1} allowed between {source} and {auxiliary}")
        elif remainder == 0:
            print(f"'Move {i + 1} allowed between {auxiliary} and {target}'")
    print(rods)

# initiate call from source A to target C with auxiliary B
move(number_of_disks, "A", "B", "C")