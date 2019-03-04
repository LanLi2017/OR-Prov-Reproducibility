# find projectID.zip
import json
import os
from pprint import pprint
from zipfile import ZipFile

import re

from io import TextIOWrapper

import copy


def find_project_zip(projectid, path):
    for root,dirs,files in os.walk(path, topdown=True):
        for fname in dirs:
            print(fname)
            if projectid==fname.split('.')[0]:
                return os.path.join(root,fname)


def check_path(prompt):
    while True:
        name=input(prompt)
        '''
        https://github.com/OpenRefine/OpenRefine/wiki/FAQ:-Where-Is-Data-Stored%3F
        
        MacOSX:

        ~/Library/Application Support/OpenRefine/
        '''
        OR_path=os.path.expanduser('~/Library/Application Support/OpenRefine')
        path=find_project_zip(name,OR_path)
        if path is not None:
            return path
        else:
            print('Project ID not Found.')


# zip files in history folder
def deal_zipfile(file_p,text_name):
    with ZipFile(file_p)as change_f:
        with change_f.open(text_name)as history_change:
            change_P=TextIOWrapper(history_change,encoding='utf-8')
            change_list=[line.rstrip('\n') for line in change_P]
            return change_list


def extract_JSON(datazip_path):
    # unzip data.zip  -> data.txt ->  id for change.txt -> description
    # deal with data.zip
    # extract json part from data.txt
    # start from 'pastEntryCount='
    # end with 'futureEntryCount='
    start_position=0
    end_position=0
    start_regex=re.compile('pastEntryCount=[0-9]+')
    end_regex=re.compile('futureEntryCount=[0-9]+')
    data=deal_zipfile(datazip_path,'data.txt')
    for index,item in enumerate(data,start=0):
        if start_regex.match(item):
            start_position=index+1
        if end_regex.match(item):
            end_position=index
    preJson=data[start_position:end_position]

    return preJson


def form_JSON(prejson_file,json_path):
    Norm_JSON=[]
    for jsonpart in prejson_file:
        j=json.loads(jsonpart)
        Norm_JSON.append(j)
    with open(json_path,'wt')as f:
        json.dump(Norm_JSON,f,indent=2)


def get_count(change_list):
    start_regex=re.compile('cellChangeCount=[0-9]+')
    cell_change_count=0
    for index,item in enumerate(change_list,start=0):
        if start_regex.match(item):
            cell_change_count=int(item.split('=')[-1])
    return cell_change_count


def get_op_name(change_list):
    # the first line in the file
    op_name=change_list[1].split('.')[-1]
    return op_name


# mass cell changes format
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


# single cell changes format
def read_single():
    pass


# split column changes format
def read_split():

    pass


# addition column changes format
def read_addition():
    pass


# rename column changes format
def read_rename():
    pass


# removal column changes format
def read_removal():
    pass


# star row changes format
def read_star():
    pass






def extract_History(Hfiles_path_list):
    '''
    :param Hfiles_path_list: ids
    :return:
    if id== "id" in JSON
       expand dicts in JSON
    '''
    # start_regex=re.compile('cellChangeCount=[0-9]+\n')
    # start_position=0
    changes_list=[]
    f_id_list=[]
    # cell_change_count=0
    for file_p in Hfiles_path_list:
        f_id=(file_p.split('/')[-1]).split('.')[0]
        with ZipFile(file_p)as change_f:
            with change_f.open('change.txt') as history_change:
                change_P=TextIOWrapper(history_change,encoding='utf-8')
                cell_change_count=get_count(file_p)
                print(cell_change_count)
                it=iter(change_P)
                # hard code ...
                for _ in range(5):
                    next(it)
                norm_changes_edits=list(read_records(it,cell_change_count))
        changes_list.append(norm_changes_edits)
        f_id_list.append(f_id)
    All_changes_edits=[{'id':i, 'changes':c}for i,c in zip(f_id_list,changes_list)]
    pprint(All_changes_edits)
    return All_changes_edits


def combine_Data_History(norm_cell_change,data_json_path):
    # pointer: id
    # add cell_change to every pointer
    with open(data_json_path,'r+')as f:
        data_json=json.load(f)
        for file_change in norm_cell_change:
            f_id=int(file_change['id'])
            cell_change=file_change['changes']
            for d in data_json:
                d_id=d['id']
                if f_id== d_id:
                    d['edits']=cell_change
        f.seek(0) #rewind
        json.dump(data_json,f,indent=2)
        f.truncate()
                    # d['row']=cell_change['row']
                    # d['column']=cell_change['cell']
                    # edit=[{'from': old,'to': new} for old,new in zip(cell_change['old'],cell_change['new'])]
                    # d['changes']=edit



def main():
    # find project path
    project_path=check_path('Input the project ID:')
    names=os.listdir(project_path)
    print(names)
    '''
    data.zip
    history(folder)
    '''
    # deal with data.zip
    datazip_path=os.path.join(project_path,'data.zip')
    print(os.path.exists(datazip_path))
    history_path=os.path.join(project_path,'history')
    # extract JSON from data.zip
    preJson=extract_JSON(datazip_path)
    json_path='../JSON/%s.json'%(input('input the json name:'))
    form_JSON(preJson,json_path)

    # extract info from JSON -> refer to history folder -> IDs.zip
    history_files=os.listdir(history_path)
    print(history_files)
    cor_hf=[]
    for hf in history_files:
        if hf!='.DS_Store':
            cor_hf.append(hf)
    Hfiles_list=[os.path.join(history_path,cf) for cf in cor_hf]
    print(Hfiles_list)

    # raw changes extracting from History folder -> id.change.zip
    # op_name=['MassCellChange','CellChange','ColumnSplitChange','ColumnAdditionChange','ColumnRenameChange','ColumnRemovalChange','RowStarChange']
    op_action_map={
        'MassCellChange': read_records,
        'CellChange': read_single,
        'ColumnSplitChange': read_split,
        'ColumnAdditionChange': read_addition,
        'ColumnRenameChange': read_rename,
        'ColumnRemovalChange': read_removal,
        'RowStarChange': read_star,
    }


    all_changes=extract_History(Hfiles_list)

    combine_Data_History(all_changes,json_path)


if __name__=='__main__':
    main()
