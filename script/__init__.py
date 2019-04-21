if __name__ == '__main__':
    from script.extract_archive_history import extract_history
    from script.run_history import run_history
    project_file = "../test_files/airbnb_test.tar.gz"
    recipe = extract_history(project_file)
