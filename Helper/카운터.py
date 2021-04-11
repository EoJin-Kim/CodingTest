my_list  = ['Tick', 'Tock', 'Tock'] # 나의 리스트
new_list = ['Tick', 'Tock', 'Song'] # 추가로 나타난 리스트

# 나의 리스트를 센다
from collections import Counter
counter = Counter(my_list)
print(counter)