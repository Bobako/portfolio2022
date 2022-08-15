import json


class Project:
    def __init__(self,
                 name: str = "",
                 project_pic_name: str = "default_image.jpg",
                 description: str = "",
                 short_description: str = "",
                 task: str = "",
                 technologies: list[str] | None = None,
                 test_link: str = "",
                 test_notes: str = "",
                 github_link: str = "",
                 ):
        self.name = name
        self.project_pic_path = f"static/imgs/{project_pic_name}"
        self.description = description
        if not short_description:
            self.short_description = description[:100] + "..."
        else:
            self.short_description = short_description
        self.task = task.replace("\n", "<br>")
        self.technologies = technologies
        self.test_link = test_link
        self.test_notes = test_notes
        self.github_link = github_link

    @classmethod
    def get_projects(cls):
        with open("projects.json", 'r', encoding="utf-8") as file:
            project_dicts = json.load(file)
        projects = {}
        for project_dict in project_dicts:
            projects[project_dict["name"]] = Project(**project_dict)
        return projects


projects = Project.get_projects()
