class Person:
    name = ''
    age = ''
    address = ''
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Patient(Person):
    patient_id = ''
    medical_history = ''
    prescriptions = ''

    def __init__(self, name, age, address, patient_id, medical_history, prescriptions):
        super().__init__(name, age, address)
        self.patient_id = patient_id
        self.medical_history = medical_history 
        self.prescriptions = prescriptions 

    


class Doctor(Person):
    employee_id = ''
    specialty = ''
    assigned_patients = []
    def __init__(self, name, age, address, employee_id, specialty, assigned_patients=None):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.specialty = specialty
        self.assigned_patients = assigned_patients if assigned_patients is not None else []

    def add_patient(self, patient):
        self.assigned_patients.append(patient)

    
class Hospital:
    Patient = []
    doctors = []
    appointments = []
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, patient, doctor, appointment_date):
        if patient in self.patients and doctor in self.doctors:
            self.appointments.append((patient, doctor, appointment_date))
            doctor.add_patient(patient)
        else:
            raise ValueError("Patient or Doctor not found in the hospital records")

    def display(self):
        print(f"Total Patients: {len(self.patients)}")
        print(f"Total Doctors: {len(self.doctors)}")
        for doctor in self.doctors:
            print(f"""
            Doctor name :{doctor.name}
            patient assigned to doctor : {len(doctor.assigned_patients)}
            Doctor spacility :{doctor.specialty}
            """)
        for patient in self.patients:
            print(f"""
            Patient name: {patient.name} 
            Patient ID :{patient.patient_id}
          """)
        print(f"Total Appointments: {len(self.appointments)}")
        for patient, doctor, date in self.appointments:
            print(f"""
        Appointmentof Patient: {patient.name} 
        Appoint to doctor: {doctor.name} 
        Date: {date}
        """)


hospital = Hospital()

doctor1 = Doctor("Dr. Sara", 45, "Address1", "D001", "Cardiology")
doctor2 = Doctor("Dr. Hamza", 38, "Address2", "D002", "Neurology")

hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)


patient1 = Patient("Ali", 30, "Address3", "P001")
patient2 = Patient("Ahmad", 25, "Address4", "P002")

hospital.add_patient(patient1)
hospital.add_patient(patient2)
hospital.schedule_appointment(patient1, doctor1, "2024-08-01")
hospital.schedule_appointment(patient2, doctor2, "2024-08-02")

hospital.display()
