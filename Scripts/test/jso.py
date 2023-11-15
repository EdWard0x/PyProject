import json

if __name__ == '__main__':
    with open('a.json', 'r') as fr:
        a = json.load(fr)
        # print(a['rows'])
        for i in range(0,len(a['rows'])):
            print(a['rows'][i]['indicatorName'])