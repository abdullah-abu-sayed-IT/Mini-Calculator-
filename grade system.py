def check_grade():
    print("--- Grade Calculator ---")
    try:
        marks = float(input("Tomar marks koto peyecho? "))
        
        if marks >= 80:
            print("Wah! Tumi A+ peyecho. Shabaash!")
        elif marks >= 70:
            print("Khub bhalo, tumi A peyecho.")
        elif marks >= 60:
            print("Bhaloi hoyeche, tumi A- peyecho.")
        elif marks >= 50:
            print("Tumi B peyecho. Arektu chesta koro!")
        elif marks >= 40:
            print("Tumi C peyecho.")
        elif marks >= 33:
            print("Tumi D peyecho. Pass korecho konomote.")
        else:
            print("Oshobdhonota! Tumi fail korecho. Mon kharap korbe na, porer bar bhalo hobe.")
    except ValueError:
        print("Areh! Number likho, kono kotha noy.")

check_grade()
