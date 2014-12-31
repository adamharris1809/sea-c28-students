def get_user_input(prompt, *donor_list, validator = X, Y, or Z selection):
    """Prompt user to Send a Thank You, Create a Report, or Exit. Validate that the user
    selects one or the other.
    """

    if not donor_list:
        donor_list = ["None", "None"] #Needs enumerated

    if prompt = thankyou:
        dollar_input = "False" #Resets the variable for error testing variable with each iteration.
        name_input = raw_input(u"Enter 'list' for list or Enter the recipient's full name. ")
        if name_input = 'list':
            print(donor_list)
        else:
            if name_input in donor_list: #If name exists in list.
                for count in donor_list:
                    if name_input = donor_list[count]:
                        while int(dollar_input.isnumeric()) = False #Validating dollar amount.
                            dollar_input = int(raw_input(u"Enter a dollar amount."))
                        donor_list.insert(count, dollar_input) #Inserting dollar input next to name -- do this in a dictionary instead.
            else:
                donor_list.append(name_input) #If name doesn't exist in list
                while int(dollar_input.isnumeric()) = False #Validating dollar amount.
                    dollar_input = int(raw_input(u"Enter a dollar amount."))
                donor_list.insert(count, dollar_input) #Inserting dollar input next to name -- do this in a dictionary instead.

            email_input = raw_input(u"Compose a brief thank you email to %s. " % name_input)

        print(email_input)
        get_user_input()

    elif prompt == 'Exit'
        return

    else:
        #Look up all names and corresponding donations in dictionary.
        #Create list of the donors and donations from dictionary.
        #Create separate sort function that sorts all donations by highest value.
        #Create separate sort function that sums all donations.
        print(donor_report)