from effects import typewriter, clear_screen

#title-art
def title():
    print("""                    ____                          ___ ______  _                ____                                           ______                           __           
                   / __ \____ _      _____  _____/ (_) __/ /_(_)___  ____ _   / __ \_________  ____ __________ _____ ___     / ____/__  ____  ___  _________ _/ /_____  _____        
        ______    / /_/ / __ \ | /| / / _ \/ ___/ / / /_/ __/ / __ \/ __ `/  / /_/ / ___/ __ \/ __ `/ ___/ __ `/ __ `__ \   / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/  ______
        /_____/  / ____/ /_/ / |/ |/ /  __/ /  / / / __/ /_/ / / / / /_/ /  / ____/ /  / /_/ / /_/ / /  / /_/ / / / / / /  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /     /_____/                     
                /_/    \____/|__/|__/\___/_/  /_/_/_/  \__/_/_/ /_/\__, /  /_/   /_/   \____/\__, /_/   \__,_/_/ /_/ /_/   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/             
                                                                  /____/                    /____/                                                                                   """)
    print("""\n
                                                                            /   ,@(                                                                      
                                                                            @(                                                                             
                                                                            .                                                                              
                                                                            &   @@@@  (                                                                     
                                                                            .@@@@@@@*   .,#                                                                 
                                                                            (@@@@@@@#/                                                                   
                                                                            @@/@@@@@                                                                      
                                                                            %  ,%               .                                                         
                                                                            @       /             \                                                       
                                                                            *@     #@,&  @@ # ,*@@@                                                        
                                                                        (@ @@/@@ @@@,@@@@@                                                               
                                                                        @&@@@ @@@@@@@@/@@@    (   (                                                       
                                                                        @@@@@  @@@@@@@@@@    *    @                                                      
                                                                            ,#@@    *,@@@@@@@  *,   &&,                                                     
                                                                            #@     ( @@@@@@@%/    * #*@                                                   
                                                                        #  /@@/       #@@@@@@@         #@(                                                 
                                                                        ,   @@      *@@@@@@@@@      %     @                                                
                                                                        @   @        .@@@@@@@@@     .&/     &                                             
                                                                            &@@/  /@@@&@@@@&@&&    &@%*  @@&#                   @@@@@@@@@@@@@@         
                                                    @@@@@@@@%/          @   .&   *,&@@@@&@&@@  ,   @        &     ,        #       *        &@@@@@@/       
                                        /         @@@##,@@&@@@@@         .   @      *(@@@@@(    %.. @         %   .        @  /        @    @@@@@@@@@       
                                    .    /    .@@@(. % #.@@@@@@,       .   @      @@@@.        /  ,             % @ &   @ @@,   @   @    @@@@@@@@@@@ @     
                                        #.,. @@#@@,    (   %@@@@@@(    ..     , *@@(   %@@@@@@@@@,  .      %     .@/%,  @& @@# ,,  @ @%# ,@@@@@@@@@@@ @     
                                    @@(@@@@@@@@@@   /@   %@@@@@@       (@@@.@@@@   *#%, #..*.*, @ ,             @@@@@@@@@@@@,@,@*,.@%@@*@@@@@@@&,,,,, @     
                                    ,@@@@@@@@@@@@/@@@@@@@@@@@@@          *@@@@@                    .@     @@#   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  &    @     
                                    @@@@@@@@@@@@@@@@@@@@@@@@@.       (  @@@@@@                    &@*@@ .@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ (@# @@ @   
                                        @@@@@@@@@@@@@@@@@@@@@@@         *  @@@@@@                     &(  ,@@@@*  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
                                        @@@@@@@@@@@@@@@@@@             @@@@@@@                       @/ .@@@@.  .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
                                                                    , @@@@@                          @.@@@@.    /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
                                                                        @/@@@                          .@ /@@&       .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        
                                                                    @*@@@@                             (@@@              .@@@@@@@@@@@@@@@@@@@@@@@         
                                                                    *@@@%/&@,                           @@@@                                               
                                                                (      @@@@@@&                          /@@@@@                                              
                                                            (@@@@@@@@@@@@@@,                            %   &,#                                             
                                                                                                            .*&                                               
                                                                                                        #&    .#@                                            
                                                                                                          @@@@@*#                                            """)

    #intro
    print(
        "\n\nWelcome to the Powerlifting Program Generator. This generator follows the 'Conjugate Method'. What is the Conjugate Method? It is a program that mixes in different variants"
        "\nof the Squat, Bench, Deadlift, and Overhead Press (OHP). The ultimate goal is to progress your strength in all areas, and take your 1RM (Rep Max) to the next level."

        "\n\nThis strength program spans 12 weeks. Every week you will have a total of 4 workouts. 2 'Max Effort' days and 2 'Dynamic Effort' days, both which contain 'Upper Body' and"
        "\n'Lower Body' workouts. Think of Max Effort as your heavy day and Dynamic Effort as your light day. There are 3 phases within this program which will last 4 weeks"
        "\nindividually."

        "\n\nPress 1 and enter to generate your powerlifting program template." 
        "\nPress 2 and enter to review information on how this program works."
        "\nPress 3 and enter to exit the generator.")

#options
def options():
    while True:
        title()
        print(
            '\n\n1. Generate'
            '\n2. Info'
            '\n3. Exit')
        choice = input('\nSelect your option: ')

        if choice == '1':
            typewriter('\nGenerating program ...')
            

        elif choice == '2':
            from info import whole_module
            whole_module()
        
        elif choice == '3':
            print('\nExiting generator...')
            exit()

        else:
            typewriter('\nInvalid command.')
            input('\nPress any key to continue...')
            clear_screen()

options()