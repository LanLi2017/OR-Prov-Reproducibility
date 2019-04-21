from google.refine import refine

def run_history(input_file,project_name,recipe,output_file=None,refine_server_url="http://127.0.0.1:3333"):
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
    new_project = refine_server.new_project(input_file,project_name=project_name)

    # execute operations
    for op in recipe:
        new_project.execute_json_op(op)

    print(new_project)
    #raise NotImplementedError





