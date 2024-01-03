import random
from multiprocessing.pool import ThreadPool

def create_file(file_name):
    try:
        with open(file_name, "w") as file:
            file.write(f"This is demo file {file_name}.")
    except Exception as e:
        print(f"Failed to create the file with name {file_name} due to {e}")

random_list = []
for _ in range(5):
    rand_int = random.randint(0,100)
    file_name = f"filename_{rand_int}.txt"
    random_list.append(file_name)   

with ThreadPool(5) as pool:
    pool.map(create_file, random_list)