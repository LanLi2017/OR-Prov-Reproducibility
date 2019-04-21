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
        name=raw_input(prompt)
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
    data_Json=data[start_position:end_position]
    d=[]
    for info in data_Json:
        json_acceptable_string=info.replace("'","\"")
        d.append(json.loads(json_acceptable_string))
    return d


def read_missing_records(change_list):
    """
    :param change_list: change list from data.zip
    :return: new dict
    """
    use_data=change_list[2:len(change_list)-1]
    cell_change={}
    for d in use_data:
        key,value=d.split('=')
        cell_change[key]=value
    return cell_change


# return the file
def deal_mis_history_file_path(history_path,id):
    # missing_path=history_path/id.change.zip
    # unzip missing_path
    # ../data.txt
    history_file=os.path.join(history_path,'%d.change.zip'%id)
    print("=====")
    print(history_file)
    print("======")
    data=deal_zipfile(history_file,'change.txt')
    return data


def store_JSON(data_json,json_path):
    with open(json_path,'wt')as f:
        json.dump(data_json,f,indent=2)
    # Norm_JSON=[]
    # for jsonpart in data_json_file:
    #     j=json.loads(jsonpart)
    #     Norm_JSON.append(j)
    # with open(json_path,'wt')as f:
    #     json.dump(Norm_JSON,f,indent=2)


def extract_history(input_file):
    """
    use any function that have been developed
    process an openrefine project file
    extract the history including the hidden activities (non "op" activities)
    for the non "op" activities, add customize "op", specify the input structure
    for each case and add it in this documentation and add "custom": True in the
    dictionary structure.
    For example:
    single_edit: "op": { "name": "single_edit",
                        "col_index": <int value of column index edited>,
                        "row_index": <int value of row index edited>,
                        "old_value": <old_string>
                        "new_value": <new_string>
                        }


    :param input_file: string, file path of the exported project
    :return: dictionary of history
    """
    # read data.txt
    # get operations which do not have 'op'
    # enhanced JSON recipe = 'op' operations + reviewed_'op'
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

    # path of history
    history_path=os.path.join(project_path,'history')

    # extract JSON from data.zip which contains operations without 'op'
    inComplete_Json=extract_JSON(datazip_path)


    # deal with inComplete_Json
    # get the ids of "missing" operations
    complete_Json=[]
    for dicts in inComplete_Json:
        if "operation" not in dicts.keys():
            id=dicts['id']
            # id_missing_list.append(id)
            # replace this with the new one
            change_list=deal_mis_history_file_path(history_path,id)
            new_dicts=read_missing_records(change_list)
            dicts.update(new_dicts)
            complete_Json.append(dicts)
        else:
            complete_Json.append(dicts)
    # store the json file : enhanced recipe
    json_path='../JSON/%s.json'%(raw_input('input the json name:'))
    store_JSON(complete_Json,json_path)

    # need to wait for updating data.zip


def main():
    """
    execute test scenarios here
    :return:

    """
    import json
    test_file = "../test_files/airbnb_test.tar.gz"
    recipe = extract_history(test_file)
    print(json.dump(recipe))


if __name__=='__main__':
    main()


