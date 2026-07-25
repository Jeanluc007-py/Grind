import json
from flask import Flask,render_template,request,redirect
app = Flask(__name__)
def load_info() :
    with open("info.json", "r") as file :
        return json.load(file)
    
    
def save_info(info) :
    with open ("info.json", "w") as file :
        return json.dump(info,file)
    
@app.route('/')
def home() :
    info = load_info()
    return render_template("index2.html", info = info )

@app.route('/survey', methods = ['GET','POST'])
def survey() :
    if request.method == 'POST' :
        print("FORM DATA: ",dict(request.form))
        user_type = request.form.get("user_type")
        choice = request.form.get("choice")
        print(f"user type : {user_type}, reason : {choice}")
        return redirect('/add')
    return redirect('/')

@app.route ('/add', methods = ['GET','POST']) 
def add_info() :
    info = load_info()
    if request.method == 'POST' :
        print("FORM DATA: ", dict(request.form))
        name = request.form.get("name")
        age = int(request.form.get("age"))
        if age < 16 :
            print("you have to be 16 or above to use this program")
        else :
            print("you are allowed to use this program")
        email = request.form.get("email")
        academic_achievement = request.form.get("academic_achievement")
        skills = request.form.get("skills")
        job_description = request.form.get("job_description")
        info.append(
            {
            "name" : name,
            "age" : age,
            "academic_achievement" : academic_achievement,
            "skills" : skills,
            "job_description" : job_description,
            "email" : email
        }
        )
        save_info(info)
        return redirect('/')
    return render_template("add2.html", info = info )

@app.route ('/edit/<int:id>', methods = ['GET','POST'])
def update_info(id) : 
    info = load_info()
    if request.method == 'POST' :
        info[id]["name"] = request.form.get("name")
        info[id]["age"] = request.form.get("age")
        info[id]["email"] = request.form.get("email")
        info[id]["academic_achievement"] = request.form.get("academic_achievement")
        info[id]["skills"] = request.form.get("skills")
        info[id]["job_description"] = request.form.get("job_description")
        save_info(info)
        return redirect('/')
    return render_template("update.html", info = info, id = id)

@app.route('/delete/<int:id>')
def delete_info(id) :
    info = load_info()
    info.pop(id)
    save_info(info)
    return redirect('/')

@app.route('/view_info')
def view_info() :
    info = load_info()
    return render_template("view.html", info = info)

if __name__ == "__main__" :
    app.run(debug = True)



                
        