import random
from multiprocessing.pool import ThreadPool

def create_file(file_name):
    with open(file_name, "w") as file:
        file.write(f"This is demo file {file_name}.")

random_list = []
for i in range(5):
    rand_int = random.randint(0,100)
    file_name = "filename_"+str(rand_int)+".txt"
    random_list.append(file_name)   

with ThreadPool(5) as pool:
    pool.map(create_file, random_list)