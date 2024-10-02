import multiprocessing
import datetime
#0:00:03.418771 линейный
#0:00:01.294292 многопроцессорный
def read_info(name):
    all_data = []  # создаёт пустой список
    with open(name, 'r') as file:  # открывает файл для чтения
        for line in file:  # читаем файл построчно
            all_data.append(line.strip())  # добавляем строки без пробелов по краям

# start = datetime.datetime.now()
# for numbers in range(1,5):
#     name = f'file {numbers}.txt'
#     read_info(name)
# end = datetime.datetime.now()
# print(end-start)
if __name__ == '__main__':
    with multiprocessing.Pool(processes = 4) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        start = datetime.datetime.now()
        pool.map(read_info,filenames)
    end = datetime.datetime.now()
    print(end-start)