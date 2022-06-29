Height=float(input("Enter your height in centimeters: "))

Weight=float(input(" your Weight in Kg: "))

Height = Height/100

def bmi_calc(Height, Weight):

    BMI=Weight/(Height*Height)

    print("your Body Mass Index is: ",BMI)

    if(BMI>0):

        if(BMI<=16):

            print("you are severely underweight")

        elif(BMI<=18.5):

            print("you are underweight")

        elif(BMI<=25):

            print("you are Healthy")

        elif(BMI<=30):

            print("you are overweight")

        else: print("you are severely overweight")

    else:("enter valid details")

body_mass_index=bmi_calc(Height, Weight)
