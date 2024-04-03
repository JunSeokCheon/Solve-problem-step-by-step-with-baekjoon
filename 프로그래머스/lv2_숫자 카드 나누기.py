def gcd_one(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def gcd_N(arr):
    gcd = arr[0]
    for item in arr:
        gcd = gcd_one(gcd, item)
    return gcd

def solution(arrayA, arrayB):
    arrayA_gcd = gcd_N(arrayA)
    arrayB_gcd = gcd_N(arrayB)
    
    for num in arrayB:
        if num%arrayA_gcd==0:
            arrayA_gcd = 0
            break
    
    for num in arrayA:
        if num%arrayB_gcd==0:
            arrayB_gcd = 0
            break
    
    return max(arrayA_gcd,arrayB_gcd) if max(arrayA_gcd,arrayB_gcd) != 0 else 0