

def extract_history(input_file:str):
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

    raise NotImplementedError