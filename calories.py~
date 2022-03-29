# calories.py offers helper functions to calculate BMI, BMR and AMR

def get_BMI(kg, cm):
    '''
    calculate the person's BMI

    >>> '%.2f' % get_BMI(90, 180)
    '27.78'
    
    '''

    BMI =  kg / (cm / 100) ** 2
    return BMI

def get_BMR(sex, kg, cm, age):
    '''
    calculate the BMR of a person (minimum level of energy in rest)

    >>> '%.2f' % get_BMR('m', 90, 180, 30)
    '2001.86'
    '''
    
    if sex == 'f':
        BMR = 655.1 + (9.563 * kg) + (1.850 * cm) - (4.676 * age)
    elif sex == 'm':
        BMR = 66.47 + (13.75 * kg) + (5.003 * cm) - (6.755 * age)
    else:
        return None
    return BMR
  
def get_AMR(sex, kg, cm, age, activity):
    '''
    calculate AMR based on activity level. 5 levels: sedentary, light,
    moderate, active, very active

    >>> '%.2f' % get_AMR('m', 90, 180, 30, 2)
    '2752.56'
    '''

    BMR = get_BMR(sex, kg, cm, age)
    
    if activity == 1:
        AMR = BMR * 1.2
    if activity == 2:
        AMR = BMR * 1.375
    if activity == 3:
        AMR = BMR * 1.55
    if activity == 4:
        AMR = BMR * 1.725
    if activity == 5:
        AMR = BMR * 1.9
    return AMR


def is_good_BMI(kg, cm):
    '''return True if BMI between 18.5 and 24.9

    >>> is_good_BMI(70, 180)
    True
    '''

    BMI = get_BMI(kg, cm)
    if 18.4 < BMI < 25:
        return True
    return False

def is_obese(kg, cm):
    ''' return True if BMI > 30

    >>> is_obese(100, 180)
    True
    '''

    BMI = get_BMI(kg, cm)
    if BMI > 29.9:
        return True
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
