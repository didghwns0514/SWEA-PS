
class User:

    def __init__(self, name, k):
        self.name = name
        self.report_set = set()
        self.k = k

    def addReport(self, name):
        self.report_set.add(name)

    def isBanned(self):
        if len(self.report_set) >= self.k:
            return True
        else: return False

def solution(id_list, report, k):

    data = {}
    for _name in id_list:
        data[_name] = {'User' : User(_name, k), 'num_reports' : 0}

    for _report in report:
        reporter, reported = _report.split(' ')
        data[reported]['User'].addReport(reporter)

    report_count = { name : 0 for name in id_list }
    for _name in id_list:
        # print('-'*20)
        # print(f'_name : {_name}')
        if data[_name]['User'].isBanned():
            #print(f'{_name} is banned')
            #report_count[_name] += 1
            #print(f"data[_name]['User'].report_set : {data[_name]['User'].report_set}")
            for reporter in data[_name]['User'].report_set:
                report_count[reporter] += 1

    return [ report_count[_name] for _name in id_list ]

if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2

    returnValue = solution(id_list, report, k)
    print(f'returnValue : {returnValue}')