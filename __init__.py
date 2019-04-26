
if __name__ == '__main__':
    from script.extract_archive_history import extract_history,store_JSON
    from script.run_history import run_history,export_file,compare_files

    # read json history from test file
    # will be changed with the on the fly script


    """
    import json
    with open("./test_files/not_complete.json","r") as file:
        ops_recipe = json.load(file)
        #recipe = extract_history("targzfile")
    """



    recipe, metadata = extract_history("./test_files/Tutorial_OR.openrefine.tar.gz")

    print(recipe)

    ops_recipe = []
    for x in recipe:
        try:
            ops_recipe.append(x["operation"])
        except:
            print("No Operation for: ",x)
            pass


    store_JSON(ops_recipe,"test.json")

    project, all_history = run_history("./test_files/Tutorial_OR.csv", project_name="tutorial_or1", recipe=ops_recipe)
    #project,all_history = run_history("./test_files/Tutorial_OR.csv",project_name="tutorial_or1",recipe=ops_recipe,metadata=metadata)

    print("all history:")
    print(all_history)

    # export file
    exported = export_file("test.csv",project)

    # compare processed files and cleaned files
    compare_files("test.csv","test_files/Tutorial_OR_clean.csv")

    # delete the openrefine project file
    # because project just for temporarily purpose
    #project.delete()

    #project_file = "../test_files/airbnb_test.tar.gz"
    #recipe = extract_history(project_file)