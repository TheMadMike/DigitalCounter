from MM import MinimizationMethod
from QMc import QuineMcCluskey
from ArgParser import ArgParser


class Minimizer:

    method: MinimizationMethod

    def __init__(self, sequence: list, arg_parser: ArgParser):
        self.sequence = sequence
        self.args = arg_parser
        self.method = self.__get_method_by_name()


    def run(self):
        functions = self.method.minimize(self.sequence)
        for i in range(0, len(functions)):
            print(f"D{i} = {functions[i]}")


    def __get_method_by_name(self):
        if self.args.minimization_method == "QMc":
            return QuineMcCluskey(self.args.verbose)
        elif self.args.minimization_method == "KMap":
            raise RuntimeError("KMap is not supported yet")
        else:
            raise RuntimeError(f"Unknown minimization method: {self.args.minimization_method}")

