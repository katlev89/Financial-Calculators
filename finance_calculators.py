import math

# Printing out the initial sentence:
print("investment   - to calculate the amount of interest you will earn on your investment")
print("bond         - to calculate the amount you will have to pay on a home loan")

# Getting the user's input:
users_input = (input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()

# If user's input is 'investment', getting the requested information to calculate the interest:
if users_input == "investment":
    P = float(input("Please put the amount of money you wish to deposit: "))
    r = float(input("Please enter the interest rate: ")) / 100
    t = float(input("Please enter the number of years you plan to invest: "))
    interest = (input("Please enter either 'simple' or 'compound' to calculate the desirable type of interest: ")).lower()
    
    # If user chooses simple interest, calculating and printing out the requested information:    
    if interest == "simple":
        A = P *(1 + r*t)
        print("The total ammount once the simple interest has been applied is: ", A)

    # If user chooses compound interest, calculating and printing out the total ammount once the compound interest has been applied:
    elif interest == "compound":
        A = P * math.pow((1+r),t)
        print("The total ammount once the compound interest has been applied is: ", A)

# If user's choice is 'bond', getting the requested information to caltulate the monthly repayment amount: 
elif users_input == "bond":
    v = float(input("Please enter the present value of the house: "))
    i_r = float(input("Please enter the current interest rate: ")) / 100
    n = float(input("Please enter the number of months you plan to repay the bond: "))
    repayment = (i_r * v)/(1 - (1 + i_r)**(-n))
    print("Monthly repayment will be: ", repayment)
   
else:
     print("Invalid input. Please enter either 'investment' or 'bond'.")