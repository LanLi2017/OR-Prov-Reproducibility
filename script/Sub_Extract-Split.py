# get new split names
import re

import itertools
from collections import OrderedDict
from pprint import pprint


def deal_regex(file_list,start_regex, end_regex):
    start_index=0
    end_index=0
    start=re.compile(start_regex)
    end=re.compile(end_regex)
    for index,item in enumerate(file_list,start=0):
        item=item.split('=')[0]
        if start.match(item):
            start_index=index+1
        if end.match(item):
            end_index=index
    return file_list[start_index:end_index]


def main():
    with open('test-split.txt','r')as f:
        data=f.read().splitlines()
    start_col_regex='columnNameCount'
    end_col_regex='rowIndexCount'
    new_col_names=deal_regex(data,start_col_regex,end_col_regex)
    end_row_index_regex='tupleCount'
    row_index=deal_regex(data,end_col_regex,end_row_index_regex)
    end_row_value_regex='removeOriginalColumn'
    row_value=deal_regex(data,end_row_index_regex,end_row_value_regex)
    result=[]
    it=iter(row_value)
    # Edits=OrderedDict.fromkeys(new_col_names)
    while True:
        try:
            n=next(it)
            row=[]
            for i in range(int(n)):
                row.append(next(it))
            result.append(row)
        except StopIteration:
            break
    zip1=[]
    for r in itertools.zip_longest(*result):
        zip1.append(list(zip(row_index,r)))


    Edits=list(zip(new_col_names,zip1))
    pprint(Edits)



if __name__=='__main__':
    main()
