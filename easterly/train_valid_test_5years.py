import os
import numpy as np
import collections
import pandas as pd
import sys
# txt 파일이 있는 폴더의 이전 폴더


def min_max_calculation(save_drive=None):
    if not os.path.exists("{}/5년치종합".format(save_drive)):
        os.makedirs("{}/5년치종합".format(save_drive))

    if not os.path.exists("{}/5년치종합/2013_2017_csv".format(save_drive)):
        os.makedirs("{}/5년치종합/2013_2017_csv".format(save_drive))
    name_list = ['pl_max', 'pl_min', 'sfc_max', 'sfc_min']

    #각 년도 별로 pressure최대,최소 surface최대,최소를 호출
    f_2013_pl_max = open("{}/2013_csv/2013_최대최소/2013_pl_max_factor.txt".format(save_drive), 'r')
    f_2013_pl_min = open("{}/2013_csv/2013_최대최소/2013_pl_min_factor.txt".format(save_drive), 'r')
    f_2013_sfc_max = open("{}/2013_csv/2013_최대최소/2013_sfc_max_factor.txt".format(save_drive), 'r')
    f_2013_sfc_min = open("{}/2013_csv/2013_최대최소/2013_sfc_min_factor.txt".format(save_drive), 'r')

    f_2014_pl_max = open("{}/2014_csv/2014_최대최소/2014_pl_max_factor.txt".format(save_drive), 'r')
    f_2014_pl_min = open("{}/2014_csv/2014_최대최소/2014_pl_min_factor.txt".format(save_drive), 'r')
    f_2014_sfc_max = open("{}/2014_csv/2014_최대최소/2014_sfc_max_factor.txt".format(save_drive), 'r')
    f_2014_sfc_min = open("{}/2014_csv/2014_최대최소/2014_sfc_min_factor.txt".format(save_drive), 'r')

    f_2015_pl_max = open("{}/2015_csv/2015_최대최소/2015_pl_max_factor.txt".format(save_drive), 'r')
    f_2015_pl_min = open("{}/2015_csv/2015_최대최소/2015_pl_min_factor.txt".format(save_drive), 'r')
    f_2015_sfc_max = open("{}/2015_csv/2015_최대최소/2015_sfc_max_factor.txt".format(save_drive), 'r')
    f_2015_sfc_min = open("{}/2015_csv/2015_최대최소/2015_sfc_min_factor.txt".format(save_drive), 'r')

    f_2016_pl_max = open("{}/2016_csv/2016_최대최소/2016_pl_max_factor.txt".format(save_drive), 'r')
    f_2016_pl_min = open("{}/2016_csv/2016_최대최소/2016_pl_min_factor.txt".format(save_drive), 'r')
    f_2016_sfc_max = open("{}/2016_csv/2016_최대최소/2016_sfc_max_factor.txt".format(save_drive), 'r')
    f_2016_sfc_min = open("{}/2016_csv/2016_최대최소/2016_sfc_min_factor.txt".format(save_drive), 'r')

    f_2017_pl_max = open("{}/2017_csv/2017_최대최소/2017_pl_max_factor.txt".format(save_drive), 'r')
    f_2017_pl_min = open("{}/2017_csv/2017_최대최소/2017_pl_min_factor.txt".format(save_drive), 'r')
    f_2017_sfc_max = open("{}/2017_csv/2017_최대최소/2017_sfc_max_factor.txt".format(save_drive), 'r')
    f_2017_sfc_min = open("{}/2017_csv/2017_최대최소/2017_sfc_min_factor.txt".format(save_drive), 'r')

    dict_2013 = collections.OrderedDict()
    dict_2014 = collections.OrderedDict()
    dict_2015 = collections.OrderedDict()
    dict_2016 = collections.OrderedDict()
    dict_2017 = collections.OrderedDict()

    dict_2013['pl_max'] = f_2013_pl_max.readlines()
    dict_2013['pl_min'] = f_2013_pl_min.readlines()
    dict_2013['sfc_max'] = f_2013_sfc_max.readlines()
    dict_2013['sfc_min'] = f_2013_sfc_min.readlines()

    dict_2014['pl_max'] = f_2014_pl_max.readlines()
    dict_2014['pl_min'] = f_2014_pl_min.readlines()
    dict_2014['sfc_max'] = f_2014_sfc_max.readlines()
    dict_2014['sfc_min'] = f_2014_sfc_min.readlines()

    dict_2015['pl_max'] = f_2015_pl_max.readlines()
    dict_2015['pl_min'] = f_2015_pl_min.readlines()
    dict_2015['sfc_max'] = f_2015_sfc_max.readlines()
    dict_2015['sfc_min'] = f_2015_sfc_min.readlines()

    dict_2016['pl_max'] = f_2016_pl_max.readlines()
    dict_2016['pl_min'] = f_2016_pl_min.readlines()
    dict_2016['sfc_max'] = f_2016_sfc_max.readlines()
    dict_2016['sfc_min'] = f_2016_sfc_min.readlines()

    dict_2017['pl_max'] = f_2017_pl_max.readlines()
    dict_2017['pl_min'] = f_2017_pl_min.readlines()
    dict_2017['sfc_max'] = f_2017_sfc_max.readlines()
    dict_2017['sfc_min'] = f_2017_sfc_min.readlines()

    pl_max = []
    pl_min = []
    sfc_max = []
    sfc_min = []

    for i in range(len(dict_2013['pl_max'])):
        pl_max.append(float(dict_2013[name_list[0]][i][11:-1]))
        pl_max.append(float(dict_2014[name_list[0]][i][11:-1]))
        pl_max.append(float(dict_2015[name_list[0]][i][11:-1]))
        pl_max.append(float(dict_2016[name_list[0]][i][11:-1]))
        pl_max.append(float(dict_2017[name_list[0]][i][11:-1]))

        pl_min.append(float(dict_2013[name_list[1]][i][11:-1]))
        pl_min.append(float(dict_2014[name_list[1]][i][11:-1]))
        pl_min.append(float(dict_2015[name_list[1]][i][11:-1]))
        pl_min.append(float(dict_2016[name_list[1]][i][11:-1]))
        pl_min.append(float(dict_2017[name_list[1]][i][11:-1]))
    for k in range(30 * 5):
        if pl_max[k] < pl_min[k]:
            print("pl오류_{}번째 오류".format(k))
            sys.exit()

    for i in range(len(dict_2013['sfc_max'])):
        if i in [0, 1, 3, 4]:
            offset = 5
        elif i == 2:
            offset = 6
        else:
            offset = 9
        sfc_max.append(float(dict_2013[name_list[2]][i][offset:-1]))
        sfc_max.append(float(dict_2014[name_list[2]][i][offset:-1]))
        sfc_max.append(float(dict_2015[name_list[2]][i][offset:-1]))
        sfc_max.append(float(dict_2016[name_list[2]][i][offset:-1]))
        sfc_max.append(float(dict_2017[name_list[2]][i][offset:-1]))

        sfc_min.append(float(dict_2013[name_list[3]][i][offset:-1]))
        sfc_min.append(float(dict_2014[name_list[3]][i][offset:-1]))
        sfc_min.append(float(dict_2015[name_list[3]][i][offset:-1]))
        sfc_min.append(float(dict_2016[name_list[3]][i][offset:-1]))
        sfc_min.append(float(dict_2017[name_list[3]][i][offset:-1]))
    for k in range(6*5):
        if sfc_max[k] < sfc_min[k]:
            print("sfc오류_{}번째 오류".format(k))
            sys.exit(1)

    pl_max_dict = collections.OrderedDict()
    pl_min_dict = collections.OrderedDict()
    sfc_max_dict = collections.OrderedDict()
    sfc_min_dict = collections.OrderedDict()

    pl_max_dict_before = np.zeros((5,6))
    pl_min_dict_before = np.zeros((5,6))
    #5년 pressure 각 6개 인자,5hpa의 총 30개 평균계산
    for i in range(len(pl_max) // 5):
        offset1 = i * 5
        pl_max_dict_before[i//6, i % 6] = sum(pl_max[offset1:offset1 + 5]) / 5
        pl_min_dict_before[i//6, i % 6] = sum(pl_min[offset1:offset1 + 5]) / 5
    # pressure인자에서 한 인자당 5개 hpa에서 최대,최소추출
    for i in range(len(pl_max) // 5):
        pl_max_dict[str(i)] = sorted(pl_max_dict_before[:, i % 6])[-1]
        pl_min_dict[str(i)] = sorted(pl_min_dict_before[:, i % 6])[0]
    #5년 surface 6개 인자의 평균계산
    for i in range(len(sfc_max) // 5):
        offset1 = i * 5
        sfc_max_dict[str(i + 30)] = sum(sfc_max[offset1:offset1 + 5]) / 5
        sfc_min_dict[str(i + 30)] = sum(sfc_min[offset1:offset1 + 5]) / 5

    for hpa in [700,850,925]:
        split(save_drive, hpa, pl_max_dict, pl_min_dict, sfc_max_dict, sfc_min_dict) #700,850,925hpa별로 train,validation,test추출

def split(save_drive=None,hpa=None,pl_max_dict=None, pl_min_dict = None, sfc_max_dict = None, sfc_min_dict = None):
    total_year_index = collections.OrderedDict()

    for year in ['2013','2014','2015','2016','2017']:
        folder_name = '{}{}_csv/label_추가/label_0{}'.format(save_drive, year, hpa)
        file_list = os.listdir(folder_name)
        total_year_index[year] = file_list


    for idx in range(len(total_year_index['2013'])):

        file_csv_list = []

        for i in ['2013','2014','2015','2016','2017']:
            folder_name = '{}{}_csv/label_추가/label_0{}'.format(save_drive, i, hpa)
            file_csv_list.append(folder_name+'/'+total_year_index[i][idx])

        #5년치 csv파일을 concatenate합니다.
        csv_data = np.concatenate((pd.read_csv(file_csv_list[0], header=None)._values,
                                  pd.read_csv(file_csv_list[1], header=None)._values,
                                  pd.read_csv(file_csv_list[2], header=None)._values,
                                  pd.read_csv(file_csv_list[3], header=None)._values,
                                   pd.read_csv(file_csv_list[4], header=None)._values
                                   ),axis=0)
        idx_list = []
        prec_list = []
        nonprec_list = []

        for i in range(8760+8760+8760+8784+8760): #2013,2014,2015,2016,2017년 각 년도별로 그해년도 *24시간을 의미
            idx_list.append(i)
            if csv_data[i, 0] == 1:
                prec_list.append(i)
            else:
                nonprec_list.append(i)
        #train : valid : test = 4 : 1 : 1의 비율로 추출
        #각 train,valid,test에서 동풍 : 비동풍 = 1: 2의 비율로 추출
        number_of_train = round(len(prec_list) * 4 / 6)
        number_of_test = round(len(prec_list) / 6)
        number_of_valid = len(prec_list) - number_of_train - number_of_test

        train_true_random_idx = np.random.choice(prec_list, number_of_train, replace=False) #random으로 train 동풍 index를 추출
        train_false_random_idx = np.random.choice(nonprec_list, number_of_train * 2, replace=False) #random으로 train 비동풍 index를 추출
        train_list = np.zeros((len(train_true_random_idx) * 3, 43)) # 43 --->>> 2(label) + 36(36개인자) + 1(현재시각) + 4(v정규화O, v정규화X, u정규화O, u정규화X)

        for i in range(train_list.shape[0]):
            if i < len(train_true_random_idx):

                train_list[i, :40] = csv_data[train_true_random_idx[i], :40]
                train_list[i, 40] = csv_data[train_true_random_idx[i], 39]
                train_list[i, 41] = csv_data[train_true_random_idx[i], 40]
                train_list[i, 42] = csv_data[train_true_random_idx[i], 40]
                prec_list.remove(train_true_random_idx[i])
            else:
                train_list[i, :40] = csv_data[train_false_random_idx[i - len(train_true_random_idx)], :40]
                train_list[i, 40] = csv_data[train_false_random_idx[i - len(train_true_random_idx)], 39]
                train_list[i, 41] = csv_data[train_false_random_idx[i - len(train_true_random_idx)], 40]
                train_list[i, 42] = csv_data[train_false_random_idx[i - len(train_true_random_idx)], 40]
                nonprec_list.remove(train_false_random_idx[i - len(train_true_random_idx)])

        test_true_random_idx = np.random.choice(prec_list, number_of_test, replace=False) #random으로 test 동풍 index를 추출
        test_false_random_idx = np.random.choice(nonprec_list, number_of_test * 2, replace=False) #random으로 test 비동풍 index를 추출
        test_list = np.zeros((len(test_true_random_idx) * 3, 43))

        for j in range(test_list.shape[0]):
            if j < len(test_true_random_idx):
                test_list[j, :40] = csv_data[test_true_random_idx[j], :40]
                test_list[j, 40] = csv_data[test_true_random_idx[j], 39]
                test_list[j, 41] = csv_data[test_true_random_idx[j], 40]
                test_list[j, 42] = csv_data[test_true_random_idx[j], 40]
                prec_list.remove(test_true_random_idx[j])
            else:
                test_list[j, :40] = csv_data[test_false_random_idx[j - len(test_true_random_idx)], :40]
                test_list[j, 40] = csv_data[test_false_random_idx[j - len(test_true_random_idx)], 39]
                test_list[j, 41] = csv_data[test_false_random_idx[j - len(test_true_random_idx)], 40]
                test_list[j, 42] = csv_data[test_false_random_idx[j - len(test_true_random_idx)], 40]
                nonprec_list.remove(test_false_random_idx[j - len(test_true_random_idx)])

        valid_true_random_idx = np.random.choice(prec_list, number_of_valid, replace=False) #random으로 valid 동풍 index를 추출
        valid_false_random_idx = np.random.choice(nonprec_list, number_of_valid * 2, replace=False) #random으로 valid 비동풍 index를 추출
        valid_list = np.zeros((len(valid_true_random_idx) * 3, 43))

        for k in range(valid_list.shape[0]):
            if k < len(valid_true_random_idx):
                valid_list[k, :40] = csv_data[valid_true_random_idx[k], :40]
                valid_list[k, 40] = csv_data[valid_true_random_idx[k], 39]
                valid_list[k, 41] = csv_data[valid_true_random_idx[k], 40]
                valid_list[k, 42] = csv_data[valid_true_random_idx[k], 40]
            else:
                valid_list[k, :40] = csv_data[valid_false_random_idx[k - len(valid_true_random_idx)], :40]
                valid_list[k, 40] = csv_data[valid_false_random_idx[k - len(valid_true_random_idx)], 39]
                valid_list[k, 41] = csv_data[valid_false_random_idx[k - len(valid_true_random_idx)], 40]
                valid_list[k, 42] = csv_data[valid_false_random_idx[k - len(valid_true_random_idx)], 40]

        # 6by6(36) + u,v(2)
        #(인자값 - 최솟값)/(최댓값 - 최솟값)으로 정규화
        for i in range(38):
            if i < 30:
                train_list[:, i + 2] = (train_list[:, i + 2] - pl_min_dict[str(i)]) / (pl_max_dict[str(i)] - pl_min_dict[str(i)])
                test_list[:, i + 2] = (test_list[:, i + 2] - pl_min_dict[str(i)]) / (pl_max_dict[str(i)] - pl_min_dict[str(i)])
                valid_list[:, i + 2] = (valid_list[:, i + 2] - pl_min_dict[str(i)]) / (pl_max_dict[str(i)] - pl_min_dict[str(i)])

            elif i >= 30 and i < 36:
                train_list[:, i + 2] = (train_list[:, i + 2] - sfc_min_dict[str(i)]) / (sfc_max_dict[str(i)] - sfc_min_dict[str(i)])
                test_list[:, i + 2] = (test_list[:, i + 2] - sfc_min_dict[str(i)]) / (sfc_max_dict[str(i)] - sfc_min_dict[str(i)])
                valid_list[:, i + 2] = (valid_list[:, i + 2] - sfc_min_dict[str(i)]) / (sfc_max_dict[str(i)] - sfc_min_dict[str(i)])

            elif i==36:
                if hpa == 700:
                    train_list[:, i + 3] = (train_list[:, i + 3] - pl_min_dict[str(16)]) / (pl_max_dict[str(16)] - pl_min_dict[str(16)])
                    test_list[:, i + 3] = (test_list[:, i + 3] - pl_min_dict[str(16)]) / (pl_max_dict[str(16)] - pl_min_dict[str(16)])
                    valid_list[:, i + 3] = (valid_list[:, i + 3] - pl_min_dict[str(16)]) / (pl_max_dict[str(16)] - pl_min_dict[str(16)])
                elif hpa== 850:
                    train_list[:, i + 3] = (train_list[:, i + 3] - pl_min_dict[str(22)]) / (pl_max_dict[str(22)] - pl_min_dict[str(22)])
                    test_list[:, i + 3] = (test_list[:, i + 3] - pl_min_dict[str(22)]) / (pl_max_dict[str(22)] - pl_min_dict[str(22)])
                    valid_list[:, i + 3] = (valid_list[:, i + 3] - pl_min_dict[str(22)]) / (pl_max_dict[str(22)] - pl_min_dict[str(22)])
                else:
                    train_list[:, i + 3] = (train_list[:, i + 3] - pl_min_dict[str(28)]) / (pl_max_dict[str(28)] - pl_min_dict[str(28)])
                    test_list[:, i + 3] = (test_list[:, i + 3] - pl_min_dict[str(28)]) / (pl_max_dict[str(28)] - pl_min_dict[str(28)])
                    valid_list[:, i + 3] = (valid_list[:, i + 3] - pl_min_dict[str(28)]) / (pl_max_dict[str(28)] - pl_min_dict[str(28)])

            elif i==37:
                if hpa == 700:
                    train_list[:, i + 4] = (train_list[:, i + 4] - pl_min_dict[str(15)]) / (pl_max_dict[str(15)] - pl_min_dict[str(15)])
                    test_list[:, i + 4] = (test_list[:, i + 4] - pl_min_dict[str(15)]) / (pl_max_dict[str(15)] - pl_min_dict[str(15)])
                    valid_list[:, i + 4] = (valid_list[:, i + 4] - pl_min_dict[str(15)]) / (pl_max_dict[str(15)] - pl_min_dict[str(15)])
                elif hpa== 850:
                    train_list[:, i + 4] = (train_list[:, i + 4] - pl_min_dict[str(21)]) / (pl_max_dict[str(21)] - pl_min_dict[str(21)])
                    test_list[:, i + 4] = (test_list[:, i + 4] - pl_min_dict[str(21)]) / (pl_max_dict[str(21)] - pl_min_dict[str(21)])
                    valid_list[:, i + 4] = (valid_list[:, i + 4] - pl_min_dict[str(21)]) / (pl_max_dict[str(21)] - pl_min_dict[str(21)])
                else:
                    train_list[:, i + 4] = (train_list[:, i + 4] - pl_min_dict[str(27)]) / (pl_max_dict[str(27)] - pl_min_dict[str(27)])
                    test_list[:, i + 4] = (test_list[:, i + 4] - pl_min_dict[str(27)]) / (pl_max_dict[str(27)] - pl_min_dict[str(27)])
                    valid_list[:, i + 4] = (valid_list[:, i + 4] - pl_min_dict[str(27)]) / (pl_max_dict[str(27)] - pl_min_dict[str(27)])

        #train,valid,test csv파일을 저장
        file_name="2013_2017"
        if not os.path.isdir('{}/5년치종합/{}_csv/split_0{}/'.format(save_drive,file_name, hpa)):
            os.mkdir('{}/5년치종합/{}_csv/split_0{}/'.format(save_drive,file_name, hpa))
        print("시작")
        np.savetxt(
            '{}/5년치종합/{}_csv/split_0{}/'.format(save_drive,file_name, hpa) + file_list[idx][:9] + 'train_' + file_list[idx][9:], train_list, delimiter=',')
        print("train완료")
        np.savetxt(
            '{}/5년치종합/{}_csv/split_0{}/'.format(save_drive,file_name, hpa) + file_list[idx][:9] + 'test_' + file_list[idx][9:], test_list, delimiter=',')
        print("test완료")
        np.savetxt(
            '{}/5년치종합/{}_csv/split_0{}/'.format(save_drive,file_name, hpa) + file_list[idx][:9] + 'valid_' + file_list[idx][9:], valid_list, delimiter=',')
        print("valid완료")

        del (csv_data,train_list,train_true_random_idx,train_false_random_idx,
            valid_list,valid_true_random_idx,valid_false_random_idx,
            test_list,test_true_random_idx,test_false_random_idx)