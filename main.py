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

def main():
    student = get_students("Hassan Raza" , 141 )
    print(student)
if __name__ == "__main__":
    main()