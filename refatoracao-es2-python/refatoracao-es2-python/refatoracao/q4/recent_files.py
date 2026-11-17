class RecentFiles(list):

    def __init__(self, limit: int):
        super().__init__()
        self._limit = limit

    def add_file(self, path: str) -> None:
        if path in self:
            self.remove(path)
        self.insert(0, path)
        while len(self) > self._limit:
            self.pop()
