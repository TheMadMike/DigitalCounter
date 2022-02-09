import sys

class ArgParser:


    verbose: bool = False


    def __init__(self, argv):
        self.minimization_method = "QMc"
        self.__parse(argv)


    def __parse(self, argv):
        if len(argv) < 2:
            return

        for i in range(1, len(argv)):
            arg = argv[i]
            if arg.startswith("-m="):
                self.minimization_method = arg.split("=")[1]
            elif arg == "--verbose" or arg == "-V":
                self.verbose = True
            elif arg == "-h" or arg == "--help":
                self.__print_help()
                sys.exit(0)
            elif arg == "-v" or arg == "--version":
                self.__print_version()
                sys.exit(0)


    def __print_help(self):
        print(self.HELP_STR)
    

    def __print_version(self):
        print(self.VERSION_MESSAGE)


    HELP_STR: str = """Args:
    -m=<minimization method> # [QMc/KMap] (Quine-McCluskey / Karnaugh maps)
    -h --help # print help 
    -V --verbose # print minimization steps
    -v --version # print program's version
    """


    VERSION_STR: str = "1.0.0"


    VERSION_MESSAGE: str = f"""
Synchronous digital counter logic minimalization script
Copyright 2022 by Michał Gibas [@TheMadMike]
Version {VERSION_STR}
"""
