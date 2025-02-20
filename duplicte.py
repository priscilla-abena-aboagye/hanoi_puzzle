number_of_disks = 3
number_of_moves = 2 ** number_of_disks - 1

rods = {
    "A": list(range(number_of_disks, 0, -1)),
    "B": [],
    "C": []
}

def make_allowed_move(rod1, rod2):
    forward = False
    if not rods[rod2]:
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        forward = True
    if forward:
        print(f"Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
        rods[rod2].append(rods[rod1].pop())
    else:
        print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
        rods[rod1].append(rods[rod2].pop())

    # display the progress

    print(rods, "\n")

def move(n, source, auxiliary, target):

    # display starting configuration
    print(rods, "\n")

    
    

# initiate call from source A to target C with auxiliary B

move(number_of_disks, "A", "B", "C")