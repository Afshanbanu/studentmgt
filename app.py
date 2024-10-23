from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
students = []

@app.route('/')
def index():
    return "Welcome to the Student Management System!"
@app.route('/students')
def list_students():
    return render_template('students.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        students.append({'name': name, 'age': age})
        return redirect(url_for('list_students'))
    return render_template('add_student.html')


if __name__ == '__main__':
    app.run(debug=True)