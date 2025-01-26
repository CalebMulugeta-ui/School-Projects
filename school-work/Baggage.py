#COMP 1005/1405 Section [A] - Assignment [1] Program [1]
#Project Details
    #Name: Caleb Mulugeta
    #Student #: 101352144
    #Date Created: [Septemper 26th]

#Get users baggage weight
userWeight = float(input("Enter your baggage weight in kg here: "))

#prints the following message if users input weight is below 20kg
if userWeight <= 20.0:
    print("Flight Ticket Cost: $120")
    print("Baggage Charges: $0")
    print("Total: $120")

#Does the following if user input is larger than 20kg
if userWeight > 20.0:
    newWeight = userWeight - 20.0 #Gets extra weight
    extraCharge = newWeight * 1.80  #Calculates extra charge
    print("Flight Ticket Cost: $120")
    print(f"Baggage Chaerges: ${extraCharge}") 
    print(f"Total: ${120 + extraCharge}")