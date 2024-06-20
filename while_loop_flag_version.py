def get_starting_number():
    bottles = input("Enter bottles: ")
    while not bottles.isnumeric() or int(bottles) < 1:
        bottles = input("Enter bottles: ")
    return int(bottles) 

def sing(bottles):
    i = bottles
    continue_to_sing = True
    while continue_to_sing:
        bottles_minus_one = i - 1
        if i == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down, pass it around, 1 bottle of beer on the wall.\n")
        elif i == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer\nTake it down, pass it around, no more bottles of beer on the wall!\n")
        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down, pass it around, {bottles_minus_one} bottles of beer on the wall.\n")
        i = i - 1
        if i > 0:
            continue_to_sing = True
        else:
            continue_to_sing = False
