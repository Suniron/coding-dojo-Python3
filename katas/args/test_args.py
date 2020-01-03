from args import getArgsDict


def test_getArgsDict():
    assert len(getArgsDict("-l -p 8080 -d /usr/logs")) == 3
