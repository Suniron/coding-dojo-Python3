

def getArgsDictFromList(argsList):
    "Return a Dict of [arg: [parameters]] or [arg: True]"

    argsDict = {}

    for arg in argsList:
        argSplit = arg.split()

        if len(argSplit) == 1:
            argsDict[argSplit[0]] = True
        else:
            argsDict[argSplit[0]] = argSplit[1]
    print(argsDict)
    return argsDict


def getArgsDict(argsString):
    "Return a Dict of key/values of gived args (as a string)"
    args = argsString[1:].split(' -')

    return args


if __name__ == "__main__":
    pass
