# Defines
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

# Code
print("В команде Мастера кода участников: %s !" % team1_num)
print("В команде Волшебники данных участников: %s !" % team2_num)
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s !" % {'team1_num': team1_num, 'team2_num': team2_num})
print("Команда Мастера кода решила задач: {} !".format(score_1))
print("Мастера кода решили задачи за {} с !".format(team1_time))
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {} с !".format(team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')

# Calculation of result
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = "Победа команды Волшебники Данных!"
else:
    challenge_result = "Ничья!"

# Calculation of stats
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!.')