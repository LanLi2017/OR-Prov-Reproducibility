

def run_history(input_file,history_dict,output_file):
    """
    From dictionary use openrefine client api, customized
    and run the operation in a sequential order
    based on the recipe including the custom/hidden recipe

    :param input_file: raw data input file that will be cleaned
    :param history_dict: dictionary of history
    :param output_file: save the process in the output file
    :return: new file
    """

    raise NotImplementedError



if __name__ == '__main__':
    from script.extract_archive_history import extract_history
    project_file = "../test_files/airbnb_test.tar.gz"
    recipe = extract_history(project_file)
    
