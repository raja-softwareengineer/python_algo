from re import A


def selection_sort(arr):
    spot_marker = 0
    while spot_marker < len(arr):
        
        for num in range(spot_marker,len(arr)):
            if arr[num] < arr[spot_marker]:
                #print("swap candidate found")
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
                #print(arr)
        spot_marker += 1
        print("iteration: " + str(arr))    

     


l = [6,8,1,4,10,22,3,2,8,5,0]
print("initial array")
print(l)
selection_sort(l)