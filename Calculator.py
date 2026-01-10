print("ক্যালকুলেটর")
print("অপারেশন: +, -, *, /")
print("(বের হতে চাইলে q লিখো)\n")

while True:
    n1 = input("প্রথম সংখ্যা: ")
    
    if n1 == "q":
        print("বাই বাই!")
        break
    
    try:
        n1 = float(n1)
    except:
        print("দয়া করে সঠিক সংখ্যা দিন!")
        print("---------------")
        continue
    
    op = input("কি করবো? (+ - * /): ")
    
    try:
        n2 = float(input("দ্বিতীয় সংখ্যা: "))
    except:
        print("দয়া করে সঠিক সংখ্যা দিন!")
        print("---------------")
        continue
    
    if op == "+":
        print(n1 + n2)
    elif op == "-":
        print(n1 - n2)
    elif op == "*" or op == "x" or op == "X":
        print(n1 * n2)
    elif op == "/":
        if n2 == 0:
            print("০ দিয়ে ভাগ করা যায় না!")
        else:
            print(n1 / n2)
    else:
        print("ভুল অপারেটর! শুধু +, -, *, / ব্যবহার করুন")
    
    print("---------------\n")
