import sys


parameters = {
    "l": {"name": "Logging", "description": "Logging if it True", "type": "boolean", "default_value": False},
    "p": {"name": "Port", "description": "The port which application listen", "type": "integer", "default_value": 0},
    "d": {"name": "Directory", "description": "The directory used by application datas", "type": "string", "default_value": ""},
    "error": {"name": "Error", "description": "A flag is unknow", "type": "error", "default_value": "error"}
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
    "Return a Dict of [arg: [parameters]] or [arg: True]."

    argsDict = {}

    flag = None

    for arg in argsList:
        # If it's flag or negative number:
        if arg[0] is '-':
            arg = arg[1:]
            # If number it's a number and if flag is already set:
            if arg.isdigit() and flag:
                argsDict[flag] = {"value": arg}
                flag = None  # Reinit flag
            # If Unknow flag:
            elif arg not in parameters:
                # TODO: Continue here
                flag = "error"
            # If no flag:
            elif flag is None:
                if parameters[arg]["type"] == "boolean":
                    argsDict[arg] = {"value": True}
                else:
                    flag = arg
                    if arg == argsList[-1][1:]:
                        argsDict[flag] = {"value": getDefaultValue(flag)}
                        flag = None  # Reinit flag
            else:
                # Get and put default value last flag
                argsDict[flag] = {"value": getDefaultValue(flag)}
                # Set next flag:
                flag = arg
        elif parameters[flag]["type"] == 'error':
            # If isn't a flag or negative number:
            pass
        else:
            flagType = parameters[flag]["type"]

            # Check type:
            if flagType is "integer":
                if arg.isdigit():
                    argsDict[flag] = {"value": int(arg)}
                else:
                    argsDict[flag] = {"value": 0}
                flag = None  # Reinit flag

            elif flagType is "string":
                argsDict[flag] = {"value": str(arg)}
                flag = None  # Reinit flag

            else:
                argsDict[flag] = {"value": str(arg)}
                flag = None  # Reinit flag

    return argsDict


def getSchema(args):
    "Return a description of flag/args used"

    argsDescription = "\nYou give this flags and values:"
    argsDict = getArgsDictFromList(args)

    for arg in argsDict:
        # Name
        text = "\n-{}, {}".format(arg, parameters[arg]['name'])
        # Value
        text += ", value: {}".format(argsDict[arg]['value'])
        if argsDict[arg]['value'] == parameters[arg]['default_value']:
            text += " (default)"
        # Description
        text += " -> {}".format(parameters[arg]['description'])
        # End
        argsDescription += text

    return argsDescription


if __name__ == "__main__":
    # Use case:
    # call this program with "python args.py -l -p 8080 -d /usr/logs"
    args = sys.argv[1:]

    print(getSchema(args))
