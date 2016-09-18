def return_classes(color, color_order):
    try:
        return color.split('/')[color_order] 
    except:
        return 'None'





def to_days(column):
    age_list = []
    for age in column:  
        try:
            time_span = age.split(' ')[1]
            number = int(age.split(' ')[0])

            if time_span == 'years' or time_span == 'year':
                age_list.append(number * 365)
            elif time_span == 'months':
                age_list.append(number * 30)
            elif time_span == 'weeks' or time_span == 'week':
                age_list.append(number*7)
            else:
                age_list.append(number)
        except:
            age_list.append(age)
    return age_list 



def in_dict(breed, dictionary):
    if 'Shepherd' in breed:
        name = 'Shepherd'
    elif 'Hound' in breed:
        name = 'Hound'
    elif 'Terrier' in breed:
        name = 'Terrier'
    elif 'Poodle' in breed:
        name = 'Poodle'
    elif 'Pointer' in breed:
        name = 'Pointer'
    elif 'Bulldog' in breed:
        name = 'Bulldog'
    elif 'Coonhound' in breed:
        name = 'Hound'
    elif 'Staffordshire' in breed:
        name = 'Terrier'
    else:
        name = breed
        
    try:
        return dictionary[name]
    except:
        return 'other'

