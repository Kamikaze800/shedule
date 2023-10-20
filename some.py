class Notes:
    def __init__(self, filename):
        file = map(str.rstrip, open(filename, encoding='utf-8').readlines())
        self.data = {}
        new_date = True
        day = month = ''
        for line in file:
            if new_date:
                day, month = line.split()
                new_date = False
            elif not line:
                new_date = True
            else:
                self.data[(int(day), month)] = self.data.get((int(day), month), []) + [line]

    def get_data(self):
        return self.data

    def get_month(self, month):
        result = []
        for k, v in self.data.items():
            if k[-1] == month:
                result.append(f'{k[0]} {k[1]}')
                result.extend(v)
                result.append('')
        return result

    def __len__(self):
        return len(self.data)

    def notes(self):
        return sum(len(v) for v in self.data.values())

    def save(self, data, filename):
        with open(filename, 'w', encoding='utf8') as file:
            file.writelines([f'{x}\n' for x in data])


if __name__ == '_main_':
    pc = Notes('notes.txt')
    data = pc.get_month('июль')
    pc.save(data, 'month.txt')
