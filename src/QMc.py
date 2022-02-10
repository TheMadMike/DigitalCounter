from MM import MinimizationMethod

class QuineMcCluskey(MinimizationMethod):

    def __init__(self, verbose = False):
        super().__init__(verbose)

    def minimize(self, sequence: list):
        self.functions = []
        
        for i in range(0, len(sequence[0])):
            self.__minimze_for(sequence, i)
        
        return self.functions


    def __count_ones(self, minterm):
        count = 0
        for bit in minterm:
            if bit == '1':
                count += 1
        
        return count

    def __minimze_for(self, sequence: list, index: int):
        minterms = []
        for i in range(0, len(sequence)):
            if sequence[(i+1) % len(sequence)][index] == '1':
                minterms.append(sequence[i])
        
        
        super().vprint(f"Minterms for D{index}")
        super().vprint(minterms)

        n_groups = {}
        for i in range(0, len(minterms)):
            n_ones = self.__count_ones(minterms[i])
            if not (n_ones in n_groups):
                n_groups[n_ones] = [i]
            else:
                n_groups[n_ones].append(i)

        super().vprint("1st grouping:")
        super().vprint(n_groups)

        merges = self.__merge_minterms(minterms, n_groups)

        while merges > 0:
            merges = self.__merge_minterms(minterms, n_groups)

        self.__remove_empty_groupings(n_groups)

        self.functions.append(self.__get_minimized_function(n_groups, minterms))

        super().vprint("\n")

    
    def __minterm_diff(self, first: str, second: str):
        diff = 0
        index = -1
        for i in range(0, len(first)):
            if first[i] != second[i]:
                diff += 1
                index = i
        return (diff, index)

    def __merge_minterms(self, minterms: list, n_groups: dict):
        merges = 0
        for key in n_groups.keys():
            if (key+1) in n_groups:
                for n in n_groups[key]:
                    for m in n_groups[key+1]:
                        d = self.__minterm_diff(minterms[n], minterms[m])
                        if d[0] == 1:
                            index = d[1]
                            n_groups[key+1].remove(m)
                            n_groups[key].append(m)
                            minterms[n] = minterms[n][:index] + '_' + minterms[n][index+1:]
                            minterms[m] = minterms[m][:index] + '_' + minterms[m][index+1:]
                            merges += 1

        if merges > 0:
            super().vprint("next grouping:")
            super().vprint(n_groups)
            super().vprint(minterms)
        else:
            super().vprint("-- grouping stop --")


        return merges
    
    def __remove_empty_groupings(self, n_groups: dict):
        super().vprint("removing empty groupings")
        to_delete = []
        for key in n_groups.keys():
            if len(n_groups[key]) == 0:
                to_delete.append(key)

        for key in to_delete:
            del n_groups[key]
                        
        super().vprint(n_groups)
        super().vprint("----")

    def __get_minimized_function(self, n_groups: dict, minterms: list):
        raw_expression = []

        if len(n_groups) <= 1:
            for n in n_groups.keys():
                raw_expression.append(minterms[n_groups[n][0]])

        else:
            for n in n_groups.keys():
                for m in n_groups.keys():
                    if n == m:
                        continue
                    for i in n_groups[n]:
                        if not (i in n_groups[m]):
                            raw_expression.append(minterms[n_groups[n][0]])
                            break
        
        super().vprint(f"raw: {raw_expression}")
    
        return self.__parse_raw_expression(raw_expression)


    def __parse_raw_expression(self, raw_expression: list):
        parsed = ""
        for s in raw_expression:
            parsed += " + "
            for i in range(0, len(s)):
                if s[i] == '1':
                    parsed += f"Q{i}"
                if s[i] == '0':
                    parsed += f"(~Q{i})"       

        return parsed[3:]


