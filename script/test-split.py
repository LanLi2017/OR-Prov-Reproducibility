import re
from pprint import pprint

import itertools


def get_new_column_count():
    pass


def get_new_row_count():
    pass



# column name
'''
:keyword: columnNameCount=4
:keyword: rowIndexCount=102
'''

# row index list
'''
:keyword: rowIndexCount=102
:keyword: tupleCount=102
'''
# cell values per row
'''
:keyword: tupleCount=102
:keyword: removeOriginalColumn=true
'''

# return: column_name:[{row_index: cell_value},{},...] 2-D matrix
# column :
# data=[
# ["supper lunch","history", "Mr.Li", "his"],
# ["ice", "brilliant", "her"],
# ...,
# ]

def main():
    # data=[4,'a','b','c','d',3,1,'f','g']
    # result=[]
    # it=iter(data)
    # while True:
    #     try:
    #         n=next(it)
    #         row=[]
    #         for i in range(n):
    #             row.append(next(it))
    #         result.append(row)
    #     except StopIteration:
    #         break
    # print(result)

    start_pos=re.compile('tupleCount=[0-9]+\n')
    start_point=0
    end_point=0
    with open('test-split.txt','r')as f:
        data=f.read().splitlines()
        print(data)
        # for index,item in enumerate(data,start=0):
        #     if start_pos.match(item):
        #         start_point=index+1
        #         print(start_point)
        #     if item=='removeOriginalColumn=true\n' or item=='removeOriginalColumn=false\n':
        #         end_point=index
        #         print(end_point)
        use_data=data[112:320]
        print(use_data)
        result=[]
        it=iter(use_data)
        while True:
            try:
                n=next(it)
                row=[]
                for i in range(int(n)):
                    row.append(next(it))
                result.append(row)
            except StopIteration:
                break
        print(result)

        for r in itertools.zip_longest(*result):
            pprint(r)





if __name__=='__main__':
    main()
