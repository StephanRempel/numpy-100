with open('exercises101.ktx',encoding='utf8') as fd:
    # lines=[]
    # for line in fd:
    #     print(line.strip())
   lines = fd.readlines()
# exit()
cnt = 1
with open('exercises101a.ktx','w',encoding='utf8') as fd:
    for line in lines:
        if line.startswith('< q'):
            line=f'< q{cnt}\n'
        if line.startswith('< a'):
            line=f'< a{cnt}\n'
            cnt += 1
        if line.startswith('< h'):
            line=f'< h{cnt}\n'
        fd.write(line)
