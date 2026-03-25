# 03-Student grade analyzer- Hiruni
print("=====STUDENT GRADE ANALYZER=====")

students= int(input("\n How many students :"))
count=0
total_average=0
pass_count=0
fail_count=0

while (count<students):
    print(f"\n------Student {count+1}------")
    name=input("\nName :")

    subject=1
    total_marks=0
    
    while subject<=5 :
       grade=int(input(f"Enter grade for subject {subject} :"))
       if grade>=0 and grade<=100:
           total_marks=total_marks+grade
           subject=subject+1
       else:
          print("\n Invalid Grade !")

    average=total_marks/5
    total_average=total_average+average


    if average>=90 and average<=100:
        Letter_Grade= "A"
    elif average>=80 and average<=89.9:
        Letter_Grade= "B"
    elif average>=70 and average<=79.9:
        Letter_Grade= "C"
    elif average>=60 and average<=69.9:
        Letter_Grade= "D" 
    else: 
        Letter_Grade= "F"

    if average>=60:
        status="PASSED"
        pass_count=pass_count+1
    else:    
        status= "FAIL"
        fail_count=fail_count+1  

    count=count+1  

    print(f"\nName : {name}")
    print(f"Average : {average}")
    print(f"Letter Grade : {Letter_Grade}")
    print(f"Status : {status}")

classAverage= total_average/students

print("\n----CLASS SUMMARY---")
print(f"\n Total students : {students}")
print(f"Passing :{pass_count}")
print(f"Failing : {fail_count}")
print(f"Class Average : {classAverage}")
print(f"total average {total_average}")