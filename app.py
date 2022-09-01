
from flask import Flask, render_template,  request 
import pickle


app = Flask(__name__)


@app.route('/', methods =['POST','GET'])
def home():
     if request.method == "POST":
        fs=int(request.form["FS"])
        fu=int(request.form["FU"])
        with open('my_model','rb') as f:
            model=pickle.load(f)

        result = model.predict([[fs,fu]])
        if result[0] == "NO":
             return render_template('home.html',data=["Congratulations You dont have diabetes","green"]) 
        else:
              return render_template('home.html',data=["Sorry you might have diabeties","red"])  
        
     else:
        return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


   



if __name__ == "__main__":
    app.run(debug=True)
