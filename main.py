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

          
def insert_student(studentId , fullName, password , program ,semester ,  section ,semesterGPA ,  cgpa , status , courses):
    document = { "studentId": studentId, "fullName": fullName, "password": password, "program": program, "semester": semester,\
                 "section": section, "semesterGPA": semesterGPA, "cgpa": cgpa, "status": status , "enrolledCourses" : courses}
    students.insert_one(document)

def show_courses(name):
    courses = students.find({"fullName" : name}, {"enrolledCourses": 1, "_id": 0})

    for course in courses:
        courses_list = (course["enrolledCourses"])
        new_list = []
        for couse in courses_list:
            new_list.append([couse["courseName"],couse["totalMarks"],couse["marksObtained"],couse["grade"]])
            
    return new_list

def get_gpa(name):
    gpa = students.find({"fullName" : name},{"semester" : 1 , "semesterGPA" : 1 ,"cgpa" : 1, "_id" : 0} )
    for value in gpa:
        return value 

def get_stat(name):
    result = students.aggregate([
        {"$match": {"fullName": name}},
        {"$unwind": "$enrolledCourses"},   #since the enrolled courses is the list it converts it into the single documents so we can do aggregation
        {"$facet": {  #it allow us to run multiply aggregation piplines
            "MaxCourse": [
                {"$sort": {"enrolledCourses.marksObtained": -1}},
                {"$limit": 1},
                {"$project": {"MaxCourseName": "$enrolledCourses.courseName", "MaxObtainedMarks": "$enrolledCourses.marksObtained", "_id": 0}}
            ],
            "MinCourse": [
                {"$sort": {"enrolledCourses.marksObtained": 1}},
                {"$limit": 1},
                {"$project": {"MinCourseName": "$enrolledCourses.courseName", "MinObtainedMarks": "$enrolledCourses.marksObtained", "_id": 0}}
            ],
            "AvgCourse": [
                {"$group": {"_id": None, "average": {"$avg": "$enrolledCourses.marksObtained"}}},  #finding the average based on the marks
                {"$project": {"average": {"$round": ["$average", 2]}, "_id": 0}} 
            ]
        }}
    ])

    for value in result :
        return value

def get_total_Student(program , semester):
    total_students = students.count_documents({ "program" : program ,"semester" : semester })
    return total_students

def get_rank(name):
    rank = students.aggregate([
    {
        "$setWindowFields": {     #in order to find the rank we use window
        "partitionBy": { "program": "$program", "semester": "$semester" },  #how we group when finding the rank
        "sortBy": { "cgpa": -1 },
        "output": {
            "ranking": { "$denseRank": {} }  #we use dense rank beacuse simple rank skips the rank if two people hv same position
        }
        }
    },
    {
        "$match": { "fullName": name }  
    },
    {
        "$project": {"ranking": 1,  "program" : 1 , "semester": 1 , "_id": 0 } 
    }
    ])    

    for value in rank:
        value["total_student"] = get_total_Student(value["program"] ,value["semester"] )
    
    return value

def get_course_stats(name):
    result = students.aggregate([
        {"$match": {"fullName": name}},
        {"$unwind": "$enrolledCourses"},
         {"$group": {"_id": None, "sum": {"$sum": "$enrolledCourses.creditHours"} , "courses" : {"$push" : "$enrolledCourses"}}},
        {"$project": {"courses.courseName" : 1, "courses.courseCode": 1,"courses.instructor": 1,"courses.creditHours": 1, "sum" : 1, "_id": 0}}])    
    
    for value in result:
        return value

def directory():
    directory = students.find({},{"studentId" : 1 , "fullName" : 1 , "semester" : 1 , "section" : 1 , "cgpa" : 1 , "status" : 1 , "_id" : 0 })
    list_students = []
    for data in directory:
        list_students.append(data)
    
    return list_students

def top_scores():
    result = students.aggregate([
        {"$unwind": "$enrolledCourses"},  # flatten courses
        {"$sort": {"enrolledCourses.marksObtained": -1}},  
        {"$group": {
                    "_id": "$enrolledCourses.courseCode",            
                    "CourseName": {"$first": "$enrolledCourses.courseName"},
                    "MaxStudenName": {"$first": "$fullName"},                 
                    "MaxObtainedMarks": {"$first": "$enrolledCourses.marksObtained"},  
                    "MinObtainedMarks": {"$last": "$enrolledCourses.marksObtained"},
                    "AverageMarks": {"$avg": "$enrolledCourses.marksObtained"}
                }},
        {"$project": {
                    "_id": 0,
                    "CourseCode": "$_id",
                    "CourseName": 1,
                    "MaxStudenName": 1,
                    "MaxObtainedMarks": 1,
                    "MinObtainedMarks": 1,
                    "AverageMarks": {"$round": ["$AverageMarks", 2]}                    
                }}
                    
    ])
    top_scores = []
    for data in result:
        top_scores.append(data)
    
    return top_scores

def get_all_info(id):
    result = students.find({"studentId" : id})
    for data in result:
        return data
def main():
    # student = get_students("Hassan Raza" , 141 )
    # print(student)
    # insert_student("0423","awais",123,"bcs",4,"B",3.2,3.2,"Active")
    # print(get_gpa("Ali Raza"))
    # get_stat("Ali Raza")
    # get_rank("Ali Raza")
    # get_course_stats("Ali Raza")
    # print(directory())
    # print(top_scores())
    print(get_all_info("2026-CS-001"))
    
if __name__ == "__main__":
    main()