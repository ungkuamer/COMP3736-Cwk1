from app import app
from .functions import generate_random_data, question_generator, scatter_plot, heatmap_plot
from .question import Question

from flask import render_template, session, redirect, url_for, request
import io
import base64
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import firebase_admin
from firebase_admin import firestore
from datetime import datetime, timezone

matplotlib.use('Agg')

firebase_app = firebase_admin.initialize_app()
db = firestore.client()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/start')
def start():
    random_data = generate_random_data()

    session['count'] = session.get('count', 0) + 1

    if session.get('count') > 20:
        session.pop('count')
        session.pop('user')
        session.pop('reaction_time')
        return redirect(url_for('home'))

    if 'user' not in session:
        add_user = db.collection("participants").add(
            {"start_time": datetime.now(timezone.utc)})
        session['user'] = add_user[1].id

    user = session.get('user')

    if session['count'] % 2 == 0:
        plot = scatter_plot(random_data)
    else:
        plot = heatmap_plot(random_data)

    question = question_generator(random_data)
    session['correct_answer'] = question.answer_choice[question.answer_pos]

    feedback = session.pop('feedback', None)

    session['question_start_time'] = datetime.now()

    if 'reaction_time' in session:
        time = session.get('reaction_time')
    else:
        time = None

    return render_template('questions.html', plot=plot, question=question.question, choices=question.answer_choice, feedback=feedback, count=session.get('count'), user=user, time=time)


@app.route('/check', methods=['POST'])
def submit_check():
    start_time = session.get('question_start_time')
    if start_time:
        reaction_time = (datetime.now(timezone.utc) -
                         start_time).total_seconds()
        session['reaction_time'] = reaction_time

    selected_choice = request.form.get('selected_choice')

    correct_answer = session.get('correct_answer')

    user_id = session.get('user')
    curr_ques = session.get('count')
    question_num = "q" + str(curr_ques)

    if curr_ques % 2 == 0:
        question_type = 1
    else:
        question_type = 2

    if selected_choice == correct_answer:
        answer = True
    else:
        answer = False

    data = {question_num: {"answer": answer,
                           "res_time": reaction_time, "type": question_type}}
    db.collection("participants").document(user_id).set(data, merge=True)

    return redirect(url_for('start'))


@app.route('/end')
def end():
    session.pop('count')
    session.pop('user')
    if 'reaction_time' in session:
        session.pop('reaction_time')

    return redirect(url_for('home'))


@app.route('/answer')
def answer():
    school_data = generate_random_data()

    months = list(range(1, 13))
    months_name = ["Jan", "Feb", "Mar", "Apr", "May",
                   "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    schools_name = ["School " + str(i) for i in range(10)]

    # Scatter Plot
    plt.figure(figsize=(10, 6))
    for i, school in enumerate(school_data):
        plt.scatter(months, school, label=f'Sc {i}', alpha=0.7)
    plt.xlabel("Month")
    plt.ylabel("Random Value")
    plt.title("Scatter Plot of Random Data for Schools Across Months")
    plt.xticks(months, months_name)
    plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img1 = base64.b64encode(buf.getvalue()).decode('utf8')
    plt.close()

    # Heatmap
    plt.figure(figsize=(8, 6))
    plt.imshow(school_data, cmap="viridis", aspect="auto")
    for i in range(len(schools_name)):
        for j in range(len(months)):
            plt.text(j, i, school_data[i][j],
                     ha="center", va="center", color="w")

    plt.xticks(ticks=np.arange(len(months)), labels=months_name, rotation=45)
    plt.yticks(ticks=np.arange(len(schools_name)), labels=schools_name)
    plt.title("Heatmap of Random Data for Schools Across Months")

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img2 = base64.b64encode(buf.getvalue()).decode('utf8')
    plt.close()

    return render_template('answer.html', plot1=img1, plot2=img2)
