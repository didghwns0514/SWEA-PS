


def solution(fees, records):

    기본_시간, 기본_요금, 단위_시간, 단위_요금 = fees

    record_data = {
    }

    for record in records:
        time, carNum, Direction = record.split(' ')
        print(f'time, carNum, Direction : {time, carNum, Direction}')

        if carNum not in record_data:
            record_data[carNum] = {
                'IN':[],
                'OUT':[]
            }

        if Direction == 'IN':
            record_data[carNum]['IN'].append(time)
        elif Direction == 'OUT':
            record_data[carNum]['OUT'].append(time)


    # Index correction
    for carNum in record_data:
        len1 = len(record_data[carNum]['IN'])
        len2 = len(record_data[carNum]['OUT'])
        if len1 !=  len2:
            for _ in range(int(len1-len2)):
                record_data[carNum]['OUT'].append('23:59')


    # calculate fees
    fees_history = {
        key:0 for key in record_data.keys()
    }
    for key, val in record_data.items():
        print(f'key : {key}')
        timeLaps = 0
        for group in zip(val['IN'], val['OUT']):
            print(f'group : {group}')
            tmpTimeLaps = praseMinute(group[0], group[1])
            print(f'tmpTimeLaps : {tmpTimeLaps}')
            timeLaps += tmpTimeLaps

        totalCharge = 0
        if timeLaps <= 기본_시간:
            totalCharge += 기본_요금
        else:
            totalCharge += 기본_요금
            tmpUpper = ( (timeLaps - 기본_시간) / 단위_시간 )
            tmpUpper = int(tmpUpper + 1) if int(tmpUpper) < tmpUpper else int(tmpUpper)
            totalCharge += tmpUpper * 단위_요금

        fees_history[key] = totalCharge



    return [ fees_history[key] for key in sorted(fees_history.keys()) ]

def praseMinute(string1, string2):
    h1, m1 = string1.split(':')
    h1, m1 = int(h1), int(m1)

    h2, m2 = string2.split(':')
    h2, m2 = int(h2), int(m2)

    total1, total2 = (h1 * 60) + m1, (h2 * 60) + m2

    return abs(total2-total1)


if __name__ == "__main__":
    type = 0
    if type == 0:
        fees = [180, 5000, 10, 600]
        records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

    solution(fees, records)