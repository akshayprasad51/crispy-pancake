import time
import random

def get_random_list(entries):
    return random.sample(range(1, 10000), entries)

def bubble_sort(unsorted_list):
    start_time = time.time()
    for p in range(len(unsorted_list)-1,0,-1):
        for i in range(p):
            if unsorted_list[i]>unsorted_list[i+1]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i+1]
                unsorted_list[i+1] = temp
    end_time = time.time()
    return unsorted_list, end_time - start_time

def selection_sort(unsorted_list):
    start_time = time.time()
    for i in range(len(unsorted_list)):
        m=i
        for j in range(i+1,len(unsorted_list)):
            if unsorted_list[j]<unsorted_list[m]:
                m=j
        unsorted_list[i],unsorted_list[m]=unsorted_list[m],unsorted_list[i]
    end_time = time.time()
    return unsorted_list, end_time - start_time

def insertionSort(unsorted_list):
    start_time = time.time()
    for i in range(1,len(unsorted_list)):
        currentvalue = unsorted_list[i]
        position = i

        while position>0 and unsorted_list[position-1]>currentvalue:
            unsorted_list[position]=unsorted_list[position-1]
            position = position-1
        unsorted_list[position]=currentvalue
    end_time = time.time()
    return unsorted_list, end_time - start_time

if __name__ == '__main__':
    # fully random
    l1 = get_random_list(5000)

    # fully sorted - descending
    # l1 = range(5000, 1, -1)

    # partially sorted
    # l1 = range(1, 2500) + get_random_list(2500)

    # fully sorted array
    # l1 = range(1, 5000)

    # all equal elements
    # l1 = 5000 * [10]

    l2 = list(l1)
    l3 = list(l1)
    l4 = list(l1)



    print 'bubble sort - time taken {0}'.format(bubble_sort(l1)[1])
    print 'selection sort - time taken {0}'.format(selection_sort(l2)[1])
    print 'insertion sort - time taken {0}'.format(insertionSort(l3)[1])
