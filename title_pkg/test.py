import random

def random_exercise(exercise_list):
    random_select = random.randint(0, len(exercise_list) - 1)
    return exercise_list[random_select]

def random_sample_exercise(exercise_list, n):
    return random.sample(exercise_list, n)

def program_template():
    lb_acc = ['Good Mornings', 'Hip Thrust', 'Romanian Deadlift', 'Barbell Pendlay Rows', 'Sissy Leg Press', 'Hip Abductors', 'Hip Adductors', 'Hamstring Curl', 'Leg Extension', 'Calf Raises']
    
    # Sample four random accessories
    random_accessories = random_sample_exercise(lb_acc, 4)
    print('\n   Accessories:\n   ' + sets('acc_sets') + '\n   ' + '\n   '.join(random_accessories))

'''# Ensure a valid `sets` function exists
def sets(param):
    return "Set Info"  # Adjust this with the actual implementation'''

program_template()