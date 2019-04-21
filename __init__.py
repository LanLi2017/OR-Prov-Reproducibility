
if __name__ == '__main__':
    from script.extract_archive_history import extract_history
    from script.run_history import run_history

    # read json history from test file
    # will be changed with the on the fly script
    import json
    with open("./test_files/airbnb_operations_normal.json","r") as file:
        recipe = json.load(file)
        #recipe = extract_history("targzfile")

    run_history("./test_files/airbnb_test_raw.csv",project_name="test_bnb1",recipe=recipe)
    #project_file = "../test_files/airbnb_test.tar.gz"
    #recipe = extract_history(project_file)