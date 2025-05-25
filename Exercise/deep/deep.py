print("What is the Answer to the Great Question of Life, the Universe, and Everything?")
str = input()

ans = str.lower().replace(" ", "").replace("-", "")

if ans == "42" or ans == "fortytwo":
    print("Yes")
else:
    print("No")