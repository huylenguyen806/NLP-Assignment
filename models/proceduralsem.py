def procedural_semantic(logical_form):
    proc_sem = []
    for log in logical_form:
        if log[0] == 'WH':
            proc_sem.append(('PRINT-ALL', log[1]))
        elif log[0] == 'WH_TIME':
            proc_sem.append(('FIND-THE', 'RUN_TIME'))
        elif log[0] == 'W_TIME':
            if log[1] == 'đến':
                proc_sem.append(('FIND-THE', 'ATIME'))
            elif log[1] == 'từ':
                proc_sem.append(('FIND-THE', 'DTIME'))
        elif log[0] == 'AGENT':
            if len(log) > 2:
                proc_sem.append((log[1], log[2]))
            else:
                proc_sem.append((log[1],))
        elif log[0] == 'FROM':
            proc_sem.append(('SOURCE', log[1]))
        elif log[0] == 'THEME':
            if len(log) > 2:
                proc_sem.append(('DEST', log[2]))
            else:
                proc_sem.append(('DEST', log[1]))
        elif log[0] in ['ATIME', 'DTIME']:
            proc_sem.append(log)
    return proc_sem
