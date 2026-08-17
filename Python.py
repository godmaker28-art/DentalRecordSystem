def update_appointment():
    print("\n-- Update Appointment --")
    
    booked_slots_list = []
    for doc in dentist_schedule:
        for slot in doc["slots"]:
            if slot["patient"] is not None:
                booked_slots_list.append({
                    "doctor_obj": doc,
                    "slot_obj": slot,
                    "patient": slot["patient"],
                    "doctor": doc["doctor"],
                    "date": doc["date"],
                    "time": slot["time"]
                })
                
    if not booked_slots_list:
        print("No active appointments found to update.\n")
        return
        
    table_data = []
    for idx, item in enumerate(booked_slots_list, 1):
        table_data.append({
            "record_no": idx,
            "patient": item["patient"],
            "doctor": item["doctor"],
            "date": item["date"],
            "time": item["time"]
        })
        
    custom_headers = {
        "record_no": "No.",
        "patient": "Patient Name",
        "doctor": "Dentist's Name",
        "date": "Date",
        "time": "Time"
    }
    
    print(tabulate(table_data, headers=custom_headers, tablefmt="grid"))
    
    try:
        choice = int(input("Enter the Record No. to update/rebook (0 to return): "))
        if choice == 0:
            return
            
        if 1 <= choice <= len(booked_slots_list):
            selected_record = booked_slots_list[choice - 1]
            old_doc = selected_record["doctor_obj"]
            old_slot = selected_record["slot_obj"]
            patient_name = old_slot["patient"]
            
            print(f"\nUpdating appointment for: {patient_name} (Currently with {old_doc['doctor']} at {old_slot['time']})")
            print("Choose a new dentist/slot:")
            
            table_data = []
            for doc in dentist_schedule:
                available_slots = [slot["time"] for slot in doc["slots"] if slot["patient"] is None]
                time_str = " / ".join(available_slots) if available_slots else "Fully Booked"
                
                table_data.append({
                    "index": doc["index"], 
                    "name": doc["doctor"], 
                    "date": doc["date"], 
                    "time": time_str
                })

            print(tabulate(table_data, headers={"index": "No.", "name": "Dentist's Name", "date": "Date Available", "time": "Available Time Slots"}, tablefmt="grid"))
            
            dentist_no = int(input("Choose new dentist [1-3, 0 to cancel]: "))
            if dentist_no == 0:
                return
                
            if 1 <= dentist_no <= len(dentist_schedule):
                new_doc = dentist_schedule[dentist_no - 1]
                unbooked_slots = [slot for slot in new_doc["slots"] if slot["patient"] is None or slot == old_slot]
                
                if not unbooked_slots:
                    print("[NOTE] Selected doctor has no available time slots left.\n")
                    return
                    
                print(f"\nAvailable times for {new_doc['doctor']}:")
                for i, slot in enumerate(unbooked_slots, 1):
                    current_tag = " (Current)" if slot == old_slot else ""
                    print(f"[{i}] {slot['time']}{current_tag}")
                    
                time_choice = int(input("Choose time slot number: ")) - 1
                if 0 <= time_choice < len(unbooked_slots):
                    new_slot = unbooked_slots[time_choice]
                    
                    old_slot["patient"] = None
                    new_slot["patient"] = patient_name
                    print(f"\nAppointment successfully updated for {patient_name} with {new_doc['doctor']} at {new_slot['time']}!\n")
                else:
                    print("Invalid time slot choice.")
            else:
                print("Invalid dentist choice.")
        else:
            print("Invalid record number selection.")
    except ValueError:
        print("Invalid Input! Please enter a valid number.")