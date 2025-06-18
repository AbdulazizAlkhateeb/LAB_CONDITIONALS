# '''
# ### write a program that Calculates the BMI (body mass index) of the user:
# - Ask the user to provide his wieght.
# - Ask the user to provide hi height.
# - print the BMI for the user.
# - using conditionals tell the user that either :
# - - You are overwieght you need to work out more and watch your diet.
# - - You are fit & healthy.
# - - You are underweight. Watch your health.
# '''


print("To Calculates the BMI (body mass index)")

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height meters:"))

bmi = weight / (height * height)
print(f"your BMI:{bmi}")

if bmi >= 30:
    print("You are overwieght you need to work out more and watch your diet")
elif bmi >=18.5:
    print("You are fit & healthy")

else:
    print("You are underweight. Watch your health")


