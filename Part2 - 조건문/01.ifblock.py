if True:
    print('True')
    print('들여쓰기')
    if True:
        print('Block 속 Block')
    if False:
        print('Block 속 Block')

print('끝난 블록')

if False:
    print('조건이 안 맞는 블록')
    if True:
        print('조건이 안 맞는 블록 속 IF')
    print('Block In print')
