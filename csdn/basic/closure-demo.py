def balance(weight, price):
    return (weight - 0.1) * price
a = balance(10.1, 4)
print(a)
'''
闭包：
    1. 内置函数
    2. 内置函数使用外部函数变量
    3. 外函数返回内函数
'''
def cost(price):
    def balance(weight):
        return (weight - 0.1) * price
    return balance
b = cost(4)
print(b(5.1))
'''
计算数N次方
'''
def power(n):
    def calculate(number):
        return number ** n
    return calculate
ten = power(4)
print(ten(4))