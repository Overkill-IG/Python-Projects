while(True):
    weight = int(input("Input weight (in kg): "))
    height_mode = input("Enter mode of height (in cm or m): ")
    if "cm" in height_mode:
        height = float(input("Enter: "))
        bmi_cm = (weight/(height*height))*10000
        print(bmi_cm)
        exit = input("Do you want to exit the program? (Y or N):")
        if exit == 'Y':
            break
        elif exit == 'N':
            continue

    elif "m" in height_mode:
        height = float(input("Enter: "))
        bmi_m =  weight/(height*height)
        print(bmi_m)
        exit = input("Do you want to exit the program? (Y or N):")
        if exit == 'Y':
            break
        elif exit == 'N':
            continue
