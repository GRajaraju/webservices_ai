# This is a sample webservice created in Python using flask

from flask import Flask # importing flask

app = Flask(__name__) # creating Flask object

@app.route('/') # '/' specifies root or home page. @app is a decorator to which we are attaching a function.
def test_service():
  return "test passed" # on access to '/' in the web browser, the string 'test passed' is returned.
 
app.run(port=5000) # running the web service available at port 5000


