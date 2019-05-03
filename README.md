# OR-Prov-Reproducibility

Clone this Github Project with recursive command
```
$ git clone --recursive https://github.com/LanLi2017/OR-Prov-Reproducibility
```

Change directory to the Github source code folder
```
cd OR-Prov-Reproducibility
```

Create a python2 virtual environment, this will create conda virtual environment directory (or-venv) on the folder
and activate the virtual environment

```
conda create --prefix or-venv python=2.7
source activate or-venv
```

Install requirements
```
pip install -r requirements.txt
```

This experiment modules use the enhanced/customized refine-client-py OpenRefine Client API based on python 2.7, 
you can install the module by executing
```
cd refine-client-py
python setup.py install
```
or if  you are in the development machine and want to use the script directly you can make a symbolic link
```
ln -s refine-client-py/google ./google
```

Command for using the orcli script
```
usage: orcli.py <command> [<args>]

        orcli commands are:        
           extract          Extract enhanced recipe from OpenRefine project file
           list             List Projects from the openrefine server
           run              Run openrefine extracted history on the OpenRefine server
           compare          Compare two OpenRefine files output
           compare_recipes  Compare two OpenRefine extracted history
```

## Extract Complete Operation History

```
usage: python orcli.py extract [-h] [-i INPUT] [-o OUTPUT]

Extract enhanced recipe from the OpenRefine project (format file: tar.gz)

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        OpenRefine project file (tar.gz)
  -o OUTPUT, --output OUTPUT
                        OpenRefine extracted history/recipe (in json format),
                        if not specified: <project_file_name>.json
```
#### Example
```
$ python orcli.py extract -i test_files/Tutorial_OR.openrefine.tar.gz 
create a folder
{u'contributors': u'',
 u'created': u'2019-04-20T22:38:19Z',
 u'creator': u'',
 u'customMetadata': {},
 u'description': u'',
 u'encoding': u'UTF-8',
 u'encodingConfidence': 0,
 u'homepage': u'',
 u'image': u'',
 u'importOptionMetadata': [{u'fileSource': u'Dataset/Menu.csv',
                            u'guessCellValueTypes': False,
                            u'headerLines': 1,
                            u'ignoreLines': -1,
                            u'includeFileSources': False,
                            u'limit': -1,
                            u'linesPerRow': 1,
                            u'processQuotes': True,
                            u'projectName': u'Tutorial_OR',
                            u'separator': u',',
                            u'skipDataLines': 0,
                            u'storeBlankCellsAsNulls': True,
                            u'storeBlankRows': True,
                            u'storeEmptyStrings': True,
                            u'trimStrings': False}],
 u'license': u'',
 u'modified': u'2019-04-21T18:49:14Z',
 u'name': u'Tutorial_OR',
 u'password': u'',
 u'preferences': {u'entries': {u'scripting.expressions': {u'class': u'com.google.refine.preference.TopList',
                                                          u'list': [],
                                                          u'top': 100},
                               u'scripting.starred-expressions': {u'class': u'com.google.refine.preference.TopList',
                                                                  u'list': [],
                                                                  u'top': 2147483647}}},
 u'rowCount': 17545,
 u'subject': u'',
 u'tags': [],
 u'title': u'',
 u'version': u''}
Complete Operation History saved as : test_files/Tutorial_OR.openrefine.json
```

## List OpenRefine Projects

List OpenRefine Projects, needed to get the project id or project name for runner script. OpenRefine must run in the same machine if the "server" parameter is not provided 
```
usage: python orcli.py list [-h] [-s SERVER]

List OpenRefine projects from the server

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        openrefine server address (default:
                        http://localhost:3333

```
#### Example
```
$ python orcli.py list
id		name (created_time)
1640253865572	Airbnblistings_dirty csv (2019-05-02T18:52:42Z)
2268292899761	Traffic_Violations csv (2019-05-02T18:52:42Z)
1611470445474	menu_question csv (2019-05-02T18:52:40Z)
2490367294591	Airbnblistings_dirty csv csv (2019-05-02T18:52:40Z)
```

## Run OpenRefine Recipe 

