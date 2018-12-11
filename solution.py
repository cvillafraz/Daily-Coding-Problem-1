def check_sum(arr,K):
    check=False
    for i in range(0,len(arr)):
        if arr[i] == K:
            check=True
            break
        else:
            for j in reversed(range(i+1,len(arr))):
                if (arr[i] + arr[j] == K):
                    check=True
                    break
            if check:
                break
    return check
print(check_sum([11,15,3,7],10))
