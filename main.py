from easterly.create_2008to2013 import *
from easterly.create_2014to2017 import *
from easterly.train_valid_test_5years import *
from rainfall.create_resion_sum9 import *
from rainfall.create_label import *
from rainfall.Gangwon_train_test import *
from rainfall.Gyeongsang_train_test import *
def easterly_5year(data_drive,save_drive):
    extract_2008to2013(2013,data_drive,save_drive) #2013년 label된 csv파일 추출 함수
    for i in [2014,2015,2016,2017]:
        extract_2014to2017(i,data_drive,save_drive) #2014,2015,2016,2017년 label된 csv파일 추출 함수
    min_max_calculation(save_drive) #2013,2014,2015,2016,2017년 5년치 묶어서 동풍 train,valid,test만드는 함수



def one_year_data(data_drive,save_drive):
    for i in [2008,2009,2010,2011,2012]:
        extract_2008to2013(i,data_drive,save_drive) #2008,2009,2010,2011,2012년 각각 label된 csv파일까지 추출하는 함수
    for i in [2013,2014,2015,2016,2017]:
        extract_2014to2017(i,data_drive,save_drive) #2013,2014,2015,2016,2017년 각각 label된 csv파일까지 추출하는 함수

def rainfall_10year(save_drive):
    rainfall_sum9(save_drive) #각지역과 주위 8개 격자점을 묶는 함수
    rainfall_label(save_drive) #4class로 label해주는 함수
    Gamgwon(save_drive) #강원지역 train,test만드는 함수
    Guepmgsang(save_drive) #경상지역 train,test만드는 함수



if __name__ == '__main__':
    data_drive = 'G:' #Era5 data 경로, 경로에 / 쓰지 않음
    save_drive = 'E:' #csv파일을 저장할 경로, 경로에 / 쓰지않음

    '''
    아래 3개함수
    easterly_5year : 동풍용 data 만드는 함수
    rainfall_10year : 강수용 data 만드는 함수
    one_year_data : 2008,2009,2010,2011,2012,2013,2014,2015,2016,2017년 각각 label된 csv파일까지 추출하는 함수
    '''

    easterly_5year(data_drive,save_drive)
    #rainfall_10year(save_drive)
    #one_year_data(data_drive,save_drive)
