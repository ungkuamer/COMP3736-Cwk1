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


def generate_random_answer_month(answer, month):
    answer_choice = [None] * 4
    answer_choice[0] = answer

    for i in range(1, 4):
        while True:
            plus_minus = randint(0, 1)
            if plus_minus == 0:
                answer_calc = answer - randrange(0, 11)
            else:
                answer_calc = answer + randrange(0, 11)

            if answer_calc not in answer_choice and 0 <= answer_calc <= 11:
                answer_choice[i] = answer_calc
                break

    answer_choice.sort()

    answer_pos = answer_choice.index(answer)
    answer_choice = [month[i] for i in answer_choice]

    return answer_choice, answer_pos


def question_generator(random_data):
    question_num = randint(1, 7)

    school_num = randint(1, 10)
    month = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
    month_choice = choice(month)

    if question_num == 1:
        question = f"What is the number of students absent in School {school_num} for the month {month_choice}?"
        answer = random_data[school_num-1][month.index(month_choice)]

        answer_choice, answer_pos = generate_random_answer(answer)

        return Question(question, answer_pos, answer_choice)

    if question_num == 2:
        question = f"What is the maximum number of students absent in School {school_num}?"
        print(random_data[school_num-1])
        answer = max(random_data[school_num-1])

        answer_choice, answer_pos = generate_random_answer(answer)

        return Question(question, answer_pos, answer_choice)

    if question_num == 3:
        question = f"What is the minimum number of students absent in School {school_num}?"
        print(random_data[school_num-1])
        answer = min(random_data[school_num-1])

        answer_choice, answer_pos = generate_random_answer(answer)

        return Question(question, answer_pos, answer_choice)

    if question_num == 4:
        question = f"Which school had the highest number of students absent in the month of {month_choice}?"

        new_list = [random_data[i][month.index(
            month_choice)] for i in range(10)]
        answer = new_list.index(max(new_list)) + 1

        answer_choice, answer_pos = generate_random_answer_class(answer)

        return Question(question, answer_pos, answer_choice)

    if question_num == 5:
        question = f"Which school had the lowest number of students absent in the month of {month_choice}?"
        new_list = [random_data[i][month.index(
            month_choice)] for i in range(10)]
        answer = new_list.index(min(new_list)) + 1

        answer_choice, answer_pos = generate_random_answer_class(answer)

        return Question(question, answer_pos, answer_choice)

    if question_num == 6:
        question = f"Which month has the lowest number of total absences?"

        new_list = [sum(random_data[i][month] for i in range(10))
                    for month in range(12)]
        print(new_list)
        month_choosen_num = new_list.index(min(new_list))
        answer = month[new_list.index(min(new_list))]

        answer_pos, answer_choice = generate_random_answer_month(
            month_choosen_num, month)

        return Question(question, answer_pos, answer_choice)

    if question_num == 7:
        question = f"Which month has the highest number of total absences?"
        new_list = [sum(random_data[i][month] for i in range(10))
                    for month in range(12)]
        print(new_list)
        month_choosen_num = new_list.index(max(new_list))

        answer_pos, answer_choice = generate_random_answer_month(
            month_choosen_num, month)

        return Question(question, answer_pos, answer_choice)
