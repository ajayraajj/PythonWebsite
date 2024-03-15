from flask import Flask

app=Flask(__name__)

@app.route("/")

def hello():
  return "<button style='color:black;background:white;width:50%'>Clcik me</button>"
print(__name__)
if __name__=="__main__":
  app.run(host='0.0.0.0')

