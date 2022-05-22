#performing flask imports
#from flask import Flask,jsonify,request


#app = Flask(__name__) #intance of our flask application 

#Route '/' to facilitate get request from our flutter app
#@app.route('/api', methods = ['GET'])
#def index():
#    d={}
#    d['Query']= str(request.args['Query'])
#    return jsonify(d) #returning key-value pair in json format


#if __name__ == "__main__":
#    app.run(host='192.168.1.249',port=5000,debug=True) #debug will allow changes without shutting down the server python G.py
#from flask import send_file,request,Flask
#from flask.templating import render_template_string
#app = Flask(__name__)
#@app.route('/get/<String:name>')
#def get(name):
#    filename = 'localmap.jpg'
#    return render_template_string(name=filename)

#if __name__ == "__main__":
#    app.run(host='192.168.1.10',port=5000,debug=True)    


import base64
with open("static\localmap.jpg", "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())
print(" The String IS :::",b64_string)


with open("static\localmap.jpg", "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())
print(" The String IS without b::: ",b64_string.decode('utf-8'))