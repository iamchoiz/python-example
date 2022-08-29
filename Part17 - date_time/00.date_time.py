import datetime

start_time = datetime.datetime.now()
print(start_time)

start_time = start_time.replace(year = 2017, month=2)
print(start_time)

start_time = datetime.datetime(2016,2,1)
print(start_time)


"""
코드의 5번째 줄을 수정해서 days_until_christmas 함수가 오늘부터 2030년 12월 25일 사이에 몇일이 있는지를 리턴하도록 만들어 보세요.
"""
def days_until_christmas():
    christmas_2030 = datetime.datetime(2030, 12, 25)
    how_long = christmas_2030 - datetime.datetime.now()
    days = how_long.days
    return days


print("{}일".format(days_until_christmas()))

