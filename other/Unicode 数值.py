while True:
    try:
        huoqu = input('>>>')
        if huoqu == '1':
            while True:
                shuru = input('<>>')
                if shuru == 'q':
                    break
                shuru = ord(shuru)
                print(shuru)
        elif huoqu == '2':
            shuru = int(input('<<>'))
            minwen = chr(shuru)
            print(minwen)
            if shuru == 'q':
                break
        elif huoqu == 'q':
            break
    except:
        print('error')
