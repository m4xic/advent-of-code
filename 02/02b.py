def is_safe(increasing, n1, n2):
    if increasing:
        return n2 in range(n1+1, n1+4)
    else:
        return n2 in range(n1-3, n1)


with open('input', 'r') as f:
    reports = f.read().splitlines()

print(reports)

report_report = {'safe': 0, 'unsafe': 0}

for original_report in reports:
    this_report = False
    original_report = [ int(x) for x in original_report.split() ]
    
    for i in range(len(original_report)):
        report = list(original_report)
        report.pop(i)

        
        copied = list(report)
        copied.sort()
        if report == copied:
            going = True
        elif report == copied[::-1]:
            going = False
        else:
            continue

        
        while len(report) != 1:
            if is_safe(going, report[0], report[1]):
                report.pop(0)
                continue
            else:
                break

        if len(report) == 1:
            this_report = True
            continue
        else:
            continue
    
    if this_report:
        report_report['safe'] += 1
    else:
        report_report['unsafe'] += 1

   

print(report_report)
