def reverse(x):
    result,x_remain = 0,abs(x)
    while x_remain:
        result = result *10 + x_remain%10
        x_remain //= 10
    print( - result if x <0 else result)

reverse(- 231)
reverse(656)