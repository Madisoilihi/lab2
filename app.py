from flask import Flask, render_template, request, redirect, url_for
import logging

app = Flask(__name__)

tasks = []

# Configurer le logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    logging.debug(f"Tâches actuelles : {tasks}")
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    logging.debug(f"Tâche reçue : {task}")
    if task:
        tasks.append(task)
        logging.debug(f"Tâche ajoutée : {tasks}")
    else:
        logging.debug("Aucune tâche reçue")
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    logging.debug(f"ID de la tâche à supprimer : {task_id}")
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        logging.debug(f"Tâche supprimée. Nouvelles tâches : {tasks}")
    else:
        logging.debug("ID de tâche invalide")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

