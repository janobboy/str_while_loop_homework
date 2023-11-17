def main(s):
    k = 0
    i = 0
    while i < len(s):
        if s[i].isdigit():
            k += 1
        i += 1
    return k

print(main("python 2022"))
print(main("e324xE"))