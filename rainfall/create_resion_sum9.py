import pandas as pd
import collections
import numpy as np
import os
def region_sum_9(region):
    #각 지역의 격자점 index와 주위 8개 지역의 index --->4자리 앞 두개 숫자:longitude, 뒤 두개 숫자: latitude
    """
    0 1 2
    3 4 5
    6 7 8
    아래 지역_9 list index를 의미
    4번 index: 해당 지역의 index를 의미
    """
    Sokcho_9 = ['5487','5587','5687','5488','5588','5688','5489','5589','5689']
    Daegwallyeong_9 = ['5589','5689','5789','5590','5690','5790','5591','5691','5791']
    Gangneung_9 = ['5689','5789','5889','5690','5790','5890','5691','5791','5891']
    Donghae_9 = ['5690','5790','5890','5691','5791','5891','5692','5792','5892']
    Taebaek_9 = ['5691','5791','5891','5692','5792','5892','5693','5793','5893']
    Uljin_9 = ['5892','5992','6092','5893','5993','6093','5894','5994','6094']
    Pohang_9 = ['5896','5996','6096','5897','5997','6097','5898','5998','6098']
    Ulsan_9 = ['5798','5898','5998','5799','5899','5999','57100','58100','59100']
    s = [Sokcho_9,Daegwallyeong_9,Gangneung_9,Donghae_9,Taebaek_9,Uljin_9,Pohang_9,Ulsan_9]
    region_9 = collections.OrderedDict()
    for idx, r in enumerate(region):
        region_9[region[idx]] = s[idx]
    return region_9


def one_year(y):
    y = int(y)
    if (y % 4 == 0 and y % 100 != 0) or (y % 4 == 0 and y % 100 == 0 and y % 400 == 0): #그 해의 총 일수를 구하는 함수
        one_year_day = 366
        return one_year_day*24
    else:
        one_year_day = 365
        return one_year_day*24


def rainfall_sum9(save_drive):
    region = ['Sokcho','Daegwallyeong','Gangneung', 'Donghae', 'Taebaek', 'Uljin', 'Pohang', 'Ulsan'] #강원5개지역, 경상 3개지역
    path = '{}/rainfall/'.format(save_drive)
    year_list = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
    region_dict = region_sum_9(region)
    #각 지역별,각년도별로 9개 격자점을 하나의 파일로 묶음
    # 지역_9 리스트의 0 1 2 3 4 5 6 7 8 9 순서대로 36*9개를 일렬로 정렬
    for idx,one_region in enumerate(region):
        for year in year_list:
            storage = np.zeros((one_year(year),4+36*9+3))
            new_path = path + region[idx] +'/' + year +'_csv/'
            start_idx = 4
            end_idx = 40
            for region_idx in range(len(region_dict[region[idx]])):
                if (len(region_dict[region[idx]])-1) == region_idx:
                    temporary_storage = pd.read_csv(new_path + 'X' + str(region_dict[region[idx]][region_idx][:2]).zfill(3) + '_Y' + str(region_dict[region[idx]][region_idx][2:]).zfill(3) + '_700.csv',
                    header=None
                    )._values
                    storage[:,start_idx:end_idx+1] = temporary_storage[:,:-2]
                    storage[:,-2] = float(region_dict[region[idx]][4][:2])
                    storage[:,-1] = float(region_dict[region[idx]][4][2:])
                else:
                    temporary_storage = pd.read_csv(new_path +'X'+str(region_dict[region[idx]][region_idx][:2]).zfill(3) + '_Y' + str(region_dict[region[idx]][region_idx][2:]).zfill(3)+'_700.csv',
                    header = None
                    )._values
                    storage[:,start_idx:end_idx] = temporary_storage[:,:-3]
                    start_idx = end_idx
                    end_idx = end_idx + 36
            if not os.path.exists(new_path+'sum9'):
                os.makedirs(new_path+'sum9')
            filename = 'labelX_rainfall_X{}_Y{}.csv'.format(region_dict[region[idx]][4][:2].zfill(3),region_dict[region[idx]][4][2:].zfill(3))
            np.savetxt(new_path + 'sum9/'+filename,storage,delimiter=',')
            print("지역:{},{}년완료".format(region[idx],year))

    print(3)



