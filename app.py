from operator import imod
from flask import Flask
from forestcovertype.logger import logging
from forestcovertype.exception import ForestException
import sys

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def check_CICD_pipeline ():
    try:
        raise Exception("tesing coustome exception")
    except Exception as e:
        forestexception = ForestException(e,sys)
        logging.info(forestexception.error_message)
        logging.info("testing for logging module")
    return "Check for CI/CD pipeline. Check for 'changes' in CI/CD pipeline."

if __name__ == "__main__":
    app.run(debug=True)

# python app.py