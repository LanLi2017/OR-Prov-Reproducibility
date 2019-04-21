
if __name__ == '__main__':
    from script.extract_archive_history import extract_history
    from script.run_history import run_history

    # read json history from test file
    # will be changed with the on the fly script
    """
    import json
    with open("./test_files/airbnb_operations_normal.json","r") as file:
        recipe = json.load(file)
        #recipe = extract_history("targzfile")
    """

    recipe = extract_history("./test_files/Tutorial_OR.openrefine.tar.gz")

    print(recipe)

    ops_recipe = []
    for x in recipe:
        try:
            ops_recipe.append(x["operation"])
        except:
            print("No Operation for: ",x)
            pass

    all_history = run_history("./test_files/Tutorial_OR.csv",project_name="tutorial_or1",recipe=ops_recipe)

    print("all history:")
    print(all_history)

    #project_file = "../test_files/airbnb_test.tar.gz"
    #recipe = extract_history(project_file)