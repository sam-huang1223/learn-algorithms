class arrayList:
    def __init__(self):
        ''' a dynamically resizing array that captures benefits arrays while offering flexibility in size '''
        self.array = np.zeros(shape=1, dtype=int)
        self.counter = 0

    def insert(self, value):
        ''' if array is full, creates new array with double the size and copies elements over
        running time is described using amortized time:
            If array full, insertion will take O(n) time due to having to copy n elements
            If not, insertion will take O(1) time
        Amortized running time over x insertions = 1+2+4+8+16+32+64+...+x
            Read from right to left, this series starts at x and halves until it reaches 1
        Amortized running time over x insertions = x+x/2+x/4+x/8+x/16+...1
        Amortized running time over x insertions = 2x
        Therefore, x insertions take O(2x) time, amortized running time for each insertion is O(1)
        '''
        if self.counter >= len(self.array):
            new_arr = np.zeros(shape=len(self.array)*2, dtype=int)
            for i in range(len(self.array)):
                new_arr[i] = self.array[i]
            self.array = new_arr

        self.array[self.counter] = value
        self.counter += 1