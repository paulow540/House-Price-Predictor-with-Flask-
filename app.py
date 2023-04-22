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
    mybedrooms = int(request.form.get("bedrooms", False))
    mybathrooms	= int(request.form.get("bathrooms", False))
    mystories	= int(request.form.get("stories", False))
    mymainroad = int(request.form.get("mainroad", False))	
    myguestroom = int(request.form.get("guestroom", False))	
    mybasement = int(request.form.get("basement", False))	
    myhotwaterheating = int(request.form.get("hotwaterheating", False)) 	
    myairconditioning	= int(request.form.get("airconditioning", False))
    myparking	= int(request.form.get("parking", False))
    myprefarea = int(request.form.get("prefarea", False))	
    myfurnishingstatus = int(request.form.get("furnishingstatus", False))
    print([mybedrooms,mybathrooms,mystories,mymainroad,myguestroom,mybasement,myhotwaterheating,myairconditioning,myparking,  myprefarea,myfurnishingstatus ])
    myfin = np.array([[mybedrooms,mybathrooms,mystories,mymainroad,myguestroom,mybasement,myhotwaterheating,myairconditioning,myparking,  myprefarea,myfurnishingstatus ]])
    prediction = model.predict(myfin)
    return render_template("homepage.html", my_ourbeans=f"The Price of the house  is ${prediction[0]}")



if __name__ == "__main__":
    app.run(debug=True)








