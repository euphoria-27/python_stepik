n, k = int(input()), int(input())
arr = [1 for i in range(n)]
counter = 0
point_index = 0
while(sum(arr) != 1):
    if(arr[point_index] == 1):
        
        counter += 1
        
        if(counter % k == 0):
            arr[point_index] = 0
        point_index += 1
        if(point_index == n): point_index = 0
    else:
        point_index += 1
        if(point_index == n): point_index = 0
        
print(arr.index(1) + 1)
