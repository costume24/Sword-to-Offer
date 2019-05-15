from exeTime import exeTime


@exeTime
def replaceSpace(s):
    res = ""
    for i in range(len(s)):
        if s[i] != " ":
            res += s[i]
        else:
            res += "%20"
    return res


if __name__ == "__main__":
    s = "We Are Happy"
    print(replaceSpace(s))
