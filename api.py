from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort, reqparse, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
api = Api(app)
db = SQLAlchemy(app)

# Database model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)
    category = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'Task(ID={self.id}, title={self.title}, done={self.done})'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done,
            'category': self.category
        }

# Create database tables
with app.app_context():
    db.create_all()

# Request parser for creating/updating tasks
task_parser = reqparse.RequestParser()
task_parser.add_argument('title', type=str, required=True, help='Title is required')
task_parser.add_argument('description', type=str, required=True, help='Description is required')
task_parser.add_argument('done', type=bool, default=False)
task_parser.add_argument('category', type=str, default='General')

class TaskTracker(Resource):
    
    # Create a new task
    def post(self):
        args = task_parser.parse_args()
        
        # Check if task with same title already exists
        existing_task = Task.query.filter_by(title=args['title']).first()
        if existing_task:
            return {'message': 'Task with this title already exists'}, 400
        
        new_task = Task(
            title=args['title'],
            description=args['description'],
            done=args['done'],
            category=args['category']
        )
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return new_task.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
    
    # View a specific task
    def get(self, task_id):
        task = Task.query.get(task_id)
        if task:
            return task.to_dict()
        return {'message': 'Task not found'}, 404
    
    # Update a task
    def put(self, task_id):
        task = Task.query.get(task_id)
        if not task:
            return {'message': 'Task not found'}, 404
        
        args = task_parser.parse_args()
        
        try:
            task.title = args['title']
            task.description = args['description']
            task.done = args['done']
            task.category = args['category']
            
            db.session.commit()
            return task.to_dict(), 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
    
    # Delete a task
    def delete(self, task_id):
        task = Task.query.get(task_id)
        if not task:
            return {'message': 'Task not found'}, 404
        
        try:
            db.session.delete(task)
            db.session.commit()
            return {'message': 'Task deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500

class AllTasks(Resource):
    def get(self):
        tasks = Task.query.all()
        return [task.to_dict() for task in tasks], 200

class FilterByCategory(Resource):
    def get(self, category):
        tasks = Task.query.filter_by(category=category).all()
        if not tasks:
            return {'message': f'No tasks found in category: {category}'}, 404
        return [task.to_dict() for task in tasks], 200

# Register routes
api.add_resource(TaskTracker, '/tasks', '/tasks/<int:task_id>')
api.add_resource(AllTasks, '/all_tasks')
api.add_resource(FilterByCategory, '/tasks/category/<string:category>')

if __name__ == '__main__':
    app.run(debug=True)
    