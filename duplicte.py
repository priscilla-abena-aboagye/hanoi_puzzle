number_of_disks = 5

A = list(range(number_of_disks, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n > 0:
    # move n - 1 disks from source to auxiliary, so they are out of the way
        move(n-1, source, target, auxiliary)
        
        # move the nth disk from source to target
        target.append(source.pop())

        # display our progress
        print(A,B,C, "\n")

        # move the n - 1 disks that we left on auxiliary onto target
        move(n-1, auxiliary, source, target)

    

# initiate call from source A to target C with auxiliary B

move(number_of_disks, "A", "B", "C")