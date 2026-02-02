cgpa=float(input("cgpa: "))
attendance=int(input("attendance: "))
arrears=int(input("arrears: "))
if cgpa>=7.0 and attendance>=75 and arrears==0:
    print("ELIGIBLE")
else:
    print("NOT ELIGIBLE")