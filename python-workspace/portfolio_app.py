from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects_list = [
        {
            'title': 'Project 1',
            'description': 'A brief description of your first project',
            'tech': 'Python, Flask',
            'link': '#'
        },
        {
            'title': 'Project 2',
            'description': 'A brief description of your second project',
            'tech': 'HTML, CSS, JavaScript',
            'link': '#'
        },
        {
            'title': 'Project 3',
            'description': 'A brief description of your third project',
            'tech': 'Python, Django',
            'link': '#'
        }
    ]
    return render_template('projects.html', projects=projects_list)

@app.route('/skills')
def skills():
    skills_data = {
        'Frontend': ['HTML', 'CSS', 'JavaScript'],
        'Backend': ['Python', 'Flask', 'Django'],
        'Tools': ['Git', 'VS Code', 'GitHub']
    }
    return render_template('skills.html', skills=skills_data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
