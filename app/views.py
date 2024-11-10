from app import app
from .functions import generate_random_data

from flask import render_template, render_template_string
import io
import base64
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('Agg')


@app.route('/')
def home():
    return render_template('index.html')


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
