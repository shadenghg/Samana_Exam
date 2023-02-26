import string


def count_punctuation(fileName):
    cnt = 0
    with open("./" + fileName, "w+") as file:
        file.write("Hey, Alex !, How are you? Nice exam :)")
        file.seek(0)
        data = file.read()
        for char in data:
            if char in string.punctuation:
                cnt += 1
    return cnt


print(count_punctuation("Q2.txt"))
