def whole_module():
    from effects import typewriter, clear_screen
    
    def info_title():
        print('Press and enter the corresponding numbers to review each category.')

    def display_options():
        info_title()
        print('\n1. Max Effort')
        print('2. Dynamic Effort')
        print('3. Phase 1')
        print('4. Phase 2')
        print('5. Phase 3')
        print('6. Deload Week')
        print('7. Return To Main Screen')

    def show_max_effort():
        typewriter(
            "\nMax Effort is divided into two seperate workouts per week. You will choose variants of training your Bench Press or OHP on Upper Body days, and variants of your Squat or"
            "\nDeadlift on Lower Body days. Each week you will rotate what you specify in. I.E. Week 1: Max Effort - Upper Body, you will train Bench variants. For Max Effort - Lower Body,"
            "\nyou will train Squat variants. Week 2: you will rotate and train OHP variants on Upper Body, and Deadlift variants on Lower Body.")
        
    def show_dynamic_effort():
        typewriter(
            "\nDynamic Effort is divided into two seperate workouts per week. You will train both normal variants of all your lifts on these days. Like Max Effort, you will also have Upper"
            "\nand Lower Body days. I.E. Week 1: Dynamic Effort - Upper Body, you will train both Bench and OHP. For Dynamic Effort - Lower Body, you will train both Squat and Deadlift."
            "\nYou will train with accommodating resistance on top of straight weight. Straight weight will equate to 40% of your 1RM during Week 1. Your percentage will increase 5% every"
            "\nweek until Week 4, where you will then reach your deload week."
                    
            "\n\nWhat is accomodating resistance? Accommdating resistance is a technique that increases the resistance of your lift as the range of motion increases. I.E. adding resistance"
            "\nbands or chains to the barbell. With accommodating resistance, your mindset on Dynamic Effort days is to focus on speed/explosiveness, form and volume. If you do not have"
            "\naccess to accommodating resistance, you will work between 50-70% of your 1RM. Be mindful of your bar speed. If you are not explosive enough on your sets, decrease the"
            "\nweight. You don't want to overshoot, since you want to preserve your strength for your Max Effort Days. Complete 10 sets of 5 reps for all main lifts on these days.")
        
    def show_phase_1():
        typewriter(
            "\nIn the 1st phase, you will having working sets of 5RM Max Effort days. Your 5RM will change from week to week depending how you are feeling that day. Be mindful not to"
            "\novershoot your rep range during any of your phases. Build strength, do not chase ego. After your main variant sets are complete, you will move on to accessory exercises that"
            "\nwill help build strength and support your main lifts.")
        
    def show_phase_2():
        typewriter(
            "\nIn the 2nd phase, you will repeat the same cycle as the previous phase, the only difference is that you will now be working towards a 3RM during your Max Effort days.")
        
    def show_phase_3():
        typewriter(
            "\nIn the 3rd phase, you will repeat the same cycle as the previous phase, except you will now start training the standarad lift or variants that resemble very closely to"
            "\nthe standard lift. You will now be working towards a 1RM on your sets. You want to train around 90% of your 1RM. Percentages can fluctuate as you may be able to PR during"
            "\ntraining and move past your current 1RM at this point. Your reps should not feel slow, or grindy. You want to maintain a strong and explosive rep. Do not overshoot as your"
            "\nmax out day is right around the corner.")
        
    def show_phase_4():
        typewriter(
            "\nIn the 2nd phase, you will repeat the same cycle as the previous phase, the only difference is that you will now be working towards a 3RM during your Max Effort days.")
        
    def show_deload_week():
        typewriter(
            "\nDeload will occur every 4 weeks. During this week you will decrease the weight and increase volume on both Max Effort and Dynamic days. You will also train both standard" 
            "\nlifts on Max Effort days, like you do on Dynamic days. The idea of this week is to get your body acclaimated to move into the next phase without overtraining.")

    def info():
        while True:
            clear_screen()
            display_options()
            choice = input('\nSelect your option: ')

            if choice == '1':
                clear_screen()
                display_options()
                show_max_effort()
                input('\nPress any key to continue...')

            elif choice == '2':
                clear_screen()
                display_options()
                show_dynamic_effort()
                input('\nPress any key to continue...')

            elif choice == '3':
                clear_screen()
                display_options()
                show_phase_1()
                input('\nPress any key to continue...')

            elif choice == '4':
                clear_screen()
                display_options()
                show_phase_2()
                input('\nPress any key to continue...')

            elif choice == '5':
                clear_screen()
                display_options()
                show_phase_3()
                input('\nPress any key to continue...')

            elif choice == '6':
                clear_screen()
                display_options()
                show_deload_week()
                input('\nPress any key to continue...')

            elif choice =='7':
                from title import title, options
                title()
                options()
                break
            else:
                typewriter('\nInvalid command.')
                input('\nPress any key to continue...')

    info()
whole_module()