from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


'''
# 1er test
class BMIOutput(BaseModel):
    bmi: float
    message: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],)

@app.get("/")
def Hi():
    return {"message": "hello world"}

@app.get("/calculate_bmi")
def calculate_bmi(weight: float = Query(... , gt=20, lt=200, description= "en kilogramme"),
                  height: float= Query(... , gt=1, lt= 3, description= "en metre")):
    bmi=weight / (height ** 2)

    if bmi < 18.5:
        message = "Votre poid est faible, manger plus "
    elif 18.5 <= bmi < 25 :
        message = " لديك وزن طبيعي, حافظ عليه"
    elif 25 <= bmi < 30 :
        message = "vous avez plus de poid, plus d'exercice"
    else:
        message = "vous ete gros"
    #return {"Your Bmi": bmi, "message": message}
    return BMIOutput(bmi= bmi, message= message)
    '''
#test REST API

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

#model de fichier
class Student(BaseModel):
    id: int
    name: str
    grade: int
# liste pour sauvegarder les données
students = [
    Student(id=1, name ="kenza yala", grade=5),
    Student(id=2, name ="karim ali", grade=3),]

#read
@app.get("/students/")
def read_students():
    return students    

#create
@app.post("/students")
def create_student(new_student: Student):
    students.append(new_student)
    return new_student

#update
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student:Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error": "Student not found"}  

#delete
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index] 
            return {"message": "Student deleted"}
    return {"error": "Student not found"}                      