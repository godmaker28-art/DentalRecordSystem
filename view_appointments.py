patient_1 = "Joshua M. Manaliti"
patient_2 = "Jerico L. Figura"

dentist_schedule = [
    {"name":"Dr. Mancion","date":"August 17,2026","time":"9:00AM To 1:00PM"},
    {"name":"Dr. Mendoza","date":"August 18,2026","time":"10:00AM To 2:00PM"},
    {"name":"Dr. Escoto","date":"August 19,2026","time":"11:00AM To 3:00PM"}
]
    
#viewing scheduled patient
print("Appointed Pationt Name:" + patient_1)
for i in dentist_schedule:
    print(f'{i["name"]}, {i["date"]:>20}, {i["time"]:>20}')