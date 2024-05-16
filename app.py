from flask import Flask
from src.logger import logging


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing our custome file")
    except Exception as e:
        abc=CustomException(e,sys)
        logging.info(abc.error_message)
        return "welcome end to end ml project pipeline course"

if __name__=="__main__":
    app.run(debug=True)