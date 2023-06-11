class SnapshotArray:

    def __init__(self, length: int):
        self.record = collections.defaultdict(dict)
        self.id = 0

    def set(self, index: int, val: int) -> None:
        if index not in self.record:
            self.record[index] = {}
            self.record[index][0] = 0
        self.record[index][self.id] = val

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.record[index]:
            return self.record[index][snap_id]
        else:
            avail = [x for x in self.record[index]]
            i = bisect.bisect_left(avail, snap_id)
            if i > 0:
                return self.record[index][avail[i - 1]]
            return 0



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
