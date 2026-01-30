# Created by: Izram Khan
# Date completed: 30-Jan-2026
# Lisence: This code is open source
#----------------------------------------------------------------------------------------------------
import requests

BASE = 'http://127.0.0.1:5000'

tasks = {
    1: {'title': 'Python', 'description': 'This is the description', 'category': 'coding', 'done': False},
    2: {'title': 'Calculus', 'description': 'Description for calculus', 'category':'maths', 'done': False},
    3: {'title': 'WorkOut', 'description': 'Do some workout everyday', 'category': 'health', 'done': False},
    4: {'title': 'Sleep', 'description': 'Get 8 hours of sleep every day', 'category': 'health', 'done': True},
    5: {'title': 'title to delte', 'description': 'Description to delete', 'category': 'delete', 'done': True}
}

# Creating tasks. Using .post method in class TaskTrakcer.
for task_id, task_data in tasks.items():
    response = requests.post(BASE + '/tasks', json=task_data)
    print(f'Created Task: {task_id}, Status: {response.status_code}, Data: {response.json()}')

input()
# Requesting a specific task. Using .get method in class TaskTracker
request_1 = requests.get(BASE + '/tasks/1')
request_2 = requests.get(BASE + '/tasks/2')

print(f'DATA: {request_1.json()}, Status code: {request_1.status_code}')
print(f'DATA: {request_2.json()}, Status code: {request_2.status_code}')

input()
# Requesting a task with task id that doesn't exists
does_not_exists = requests.get(BASE + '/tasks/9')
print(f'DATA: {does_not_exists.json()}, Status code: {does_not_exists.status_code}')

input()
# Updating a task. Using .put method in class TaskTracker
update_request_1 = requests.put(BASE + '/tasks/1', json={'title': 'PYTHON', 'description': 'This is the new description.'})
update_request_2 = requests.put(BASE + '/tasks/2', json={'title': 'Integral calculus'})

print(f'DATA: {update_request_1.json()}, Status code: {update_request_1.status_code}')
print(f'DATA: {update_request_2.json()}, Status code: {update_request_2.status_code}')

input()
# Updating a task by task id that doesn't exists
update_not_exists = requests.put(BASE + '/tasks/12', json={'title': 'Integral calculus'})
print(f'DATA: {update_not_exists.json()}, Status code: {update_not_exists.status_code}')

input()
# Deleting a task. Using .delte method in class TaskTracker
delete_request = requests.delete(BASE + '/tasks/5')
print(f'DATA: {delete_request.json()}, Status code: {delete_request.status_code}')

input()
# Deleting a task that doesn't exist
delete_not_exists = requests.delete(BASE + '/tasks/3')
print(f'DATA: {delete_not_exists.json()}, Status code: {delete_not_exists.status_code}')

input()
# Filter tasks by category. Using class FilterByCategory
filter_request = requests.get(BASE + '/tasks/category/health')
print(f'DATA: {filter_request.json()}, Status code: {filter_request.status_code}')

input()
# Viewing all tasks. Using class AllTasks
all_tasks_request = requests.get(BASE + '/all_tasks')
print(f'DATA: {all_tasks_request.json()}, Status code: {all_tasks_request.status_code}')

