
#import modules
from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

#make a flask app
app = Flask(__name__)

app.config["DEBUG"] = True

#set a secret key to use when validating form data
app.config["SECRET_KEY"] = "password"

#Define a constant value for URL
URL = "http://127.0.0.1:5000/api/students/all"

#function to request student data from the api
#input: url
#output: JSON student data
def get_student_data(url):
    #make a request
    response = requests.get(url)

    #convert format to json
    response_json = response.json()
    return response_json

#Function to return a list of unique majors
#Input: url
#Output: List of unique majors
def get_unique_majors():
   
    #get a list of students from the student api
    student_list = get_student_data(URL)

    #produce a list of unqiue majors
    unique_majors = []

    for student in student_list:
        if student["major"] not in unique_majors:
            unique_majors.append(student["major"])
    unique_majors.sort()
    return unique_majors



#create a route for the site index page that will display all student data
@app.route("/", methods=['GET'])
def index():
    #get the student data
    #make a request to the student data api url

    student_data = get_student_data(URL)

    return render_template('index.html', student_data = student_data)


    #send the student data to the index.html

@app.route('/majors', methods=['GET'])
def majors():
    #write code that gets a unqie list of majors from student
    major_list = get_unique_majors()

    return render_template("majors.html", major_list=major_list)

@app.route('/majors', methods=['POST'])
def majors_post():
    major_list = get_unique_majors()
    result_list = []

    #get the form data that was submitted
    major = request.form.get('major')
    #validate form data. If invalid form data. Show error message
    if not major:
        flash("You must select a major")
    else:
    #Find studentd with the selected major and return to the majors.html page
    #get the student data
     student_list = get_student_data(URL)
     
     #loop through list of students
     for student in student_list:
         if student["major"] == major:
             result_list.append(student)
    
    #send the result list to the majors.html page



    return render_template('majors.html', major_list=major_list, result_list=result_list)



app.run(port=5005)
