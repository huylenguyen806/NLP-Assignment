def logical_form(gram_rel):
    logical_form = []
    dest = []
    for gram in gram_rel:
        if gram[0] == 'PRED':
            logical_form.append((gram[1],))
        elif gram[0] == 'LSUBJ':
            if len(gram) > 2:
                if gram[2][0] == 'WH':
                    logical_form.append(('WH', gram[1]))
                    if not ('AGENT', gram[1]) in logical_form:
                        logical_form.append(('AGENT', gram[1]))
                else:
                    if not ('AGENT', gram[1], gram[2]) in logical_form:
                        logical_form.append(('AGENT', gram[1], gram[2]))
            else:
                if not ('AGENT', gram[1]) in logical_form:
                    logical_form.append(('AGENT', gram[1]))
        elif gram[0] == 'LOBJ':
            if len(gram) > 2:
                logical_form.append(('THEME', gram[1], gram[2]))
            else:
                logical_form.append(('THEME', gram[1]))
        elif gram[0] in ['FROM', 'WH_TIME', 'W_TIME', 'ATIME', 'DTIME']:
            if gram[0] == 'FROM':
                dest.append(gram)
            logical_form.append(gram)
    for i in range(len(logical_form)):
        if logical_form[i][0] == 'AGENT' and ('FROM', logical_form[i][-1][-1]) in dest:
            del logical_form[i]
            break
    return logical_form
