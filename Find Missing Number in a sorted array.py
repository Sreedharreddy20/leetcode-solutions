def missing_num(arr, n):
    low = 0
    high = n-1
    if high == -1:
        return -1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid + 1:
            if low == high:
                return -1
            else:
                low = mid + 1
            
        elif arr[mid] != mid + 1:
            high = mid - 1

    return low + 1
    

def main():
    arr = [1,2,3,4,6,7,8]
    n = 7
    print(missing_num(arr,n))

if __name__ == "__main__" :
    main()
        
        
