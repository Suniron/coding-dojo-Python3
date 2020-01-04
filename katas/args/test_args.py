from args import getArgsDictFromList, getDefaultValue


def test_getArgsDictFromList():
    argsList = ['-l', '-p', '8080', '-d', '/usr/logs']
    # Check length
    assert len(getArgsDictFromList(argsList)) is 3
    assert len(getArgsDictFromList(
        ['-l', '-p', '8080', '-d', '/usr/logs/my-logs'])) is 3
    assert len(getArgsDictFromList(['-l', '-p', '-8080'])) is 2
    # Check returned type
    assert type(getArgsDictFromList(argsList)) is dict
    # Check element types
    assert type(getArgsDictFromList(argsList)["l"]) is bool
    assert type(getArgsDictFromList(argsList)["p"]) is int
    assert type(getArgsDictFromList(argsList)["d"]) is str
    # Check default values
    assert getArgsDictFromList(["-p"])["p"] is 0
    assert getArgsDictFromList(["-d"])["d"] is ""


def test_getDefautValue():
    # Check default value
    assert getDefaultValue("l") is True
    assert getDefaultValue("p") is 0
    assert getDefaultValue("d") is ""
    # Check with -
    assert getDefaultValue("-p") is 0
    # Check error with unknow flag
    assert getDefaultValue("0") is "error"
