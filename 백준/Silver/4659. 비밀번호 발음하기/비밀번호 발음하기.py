word = ""
last = ""
gather = ['a','e','i','o','u']
while(True):
    w = input()
    word = list(w)
    if w == "end":
        break
    if any(x in word for x in gather):
        flag = 0
        preword = ""
        count = 0
        mcount = 0
        for i in word:
            if i != 'e' and i != 'o' and i == preword:
                print("<{0}> is not acceptable.".format(''.join(word)))
                flag = 1
                break
            if i in gather:
                count += 1
                mcount = 0
                if count == 3:
                    print("<{0}> is not acceptable.".format(''.join(word)))
                    flag = 1
                    break
                else:
                    preword = i
            else:
                mcount -= 1
                count = 0
                if mcount == -3:
                    print("<{0}> is not acceptable.".format(''.join(word)))
                    flag = 1
                    break
                else:
                    preword = i
        if flag == 0: print("<{0}> is acceptable.".format(''.join(word)))
        continue
    else:
        print("<{0}> is not acceptable.".format(''.join(word)))
        
