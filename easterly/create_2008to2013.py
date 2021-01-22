import os
from netCDF4 import Dataset
import numpy as np
from easterly.easterly_index import *
from easterly.easterly_label import *


# 필요한 longitude-->>>41~101   (161개 -->>> 경도 총 갯수)
# 필요한 latitude--->>>71~111   (141개 --->>>위도 총 갯수)
# (time, level, latitude, longitude)--->>>Python

def extract_2008to2013(year=None, data_drive=None, save_drive=None):
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0): #그 해의 총 일수를 구하는 함수
        one_year_day = 366
    else:
        one_year_day = 365

    if not os.path.exists("{}/{}_csv".format(save_drive, year)):
        os.makedirs("{}/{}_csv".format(save_drive, year))

    factor = 6 * 6 #사용하는 36개인자를 의미합니다.

    # 마지막 현재 벡터는 v, u순서로 들어감
    present_u = 38 #csv파일에서 현재 시간 u인자의 위치를 의미
    present_v = 37 #csv파일에서 현재 시간 v인자의 위치를 의미



    pl_5 = ['z', 't', 'q', 'u', 'v', 'w']  #pressure에서 사용하는 인자 6개를 의미
    surface_6 = ['msl', 't2m', 'tcwv', 'u10', 'v10', 'p81.162'] #surface에서 사용하는 인자 6개를 의미
    level_5 = [17, 21, 25, 30, 33]  # 300--->>>17 500 --->>>21 700--->>>25 850--->>>30 925 --->>>33, #pressure에서 사용하는 hpa 5개를 의미

    row = 0

    pl_max_factor = []
    pl_min_factor = []
    sfc_max_factor = []
    sfc_min_factor = []

    lattice_point_list_700 = [[0] * 61 for i in range(41)]
    lattice_point_list_850 = [[0] * 61 for i in range(41)]
    lattice_point_list_925 = [[0] * 61 for i in range(41)]

    for lat_np in range(0, 41):
        for long_np in range(0, 61):
            lattice_point_list_700[lat_np][long_np] = np.zeros((one_year_day * 2 * 12, factor + 3))
            lattice_point_list_850[lat_np][long_np] = np.zeros((one_year_day * 2 * 12, factor + 3))
            lattice_point_list_925[lat_np][long_np] = np.zeros((one_year_day * 2 * 12, factor + 3))

    for idx in range(0, 2):

        if idx == 0:
            nc_info_pl_past = Dataset('{}/{}_nc/{}_pressure_level_data/era5_hourly_pl_{}123112'.format(data_drive, year-1, year-1,year-1)).variables #전년도 pressure data사용
            nc_info_sfc_past = Dataset('{}/{}_nc/{}_surface_level_data/era5_hourly_sfc_{}123112'.format(data_drive, year-1, year-1,year-1)).variables #전년도 surface data사용

            pl_factor_past = []
            sfc_factor_past = []

            for i in range(0, 6):
                pl_factor_past.append(nc_info_pl_past[pl_5[i]][-6:, level_5, 70:111, 40:101].filled(0)) #각 pressure인자별로 필요한 time,hpa,latitude,longitude를 추출
            for i in range(0, 6):
                sfc_factor_past.append(nc_info_sfc_past[surface_6[i]][-6:, 70:111, 40:101].filled(0) )#각 surface인자별로 필요한 time,hpa,latitude,longitude를 추출
        else:

            pl_path = "{}/{}_nc/{}_pressure_level_data/".format(data_drive, year, year)
            sfc_path = "{}/{}_nc/{}_surface_level_data/".format(data_drive, year, year)

            pl_list = os.listdir(pl_path)
            sfc_list = os.listdir(sfc_path)

            pl_factor_past = []
            sfc_factor_past = []

            for i in range(6):
                pl_factor_past.append(np.zeros((one_year_day * 24, 5, 41, 61)))
                sfc_factor_past.append(np.zeros((one_year_day * 24, 41, 61)))

            start_row = 0
            for r in range((one_year_day * 2)):
                for i in range(6):
                    pl_factor_past[i][start_row:start_row + 12, :, :, :] = Dataset(pl_path + pl_list[r])[pl_5[i]][:, level_5, 70:111, 40:101].filled(0) #그 해 pressure data 사용
                    sfc_factor_past[i][start_row:start_row + 12, :, :] = Dataset(sfc_path + sfc_list[r])[surface_6[i]][:, 70:111, 40:101].filled(0) #그 해 surface data 사용
                start_row = start_row + 12

        # pressure_max,min값 구하기

        if idx == 1:
            for i in range(0, 30):
                pl_max_factor.append(pl_factor_past[i % 6][:, i // 6, :, :].max())
                pl_min_factor.append(pl_factor_past[i % 6][:, i // 6, :, :].min())
        elif idx == one_year_day:
            for i in range(0, 30):
                max_candidate = pl_factor_past[i % 6][:-6, i // 6, :, :].max()
                min_candidate = pl_factor_past[i % 6][:-6, i // 6, :, :].min()
                if pl_max_factor[i] < max_candidate:
                    pl_max_factor[i] = max_candidate
                if pl_min_factor[i] > min_candidate:
                    pl_min_factor[i] = min_candidate
        elif idx > 1:
            for i in range(0, 30):
                max_candidate = pl_factor_past[i % 6][:, i // 6, :, :].max()
                min_candidate = pl_factor_past[i % 6][:, i // 6, :, :].min()
                if pl_max_factor[i] < max_candidate:
                    pl_max_factor[i] = max_candidate
                if pl_min_factor[i] > min_candidate:
                    pl_min_factor[i] = min_candidate
        # surface_max,min값 구하기
        if idx == 1:
            for i in range(0, 6):
                sfc_max_factor.append(sfc_factor_past[i][:, :, :].max())
                sfc_min_factor.append(sfc_factor_past[i][:, :, :].min())
        elif idx == one_year_day:
            for i in range(0, 6):
                max_candidate = sfc_factor_past[i][:-6, :, :].max()
                min_candidate = sfc_factor_past[i][:-6, :, :].min()
                if sfc_max_factor[i] < max_candidate:
                    sfc_max_factor[i] = max_candidate
                if sfc_min_factor[i] > min_candidate:
                    sfc_min_factor[i] = min_candidate
        elif idx > 1:
            for i in range(0, 6):
                max_candidate = sfc_factor_past[i][:, :, :].max()
                min_candidate = sfc_factor_past[i][:, :, :].min()
                if sfc_max_factor[i] < max_candidate:
                    sfc_max_factor[i] = max_candidate
                if sfc_min_factor[i] > min_candidate:
                    sfc_min_factor[i] = min_candidate
        #for문을 latitude*longitude만큼 돌려서 data를 격자점별로 정리
        for lat in range(0, 41):
            for long in range(0, 61):
                if idx == 0:
                    for pl_elem in range(0, 30):
                        lattice_point_list_700[lat][long][row:row + 6, pl_elem] = pl_factor_past[pl_elem % 6][:, pl_elem // 6, lat, long]

                    for sur_elem in range(0, 6):
                        lattice_point_list_700[lat][long][row:row + 6, sur_elem + 30] = sfc_factor_past[sur_elem][:, lat, long]

                    if lat == 40 and long == 60:
                        row = row + 6

                else:
                    for pl_elem in range(0, 30):
                        lattice_point_list_700[lat][long][row:, pl_elem] = pl_factor_past[pl_elem % 6][:-6, pl_elem // 6, lat, long]

                    for sur_elem in range(0, 6):
                        lattice_point_list_700[lat][long][row:, sur_elem + 30] = sfc_factor_past[sur_elem][:-6, lat, long]

                    lattice_point_list_700[lat][long][:, present_u] = pl_factor_past[3][:, 2, lat, long]
                    lattice_point_list_700[lat][long][:, present_v] = pl_factor_past[4][:, 2, lat, long]

                    lattice_point_list_850[lat][long][:, present_u] = pl_factor_past[3][:, 3, lat, long]
                    lattice_point_list_850[lat][long][:, present_v] = pl_factor_past[4][:, 3, lat, long]

                    lattice_point_list_925[lat][long][:, present_u] = pl_factor_past[3][:, 4, lat, long]
                    lattice_point_list_925[lat][long][:, present_v] = pl_factor_past[4][:, 4, lat, long]

    #other에 그 해 1월 1일 00시 부터 12월 31일 12시까지 1시간 간격으로 string으로 변형
    other = np.zeros((one_year_day * 24))
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
            other[start_row] = float(year_month_day)
            start_row = start_row + 1
        start_month = start_month + 1

    del pl_factor_past
    del sfc_factor_past

    for lat_copy in range(0, 41):
        for long_copy in range(0, 61):
            lattice_point_list_700[lat_copy][long_copy][:, -3] = other[:]
            lattice_point_list_850[lat_copy][long_copy][:, 0:-2] = lattice_point_list_700[lat_copy][long_copy][:, 0:-2]
            lattice_point_list_925[lat_copy][long_copy][:, 0:-2] = lattice_point_list_700[lat_copy][long_copy][:, 0:-2]

    if not os.path.exists('{}/{}_csv/{}_최대최소'.format(save_drive, year, year)):
        os.makedirs("{}/{}_csv/{}_최대최소".format(save_drive, year, year))

    # pressure 최대
    f = open("{}/{}_csv/{}_최대최소/{}_pl_max_factor.txt".format(save_drive, year, year, year), 'w')
    for i in range(30):
        if i // 6 == 0:
            f.write(str(300) + 'hPa' + str((i % 6) + 1) + '번째: ' + (str(pl_max_factor[i]) + '\n'))
        if i // 6 == 1:
            f.write(str(500) + 'hPa' + str((i % 6) + 1) + '번째: ' + (str(pl_max_factor[i]) + '\n'))
        if i // 6 == 2:
            f.write(str(700) + 'hPa' + str((i % 6) + 1) + '번째: ' + (str(pl_max_factor[i]) + '\n'))
        if i // 6 == 3:
            f.write(str(850) + 'hPa' + str((i % 6) + 1) + '번째: ' + (str(pl_max_factor[i]) + '\n'))
        if i // 6 == 4:
            f.write(str(925) + 'hPa' + str((i % 6) + 1) + '번째: ' + (str(pl_max_factor[i]) + '\n'))
    f.close()

    # pressure 최소
    f = open("{}/{}_csv/{}_최대최소/{}_pl_min_factor.txt".format(save_drive, year, year, year), 'w')
    for i in range(30):
        if i // 6 == 0:
            f.write(str(300) + 'hPa' + str((i % 6) + 1) + '번째: ' + (str(pl_min_factor[i]) + '\n'))
        if i // 6 == 1:
            f.write(str(500) + 'hPa' + str((i % 6) + 1) + '번째: ' + (str(pl_min_factor[i]) + '\n'))
        if i // 6 == 2:
            f.write(str(700) + 'hPa' + str((i % 6) + 1) + '번째: ' + (str(pl_min_factor[i]) + '\n'))
        if i // 6 == 3:
            f.write(str(850) + 'hPa' + str((i % 6) + 1) + '번째: ' + (str(pl_min_factor[i]) + '\n'))
        if i // 6 == 4:
            f.write(str(925) + 'hPa' + str((i % 6) + 1) + '번째: ' + (str(pl_min_factor[i]) + '\n'))
    f.close()

    # surface 최대
    f = open("{}/{}_csv/{}_최대최소/{}_sfc_max_factor.txt".format(save_drive, year, year, year), 'w')
    for i in range(6):
        f.write(str(surface_6[i]) + ': ' + str(sfc_max_factor[i]) + '\n')
    f.close()

    # surface 최소
    f = open("{}/{}_csv/{}_최대최소/{}_sfc_min_factor.txt".format(save_drive, year, year, year), 'w')
    for i in range(6):
        f.write(str(surface_6[i]) + ': ' + str(sfc_min_factor[i]) + '\n')
    f.close()
    #700hpa csv파일을 격자점 별로 저장
    if not os.path.exists('{}/{}_csv/700'.format(save_drive, year)):
        os.makedirs("{}/{}_csv/700".format(save_drive, year))
    print("0700hPa시작")
    for lat_save in range(0, 41):
        for long_save in range(0, 61):
            first_name = '{}/{}_csv/700/'.format(save_drive, year) + 'X' + str(1 + 40 + long_save).zfill(3) + '_Y' + str(1 + 70 + lat_save).zfill(3) + '_' + str(700) + '.csv'
            np.savetxt(first_name, lattice_point_list_700[lat_save][long_save], delimiter=',')

    del lattice_point_list_700
    #850hpa csv파일을 격자점 별로 저장
    if not os.path.exists('{}/{}_csv/850'.format(save_drive, year)):
        os.makedirs("{}/{}_csv/850".format(save_drive, year))
    print("0850hPa시작")
    for lat_save in range(0, 41):
        for long_save in range(0, 61):
            first_name = '{}/{}_csv/850/'.format(save_drive, year) + 'X' + str(1 + 40 + long_save).zfill(3) + '_Y' + str(1 + 70 + lat_save).zfill(3) + '_' + str(850) + '.csv'
            np.savetxt(first_name, lattice_point_list_850[lat_save][long_save], delimiter=',')

    del lattice_point_list_850
    #925hpa csv파일을 격자점 별로 저장
    if not os.path.exists('{}/{}_csv/925'.format(save_drive, year)):
        os.makedirs("{}/{}_csv/925".format(save_drive, year))
    print("0925hPa시작")
    for lat_save in range(0, 41):
        for long_save in range(0, 61):
            first_name = '{}/{}_csv/925/'.format(save_drive, year) + 'X' + str(1 + 40 + long_save).zfill(3) + '_Y' + str(1 + 70 + lat_save).zfill(3) + '_' + str(925) + '.csv'
            np.savetxt(first_name, lattice_point_list_925[lat_save][long_save], delimiter=',')

    del lattice_point_list_925

    easterly_index = function_easterly_index(year) #그 해의 동풍사례를 index로 변환
    function_easterly_label(year,easterly_index,save_drive) #그 해의 동풍사례와 현재 u인자를 고려하여 label


