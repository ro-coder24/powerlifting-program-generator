import random

#sets
def sets(option):
    set_reps = {
        'me_sets': '5 Sets of 5 Reps',
        'de_sets': '10 Sets of 5 Reps',
        'acc_sets': '3-4 Sets of 8-10 Reps'
    }
    return set_reps.get(option, 'Invalid Option')

#randomizer
def random_exercise(exercise_list):
    random_select = random.randint(0, len(exercise_list) -1)
    return exercise_list[random_select]

def random_sample_exercise(exercise_list, n):
    return random.sample(exercise_list, n)

def program_template():
    #list-of-exercises
    me_ub_variant = ['Half Board Press', 'Pause Bench', 'Rack Press', 'Tempo Bench', 'Push Press', 'Rack OHP', 'Seated Barbell Shoulder Press', 'Tempo OHP']
    st_ub = ['Bench Press', 'OHP']
    me_lb_variant = ['Pause Squat', 'Box Squat', 'Front Squat', 'Tempo Squat', 'Deficit Deadlift', 'Block Pull', 'Pause Deadlift', 'Dorian Deadlift']
    st_lb = ['Squat', 'Deadlift']
    ub_acc = ['Face Pulls', 'Rear Delt Flyes', 'Bench Grip Cable Row', 'Lat Pulldown', 'Tricep Pushdown', 'Tricep Dips', 'Hammer Curls', 'Strict Curls', 'Kettlebell Halos']
    lb_acc = ['Good Mornings', 'Hip Thrust', 'Romanian Deadlift', 'Barbell Pendlay Rows', 'Sissy Leg Press', 'Hip Abductors', 'Hip Adductors', 'Hamstring Curl', 'Leg Extension', 'Calf Raises']

    #print-random-exercises-from-each-list
    print('\nMax Effort - Upper Body:\n' + random_exercise(me_ub_variant))

    print('\nMax Effort - Lower Body:\n' + random_exercise(me_lb_variant))

    print('\nDynamic Effort - Upper Body:\n' + sets('de_sets') + '\n\n' + st_ub[0], '\n' + st_ub[1])

    print('\n   Accessories:\n' + '   ' + sets('acc_sets') + '\n' + '   ' + '\n' + '   ' + random_exercise(ub_acc))

    print('\nDynamic Effort - Lower Body:\n' + sets('de_sets') + '\n\n' + st_lb[0], '\n' + st_lb[1])

    random_accessories = random_sample_exercise(lb_acc, 4)
    print('\n   Accessories:\n' + '   ' + sets('acc_sets') + '\n' + '   ' + '\n' + '   '.join(random_accessories))

program_template()
