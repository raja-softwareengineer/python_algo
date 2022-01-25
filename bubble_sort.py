from re import A


def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened =  False
        print("bubble sort status: " +  str(arr))

        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                #print("swap happened")
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]
                #print(arr)

l = [6,8,1,4,10,22,3,2,8,5,0]
#print("initial array")
#print(l)
bubble_sort(l)
 
