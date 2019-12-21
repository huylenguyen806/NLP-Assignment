from models.config import name_to_pos


def grammarical_relation(alpha):
    gram_rel = []
    for i in range(len(alpha)):
        dep = alpha[i]
        if dep[0] == 'nmod':
            if dep[2][0] == 'nào':
                temp = ('LSUBJ', dep[1][0], ('WH', dep[2][0]))
            else:
                done = False
                for i in range(len(gram_rel)):
                    if ('LOBJ', dep[1][0]) == gram_rel[i]:
                        gram_rel[i] = ('LOBJ', dep[1][0], ('NAME', dep[2][0]))
                        done = True
                        break
                if not done:
                    temp = ('LSUBJ', dep[1][0], ('NAME', dep[2][0]))
                else:
                    continue
            temp1 = None
        elif dep[0] == 'dobj':
            if dep[1][-1] == name_to_pos['verb']:
                temp = ('LOBJ', dep[2][0])
            else:
                temp = ('LOBJ', dep[1][0])
            temp1 = None
        elif dep[0] == 'nsubj':
            temp = ('PRED', dep[1][0])
            temp1 = ('LSUBJ', dep[2][0])
        elif dep[0] == 'wh_time':
            temp = ('WH_TIME', dep[2][0])
            temp1 = None
        elif dep[0] == 'case':
            if dep[2][0] == 'từ':
                temp = ('FROM', dep[1][0])
            elif dep[2][0] == '':
                temp = ('TO', dep[1][0])
            temp1 = None
        elif dep[0] == 'time':
            _type = None
            tim = dep[2][0]
            if 'lúc' in tim.lower():
                tim = tim.replace('lúc_', "")
            if 'hr' in tim.lower():
                tim = tim.lower().replace('hr', "")
            on_name = dep[1][0]
            x = []
            for j in range(i-1, -1, -1):
                x.append(alpha[j][1][0])
            for j in range(i-1, -1, -1):
                proper_n = alpha[j]
                if proper_n[1][0] == on_name:
                    if proper_n[2][0] == 'từ':
                        _type = "DTIME"
                    elif proper_n[2][0] == 'đến':
                        _type = "ATIME"
                    break
                elif proper_n[2][0] == on_name and on_name not in x:
                    on_name = proper_n[1][0]
            temp = (_type, tim)
            temp1 = None
        if temp in gram_rel:
            continue
        gram_rel.append(temp)
        if temp1:
            gram_rel.append(temp1)
    return gram_rel
