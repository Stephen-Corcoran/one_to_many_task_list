from models.task import Task
from psycopg2.extensions import SQL_IN
from db.run_sql import run_sql 

from models.user import User

def save(user):
    sql = "INSERT INTO user (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [user.first_name, user.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def select_all():
    user =[]

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['first_name'], row ['last_name'], row['id'])
        users.append(user)
    return users

def select(id):
    user = None
    sql ="SELECT * FROM users WHERE id = %s"
    values =[id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['first_name'], result['last_name'], result['id'])
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    value = [id]
    run_sql(sql, value)

def update(user):
    sql = "UPDATE users SET (first_name, last_name) = (%s. %s) WHERE id = %s"
    values = [user.first_name, user.last_name, user.id]
    run_sql(sql, values)

def tasks(user):
    task = []

    sql = "SELECT * FROM tasks WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        task = Task(row['description'], user, row['duration'], row['completed'], row['id'])
        tasks.append(task)
    return tasks