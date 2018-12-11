def check_sum(arr,K):
    check=False
    ### Iterate through the arrey from left to rigth
    for i in range(0,len(arr)):
        ### Check if current element is equal to K
        if arr[i] == K:
            check=True
            break
        else:
            ### Iterate through the array from right to left
            for j in reversed(range(i+1,len(arr))):
                ### Sum each element to its next elements and compare to K
                if (arr[i] + arr[j] == K):
                    check=True
                    break
            if check:
                break
    return check
print(check_sum([11,15,3,7],10))
