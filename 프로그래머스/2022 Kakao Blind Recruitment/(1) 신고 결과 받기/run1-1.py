
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



    answer = []
    return answer