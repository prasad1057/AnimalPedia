from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect("animals.db") as con:
        con.execute('''CREATE TABLE IF NOT EXISTS animals
                     (id INTEGER PRIMARY KEY, name TEXT, info TEXT, image_url TEXT)''')

@app.route('/')
def index():
    con = sqlite3.connect("animals.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM animals")
    animals = cur.fetchall()
    return render_template('animal.html', animals=animals)

@app.route('/add', methods=['GET', 'POST'])
def add_animal():
    if request.method == 'POST':
        name = request.form['name']
        info = request.form['info']
        image_url = request.form['image_url']
        with sqlite3.connect("animals.db") as con:
            con.execute("INSERT INTO animals (name, info, image_url) VALUES (?, ?, ?)", (name, info, image_url))
        return redirect('/')
    return render_template('add_animal.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
