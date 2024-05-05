from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/contacts/")
def contacts():
    developer_name = "Elon Mask"
    telephone = "88005553535"
    return render_template('c.html', name=developer_name, tel=telephone)


if __name__ == "__main__":
    app.run(debug=True)
