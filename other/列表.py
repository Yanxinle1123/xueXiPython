list = []
while True:
    beichazhao = input('>>>')
    list.append(beichazhao)
    print(list)
    word = list[0]
    jieguo = word[3:-4]
    print(jieguo)
    list.clear()
    print(list)
    if beichazhao == 'q':
        break
