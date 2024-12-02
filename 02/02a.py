def is_safe(increasing, n1, n2):
    if increasing:
        return n2 in range(n1+1, n1+4)
    else:
        return n2 in range(n1-3, n1)


with open('input', 'r') as f:
    reports = f.read().splitlines()

print(reports)

report_report = {'safe': 0, 'unsafe': 0}

for report in reports:
    report = report.split()
    report = [ int(x) for x in report ]
    copied = list(report)
    copied.sort()
    if report == copied:
        going = True
    elif report == copied[::-1]:
        going = False
    else:
        report_report['unsafe'] += 1
        continue
    

    while len(report) != 1:
        if is_safe(going, report[0], report[1]):
            report.pop(0)
            continue
        else:
            break

    if len(report) == 1:
        report_report['safe'] += 1
        continue
    else:
        report_report['unsafe'] += 1
        continue

   

print(report_report)
