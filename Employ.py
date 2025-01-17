
class Employee:
    def __init__(self , name , emp_id , deptt , salary):
        self.name = name
        self.emp_id = emp_id
        self.deptt = deptt
        self.salary = salary

    def display_info(self):
        st = f'''Name: {self.name} 
Emp_id: {self.emp_id} 
Department: {self.deptt} 
salary: {self.salary}'''
        print(st)

    def update_info(self , name=None , deptt=None, salary=None):
        if name:
            self.name = name  
        if deptt:
            self.deptt = deptt
        if salary:
            self.salary = salary

    def update_salary(self , salary_percent):
        self.salary = self.salary + self.salary * salary_percent / 100
        
class Employee_management:
    def __init__(self):
        self.reg = {}
        self.last_emp_id = 0

    def generate_emp_id(self):
        self.last_emp_id += 1
        return f'gla{self.last_emp_id:05d}'

    def add_employee(self , name , deptt , salary):   
        emp_id = self.generate_emp_id()
        if emp_id not in self.reg:
            self.reg[emp_id] = Employee(name , emp_id , deptt , salary)
            print(f'Employee id {emp_id} added successfully')
        else:
            print('Employee id already exist')
    
    def display_all_employees(self):
        for _, employee in self.reg.items():
            employee.display_info() 
            print('----------------------')

    def update_employee_salary(self, emp_id, salary_percent):
        if emp_id in self.reg:
            self.reg[emp_id].update_salary(salary_percent)
            print(f'Employee id {emp_id} salary updated successfully')
        else:
            print('Employee id not found')

# main code
systm = Employee_management()
systm.add_employee('ravi', 'cse', 10000)
systm.add_employee('raj', 'cse', 20000)
# Update salary by percentage
systm.update_employee_salary('gla00001', 10)
# Display all employees
systm.display_all_employees()