Run OpenRefine recipe on the particular ProjectID or ProjectName in the OpenRefine server
```
usage: python orcli.py run [-h] [-i INPUT] [-pid PROJECT_ID] [-pname PROJECT_NAME]
                [-s SERVER]

recipe runner, will execute open refine recipe on the server using openrefine
client api

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        openrefine operation history file (usually in json
                        format)
  -pid PROJECT_ID, --project-id PROJECT_ID
                        project id for target script execution
  -pname PROJECT_NAME, --project-name PROJECT_NAME
                        project name for executed script, if project id
                        assigned, will use project id instead
  -s SERVER, --server SERVER
                        openrefine server address (default:
                        http://localhost:3333
```
#### Example
```
$ python orcli.py run -i test_files/Tutorial_OR.openrefine.json -pid 1883642963987 
recipe test_files/Tutorial_OR.openrefine.json executed on project id: 1883642963987
```

## Compare Files

```
usage: python orcli.py compare [-h]

Command orcli.py compare <file1> <file2> Compare two OpenRefine output files
<file1> and <file2>
```

#### Example

```
$ python orcli.py compare test_files/Tutorial_OR.csv test_files/Tutorial_OR_clean.csv 
+35511,E. Ettinger Café and Restaurant,e. ettinger café and restaurant,,,,,,,,1913-09-23,,,,2 images,1913-0742_wotm,,,E. Ettinger Café and Restaurant,,Dollars,$,complete,2,64

+35512,Whites,whites,,,,,,,,1913-09-24,,,,4 images,1913-0743_wotm,,,Whites,,Dollars,$,complete,4,297

+35513,Riggs',riggs',,,,,,,,1913-09-24,,,,4 images,1913-0744_wotm,,,Riggs',,Dollars,$,complete,4,321

+35514,Woolpack Hotel,woolpack hotel,,,,,,,,1913-09-24,,,,2 images,1913-0745_wotm,,,Woolpack Hotel,,,,complete,2,8

+35515,Hotel LaSalle,hotel lasalle,,,,,,,,1913-09-24,,,,1 image,1913-0746_wotm,,,Hotel LaSalle,,,,complete,1,22

+35516,Dennett's,dennett's,,,,,,,,1913-09-24,,,,1 image,1913-0747_wotm,,,Dennett's,,Dollars,$,complete,1,125

+35517,The Cortlandt,the cortlandt,,,,,,,,1913-09-24,,,,1 image,1913-0748_wotm,,,The Cortlandt,,Dollars,$,complete,1,101

+35518,Hotel Schynige Platte und Hotel Bellevue,hotel schynige platte und hotel bellevue,,,,,,,,1913-09-24,,,,4 images,1913-0749_wotm,,,Hotel Schynige Platte und Hotel Bellevue,,Swiss Francs,Fr,complete,4,161

+35526,"Christmas Dinner, Troop F 19: Fort Huachuca, Arizona, 10th Cavalry, Christmas",christmas dinner, troop f 19: fort huachuca, arizona, 10th cavalry, christmas,,,,1920-12-25,,,,"Fort Huachuca, Arizona",C.10_wotm,,,"Christmas Dinner, Troop F 19: Fort Huachuca, Arizona, 10th Cavalry, Christmas",,,,complete,10,32

found differences between test_files/Tutorial_OR.csv and test_files/Tutorial_OR_clean.csv
```

## Compare Operation Histories / Recipes

```
usage: python orcli.py compare_recipes [-h]

Command orcli.py compare_recipes <file1> <file2> Compare two OpenRefine recipe
files <file1> and <file2>
```

#### Example

```
$ python orcli.py compare_recipes ./test_files/Tutorial_OR_ui_ops.json ./test_files/Tutorial_OR_complete_ops.json 
{insert: [(2, {u'cell': u'3', u'new': u'{"v":"tutorial_menu"}', u'row': u'3', u'old': u'{"v":"LUNCH;"}', u'op': u'custom/single-edit'}), (7, {u'oldFlagged': u'false', u'row': u'1', u'newFlagged': u'true', u'op': u'custom/flag'}), (8, {u'oldStarred': u'false', u'row': u'1', u'newStarred': u'true', u'op': u'custom/star'}), (11, {u'cell': u'3', u'new': u'{"v":"Abendessen"}', u'row': u'1', u'old': u'{"v":"[DINNER]"}', u'op': u'custom/single-edit'})]}
```



