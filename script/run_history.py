from openrefine_client.google.refine import refine

def run_history(input_file,project_name,recipe,output_file=None,metadata=None,refine_server_url="http://127.0.0.1:3333"):
    """
    From dictionary use openrefine client api, customized
    and run the operation in a sequential order
    based on the recipe including the custom/hidden recipe

    :param input_file: raw data input file that will be cleaned
    :param history_dict: dictionary of history
    :param output_file: save the process in the output file
    :return: new file
    """

    # initialize refine server
    refine_server = refine.Refine(refine.RefineServer(refine_server_url))

    # create new project
    if metadata!=None:
        """
        {u'contributors': u'',
         u'created': u'2019-04-20T22:38:19Z',
         u'creator': u'',
         u'customMetadata': {},
         u'description': u'',
         u'encoding': u'UTF-8',
         u'encodingConfidence': 0,
         u'homepage': u'',
         u'image': u'',
         u'importOptionMetadata': [{u'fileSource': u'Dataset/Menu.csv',
                                    u'guessCellValueTypes': False,
                                    u'headerLines': 1,
                                    u'ignoreLines': -1,
                                    u'includeFileSources': False,
                                    u'limit': -1,
                                    u'linesPerRow': 1,
                                    u'processQuotes': True,
                                    u'projectName': u'Tutorial_OR',
                                    u'separator': u',',
                                    u'skipDataLines': 0,
                                    u'storeBlankCellsAsNulls': True,
                                    u'storeBlankRows': True,
                                    u'storeEmptyStrings': True,
                                    u'trimStrings': False}],
         u'license': u'',
         u'modified': u'2019-04-21T18:49:14Z',
         u'name': u'Tutorial_OR',
         u'password': u'',
         u'preferences': {u'entries': {u'scripting.expressions': {u'class': u'com.google.refine.preference.TopList',
                                                                  u'list': [],
                                                                  u'top': 100},
                                       u'scripting.starred-expressions': {u'class': u'com.google.refine.preference.TopList',
                                                                          u'list': [],
                                                                          u'top': 2147483647}}},
         u'rowCount': 17545,
         u'subject': u'',
         u'tags': [],
         u'title': u'',
         u'version': u''}        
        """
        """
        new_project(self, project_file=None, project_url=None, project_name=None, project_format='text/line-based/*sv',
                            encoding='',
                            separator=',',
                            ignore_lines=-1,
                            header_lines=1,
                            skip_data_lines=0,
                            limit=-1,
                            store_blank_rows=True,
                            guess_cell_value_types=True,
                            process_quotes=True,
                            store_blank_cells_as_nulls=True,
                            include_file_sources=False,
                            **opts):        
        """
        metadata_option = metadata["importOptionMetadata"][0]
        new_project = refine_server.new_project(input_file, project_name=metadata_option["projectName"],
                                                encoding=metadata["encoding"],
                                                separator=metadata_option["separator"],
                                                ignore_lines=metadata_option["ignoreLines"],
                                                header_lines=metadata_option["headerLines"],
                                                skip_data_lines=metadata_option["skipDataLines"],
                                                limit=metadata_option["limit"],
                                                store_blank_rows=metadata_option["storeBlankRows"],
                                                guess_cell_value_types=metadata_option["guessCellValueTypes"],
                                                process_quotes=metadata_option["processQuotes"],
                                                store_blank_cells_as_nulls=metadata_option["storeBlankCellsAsNulls"],
                                                include_file_sources=metadata_option["includeFileSources"])
    else:
        new_project = refine_server.new_project(input_file,project_name=project_name)



    # execute operations

    all_history = []
    for op in recipe:
        result = new_project.execute_json_op(op)
        #print(result)
        #if result["code"] == "ok":
        #    if 'historyEntry' in result:
        #        all_history.append(result["historyEntry"])


    return new_project,new_project.list_history()
    #raise NotImplementedError

def select_project_byid(project_id,refine_server):
    return refine_server.open_project(project_id)

def select_project_byname(project_name,refine_server):
    refine_projects = list_projects(refine_server)
    #found = 0
    found_list = []
    for key,val in refine_projects.items():
        if val["name"]==project_name:
            found_list.append((key,val["name"],val["created"]))
            #found+=1
    if len(found_list)==1:
        return refine_server.open_project(found_list[0][0])
    else:
        for x in found_list:
            print("\t".join([x[0], x[1] + " (" + x[2] + ")"]))
        raise Exception("found more than one project name: "+project_name+" use pid to select the project")


def run_history_on_project(refine_project,recipe):
    for op in recipe:
        result = refine_project.execute_json_op(op)
    return refine_project.list_history()

def export_file(export_file,refine_project,export_format="csv"):
    """
    from input a project file
    export the file and save it based on the <export_file> name
    with export_format

    :param export_file:
    :param refine_project:
    :param export_format:
    :return:
    """
    project_file = refine_project.export(export_format=export_format)
    with open(export_file,"w") as file:
        for line in project_file:
            file.write(line)
    #with open(export_file,"w") as file:
    #    file.writelines(project)

def or_connect(or_address="http://localhost:3333"):
    return refine.Refine(refine.RefineServer(or_address))

def list_projects(refine_server):
    #refine_server = refine.Refine(refine_server)
    refine_projects = refine_server.list_projects()
    """
    {u'1877818633188': {
            'id': u'1877818633188', u'name': u'akg',
            u'modified': u'2011-04-07T12:30:07Z',
            u'created': u'2011-04-07T12:30:07Z'
    }
    """
    return refine_projects

def show_projects(refine_projects):
    print("\t".join(["id","\tname (created_time)"]))
    for x in refine_projects.items():
        #print(x)
        print("\t".join([x[0],x[1]["name"]+" ("+x[1]["created"]+")"]))


def compare_files(file1,file2):
    import difflib
    text1 = open(file1).readlines()
    text2 = open(file2).readlines()

    n_diff = 0
    for line in difflib.unified_diff(text1, text2):
        # print the differences using difflib
        print(line)
        n_diff+=1

    if n_diff==0:
        print file1,"and",file2,"are totally the same"
    else:
        print "found",n_diff,"differences between",file1,"and",file2

    return n_diff





