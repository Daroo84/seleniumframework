

items = ["one", "two", "three"]

for item in items:
    with open("{}hello_world.txt".format(item), "w") as f:
        f.write("This is my first line of code")
        f.write("\nThis is my second line of code with {} the first item in my list".format(item))
        f.write("\nAnd this is my last line of code")