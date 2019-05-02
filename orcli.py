import sys
import argparse;
from script.run_history import list_projects,\
    show_projects,\
    or_connect,\
    select_project_byid,\
    run_history_on_project,\
    select_project_byname,\
    compare_files
from script.extract_archive_history import extract_history,store_JSON
import json

class ORCLI(object):
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='OpenRefine command line interface Demo',
            usage='''orcli <command> [<args>]

        orcli commands are:        
           extract          Extract enhanced recipe from OpenRefine project file
           list             List Projects from the openrefine server
           run              Run openrefine extracted history on the OpenRefine server
           compare          Compare two OpenRefine files output
           compare_recipes  Compare two OpenRefine extracted history           
        ''')

        parser.add_argument('command', help='orcli commands')
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def list(self):
        parser = argparse.ArgumentParser(
            description='List OpenRefine projects from the server')
        # now that we're inside a subcommand, ignore the first
        # TWO argvs, ie the command (git) and the subcommand (commit)

        #parser = argparse.ArgumentParser(description='list project from the openrefine server')

        parser.add_argument('-s',"--server",
                help="openrefine server address (default: http://localhost:3333",default="http://localhost:3333")

        args = parser.parse_args(sys.argv[2:])
        argobj = vars(args);

        try:
            # print(argobj.keys())
            or_address = argobj["server"]
            refine_server = or_connect(or_address)
            refine_projects = list_projects(refine_server)
            show_projects(refine_projects)
        except BaseException as exc:
            import traceback
            # parser.print_help()
            traceback.print_exc()
            # raise exc

    def extract(self):
        parser = argparse.ArgumentParser(description='Extract enhanced recipe from the OpenRefine project (format file: tar.gz)')

        parser.add_argument('-i','--input',default=None,
                help='OpenRefine project file (tar.gz)')
        parser.add_argument('-o',"--output",
                help="OpenRefine extracted history/recipe (in json format), if not specified: <project_file_name>.json",default=None)

        args = parser.parse_args(sys.argv[2:])
        argobj = vars(args);
        try:
            if argobj["input"] != None:
                input_file = argobj["input"]
                if not input_file.endswith(".tar.gz"):
                    raise BaseException("Input file must be saved in .tar.gz format: {}".format(input_file))
                if argobj["output"] == None:
                    output_file = input_file[:-(len(".tar.gz"))]+".json"
                else:
                    output_file = argobj["output"]
                data_json = extract_history(input_file)[0]
                store_JSON(data_json, output_file)
                print("Complete Operation History saved as : {}".format(output_file))
            else:
                parser.print_help()
        except BaseException as exc:
            import traceback
            # parser.print_help()
            traceback.print_exc()
            # raise exc

    def run(self):
        parser = argparse.ArgumentParser(description='recipe runner, will execute open \
            refine recipe on the server using openrefine client api')

        parser.add_argument('-i','--input',default=None,
                help='openrefine operation history file (usually in json format)')
        parser.add_argument("-pid","--project-id",default=None,help="project id for target script execution")
        parser.add_argument("-pname", "--project-name", default=None, help="project name for executed script, \
            if project id assigned, will use project id instead")
        parser.add_argument('-s',"--server",
                help="openrefine server address (default: http://localhost:3333",default="http://localhost:3333")

        args = parser.parse_args(sys.argv[2:])
        argobj = vars(args);

        try:
            # print(argobj.keys())
            or_address = argobj["server"]
            refine_server = or_connect(or_address)
            if argobj["input"] != None:
                json_input = argobj["input"]
                with open(json_input, "r") as file:
                    ops = json.load(file)

                pid = argobj["project_id"]
                pname = argobj["project_name"]
                if pid != None:
                    refine_projects = list_projects(refine_server)
                    if pid not in refine_projects.keys():
                        raise Exception("cannot find project id {} on the server".format(pid))
                    refine_project = select_project_byid(pid, refine_server)
                    run_history_on_project(refine_project, ops)
                    print("recipe {} executed on project id: {}".format(json_input, pid))
                elif pname != None:
                    refine_project = select_project_byname(pname, refine_server)
                    run_history_on_project(refine_project, ops)
                    print("recipe {} executed on project: {}".format(json_input, pname))
                else:
                    raise Exception("Must specify Project ID or Project Name")
            else:
                parser.print_help()
        except BaseException as exc:
            import traceback
            # parser.print_help()
            traceback.print_exc()
            # raise exc

    def compare(self):
        parser = argparse.ArgumentParser(
            description='''Command orcli compare <file1> <file2>
            Compare two OpenRefine output files <file1> and <file2>''')
        #args = parser.parse_args(sys.argv[2:])
        #print(sys.argv[2:])
        argobj = sys.argv[2:]
        #argobj = vars(sys.argv[2:]);
        if len(argobj) < 2:
            parser.print_help()
            raise BaseException("Must specify two parameters: <file1> and <file2> to compare")
        else:
            compare_files(argobj[0],argobj[1])

    def compare_recipes(self):
        parser = argparse.ArgumentParser(
            description='''Command orcli compare_recipes <file1> <file2>
            Compare two OpenRefine recipe files <file1> and <file2>''')
        #args = parser.parse_args(sys.argv[2:])
        #print(sys.argv[2:])
        argobj = sys.argv[2:]
        #argobj = vars(sys.argv[2:]);
        if len(argobj) < 2:
            parser.print_help()
            raise BaseException("Must specify two parameters: <file1> and <file2> to compare")
        else:
            import jsondiff
            file1 = argobj[0]
            file2 = argobj[1]
            with open(file1,"r") as file:
                json1 = json.load(file)
            with open(file2,"r") as file:
                json2 = json.load(file)
            diff = jsondiff.diff(json1,json2)
            print(diff)

