# -*- coding: utf-8 -*-

def init(file_name):
    global data
    data = []
    f = open(file_name)
    lines = f.readlines()
    del lines[0]
    for line in lines:
        info = line.strip().split(',')
        data.append(info)
    
def genderDistribution():
    gender = {}
    F = 0
    M = 0
    for d in data:
        if d[-1] == 'M':
            M += 1
        elif d[-1] == 'F':
            F += 1
    gender['F'] = F
    gender['M'] = M
    return gender

def collegeDistribution():
    colleges = []
    for d in data:
        if d[0] not in colleges:
            colleges.append(d[0])
    college = {}
    for col in colleges:
        M = 0
        F = 0
        for d in data:
            if d[0] == col:
                if d[-1] == 'M':
                    M += 1
                elif d[-1] == 'F':
                    F += 1
        college[col] = {'M':M,'F':F}
    return college
    
def departmentDistribution():
    departments = []
    for d in data:
        try:
            departments.append(d[2])
        except:
            continue
    unique_d = set(departments)
    department = {}
    for unique in unique_d:
        M = 0
        F = 0
        for d in data:
            try:
                if d[2] == unique and d[-1] == 'M':
                    M +=1
                elif d[2] == unique and d[-1] == 'F':
                    F += 1
            except:
                continue
        department[unique] = {'M':M,'F':F}
    return department

def majorDistribution():
    majors = []
    for d in data:
        try:
            majors.append(d[3])
        except:
            continue
    unique_m = set(majors)
    major = {}
    for unique in unique_m:
        M = 0
        F = 0
        for d in data:
            if len(d)!=6:
                continue
            if d[3] == unique:
                if d[-1] == 'M':
                    M +=1
                elif d[-1] == 'F':
                    F += 1
        major[unique] = {'M':M,'F':F}
    return major

def termDistribution():
    terms = []
    for d in data:
        if len(d) != 6:
            continue
        terms.append(d[-2])
    unique_t = set(terms)
    term = {}
    for unique in unique_t:
        M = 0
        F = 0
        for i in range(len(data)):
            d = data[i]
            if len(d)!=6:
                continue
            if d[-2] == unique:
                if d[-1] == 'M':
                    M +=1
                elif d[-1] == 'F':
                    F += 1
        term[unique] = {'M':M,'F':F}
    return term
    
    


        
        


