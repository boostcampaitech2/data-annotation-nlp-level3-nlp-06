import csv
import pandas as pd

ANNOTATOR_NUM = 7 # annotator 수
START_COLUMN = 3 # tagging이 시작되는 열
GROUND_TRUTH_COLUMN = 2 # ground_truth 열


labels = {'기술 : 개발일' : 1, '기술 : 정의' : 2, '기술 : 하위 기술' : 3, '기술 : 개발_단체' : 4, '인물 : 개발_기술' : 5, '인물 : 출판물' : 6, '서비스 : 출시 주체' : 7, '서비스 : 출시일' : 8, '서비스 : 기반 기술' : 9, 'ERROR' : 10, '기술:개발일' : 1, '기술:정의' : 2, '기술:하위기술' : 3, '기술:개발단체' : 4, '인물:개발기술' : 5, '인물:출판물' : 6, '서비스:출시주체' : 7, '서비스:출시일' : 8, '서비스:기반기술' : 9}

tsv_file = open('./datasets.tsv')
read_tsv = csv.reader(tsv_file, delimiter = "\t")
datasets = list(read_tsv)
raw_data = {}


for idx in range(ANNOTATOR_NUM): 
    key = datasets[0][START_COLUMN:START_COLUMN+ANNOTATOR_NUM][idx]
    raw_data[key] = []
    for row in datasets[1:]: # head 제외하고 value 값이 있는 row 부터 시작
        
        # tagging되지 않은 부분('')은 새로운 relation로 정의
        # if row[idx+START_COLUMN] == '':
        #     raw_data[key].append(11)
        # else:
        #     raw_data[key].append(labels[row[idx+START_COLUMN]])

        # tagging되지 않은 부분('')을 ERROR(no_relation)로 정의
        # if row[idx+START_COLUMN] == '':
        #     raw_data[key].append(labels['ERROR'])
        # else:
        #     raw_data[key].append(labels[row[idx+START_COLUMN]])

        # tagging되지 않은 부분('')을 ground_truth로 정의
        if row[idx+START_COLUMN] == '':
            raw_data[key].append(labels[row[GROUND_TRUTH_COLUMN]])
        else:
            raw_data[key].append(labels[row[idx+START_COLUMN]])


pd_data = pd.DataFrame(raw_data)
pd_data.to_excel(excel_writer='iaa_input.xlsx')