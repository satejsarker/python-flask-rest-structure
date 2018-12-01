from flask import Flask ,jsonify,request


app=Flask(__name__)

lang=[
    {'name':'java'},
    {'name':'python'},
    {'name':'javascript'}

]
#get  request
@app.route("/lang",methods=['GET'])
def allLnag():
    return jsonify({'allLang':lang})
# particular one get 

@app.route('/getOne/<string:name>',methods=['GET'])
def oneGet(name):
    langs=[]
    for i in lang:
        if(i['name']==name):
            langs.append(i['name'])
    return jsonify({'selectedOne':langs})
#Post request

@app.route('/langAdd',methods=['POST'])
def addLang():
    newLnag={'name': request.json['name']}
    lang.append(newLnag)
    return jsonify({'allLang':lang})

if __name__ == "__main__":
    app.run(debug=True,port=4000)