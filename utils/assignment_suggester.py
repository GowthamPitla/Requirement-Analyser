def suggest_assignments(missing_skills):
    assignment_bank = {
        "python": [
            "Build a CLI calculator using Python",
            "Write a script to automate file renaming"
        ],
        "machine learning": [
            "Train a classifier on Iris Dataset using scikit-learn",
            "Implement Linear Regression from scratch"
        ],
        "flask": [
            "Develop a Flask API for a note-taking app",
            "Build a RESTful login/signup Flask web app"
        ],
        "sql": [
            "Design a database schema and perform CRUD operations using SQLite",
            "Solve 10 SQL queries using LeetCode SQL Practice"
        ],
        "html": [
            "Build a static portfolio website using HTML/CSS",
            "Clone a landing page layout (e.g., Netflix)"
        ],
        "css": [
            "Style a portfolio site with responsive design using CSS",
            "Use Flexbox/Grid to layout a blog page"
        ],
        "git": [
            "Create a GitHub repo and push a Flask app to it",
            "Demonstrate version control using branches & merges"
        ],
        "react": [
            "Build a Todo App with ReactJS",
            "Integrate a simple API with React and display the data"
        ],
        "docker": [
            "Dockerize a Python Flask app",
            "Write a Dockerfile to containerize a ML model"
        ],
        "linux": [
            "Write shell scripts to automate tasks",
            "Set up a local server using Linux terminal"
        ],
    }

    suggestions = []
    for skill in missing_skills:
        items = assignment_bank.get(skill.lower(), [f"Explore beginner projects for {skill} on GitHub or Kaggle"])
        suggestions.extend([f"{skill.title()} → {item}" for item in items])
    return suggestions
