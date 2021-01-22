import numpy as np


def function_easterly_index(year=None):
    easter_idx = []
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0): #그 해의 총 일수를 구하는 함수
        one_year_day = 366
    else:
        one_year_day = 365

    f = open("./easterly_case/hourly_easterly_case_{}.txt".format(year), 'r')
    line = f.readlines()

    txt_data = []

    for i in range(len(line)):
        if i == len(line) - 1:
            txt_data.append(line[i][:])
        else:
            txt_data.append(line[i][:-1])
    # other에 그 해 1월 1일 00시 부터 12월 31일 12시까지 1시간 간격으로 string으로
    other = np.zeros((one_year_day * 24), dtype='int32')
    start_month = 1
    start_row = 0
    for present_time in range(0, 12):
        if start_month == 1 or start_month == 3 or start_month == 5 or start_month == 7 or start_month == 8 or start_month == 10 or start_month == 12:
            day = 31
        elif start_month == 4 or start_month == 6 or start_month == 9 or start_month == 11:
            day = 30
        elif (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
            day = 29
        else:
            day = 28
        for i in range(0, day * 24):
            year_month_day = str(year) + str(start_month).zfill(2) + str((i // 24) + 1).zfill(2) + str(i % 24).zfill(2)
            other[start_row] = int(year_month_day)
            start_row = start_row + 1
        start_month = start_month + 1
    #그 해 동풍사례의 시간을 other의 순서에 맞는 index로 변환
    idx = 0
    for i in range(one_year_day * 24):
        if idx == len(txt_data):
            break
        elif str(other[i]) == txt_data[idx]:
            idx = idx + 1
            easter_idx.append(i)
    return easter_idx
