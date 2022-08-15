from flask import render_template

from sweater import app
from sweater.projects import projects


@app.route("/projects")
def index():
    return render_template("index.html", projects=projects.values())


@app.route("/project/<name>")
def project_card(name):
    if name not in projects:
        return "Project does not exist"
    return render_template("project-card.html", project=projects[name])
