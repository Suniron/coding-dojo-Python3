import sys

parameters = {
    "l": {"description": "Logging", "type": "boolean", "default_value": True},
    "p": {"description": "Port", "type": "integer", "default_value": 0},
    "d": {"description": "Directory", "type": "string", "default_value": ""}
}


def getDefaultValue(flag):
    "Return defaut value for flag"

    # Remove - if here
    if flag[0] == '-':
        flag = flag[1:]

    if flag in parameters.keys():
        return parameters[flag]['default_value']

    else:
        # TODO: raise exeption ?
        print("Error:", flag, "is unknow flag.")
        return "error"


def getArgsDictFromList(argsList):
    "Return a Dict of [arg: [parameters]] or [arg: True]. TODO: Check if flag exist in parameters"

    argsDict = {}

    flag = None

    for arg in argsList:
        # If it's flag or negative number:
        if arg[0] is '-':
            arg = arg[1:]
            # Check if number and if flag is already set
            if arg.isdigit() and flag:
                argsDict[flag] = arg
                flag = None  # Reinit flag

            else:
                if flag is None:
                    if parameters[arg]["type"] == "boolean":
                        argsDict[arg] = True
                    else:
                        flag = arg
                        if len(argsList) == 1:
                            argsDict[flag] = getDefaultValue(flag)

                else:
                    # Get and put default value last flag
                    argsDict[flag] = getDefaultValue(flag)
                    # Set next flag:
                    flag = arg

        else:
            if flag is None:  # If no flag for this
                print("Error: no flag for '"+arg+"'!")
            else:
                flagType = parameters[flag]["type"]

                # Check type:
                if flagType is "integer":
                    argsDict[flag] = int(arg)

                elif flagType is "string":
                    argsDict[flag] = arg

    return argsDict


def getSchema(args):
    "Return a description of settings used"
    # TODO: Continue here

    return


if __name__ == "__main__":
    # Use case:
    # call this program with "python args.py -l -p 8080 -d /usr/logs"
    args = sys.argv[1:]

    print(getArgsDictFromList(args))
