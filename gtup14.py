#Write a program in python to implement Salary printing file read operation.
#(Fileformat:Employee No, name, deptno, basic, DA, HRA, Conveyance)
#should perform below operations.
#a) Print Salary Slip for given Employee Number
#b) Print Employee List for Given Department Number

# define a function to print the salary slip
def print_salary_slip(emp_no):
 with open('salary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(',')
        if data[0] == emp_no:
 # calculate gross salary
            basic = int(data[3])
            da = int(data[4])
            hra = int(data[5])
            conveyance = int(data[6])
            gross_salary = basic + da + hra + conveyance
 # print salary slip
            print(f"Salary Slip for Employee No: {data[0]}")
            print(f"Name: {data[1]}")
            print(f"Department No: {data[2]}")
            print(f"Basic Salary: {basic}")
            print(f"Dearness Allowance: {da}")
            print(f"House Rent Allowance: {hra}")
            print(f"Conveyance Allowance: {conveyance}")
            print(f"Gross Salary: {gross_salary}")
    return print("Employee not found")
# define a function to print the employee list for a given department number
def print_employee_list(dept_no):
 with open('salary.txt', 'r') as f:
    print(f"Employee List for Department No: {dept_no}")
    for line in f:
            data = line.strip().split(',')
            if data[2] == dept_no:
                print(f"{data[0]} {data[1]}")
                print()
# test the functions
print_salary_slip('102')
print_employee_list('2')

