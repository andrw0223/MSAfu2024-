class Student():
    #create the constructor
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__id_number = id_number
    
    #cerate the get and set methods
    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name
    
    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name    

    def get_major(self):
        return self.__major
    def set_major(self, new_major):
            self.__major = new_major

    def get_credit_hours(self):
        return self.__credit_hours
    def set_credit_hours(self, new_hours):
        try: 
            self.__credit_hours = int(new_hours)
        except:
            print("Error: Number of credit hours must be an integer")

    def get_gpa(self):
        return self.__gpa
    def set_gpa(self, new_gpa):
        try:
            self.__gpa = float(new_gpa)
        except:
            print("Error: GPA must be a number")

    def get_id_number(self):
        return self.__id_number
    
    #create a method to get class level based on the students credit hours
    def get_class_level(self):
        if (- 1 < int(self.__credit_hours) < 31): 
            return "Freshman"
        if (30 < int(self.__credit_hours) < 61): 
             return "Sophmore"
        if (60 < int(self.__credit_hours) < 91): 
             return "Junior"
        if (int(self.__credit_hours) > 90): 
             return "Senior"
    
    #create a method to update the credit hours
    def update_credit_hours(self, additional_hours):
        if(additional_hours > 0):
            try:
                self.__credit_hours += additional_hours
            except: 
                print("Error: Additonal hours must be a positive number")
        else: 
            print("Error: Additonal hours must be a positive number")
       
    
    #create a method to print all the data
    def print_info(self):
        print(f"First Name: {self.__first_name}")
        print(f"Last Name: {self.__last_name}")
        print(f"Class: {self.get_class_level()}")
        print(f"Major: {self.__major}")
        print(f"Credit Hours: {self.__credit_hours}")
        print(f"GPA: {self.__gpa}")
        print(f"ID Number: {self.__id_number}\n")




        
