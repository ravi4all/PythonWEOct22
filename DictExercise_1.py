data = {
    "names" : ['John','Shawn','Max','Sam','Tom','Nick','Steve'],
    "dept" : ['IT','HR','IT','IT','Admin','Sales','HR'],
    "salary" : [56000,78000,40000,35000,67000,25000,50000]
}

emp_name = input("Enter employee name : ")
index = data["names"].index(emp_name)
print("Name :",emp_name)
print("Dept :",data["dept"][index])
print("Salary :",data["salary"][index])

sum = 0
for i in range(len(data["names"])):
    sum += data["salary"][i]

print("Total Salary...",sum)

# 1. Find out total salary of IT Department
# 2. Find out avg salary of HR Department
# 3. Find out employee with the highest salary
# 4. Find out total salary of employees whose name starts with 'S'

