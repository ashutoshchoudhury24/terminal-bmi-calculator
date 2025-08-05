'''                                   BMI CALCULATOR                                                     
'''




"""


::: TEST CASES APPLIED :::

            1> You can enter 'exit' to exit from the mid screen where ever you present at the time and it will set the screen to default.
            2> you can't enter other texts with out 'exit'.
            3> You can only enter the given options [1,2,3], because there are only 3 options are available for this program.
                                    'Weight' = { 1 : 'Kilogram',
                                                 2 : 'Pound',
                                                 3 : 'gram'}
                                        
                                    'Height' = { 1 : 'Feet',
                                                 2 : 'Centimeter',
                                                 3 : 'Meter'}

            4> If you enter anything other than the given options, the program will keep asking for the same input repeatedly until you type 'exit' to return to the start screen.

            5> Whatever you enter in the options (if they are valid inputs) for each category will be displayed at the top. As you enter the next parameters, the display will update automatically.

            
            

::: WARNING :::

            --> Emojis have been used in this file. To run the code properly, please save the file as a Python file (.py).
            --> Otherwise, you can use "--" symbol in front of each comment to comment it out if it's not behaving like a comment, or simply remove the emojis.


            
"""





######## LIBRARIES IMORTED

import os
import time





########## FUNCTION DEFINITION AREA


####### function - 1

def is_float(value):

    try:
        float(value)
        return True
    except ValueError:
        return False
    




####### Function - 2

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')






####### Function - 3

def header_with_entries(weight_unit_01 = 'None', weight_02 = 'None', height_unit_03 = 'None', height_04 = 'None', weight_unit_dict_05 = {1 : 'kilogram', 2 : 'pound', 3 : 'gram'}, height_unit_dict_06 = {1 : 'feet', 2 : 'centimeter', 3 : 'meter'}):

    clear_screen() 
    print("\t\t\t\t\tBMI CALCULATOR\n\t\t\t\t       ----------------\n\n")

    if weight_unit_01 == weight_02 == height_unit_03 == height_04 == 'None':
            print(f'''Entered weight unit : {weight_unit_01}
Entered weight : {weight_02}
Entered height unit : {height_unit_03}
Entered height : {height_04}\n\n''')
            
    elif weight_02 == height_unit_03 == height_04 == 'None':
        print(f'''Entered weight unit : {weight_unit_dict_05.get(weight_unit_01)}
Entered weight : {weight_02}
Entered height unit : {height_unit_03}
Entered height : {height_04} \n\n''')
            
    elif height_unit_03 == height_04 == 'None':
        print(f'''Entered weight unit : {weight_unit_dict_05.get(weight_unit_01)}
Entered weight : {weight_02} {weight_unit_dict_05.get(weight_unit_01)}
Entered height unit : {height_unit_03} 
Entered height : {height_04} \n\n''')
            
    elif height_04 == 'None':
        print(f'''Entered weight unit : {weight_unit_dict_05.get(weight_unit_01)}
Entered weight : {weight_02}  {weight_unit_dict_05.get(weight_unit_01)}
Entered height unit : {height_unit_dict_06.get(height_unit_03)}
Entered height : {height_04} \n\n''')

    else:
        print(f'''Entered weight unit : {weight_unit_dict_05.get(weight_unit_01)}
Entered weight : {weight_02}  {weight_unit_dict_05.get(weight_unit_01)}
Entered height unit : {height_unit_dict_06.get(height_unit_03)}
Entered height : {height_04} {height_unit_dict_06.get(height_unit_03)}  \n\n''')






####### Function - 4

def header_with_clrscr():
    clear_screen() 
    print("\t\t\t\t\tBMI CALCULATOR\n\t\t\t\t       ----------------\n\n")











########## PROGRAM AREA



weight_unit_dict = {1 : 'kilogram', 2 : 'pound', 3 : 'gram'}
height_unit_dict = {1 : 'feet', 2 : 'centimeter', 3 : 'meter'}
weight = height = 'EMPTY'






