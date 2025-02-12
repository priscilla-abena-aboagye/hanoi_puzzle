number_of_disks = 3
number_of_moves = 2 ** number_of_disks - 1

rods = {
    "A": list(range(number_of_disks, 0, -1)),
    "B": [],
    "C": []
}

def move(n, source, auxiliary, target):
    print(rods)


move(number_of_disks, "A", "B", "C")