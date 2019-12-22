def query(proc_sem):
    query = {}
    for proc in proc_sem:
        if proc[0].lower() == 'xe_buýt':
            if len(proc) == 1:
                continue
            if len(proc) > 1:
                query['BUS'] = proc[1][-1]
        elif proc[0] == 'DEST':
            if len(proc[1]) > 1 and type(proc[1]) is tuple:
                query['DEST'] = proc[1][-1]
            else:
                query['DEST'] = proc[1]
            if query['DEST'].lower() == 'hồ_chí_minh':
                query['DEST'] = 'HCMC'
            elif query['DEST'].lower() == 'đà_nẵng':
                query['DEST'] = 'DANANG'
            elif query['DEST'].lower() == 'huế':
                query['DEST'] = 'HUE'
        elif proc[0] == 'SOURCE':
            if len(proc[1]) > 1 and type(proc[1]) is tuple:
                query['SOURCE'] = proc[1][-1]
            else:
                query['SOURCE'] = proc[1]
            if query['SOURCE'].lower() == 'hồ_chí_minh':
                query['SOURCE'] = 'HCMC'
            elif query['SOURCE'].lower() == 'đà_nẵng':
                query['SOURCE'] = 'DANANG'
            elif query['SOURCE'].lower() == 'huế':
                query['SOURCE'] = 'HUE'
        elif proc[0] in ['FIND-THE', 'PRINT-ALL']:
            if proc[1].lower() == 'xe_buýt':
                query['FIND'] = 'BUS'
            else:
                query['FIND'] = proc[1]
        elif proc[0] in ['ATIME', 'DTIME']:
            query[proc[0]] = proc[1]
    return query

def conduct_query(query, data):
    find = query['FIND']
    del query['FIND']
    results = []
    def check_contidion(line, query):
        is_checked = True
        for key in query.keys():
            if line[key].lower() != query[key].lower():
                is_checked = False
                break
        return is_checked

    for line in data:
        if not check_contidion(line, query):
            continue
        results.append(line[find])
    return results


