from args import getArgsDict, getArgsDictFromList


def test_getArgsDict():
    args = "-l -p 8080 -d /usr/logs"

    assert len(getArgsDict(args)) is 3
    #assert getArgsDict(args)[0] == ["l"]
    #assert len(getArgsDict(args)[1]) == 2


def test_getArgsDictFromList():
    argsList = ["l", "p 8080", "d /usr/logs"]

    assert len(getArgsDictFromList(argsList)) is 3
    assert getArgsDictFromList(argsList) is {
        'd': '/usr/logs', 'l': True, 'p': '8080'}
