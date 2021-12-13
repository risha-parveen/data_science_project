from flask import flask, request
app=flask(__name__)

@app.route('/hello')
def hello():
    return "hi"



if __name__=="__main__":
    print("starting python flask server for home price prediction")
    app.run()