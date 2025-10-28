def calculator():
    num1 = float(input("请输入第一个数字："))
    operator = input("请输入运算符（+、-、*、/）：")
    num2 = float(input("请输入第二个数字："))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = "无效的运算符"

    print(f"结果：{result}")

calculator()