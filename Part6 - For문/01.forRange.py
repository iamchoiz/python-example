patterns = ['가위', '바위', '보']

for i in range(3):
    name = patterns[i]
    print('{}번은 {}'.format(i,name))


for i in range(len(patterns)):
    name = patterns[i]
    print('{}번은 {}'.format(i,name))

for i, name in enumerate(patterns):
    print('{}번은 {}'.format(i,name))


