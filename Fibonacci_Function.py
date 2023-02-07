print("Fibonacci series for 16:", )

num0 = 0
num1 = 1


def function(num0, num1):
    for num in range(16):
        print(num0, end = ",")
        result = num0 + num1
        num0 = num1
        num1 = result
   
    return result


function(num0, num1)


