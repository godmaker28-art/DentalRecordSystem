dr = ["[1]Mendoza", "[2]Mancion", "[3]Escoto"]

dentist_appointments = [
    {},
    {},
    {}
]
print("Dentist Appointment Logs")

choice = input("Want to Add Appointment?[Press y/n]: ")
choice2 = input ("Choose Denstist to see the details[1,2,3]:")

if choice.lower() == 'y':
    print("Great! Let's schedule an appointment.")
else:
    print("Goodbye!")

print("Available dentists: " + ", ".join(dr))

if choice2() == '1':
        print("Name: Dr. Mendoza" )
    elif choice2() == '2':
        print("Name: Dr. Mancion")
    elif choice2() == '3':
        print("Name: Dr. Escoto")

    else:
        print("Goodbye!")
