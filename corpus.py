import random
from random import choice
import os

cropus_num = 2000  #Set the number of corpora

def get_cropus(f): # Randomly generate year

    # year = random.randint(0, 22) # Randomly generate month
    
    # month = random.randint(1, 12) # Randomly generate a date
    
    # day_dict = {31: [1,3,5,7,8,10,12], 30: [4,6,9,11], 28: [2]}
    # for item in day_dict:
    #     if month in day_dict[item]:
    #         day = random.randint(0, item) # Randomly generate hours
   
    # hours = random.randint(0, 24) # Randomly generate minutes
    
    # minute = random.randint(0, 60) # Randomly generate seconds
    
    # second = random.randint(0, 60)

    # Randomly generate product identification characters
    length = random.randint(6, 7)
    file_id = []

    char_dict = [k for k in range(65,90)]  # Uppercase only

    for i in range(length):
        sel = choice(char_dict)
        my_ascii = chr(sel)
        file_id.append(my_ascii)
    char_str = ''.join(file_id)

    file_id = []
    nums_dict = [k for k in range(0,9)]
    for i in range(length):
        file_id.append(str(choice(nums_dict)))
    num_str = ''.join(file_id)

    
    f.write(char_str)
    f.write('\n')
    f.write(num_str)


if __name__ == "__main__":
    file_path = 'data/corpus'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_name = os.path.join(file_path, 'books.txt')
    f = open(file_name, 'w', encoding="utf-8")
    for i in range(cropus_num):
        get_cropus(f)
        if i < cropus_num-1:
            f.write('\n')

    f.close()