while True:

    header_with_entries()


    ##### For selecting the weight

    while True:

        
        weight_unit = input('Select the unit of weight...\nChoose \'1\' to enter the weight in "kilogram" and \'2\' for enter the weight in "pound" and \'3\' for enter the weight in "gram"...\n\nPlease enter your choice ☺️  : ')


        ### Checking the selection of units by the user is valid or not.

        if ( is_float(weight_unit)==True ) and ( int(weight_unit) in [1,2,3] ):
            
            weight_unit = int(weight_unit)

            header_with_entries(weight_unit)



            ### Taking the weight of the user

            while True :                     

                weight = input(f'\nEnter your weight (numbers only) in {weight_unit_dict.get(weight_unit)} or enter "exit" to exit ☺️  : ')


                ### Checking the user entry               

                if is_float(weight) == True :

                    weight = float(weight)

                    ### Convert the weight in to kilogram (kg)

                    if weight_unit == 1:
                        final_weight = weight

                    elif weight_unit == 2:
                        final_weight = (weight *  0.45359237)

                    elif weight_unit == 3:
                        final_weight = (weight/100)

                    break
                

                elif weight.lower() == 'exit':
                    break


                else:
                    header_with_entries(weight_unit)

                    print("Please re-enter a valid weight (only numbers) 😵‍💫😵‍💫😵‍💫.....\n\n")

            break

        elif weight_unit.lower() == 'exit':
            break

        else :
            header_with_entries()
            print("Please re-enter a valid option for weight 😵‍💫😵‍💫😵‍💫.....\n\n")
            








    ##### For selecting the height

    if str(weight).lower() !='exit' and is_float(weight)== True:
        header_with_entries(weight_unit, weight)

        while True:

            height_unit = input('\n\nSelect the unit of height...\nChoose \'1\' to enter the height in "feet" and \'2\' for entering the height in "centimeter" and \'3\' for entering the height in "meter"...\n\nPlease enter your choice ☺️  : ')





            ### Checking the selection of units by the user is valid or not

            if ( is_float(height_unit)==True ) and ( int(height_unit) in [1,2,3] ):

                height_unit = int(height_unit)

                header_with_entries(weight_unit, weight, height_unit)



                ### Taking the height of the user

                while True : 


                    height = input(f'\n\nEnter your height (numbers only) in {height_unit_dict.get(height_unit)} or enter "exit" to exit ☺️  : ')


                    ### Checking the user entry

                    if is_float(height) == True :

                        height = float(height)


                        ### Convert the height in to meter (m) 

                        if height_unit == 1:
                            final_height = height*0.3048

                        elif height_unit == 2:
                            final_height = height/100

                        elif height_unit == 3:
                            final_height = height


                        header_with_entries(weight_unit, weight, height_unit, height)
                        


                        ### checking the BMI value and classify them in the categories.
                        
                        BMI = final_weight/(final_height)**2


                        if BMI < 18.5:
                            print(f'\n\n\nYour BMI is {round(BMI,2)} and you fall into the underweight category 😐😐😐.\n\n\n')

                        elif  BMI < 25:
                            print(f'\n\n\nYour BMI is {round(BMI,2)} and you fall into the normal category 😊😊😊.\n\n\n')

                        elif BMI < 30:
                            print(f'\n\n\nYour BMI is {round(BMI,2)} and you fall into the overweight category 😐😐😐.\n\n\n')

                        elif BMI >=  30:
                            print(f'\n\n\nYour BMI is {round(BMI,2)} and you fall into the obesity category 😶😶😶.\n\n\n')


                        weight = height = 'EMPTY'
                        final_weight = final_height = 0

                        
                        ### It will automatically clear the screen and break the loop and reset to the 1st output screen

                        print(f"Please wait for few seconds, the screen will be automatically reset...")

                        for i in range(15, 0, -1):
                            print(f"\t\t\t\t\t\t\t{i} ", end="\r")
                            time.sleep(1)

                        header_with_clrscr()
                        break

                    elif height.lower() == 'exit':
                        break

                    else:

                        header_with_entries(weight_unit, weight, height_unit)
                        print("\n\n\nPlease re-enter a valid height (only numbers) 😵‍💫😵‍💫😵‍💫.....\n\n")


                break

            elif height_unit.lower() == 'exit':
                break

            else:
                header_with_entries(weight_unit, weight)
                print("\n\n\nPlease re-enter a valid option for height 😵‍💫😵‍💫😵‍💫.....\n\n")

            
