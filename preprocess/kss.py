import os
import kss

input_dir = './data'
output_dir = './outputs'

file_list = os.listdir(input_dir)

text = ''
# 정제된 데이터를 kss 라이브러리를 사용하여 문장분리함
for name in file_list:
    with open(f'{input_dir}/{name}', 'r', encoding='UTF-8') as f:
        text += f.read()
sentences = kss.split_sentences(text)
    
# 분리된 문장들을 각각 txt로 저장
index = 1
while index <= len(sentences):
    with open(f'{output_dir}/{index}.txt', 'w') as file:
        file.writelines(sentences[index-1])
    index += 1
