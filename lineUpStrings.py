def line_up(name, number):
    num = str(number)
    if num.endswith('1') and not num.endswith('11'):
        return (f'{name}, you are the {number}st customer we serve today. Thank you!')
    elif num.endswith('2') and not num.endswith('12'):
        return (f'{name}, you are the {number}nd customer we serve today. Thank you!')
    elif num.endswith('3') and not num.endswith('13'):
        return (f'{name}, you are the {number}rd customer we serve today. Thank you!')
    else:
        return (f'{name}, you are the {number}th customer we serve today. Thank you!')
