class FileReader:
    def __init__(self, filepath):
        self.fp = open(filepath)
        self.lines = []
        self.done = False

    def __iter__(self):
        if self.done:
            return iter(self.lines)
        return self

    def __next__(self):
        line = self.fp.readline()
        if not line:
            self.done = True
            self.fp.close()
            return StopIteration
        self.lines.append(line[:-1])
        return line[:-1]
