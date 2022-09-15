from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def check_CICD_pipeline ():
    return "Check for CI/CD pipeline. Check for 'changes' in CI/CD pipeline."

if __name__ == "__main__":
    app.run(debug=True)