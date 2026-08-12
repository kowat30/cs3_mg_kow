def calculate_space_weight(earth_weight, destination):
    destination = destination
    if destination == 'mars':
        return earth_weight * 0.38
    elif destination == 'jupiter':
        return earth_weight * 2.34
    elif destination == 'moon':
        return earth_weight * 0.16
    elif destination == 'venus':
        return earth_weight * 0.91
    else:
        print("Destination is not valid")
       
print(calculate_space_weight(3, 'jupiter'))

