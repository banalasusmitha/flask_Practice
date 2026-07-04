# Student Registration System

A simple **Flask** web application to manage student records with **MongoDB** as the backend database. Users can **add, view, update, and delete** student details.

---

## Features

* List all students on the home page
* Add a new student
* Update existing student details
* Delete a student with confirmation
* Simple and responsive UI using Bootstrap

---

## Tech Stack

* **Backend:** Python, Flask
* **Database:** MongoDB (via Flask-PyMongo)
* **Frontend:** HTML, Jinja2 templates, Bootstrap 5
* **Environment Variables:** Managed via `.env` file

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Activate venv
# Windows:
venv\Scripts\activate
# Linux / Mac:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt` example:**

```
Flask
Flask-PyMongo
python-dotenv
bson
```
---

# CI/CD Pipelines

This repository implements two CI/CD pipelines for the Flask Student
Registration application: one using Jenkins and one using GitHub Actions.

## Prerequisites
- Python 3, pip, Git
- (Jenkins) An Ubuntu server with Java 21 and Jenkins installed
- (GitHub Actions) No setup — runs on GitHub-hosted runners

## Task 1 — Jenkins Pipeline
Defined in the `Jenkinsfile` at the repo root, running on a Jenkins server
hosted on an AWS EC2 (Ubuntu) instance.

Stages:
1. Build — creates a Python virtual environment and installs dependencies with pip.
2. Test — runs the test suite with pytest.
3. Deploy — deploys to a staging environment if tests pass.

Trigger: a GitHub webhook (repo Settings → Webhooks →
`http://<jenkins-ip>:8080/github-webhook/`) starts a build on every push to main.

Notifications: the `post` block emails success/failure using the SMTP server
configured under Manage Jenkins → System → E-mail Notification.

## Task 2 — GitHub Actions Workflow
Defined in `.github/workflows/ci-cd.yml`, running on GitHub-hosted Ubuntu runners.

Jobs:
- build-and-test — checkout, setup Python, install dependencies (pip), run
  pytest, and build. Runs on pushes to main and staging.
- deploy-staging — runs only on pushes to the staging branch.
- deploy-production — runs only when a GitHub Release is published (tag v1.0.0).

Deploy jobs use `needs: build-and-test`, so they run only if tests pass.

### Configuring Secrets
Stored under Settings → Secrets and variables → Actions, referenced as
`${{ secrets.NAME }}`:
- `STAGING_API_TOKEN` — used by the staging deploy job.
- `PROD_API_TOKEN`

### 4. Configure environment variables

Create a `.env` file in the project root:

```
MONGO_URI=<your-mongodb-connection-string>
SECRET_KEY=<your-secret-key>
```

### 5. Run the application

```bash
python app.py
```

Open your browser at: [http://localhost:8000](http://localhost:8000)

---

## Project Structure

```
project/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_student.html
│   ├── update_student.html
│
├── app.py
├── requirements.txt
└── .env
```

---

## Screenshots

**Home Page**
Lists all students with Edit/Delete buttons.
- <img width="1902" height="607" alt="image" src="https://github.com/user-attachments/assets/a58a6a6d-4978-4769-8074-232e4d31e69d" />


**Add Student**
Form to add a new student.
- <img width="1897" height="801" alt="image" src="https://github.com/user-attachments/assets/d65d25c3-ebb5-410a-adb1-e130ad7c5878" />


**Update Student**
Form pre-filled with student details.
- <img width="1905" height="897" alt="image" src="https://github.com/user-attachments/assets/04febf01-879f-431f-ab07-abcfb993acf1" />



---

## Notes

* Make sure MongoDB is running and accessible via the URI in `.env`
* Delete action includes a confirmation page to prevent accidental deletion
* Uses `ObjectId` from `bson` to work with MongoDB document IDs
* If you use MongoDB Atlas on macOS, install dependencies again (`pip install -r requirements.txt`). This project now uses `certifi` CA bundle explicitly to avoid common TLS certificate verification failures with `pymongo`.

---

## License

MIT License

---



