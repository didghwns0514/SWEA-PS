


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




    answer = []
    return answer


if __name__ == "__main__":
    type = 0
    if type == 0:
        fees = [180, 5000, 10, 600]
        records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

    solution(fees, records)