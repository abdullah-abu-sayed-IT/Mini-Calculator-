print("সিম্পল ক্যালকুলেটর")
print("অপারেশন: + - * /\n")

try:
    num1 = float(input("প্রথম সংখ্যা দাও: "))
    op   = input("কি করতে চাও? (+ - * /): ")
    num2 = float(input("দ্বিতীয় সংখ্যা দাও: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("দুঃখিত! শূন্য দিয়ে ভাগ করা যায় না 😅")
        else:
            print(num1 / num2)
    else:
        print("ভুল অপারেশন! শুধু +, -, *, / চলে")

except ValueError:
    print("দয়া করে শুধু সংখ্যা দাও!")