"""
def run():
    argv = sys.argv
    # required argument
    # reqs = ["input","output"]

    parser.add_argument('command', help='Subcommand to run')
    # parse_args defaults to [1:] for args, but you need to
    # exclude the rest of the args too, or validation will fail
    args = parser.parse_args(sys.argv[1:2])
    if not hasattr(self, args.command):
        print 'Unrecognized command'
        parser.print_help()
        exit(1)
    # use dispatch pattern to invoke method with same name
    getattr(self, args.command)()

    parser = argparse.ArgumentParser(description='recipe runner, will execute open \
        refine recipe on the server using openrefine client api')



    parser.add_argument("-sp","--show-project",action="store_true",default=False,help="show project name and id on the server")
    parser.add_argument('-i','--input',default=None,
            help='openrefine json file ')
    parser.add_argument("-pid","--project-id",default=None,help="project id for target script execution")
    parser.add_argument("-pname", "--project-name", default=None, help="project name for executed script, \
        if project id assigned, will use project id instead")
    parser.add_argument('-s',"--server",
            help="openrefine server address (default: http://localhost:3333",default="http://localhost:3333")

    args = parser.parse_args(argv[1:])
    argobj = vars(args);

    try:
        #print(argobj.keys())
        or_address = argobj["server"]
        refine_server = or_connect(or_address)
        if argobj["show_project"]:
            refine_projects = list_projects(refine_server)
            show_projects(refine_projects)
        elif argobj["input"]!=None:
            json_input = argobj["input"]
            with open(json_input,"r") as file:
                ops = json.load(file)

            pid = argobj["project_id"]
            pname = argobj["project_name"]
            if pid!=None:
                refine_projects = list_projects(refine_server)
                if pid not in refine_projects.keys():
                    raise Exception("cannot find project id {} on the server".format(pid))
                refine_project = select_project_byid(pid,refine_server)
                run_history_on_project(refine_project,ops)
                print("recipe {} executed on project id: {}".format(json_input,pid))
            elif pname!=None:
                refine_project = select_project_byname(pname,refine_server)
                run_history_on_project(refine_project, ops)
                print("recipe {} executed on project: {}".format(json_input, pname))
            else:
                raise Exception("Must specify Project ID or Project Name")
        else:
            parser.print_help()
    except BaseException as exc:
        import traceback
        #parser.print_help()
        traceback.print_exc()
        #raise exc
"""

if __name__ == '__main__':
    ORCLI()
