import ctypes
from time import time


class DynamicArray:

    def __init__(self, type, inc_size=0):
        self.n = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)
        self.type = type
        self.increment = inc_size

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0 <= item < self.n:
            raise IndexError('invalid index')
        return self.array[item]

    def append(self, item):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.n] = item
        self.n += 1

    def append_incremental(self, item):
        if self.n == self.capacity:
            self.resize(self.capacity + self.increment)
        self.array[self.n] = item
        self.n += 1

    def resize(self, c):
        temp_array = self.make_array(c)
        for k in range(self.n):
            temp_array[k] = self.array[k]
        self.array = temp_array
        self.capacity = c

    def make_array(self, c):
        return (c*ctypes.py_object)()

def compute_average(data, n):
    start_time = time()
    if data.type == 'double':
        for k in range(n):
            data.append(None)
    elif data.type == 'incrememt':
        for k in range(n):
            data.append_incremental(None)
    return time() - start_time

array_size = 100000000
increment_size = 10000000
doubling_array = DynamicArray('double')
incremental_array = DynamicArray('incrememt',increment_size)

print('compuing start with number of calls',array_size)
double_result = compute_average(doubling_array,array_size)
print('doubling method finished in','%.6f' % double_result,'seconds with average','%.6f' % (double_result/array_size))
increment_result = compute_average(incremental_array,array_size)
print('incremental method finished in','%.6f' % increment_result,'seconds with average','%.6f' % (increment_result/array_size),'and increment size is',increment_size)

