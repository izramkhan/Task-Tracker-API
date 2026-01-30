# TaskFlow API 📋

A production-ready RESTful task management system built with Flask, featuring complete CRUD operations, database persistence, and intelligent filtering capabilities.

# Features

* Complete CRUD Operations - Create, Read, Update, Delete

* SQLite Database with SQLAlchemy ORM

* Input Validation & Error Handling

* RESTful Design with proper HTTP codes


# API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/tasks` | Create new task |
| GET | `/all_tasks` | Get all tasks |
| GET | `/tasks/<id>` | Get specific task |
| PUT | `/tasks/<id>` | Update task |
| DELETE | `/tasks/<id>` | Delete task |
| GET | `/tasks/category/<category>` | Filter by category |


# Requirments

`
Flask==2.3.3
`
,
`
Flask-RESTful==0.3.10
`
,
`
Flask-SQLAlchemy==3.0.5
`

```bash
# Clone & setup
git clone https://github.com/izramkhan/Task-Tracker-API.git
cd taskflow-api
pip install -r requirements.txt
python api.py
