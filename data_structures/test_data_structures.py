from time import clock

if __name__ == '__main__':
    def test_arraylist():
        startTime = clock()
        al = arrayList()
        al.insert(10)
        al.insert(20)
        al.insert(30)
        print(al.array)
        endTime = clock()

        print('Time elapsed:', endTime-startTime)



    # [10, 9, 7, 6, 3, 6, 5, 4]
    h = Max_Heap()
    h.insert(4)
    h.insert(5)
    h.insert(6)
    h.insert(6)
    h.insert(3)
    h.insert(7)
    h.insert(9)
    h.insert(10)
    print(h.heap)
    print(h.extract())
    print(h.heap)