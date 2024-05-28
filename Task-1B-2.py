def calculate_flames(name1, name2):
    flames = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    
    
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    name1_list = list(name1)
    name2_list = list(name2)
    
    
    for char in name1:
        if char in name2_list:
            name2_list.remove(char)
            name1_list.remove(char)
    
    
    remaining_chars = name1_list + name2_list
    
    
    count = len(remaining_chars)
    print("The number of remaining  CHARs in 2 names is",count)
    
    while len(flames) > 1:
        index = (count % len(flames) - 1)
        if index >= 0:
            right = flames[index + 1:]
            left = flames[:index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    return flames[0]


name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
result = calculate_flames(name1, name2)
print("Relationship between", name1, "and", name2, "is:", result)
