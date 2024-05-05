from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    main_data = {
        'Город': 'Новочебоксарск',
        'Район': 'Обычный',
        'Компания': 'Iserv'
    }
    bam = {
        'Имя': 'Влад',
        'Возраст': '16',
        'Специализация': 'учусь'
    }
    return render_template('index.html', main_data=main_data, **bam)


@app.route("/contacts/")
def contacts():
    developer_name = "Влад"
    telephone = "88005553535"
    return render_template('c.html', name=developer_name, tel=telephone)


@app.route("/results/")
def results():
    data = ['Python', 'js', 'Golang', 'C#', 'C++', 'Rust', 'C']
    return render_template('results.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
