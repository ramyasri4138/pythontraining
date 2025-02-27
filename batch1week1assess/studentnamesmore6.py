# student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]
# List the name which has more than 6 characters as lone_names list using appropriate function
# 
student_name_list =["Meghan","Praavalika", "Bharath","Madhu Venkata suriya Narayana","Nithin Rajesh","Mani Prasad"]
def name_greater6(student_name_list):
    lone_names=(", ".join(name for name in student_name_list if len(name)>6))
    return lone_names
print(name_greater6(student_name_list))
    

