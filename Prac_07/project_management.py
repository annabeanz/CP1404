"""
Note: This was done in a rush and with tight circumstances... sorry for the late submission
"""

import datetime
from project import Project

PROJECTS_FILE = 'projects.txt'
MENU_PROMPT = """
Menu:
- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""


def main():
    projects = []
    choice = ''
    while choice.upper() != 'Q':
        choice.upper()
        print(MENU_PROMPT)
        choice = input("Enter your choice: ").upper()
        if choice == 'L':
            try:
                projects = load_projects()
                print("Projects loaded.")
            except FileNotFoundError:
                projects = []
                out_file(projects)
                print("Projects loaded.")

        elif choice == 'S':
            out_file(projects)
            print("Projects saved.")
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_projects_by_date(projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            print("Quitting the program.")
        else:
            print("Invalid choice. Please try again.")


def load_projects():
    projects = []
    in_file = open(PROJECTS_FILE, 'r')
    in_file.readline()
    for line in in_file:
        data = line.strip().split(',')
        name = data[0]
        start_date = datetime.datetime.strptime(data[1],
                                                '%d/%m/%Y').date()  # forgot how to use datetime had to referece
        priority = int(data[2])
        estimate = float(data[3])
        completion = int(data[4])
        project = Project(name, start_date, priority, estimate, completion)
        projects.append(project)
    return projects


def out_file(projects):
    saved_file = open(PROJECTS_FILE, 'w')
    saved_file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
    for project in projects:
        saved_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}"
                         f"\t{project.estimate}\t{project.completion}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]
    incomplete_projects.sort()
    completed_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    filtered_projects.sort()
    print("Filtered projects:")
    for project in filtered_projects:
        print(f"{project}")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: "))
    completion = int(input("Percent complete: "))
    project = Project(name, start_date, priority, estimate, completion)
    projects.append(project)
    print("New project added.")


def update_project(projects):
    print("Update project")
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    int(input("New Percentage: "))


main()
