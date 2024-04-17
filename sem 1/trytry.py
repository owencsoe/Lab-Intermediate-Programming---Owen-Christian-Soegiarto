word = "computational"
for letter1 in word:
    count=0
    for letter2 in word:
        if letter1==letter2:
            count=count+1

    if count>1:
        print(letter1,":",count)
