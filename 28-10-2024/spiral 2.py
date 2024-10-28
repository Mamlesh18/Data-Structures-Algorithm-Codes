def spiral(n):
    result = [[0] * n for _ in range(n)]
    left = 0
    right = n - 1
    top = 0
    bottom = n - 1
    i = 1
    while left <= right and top<=bottom:
            for j in range(left,right+1):
                result[top][j] = i
                i+=1
            top+=1
            for j in range(top,bottom+1):
                result[j][right] = i
                i+=1
            right-=1

            for j in range(right,left-1,-1):
                result[bottom][j] = i
                i+=1
            bottom-=1

            for j in range(bottom,top-1,-1):
                result[j][left] = i
                i+=1
            left+=1

    return result
n = 3
print(spiral(n))
