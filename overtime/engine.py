from datetime import datetime
from pytz import timezone

class ATR_Processor():
    list_finger = []

    def openfile(self):
        b = []
        f = open('media/102_attlog.dat')
        a = sorted(f.readlines())
        f.close()
        localtz = timezone('Asia/Jakarta')
        for i in a:
            i = i.split()
            date = localtz.localize(datetime.strptime(i[1] + ' ' + i[2], '%Y-%m-%d %H:%M:%S'))
            x = {'id': i[0], 'date': date}
            b.append(x)
        return b

    def processfile(self, atrfile):
        file = atrfile
        i = file[0]
        status_input = 0
        file.remove(i)


        while len(file) > 0:
            if status_input == 0:
                if i['date'].hour > 5 and i['date'].hour < 13:
                    finger = {'id': i['id'], 'date_in': i['date'], 'date_out': None}
                else:
                    finger = {'id': i['id'], 'date_in': None, 'date_out': i['date']}
            for a in file:
                if a['id'] == i['id']:
                    if a['date'].strftime('%Y-%m-%d') == i['date'].strftime('%Y-%m-%d'):
                        if a['date'].hour > 5 and a['date'].hour < 13:
                            file.remove(a)
                            status_input = 1
                            break
                        else:
                            finger['date_out'] = a['date']
                            file.remove(a)
                            status_input = 1
                            break
                    else:
                        i = a
                        file.remove(a)
                        status_input = 0
                        self.list_finger.append(finger)
                        break
                else:
                    i = a
                    file.remove(a)
                    status_input = 0
                    self.list_finger.append(finger)
                    break
        else:
            self.list_finger.append(finger)

        for i in self.list_finger:
            if i['date_in']==None:
                date = i['date_out'].replace(hour=7, minute=0, second=0)
                i['date_in']=date
            elif i['date_out']==None:
                date = i['date_in'].replace(hour=18, minute=0, second=0)