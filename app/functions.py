from question import Question

from random import randint, choice, randrange


def generate_random_data():
    return [[randint(0, 2000) for _ in range(12)] for _ in range(10)]

def generate_random_answer(answer):
    answer_choice = [None] * 4 
    answer_pos = randint(0, 3)
    answer_choice[answer_pos] = answer

    for i in range(4):
        if i != answer_pos:
            while True:
                plus_minus = randint(0, 1)
                if plus_minus == 0:
                    answer_calc = answer - randrange(10, 100, 5)
                else:
                    answer_calc = answer + randrange(10, 100, 5)
                    
                if answer_calc not in answer_choice and answer_calc >= 0:
                    answer_choice[i] = answer_calc
                    break

    return answer_choice, answer_pos

def generate_random_answer_class(answer):
        answer_choice = [None] * 4
        answer_choice[0] = answer

        for i in range(1, 4):
            while True:
                plus_minus = randint(0, 1)
                if plus_minus == 0:
                    answer_calc = answer - randrange(1, 10)
                else:
                    answer_calc = answer + randrange(1, 10)
                        
                if answer_calc not in answer_choice and answer_calc > 0 and answer_calc <= 10: 
                    answer_choice[i] = answer_calc
                    break

        answer_choice.sort()
        answer_pos = answer_choice.index(answer)

        for i in range(4):
            answer_choice[i] = "School " + str(answer_choice[i])

        return answer_choice, answer_pos

def generate_random_answer_month(answer ,month):

    answer_choice = [None] * 4
    answer_choice[0] = answer

    for i in range(1, 4):
        while True:
            plus_minus = randint(0, 1)
            if plus_minus == 0:
                answer_calc = answer - randrange(0, 11)
            else:
                answer_calc = answer + randrange(0, 11)
                    
            if answer_calc not in answer_choice and answer_calc >= 0 and answer_calc <= 11: 
                answer_choice[i] = answer_calc
                break

        answer_choice.sort()
        answer_pos = answer_choice.index(answer)
        
        for i in range(4):
            answer_choice[i] = month[answer_choice[i]]

        return answer_choice, answer_pos

def question_generator(random_data):
    question_num = 10

    school_num = randint(1, 10)
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October","November", "December"]
    month_choice = choice(month)

    if question_num == 1:    
        question = f"What is the number of students absent in School {school_num} for the month {month_choice}?"
        answer = random_data[school_num-1][month.index(month_choice)]

        answer_choice, answer_pos = generate_random_answer(answer)

        return Question(question, answer, answer_pos, answer_choice)
    
    if question_num == 2:
        question = f"What is the maximum number of students absent in School {school_num}?"
        print(random_data[school_num-1])
        answer = max(random_data[school_num-1])

        answer_choice, answer_pos = generate_random_answer(answer)

        return Question(question, answer, answer_pos, answer_choice)
    
    if question_num == 3:
        question = f"What is the minimum number of students absent in School {school_num}?"
        print(random_data[school_num-1])
        answer = min(random_data[school_num-1])

        answer_choice, answer_pos = generate_random_answer(answer)

        return Question(question, answer, answer_pos, answer_choice)
    
    '''
    if question_num == 4:
        month_copy = month.copy()
        month_copy.pop(month.index(month_choice))
        month_other = choice(month_copy)
        question = f"Were absences in School {school_num} higher in the month of {month_choice} compared to the month of {month_other}?"

        return question
    
    if question_num == 5:
        month_copy = month.copy()
        month_copy.pop(month.index(month_choice))
        month_other = choice(month_copy)
        question = f"Were absences in School {school_num} lower in the month of {month_choice} compared to the month of {month_other}?"

        return question
    
    '''

    if question_num == 6:
        question = f"Which school had the highest number of students absent in the month of {month_choice}?"

        new_list = [random_data[i][month.index(month_choice)] for i in range(10)]
        answer = new_list.index(max(new_list)) + 1

        answer_choice, answer_pos = generate_random_answer_class(answer)
            
        return Question(question, answer, answer_pos, answer_choice)

    
    if question_num == 7:
        question = f"Which school had the lowest number of students absent in the month of {month_choice}?"
        new_list = [random_data[i][month.index(month_choice)] for i in range(10)]
        answer = new_list.index(min(new_list)) + 1

        answer_choice, answer_pos = generate_random_answer_class(answer)
            
        return Question(question, answer, answer_pos, answer_choice)
    
    if question_num == 8:
        question = f"Which month has the lowest number of total absences?"

        new_list = [sum(random_data[i][month] for i in range(10)) for month in range(12)]
        print(new_list)
        month_choosen_num = new_list.index(min(new_list))
        answer = month[new_list.index(min(new_list))]

        answer_choice = [None] * 4
        answer_choice[0] = month_choosen_num
        for i in range(1, 4):
            while True:
                plus_minus = randint(0, 1)
                if plus_minus == 0:
                    answer_calc = month_choosen_num - randrange(0, 11)
                else:
                    answer_calc = month_choosen_num + randrange(0, 11)
                    
                if answer_calc not in answer_choice and answer_calc >= 0 and answer_calc <= 11: 
                    answer_choice[i] = answer_calc
                    break

        answer_choice.sort()
        
        for i in range(4):
            answer_choice[i] = month[answer_choice[i]]

        print(answer_choice)
        print(answer)
        answer_choice, answer_pos = generate_random_answer(month_choosen_num)
        return   
        #return Question(question, answer, answer_pos, answer_choice)

    if question_num == 10:
        question = f"Which month has the highest number of total absences?"
        new_list = [sum(random_data[i][month] for i in range(10)) for month in range(12)]
        print(new_list)
        month_choosen_num = new_list.index(max(new_list))
        answer = month[new_list.index(max(new_list))]

        answer_choice = [None] * 4
        answer_choice[0] = month_choosen_num
        for i in range(1, 4):
            while True:
                plus_minus = randint(0, 1)
                if plus_minus == 0:
                    answer_calc = month_choosen_num - randrange(0, 11)
                else:
                    answer_calc = month_choosen_num + randrange(0, 11)
                    
                if answer_calc not in answer_choice and answer_calc >= 0 and answer_calc <= 11: 
                    answer_choice[i] = answer_calc
                    break

        answer_choice.sort()
        
        for i in range(4):
            answer_choice[i] = month[answer_choice[i]]

        print(answer_choice)
        print(answer)
        answer_choice, answer_pos = generate_random_answer(month_choosen_num)

        return   

    
question_generator(generate_random_data())
#ques1 = question_generator(generate_random_data())
#print(str(ques1.question) + "\n" + str(ques1.answer_choice) + "\n" + str(ques1.answer_pos) + "\n" + str(ques1.answer))

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
