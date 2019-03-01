from pprint import pprint

def read_records(file,cell_change_count):
    for _ in range(cell_change_count):
        cell_change={}
        while True:
            line=file.readline()
            if line=='/ec/\n' or not line:
                break
            key,*value=line.split('=')
            value='='.join(value)
            cell_change[key]=value
        yield cell_change


def main():
    cell_change_count=3
    with open('test.txt','rt')as f:
        for _ in range(5):
            next(f)
        result=list(read_records(f,cell_change_count))
        pprint(result)


if __name__=='__main__':
    main()
# def read_records(file):
#     pprint(file)
#     for i in range(4):
#         cell_change={}
#         while True:
#             line=file[i]
#             if line=='/ec/\n' or not line:
#                 break
#             key, *value=line.split('=')
#             value='='.join(value)
#             cell_change[key]=value
#             i+=1
#         yield cell_change
#
#
# lists=[
#     'row=3\n',
#     'cell=3\n',
#     'old={"v":"CORTLAND COUNTY SOCIETY OF NEW YORK"}\n',
#     'new={"v":"cortland county society of new york"}\n',
#     '/ec/\n',
#     'row=5\n',
#     'cell=3\n',
#     'old={"v":"Gramercy Inn; H.R. Weissberg Hotel Corp."}\n',
#     'new={"v":"gramercy inn; h.r. weissberg hotel corp."}\n',
#     '/ec/\n',
#     'row=6\n',
#     'cell=3\n',
#     'old={"v":"Bethlehem Steel Club"}\n',
#     'new={"v":"bethlehem steel club"}\n',
#     '/ec/\n',
#     'row=7\n',
#     'cell=3\n',
#     'old={"v":"SUMMIT HOUSE"}\n',
#     'new={"v":"summit house"}\n',
#     '/ec/\n',
# ]
# result=list(read_records(lists))
# pprint(result)
#
