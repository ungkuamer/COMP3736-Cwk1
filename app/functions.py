from random import randint

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

def generate_random_data():
    schools = [[0 for i in range(12)] for j in range(10)]
    for i in range(10):
        for j in range(12):
            schools[i][j] = randint(0, 2000)

    return schools


# Heatmap
'''
schools_name = ["School " + str(i) for i in range(10)]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

fig, ax = plt.subplots()
school_data = np.array(generate_random_data())
im = ax.imshow(school_data)

ax.set_xticks(np.arange(len(months)))
ax.set_yticks(np.arange(len(schools_name)))
ax.set_xticklabels(months)
ax.set_yticklabels(schools_name)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(schools_name)):
    for j in range(len(months)):
        text = ax.text(j, i, school_data[i][j], ha="center", va="center", color="w")

ax.set_title("Number of Students Absents across Schools in Hogwarts")
fig.tight_layout()
plt.show()

'''

'''
school_data = generate_random_data()
months = list(range(1, 13))  # Represent months as numbers (1 to 12)

# Plotting the scatter plot
plt.figure(figsize=(10, 6))

for i, school in enumerate(school_data):
    # Use school number as the identifier for color/marker, or leave them all the same
    plt.scatter(months, school, label=f'School {i}', alpha=0.7)  # alpha for transparency

# Customize the plot
plt.xlabel("Month")
plt.ylabel("Random Value")
plt.title("Scatter Plot of Random Data for Schools Across Months")
plt.xticks(months, ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))
plt.show()
'''
