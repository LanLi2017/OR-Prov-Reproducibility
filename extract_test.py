from pprint import pprint

if __name__ == '__main__':
    from script.extract_archive_history import extract_history
    test_file = "./test_files/demo2_part1.openrefine.tar.gz"
    extract_history(test_file)
