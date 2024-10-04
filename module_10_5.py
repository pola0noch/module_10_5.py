# Домашнее задание по теме "Многопроцессное программирование"
import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, "r") as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]


#start = datetime.datetime.now()
#for file in filenames:
    #read_info(file)
#end = datetime.datetime.now()
#print(f"Время линейного способа: {end - start}")
# 0:00:10.443515


if __name__ == "__main__":
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f"Время многопроцессного способа: {end - start}")
    # 0:00:05.060322


