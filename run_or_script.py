import sys
import argparse;
from script.run_history import list_projects,show_projects,or_connect,select_project_byid,run_history_on_project,select_project_byname
import json

def run():
    argv = sys.argv
    # required argument
    reqs = ["input","output"]
    parser = argparse.ArgumentParser(description='recipe runner, will execute open \
        refine recipe on the server using openrefine client api')
    parser.add_argument("-sp","--show-project",action="store_true",default=False,help="show project name and id on the server")
    parser.add_argument('-i','--input',default=None,
            help='openrefine json file ')
    parser.add_argument("-pid","--project-id",default=None,help="project id for executed script")
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
        if argobj["input"]!=None:
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
            elif pname!=None:
                refine_project = select_project_byname(pname,refine_server)
                run_history_on_project(refine_project, ops)
            else:
                raise Exception("Must specify Project ID or Project Name")
    except BaseException as exc:
        import traceback
        #parser.print_help()
        traceback.print_exc()
        #raise exc

if __name__ == '__main__':
    run()
