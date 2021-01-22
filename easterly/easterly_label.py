import pandas as pd
import os
import numpy as np

def function_easterly_label(year,easterly_index,save_drive):
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0): #그 해의 총 일수를 구하는 함수
        one_year_day = 366
    else:
        one_year_day = 365
    present_u = 38
    for idx in range(0, 3):
        if idx==0:
            hPa=700
        elif idx == 1:
            hPa=850
        else:
            hPa =925
        precipitation_number=len(easterly_index)
        data_path = '{}/{}_csv/{}/'.format(save_drive,year, hPa)
        if not os.path.exists('E:/{}_csv/label_추가'.format(year)):
            os.mkdir('{}/{}_csv/label_추가'.format(save_drive,year))
        if not os.path.exists('E:/{}_csv/label_추가/label_0{}'.format(year, hPa)):
            os.mkdir('{}/{}_csv/label_추가/label_0{}'.format(save_drive,year, hPa))
        data_list=os.listdir(data_path)
        for idx in range(len(data_list)):
            data_storage = np.zeros((one_year_day*24, 39 + 2))
            data_storage[:, 0] = 0
            data_storage[:, 1] = 1
            lattice_data = pd.read_csv(data_path + data_list[idx], header=None)._values
            for i in range(precipitation_number):
                if lattice_data[easterly_index[i], present_u] <= (-0.5): #동풍사례와 현재 u인자를 고려하여 label
                    data_storage[easterly_index[i], 0] = 1
                    data_storage[easterly_index[i], 1] = 0
            data_storage[:,2:]=lattice_data[:,:]
            lattice_name= '{}/{}_csv/label_추가/label_0{}/easterly_'.format(save_drive,year,hPa) + data_list[idx][:-7]+str(hPa).zfill(4)+'.csv'
            np.savetxt(lattice_name, data_storage, delimiter=',')
        del data_storage

