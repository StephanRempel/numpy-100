with open('exercises101.ktx') as fd:
    line_lst = fd.readlines()

print(len(line_lst))
in_drop = False
with open('exercises101a.ktx','w') as fd:
    for idx,line in enumerate(line_lst):
        if not in_drop:
            fd.write(line)
        if line.startswith('< a') or line.startswith('< q'):
            in_drop = True
        if idx+1 < len(line_lst) and line_lst[idx+1].startswith('<'):
            fd.write('\n')
            in_drop = False

