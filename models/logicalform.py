from models.config import dep_relations, pos_tags, name_to_pos


def grammarical_relation(alpha):
    gram_rel = []
    for dep in alpha:
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
            else:
                temp = ('TO', dep[1][0])
            temp1 = None
        elif dep[0] == 'nummod':
            temp = ('TIME', dep[2][0])
            temp1 = None
        if temp in gram_rel:
            continue
        gram_rel.append(temp)
        if temp1:
            gram_rel.append(temp1)
    return gram_rel


def logical_form(gram_rel):
    logical_form = []
    for gram in gram_rel:
        if gram[0] == 'PRED':
            logical_form.append((gram[1],))
        elif gram[0] == 'LSUBJ':
            if len(gram) > 2:
                logical_form.append(('AGENT', gram[1], gram[2]))
            else:
                logical_form.append(('AGENT', gram[1]))
        elif gram[0] == 'LOBJ':
            if len(gram) > 2:
                logical_form.append(('THEME', gram[1], gram[2]))
            else:
                logical_form.append(('THEME', gram[1]))
        elif gram[0] in ['FROM', 'WH_TIME', 'TIME']:
            logical_form.append(gram)
    return logical_form
