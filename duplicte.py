number_of_disks = 3

rods = {
    "A": list(range(number_of_disks, 0, -1)),
    "B": [],
    "C": []
}


def move(n, source, auxiliary, target):
    if n > 0:
    # move n - 1 disks from source to auxiliary, so they are out of the way
        move(n-1, source, auxiliary, target)

 # display starting configuration
        print(rods, "\n")

    

# initiate call from source A to target C with auxiliary B

move(number_of_disks, "A", "B", "C")