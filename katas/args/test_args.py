from args import getArgsDictFromList, getDefaultValue, getSchema


def test_getArgsDictFromList():
    argsList = ['-l', '-p', '8080', '-d', '/usr/logs']
    argsListWithoutValues = ['-l', '-p', '-d']
    # Check length
    assert len(getArgsDictFromList(argsList)) is 3
    assert len(getArgsDictFromList(
        ['-l', '-p', '8080', '-d', '/usr/logs/my-logs'])) is 3
    assert len(getArgsDictFromList(['-l', '-p', '-8080'])) is 2
    # Check returned type
    assert type(getArgsDictFromList(argsList)) is dict
    # Check element types
    assert type(getArgsDictFromList(argsList)["l"]) is dict
    assert type(getArgsDictFromList(argsList)["l"]) is dict
    assert type(getArgsDictFromList(argsList)["p"]['value']) is int
    assert type(getArgsDictFromList(argsList)["d"]['value']) is str
    # Check default values
    assert getArgsDictFromList(argsListWithoutValues)["l"]['value'] is True
    assert getArgsDictFromList(argsListWithoutValues)["p"]['value'] is 0
    assert getArgsDictFromList(["-d"])["d"]['value'] is ""
    # Check wrong flag
    assert type(getArgsDictFromList(argsList)["l"]) is dict


def test_getDefautValue():
    # Check default value
    assert getDefaultValue("l") is False
    assert getDefaultValue("p") is 0
    assert getDefaultValue("d") is ""
    # Check with -
    assert getDefaultValue("-p") is 0
    # Check error with unknow flag
    assert getDefaultValue("0") is "error"


def test_getSchema():
    args = ['-l', '-p', '8080', '-d', '/usr/logs']
    # Check type
    assert type(getSchema(args)) is str
    # Check wrong flag
    assert type(getSchema(['-t', '200'])) is str
    assert type(getSchema(['-t'])) is str
    assert type(getSchema(['bad'])) is str
