from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Irfan! Your Flask Application has been successfully deployed on AWS EC2 using Terraform and GitHub Actions CI/CD Pipeline!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)