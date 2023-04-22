from flask import Flask , render_template, request,jsonify, url_for
import pickle
import os

picfolder = os.path.join("static","images")




import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
app.config["UPLOAD_FOLDER"] = picfolder

@app.route("/", methods = ['GET', 'POST'])
def predict():
    mybedrooms = request.form.get("bedrooms", False)
    mybathrooms	= request.form.get("bathrooms", False)
    mystories	= request.form.get("stories", False)
    mymainroad = request.form.get("mainroad", False)	
    myguestroom = request.form.get("guestroom", False)	
    mybasement =request.form.get("basement", False)	
    myhotwaterheating =request.form.get("hotwaterheating", False) 	
    myairconditioning	= request.form.get("airconditioning", False)
    myparking	= request.form.get("parking", False)
    myprefarea = request.form.get("prefarea", False)	
    myfurnishingstatus = request.form.get("furnishingstatus", False)
    myfin = np.array([[mybedrooms,mybathrooms,mystories,mymainroad,myguestroom,mybasement,myhotwaterheating,myairconditioning,myparking,  myprefarea,myfurnishingstatus ]])
    prediction = model.predict(myfin)
    return render_template("predict.html", my_ourbeans=f"The Name of the Beans is {prediction[0]}")



if __name__ == "__main__":
    app.run(debug=True)








