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

@app.route('/scatter')
def scatter():

    school_data = generate_random_data()
    
    months = list(range(1, 13))

    plt.figure(figsize=(10, 6))
    for i, school in enumerate(school_data):
        plt.scatter(months, school, label=f'Sc {i}', alpha=0.7)
    plt.xlabel("Month")
    plt.ylabel("Random Value")
    plt.title("Scatter Plot of Random Data for Schools Across Months")
    plt.xticks(months, ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))

    # Save plot to an in-memory image
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf8')
    plt.close()  # Close the plot to free up memory

    # Render HTML with embedded image
    html = f"""
    <html>
    <body>
        <h1>Scatter Plot of Random Data</h1>
        <img src="data:image/png;base64,{img_base64}" alt="Scatter Plot"/>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/heatmap')
def heatmap():

    school_data = np.array(generate_random_data())
    schools_name = ["School " + str(i) for i in range(10)]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Create the heatmap
    plt.figure(figsize=(8, 6))
    plt.imshow(school_data, cmap="viridis", aspect="auto")
    for i in range(len(schools_name)):
        for j in range(len(months)):
            text = plt.text(j, i, school_data[i][j], ha="center", va="center", color="w")

    # Set ticks and labels
    plt.xticks(ticks=np.arange(len(months)), labels=months, rotation=45)
    plt.yticks(ticks=np.arange(len(schools_name)), labels=schools_name)
    plt.title("Heatmap of Random Data for Schools Across Months")
    
    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf8')
    plt.close()  # Close the plot to free up memory

    # Embed the image in HTML
    html = f"""
    <html>
    <body>
        <h1>Heatmap of Random Data for Schools</h1>
        <img src="data:image/png;base64,{img_base64}" alt="Heatmap"/>
    </body>
    </html>
    """
    return render_template_string(html)
