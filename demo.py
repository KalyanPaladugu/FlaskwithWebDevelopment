from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "hello, this is our first flask website";  

@app.route('/show')
def show():
	
if __name__ =='__main__':  
    app.run(debug = True)  