import numpy as np
import collections
import os
import pandas as pd


def Guepmgsang(save_drive):
    file_name_rainfall = "2008_2017_rainfall"

    if not os.path.exists("{}/10년치종합".format(save_drive)):
        os.makedirs("{}/10년치종합".format(save_drive))
    if not os.path.exists("{}/10년치종합/{}_csv".format(save_drive, file_name_rainfall)):
        os.makedirs("{}/10년치종합/{}_csv".format(save_drive, file_name_rainfall))
    region = ['Uljin', 'Pohang', 'Ulsan'] #경상지역 3개를 의미
    total_year_index = collections.OrderedDict()
    folder = "{}/rainfall/".format(save_drive)
    for i in region:
        folder_name = '{}{}/total_label_후'.format(folder, i)
        file_list = os.listdir(folder_name)
        total_year_index[i] = file_list

    file_csv_list = []

    for i in region:
        folder_name = '{}{}/total_label_후'.format(folder, i)
        file_csv_list.append(folder_name + '/' + total_year_index[i][0])
    # 3개지역 csv파일을 concatenate
    csv_data = np.concatenate((pd.read_csv(file_csv_list[0], header=None)._values,
                               pd.read_csv(file_csv_list[1], header=None)._values,
                               pd.read_csv(file_csv_list[2], header=None)._values
                               ), axis=0)
    a = len(csv_data)
    total_row  = np.arange(len(csv_data))
    total_row = list(total_row)
    # train : test = 4 : 1비율
    number_of_train = round(len(total_row) * 4 / 5)
    train_random_idx = np.random.choice(len(total_row), number_of_train, replace=False)
    train_random_idx = list(train_random_idx)
    for remove_idx in range(len(train_random_idx)):
        total_row.remove(train_random_idx[remove_idx])
    test_random_idx = total_row
    train_list = np.zeros((len(train_random_idx), 4 + 36*9 + 3))
    train_list[:] = csv_data[train_random_idx, :]
    test_list = np.zeros((len(test_random_idx), 4 + 36*9 + 3))
    test_list[:] = csv_data[test_random_idx, :]
    if not os.path.isdir('{}/10년치종합/{}_csv/'.format(save_drive, file_name_rainfall)):
        os.mkdir('{}/10년치종합/{}_csv/'.format(save_drive, file_name_rainfall))
    file_name = 'rainfall_Gyeongsang_'
    print("시작")
    np.savetxt('{}/10년치종합/{}_csv/'.format(save_drive, file_name_rainfall) + file_name + 'train.csv', train_list, delimiter=',')
    print("train완료")
    np.savetxt('{}/10년치종합/{}_csv/'.format(save_drive, file_name_rainfall) + file_name + 'test.csv', test_list, delimiter=',')
    print("test완료")

