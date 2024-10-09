from tkinter import *
root = Tk()
root.geometry("650x350")

def GetValue():
    print("Data Submited:")
    print(f"{NameValue.get(), GenderValue.get(), MobValue.get(), AddressValue.get(), MedicinesValue.get(), DoctorValue.get(), DateValue.get(), VisitationValue.get()}\n")

    with open("Hospital.txt", "a") as f:
        f.write(f"{NameValue.get(), MobValue.get(), AddressValue.get(), MedicinesValue.get(), DateValue.get(), VisitationValue.get()}\n")

Label(root, text="Hospital Patient's Information", font=("Arial", 20, "italic", "bold"), background="pink", foreground="black").grid(row=0, column=3, pady=10)

# <----------------- Text for Label--------------->

Patient_name = Label(root, text="Patient Name: ", font=("Arial", 20, "bold"))
Patient_Gender = Label(root, text="Gender: ", font=("Arial", 20, "bold"))
Patient_Mob = Label(root, text="Patient Mobile: ", font=("Arial", 20, "bold"))
Patient_Address = Label(root, text="Patient Address: ", font=("Arial", 20, "bold"))
Patient_Problem = Label(root, text="Patient Problem: ", font=("Arial", 20, "bold"))
Patient_Medicines = Label(root, text="Patient Medicines: ", font=("Arial", 20, "bold"))
Doctor_Name = Label(root, text="Doctor Name: ", font=("Arial", 20, "bold"))
Visited_date = Label(root, text="Date: ", font=("Arial", 20, "bold"))
Visitation = Checkbutton(root, text="Next Visitation?",)

Submit = Button(root, text="Submit", bg="Red", fg="Black", width=10, height=1, command=GetValue).grid(row=20, column=1, pady=10)

# <---------------- text Pack -------------------->

Patient_name.grid(row=4, column=0, pady=5)
Patient_Gender.grid(row=6, column=0, pady=5)
Patient_Mob.grid(row=8, column=0, pady=5)
Patient_Address.grid(row=10, column=0, pady=5)
Patient_Medicines.grid(row=12, column=0, pady=5)
Doctor_Name.grid(row=14, column=0, pady=5)
Visited_date.grid(row=16, column=0, pady=5)
Visitation.grid(row=18, column=1, pady=5)

# <------------------ text entry ------------------>

NameValue = StringVar()
GenderValue = StringVar()
MobValue = StringVar()
AddressValue = StringVar()
MedicinesValue = StringVar()
DoctorValue = StringVar()
DateValue = StringVar()
VisitationValue = IntVar()

# <------------------Entries for text ---------------->

NameEntry = Entry(root, textvariable=NameValue, width=30, font=("arial", 10, "bold"))
GenderEntry = Entry(root, textvariable=GenderValue, width=30, font=("arial", 10, "bold"))
MobEntry = Entry(root, textvariable=MobValue, width=30, font=("arial", 10, "bold"))
AddressEntry = Entry(root, textvariable=AddressValue, width=30, font=("arial", 10, "bold"))
MedicinesEntry = Entry(root, textvariable=MedicinesValue, width=30, font=("arial", 10, "bold"))
DoctorEntry = Entry(root, textvariable=DoctorValue, width=30, font=("arial", 10, "bold"))
DateEntry = Entry(root, textvariable=DateValue, width=30, font=("arial", 10, "bold"))

# <----------------- Packing the entries ------------->

NameEntry.grid(row=4, column=1)
GenderEntry.grid(row=6, column=1)
MobEntry.grid(row=8, column=1)
AddressEntry.grid(row=10, column=1)
MedicinesEntry.grid(row=12, column=1)
DoctorEntry.grid(row=14, column=1)
DateEntry.grid(row=16, column=1)



root.mainloop()