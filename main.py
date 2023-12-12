import re
import csv

if __name__ == '__main__':

    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    result_list, phone, name, organisation, position, email, result_dict = [], [], [], [], [], [], {}
    for i in range(1, len(contacts_list)):

        fio = ' '.join(filter(None, contacts_list[i][0:3]))
        name.append(fio)
        organisation.append(contacts_list[i][3])
        position.append(contacts_list[i][4])
        email.append(contacts_list[i][6])

        tel_list = contacts_list[i][5].split('доб')
        res_tel = (re.findall(r'\d+\s*', ''.join(tel_list[0])))
        tel = ''.join(res_tel).replace(' ', '')
        if len(tel) == 11:
            tel = '+7(' + tel[1:4] + ')' + tel[4:7] + '-' + tel[7:9] + '-' + tel[9:11]

            if len(tel_list) > 1:
                res_tel = (re.findall(r'\d+\s*', ''.join(tel_list[1])))
                tel += ' доб.' + ''.join(res_tel).replace(' ', '')
        phone.append(tel)

    result_list = zip(name, organisation, position, phone, email)
    result_list = list(result_list)

    default_dict = {
        'first_name': '',
        'last_name': '',
        'surname': '',
        'organization': '',
        'position': '',
        'phone': '',
        'email': ''
    }

    for i in range(len(result_list)):

        key = " ".join(result_list[i][0].split()[0:2])
        item = result_dict.setdefault(key, default_dict.copy())

        if item['last_name'] == '':
            item['last_name'] = " ".join(result_list[i][0].split()[0:1])
        if item['first_name'] == '':
            item['first_name'] = " ".join(result_list[i][0].split()[1:2])
        if item['surname'] == '':
            item['surname'] = " ".join(result_list[i][0].split()[2:3])
        if item['organization'] == '':
            item['organization'] = result_list[i][1]
        if item['position'] == '':
            item['position'] = result_list[i][2]
        if item['phone'] == '':
            item['phone'] = result_list[i][3]
        if item['email'] == '':
            item['email'] = result_list[i][4]

    contacts_list = []
    contacts_list.append(['lastname','firstname','surname','organization','position','phone','email'])
    for item in result_dict.values():
        contacts_list.append([item['last_name'], item['first_name'], item['surname'], item['organization'], item['position'], item['phone'], item['email']])

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',',lineterminator='\n')
        datawriter.writerows(contacts_list)
