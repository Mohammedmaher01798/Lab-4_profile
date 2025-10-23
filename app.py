# from flask import Flask, render_template
# app = Flask(__name__)



# @app.route('/')
# def home():
#     student_name = "Mohamed Maher"
#     skills = ["Python", "Flask", "HTML", "CSS"] 
#     return render_template('index.html', student_name=student_name, skills=skills)

# @app.route('/about')
# def about():
#     return render_template('about.html')
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')
# @app.route('/project')
# def project():
#     project_list = [
#         {"name": "Chatbot", "year": 2024},
#         {"name": "Personal Website", "year": 2025},
#         {"name": "Image Classifier", "year": 2025}
#     ]       
#     return render_template('project.html',projects=project_list)
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)


PERSON = {
    "name": "Mohamed",
    "bio": "Computer Science TA who loves web development and Python.",
    "skills": ["Python", "Flask", "HTML", "CSS", "Git"]
}

PROJECTS = [
    {
        "name": "Personal Website",
        "year": 2025,
        "description": "My first Flask portfolio site."
    },
    {
        "name": "Chatbot",
        "year": 2024,
        "description": "A conversational AI project."
    },
    {
        "name": "Image Classifier",
        "year": 2025,
        "description": "A machine learning project for image recognition."
    }
]

@app.route('/')
def home():
    return render_template('home.html', person=PERSON)

@app.route('/about')
def about():
    return render_template('about.html', person=PERSON)

@app.route('/projects')
def projects():
    return render_template('projects.html', person=PERSON, projects=PROJECTS)

@app.route('/contact')
def contact():
    return render_template('contact.html', person=PERSON)


if __name__ == '__main__':
    app.run(debug=True)
