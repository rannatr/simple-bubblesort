def bubble(list):
    indexing_length = len(list)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0,indexing_length):
            if list[i]>list[i+1]:
                sorted = False
                list[i],list[i+1]=list[i+1],list[i]

    return list

print(bubble([4,2,5,9,-1,99]))

