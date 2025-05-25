import random
with open("textpile/test.txt", "a+", encoding="utf-8") as testfile:
    testfile.seek(0)
    li=testfile.readlines()
    todo=input("무엇을 할까요?")
    testfile.write(" \n")
    testfile.write("===============\n")

    if todo=="셔플" or todo=="shuffle" : #셔플
        random.shuffle(li)
        for i in li:
            testfile.write(i)


    if todo=="korean" : #한국어만
        for i in li:
            for j in i.strip():
                if not ('a'<= j <= 'z' or 'A'<= j <= 'Z') and not j==" ":
                    testfile.write(j)

                else:
                    pass
    testfile.write("\n")
    testfile.write("===============\n")