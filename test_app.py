from flask import Flask,render_template,request,redirect,url_for,flash
db= [
    {"id":1,
    "title":"Do Dishes",
    "completed":False,},
    
    {"id":2,
    "title":"Clean the Kitchen",
    "completed":True,},
    
    {"id":3,
    "title":"Wash the Car",
    "completed":False,},
    
    {"id":4,
    "title":"Make Dinner",
    "completed":True,}
    ]
def get_last():
    return max( do["id"] for do in db)+1

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY="dev")
@app.route("/")
def home():
    return render_template("base.html", do_list=db)
@app.route("/add",methods=["POST"])
def create_do():
    title=request.form.get("title","").strip()
    if title:
        db.append({"id":get_last(), "title":title,"completed":False})   
    else:
        flash('No exist',"error")
    return redirect(url_for("home"))
@app.route("/update/<int:id>")
def update(id):
    for do in db:
        if do["id"] == id:
            do["completed"] = not do["completed"]
            break
    else:
        flash("Task not found","error")
    return redirect(url_for("home"))
            
@app.route("/delete/<int:id>")
def delete(id):
    for do in db:
        if do["id"] == id:
            db.remove(do)
            break
    else:
        flash("Task not found","error")
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)
