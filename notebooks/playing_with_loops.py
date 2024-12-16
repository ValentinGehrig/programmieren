def draw_christmas_tree(height):
   
    for i in range(height):
        spaces = " " * (height - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

    for _ in range(2):
        spaces = " " * (height - 2)
        print(spaces + "###")


