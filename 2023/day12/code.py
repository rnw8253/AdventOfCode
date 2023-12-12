

class ConditionRecords:

    def __init__(self, fileName):
        self.records = []
        for record in open(fileName).read().splitlines():
            self.records.append(Record(record))

    def calcArrangements(self,val):
        count = 0
        for record in self.records:
            count += record.arrangements(record.cfgxX(val),record.valuesxX(val))
        return count

class Record:
    cache = {}
    def __init__(self, record):
        self.cfg, values = record.split()
        self.values = tuple(map(int, values.split(",")))

    def cfgxX(self,val):
        return "?".join([self.cfg]*val)

    def valuesxX(self,val):
        return self.values*val

    def arrangements(self, cfg, values):
        # No more configurations or values left
        if cfg == "":
            # e.g. "" (,)
            # e.g. "" (1,)
            return 1 if len(values) == 0 else 0
        if len(values) == 0:
            # e.g. "#" (,)
            # e.g. "" (,)
            return 0 if "#" in cfg else 1

        # Check to see if this path has already been handled
        key = (cfg, values)
        if key in Record.cache:
            return Record.cache[key]

        # Else continue
        result = 0
        # Handle "." or "?" == "."
        if cfg[0] in ".?":
            # e.g. ".###" (2,3)
            # e.g. "?##." (2,3)
            result += self.arrangements(cfg[1:], values)
        # Handle "#" or "?" == "#"
        if cfg[0] in "#?":
            # e.g. ".?##" (3) not "##" (3)
            # e.g. "####" (4) not "#.##" (4)
            # e.g. "###" (3)
            # e.g. "##" (2) not "#." =
            if values[0] <= len(cfg) and "." not in cfg[:values[0]] and (values[0] == len(cfg) or cfg[values[0]] != "#"):
                result += self.arrangements(cfg[values[0] + 1:], values[1:])

        Record.cache[key] = result
        return result


R = ConditionRecords("test.dat")
print(R.calcArrangements(5))
R = ConditionRecords("data.dat")
print(R.calcArrangements(5))
