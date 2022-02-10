class MinimizationMethod:

    def __init__(self, verbose: bool):
        self.verbose = verbose

    def minimize(self, sequence: list):
        pass

    def vprint(self, msg: str):
        if self.verbose:
            print(msg)