largest = None
smallest = None

while True :
    nums = input('Enter an integer: ')
    if nums == 'done' :
        break
    try:
        num = int(nums)
    except:
        print('Invalid input')
        continue
    if largest is None :
        largest = num
        smallest = num
    else :
        if num > largest :
            largest = num
        if num < smallest :
            smallest = num
    
print('Maximum is', largest)
print('Minimum is', smallest)
