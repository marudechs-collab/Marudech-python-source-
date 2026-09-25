try:
    num1 = float(input("กรอกตัวเลขตัวที่ 1: "))
    num2 = float(input("กรอกตัวเลขตัวที่ 2: "))
    operator = input("เครื่องหมาย (+,-,*,/): ")

    result = 0
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("เครื่องหมาย + - * /เท่านั้น")

    print(f"{num1} {operator} {num2} = {result}")
except ValueError:
    print("กรอกตัวเลขไองั้ง")

except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")

else:
    print("ทำงานได้สมบูรณ์")

finally:
    print("จบการทำงาน")