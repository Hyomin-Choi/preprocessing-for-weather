import pandas as pd
import numpy as np
import os

def rainfall_label(save_drive):
    region_all = ['Sokcho', 'Gangneung', 'Donghae', 'Taebaek', 'Uljin',  'Pohang', 'Ulsan','Daegwallyeong'] #강원5개지역, 경상 3개지역
    year_list = ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
    path = '{}/rainfall/'.format(save_drive)
    for region in region_all:
        file_csv_list = []
        for year in year_list:
            folder_name = path + '{}/{}_csv/sum9'.format(region, year)
            csv_file = os.listdir(folder_name)
            file_csv_list.append(folder_name + '/' + csv_file[0])
        label_data = pd.read_excel('./region_label/{}_label.xlsx'.format(region), header=None)._values #지역별 강수시간과 label불러옴
        count = 0 #날짜 일치시 label추가
        save_data = np.zeros((len(label_data),4+36*9+1+1+1))

        total_year_data = np.concatenate((pd.read_csv(file_csv_list[0], header=None)._values,
                                        pd.read_csv(file_csv_list[1], header=None)._values,
                                        pd.read_csv(file_csv_list[2], header=None)._values,
                                        pd.read_csv(file_csv_list[3], header=None)._values,
                                        pd.read_csv(file_csv_list[4], header=None)._values,
                                        pd.read_csv(file_csv_list[5], header=None)._values,
                                        pd.read_csv(file_csv_list[6], header=None)._values,
                                        pd.read_csv(file_csv_list[7], header=None)._values,
                                        pd.read_csv(file_csv_list[8], header=None)._values,
                                        pd.read_csv(file_csv_list[9], header=None)._values
                                        ), axis=0)
        for idx in range(len(total_year_data)):
            if count == len(label_data):
                break
            elif int(total_year_data[idx][-3]) == label_data[count][0]:
                if label_data[count][1] == 'w_rain':
                    save_data[count][0] = 1
                    save_data[count][4:] = total_year_data[idx][4:]
                elif label_data[count][1] == 'c_rain':
                    save_data[count][1] = 1
                    save_data[count][4:] = total_year_data[idx][4:]
                elif label_data[count][1] == 'snow':
                    save_data[count][2] = 1
                    save_data[count][4:] = total_year_data[idx][4:]
                elif label_data[count][1] == 'heavy_snow':
                    save_data[count][3] = 1
                    save_data[count][4:] = total_year_data[idx][4:]
                else:
                    print("오류")
                    exit(0)
                count =count+1
        if not os.path.exists(path + '{}/total_label_후/'.format(region)):
            os.makedirs(path + '{}/total_label_후/'.format(region))
        filename = 'rainfall_X{}_Y{}.csv'.format(str(int(save_data[0][-2])).zfill(3),str(int(save_data[0][-1])).zfill(3))
        np.savetxt(path + '{}/total_label_후/{}'.format(region,filename),save_data,delimiter=',')
        print("지역:{},갯수:{}".format(region,count))
