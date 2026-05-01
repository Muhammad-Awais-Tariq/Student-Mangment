import os
from dotenv import load_dotenv
from pymongo import MongoClient

url = os.getenv('url')
client = MongoClient(url)
try:
        database = client.get_database("SMS")
        students = database.get_collection("Students")
except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)

def get_students(name , password):
    name_password = students.find({},{"fullName" : 1 , "password" : 1 ,"status" : 1, "_id" : 0} )
    for student in name_password:
        if student["status"] == "Active" and name == student["fullName"] and int(password) == student["password"]:
            return True
    
    return False

          
def insert_student(studentId , fullName, password , program ,semester ,  section ,semesterGPA ,  cgpa , status):
    document = { "studentId": studentId, "fullName": fullName, "password": password, "program": program, "semester": semester, "section": section, "semesterGPA": semesterGPA, "cgpa": cgpa, "status": status , "enrolledCourses" : []}
    students.insert_one(document)

def main():
    student = get_students("Hassan Raza" , 141 )
    print(student)
    insert_student("0423","awais",123,"bcs",4,"B",3.2,3.2,"Active")
    
if __name__ == "__main__":
    main()