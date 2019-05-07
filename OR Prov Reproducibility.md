---


---

<h1 id="openrefine-reproducibility-demo">OpenRefine Reproducibility Demo</h1>
<p>These four demos are to test the OpenRefine <strong>reproducibility</strong><br>
We use the first 5 rows of Menu.csv from <a href="http://menus.nypl.org/data">New York Public Library</a> as our demo dataset.<br>
The version of OpenRefine is 3.1 and all of the experiments are launched on Mac OS.<br>
The csv file used here is in comma separated mode.<br>
This is the original dataset:</p>
<pre class=" language-csv"><code class="prism  language-csv">,id,name,sponsor,event,venue,place,physical_description,occasion,notes,call_number,keywords,language,date,location,location_type,currency,currency_symbol,status,page_count,dish_count
0,12463,,HOTEL EASTMAN,BREAKFAST,COMMERCIAL,"HOT SPRINGS, AR",CARD; 4.75X7.5;,EASTER;,,1900-2822,,,1900-04-15,Hotel Eastman,,,,complete,2,67
1,12464,,REPUBLICAN HOUSE,[DINNER],COMMERCIAL,"MILWAUKEE, [WI];",CARD; ILLUS; COL; 7.0X9.0;,EASTER;,"WEDGEWOOD BLUE CARD; WHITE EMBOSSED GREEK KEY BORDER; ""EASTER SUNDAY"" EMBOSSED IN WHITE; VIOLET COLORED SPRAY OF FLOWERS IN UPPER LEFT CORNER;",1900-2825,,,1900-04-15,Republican House,,,,complete,2,34
2,12465,,NORDDEUTSCHER LLOYD BREMEN,FRUHSTUCK/BREAKFAST;,COMMERCIAL,DAMPFER KAISER WILHELM DER GROSSE;,CARD; ILLU; COL; 5.5X8.0;,,"MENU IN GERMAN AND ENGLISH; ILLUS, STEAMSHIP AND SAILING VESSEL;",1900-2827,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,84
3,12466,,NORDDEUTSCHER LLOYD BREMEN,LUNCH;,COMMERCIAL,DAMPFER KAISER WILHELM DER GROSSE;,CARD; ILLU; COL; 5.5X8.0;,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH SAILING VESSEL;",1900-2828,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,63
4,12467,,NORDDEUTSCHER LLOYD BREMEN,DINNER;,COMMERCIAL,DAMPFER KAISER WILHELM DER GROSSE;,FOLDER; ILLU; COL; 5.5X7.5;,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH ROCKS AND LIGHTHOUSE; STEAMSHIP AND SAILING VESSELS; CONCERT PROGRAM; DATES:  ON GERMAN SIDE OF MENU ""MONTAG, DEN 16 APRIL 1900""; ON ENGLISH SIDE OF MENU ""MONDAY, APRIL 15TH, 1900"";",1900-2829,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,4,33

</code></pre>
<h2 id="demo-0">Demo 0</h2>
<p>This demo is supported by OpenRefine natively, should always work.<br>
Part 1:<br>
1). Create new OpenRefine project (P1) importing test data set (T).</p>
<p>Create Project steps:</p>
<ul>
<li>Click on “Create Project” and “Choose Files” from the local computer, then click on “Next”.<br>
<img src="https://lh3.googleusercontent.com/Yb93y2pRSyr3-fcw0-a7_PhVv9nDsE8nc-fVSo0wj4mozht-36qUWUiM_SCpkhVfPxr1nLaIDFP7=s8000" alt="enter image description here" title="create project"></li>
<li>OpenRefine will generate a “Configure Parsing Options” page with default settings, where users can change the choices accordingly, including “Project name”, “Character encoding”, “Columns are separated by”, etc. Here we change the project name into “demo0_part1_partMenu”, then Click on “Create Project”, a new OpenRefine project is set up.<br>
<img src="https://lh3.googleusercontent.com/WzVY3Rsd2lgdsJZJCnhrFc9qSqPCFKmpnPNYgZZzY3dMsm12G4kziBJZAIiohLSPNO2NE-Fu8K5t=s8000" alt="enter image description here" title="create_settings"></li>
<li>This is the project interface for a new OpenRefine. On the right, users can do data cleaning manipulations on the table (see the picture below), and all of the manipulations will be recorded in the “Undo/Redo”  sidebar on the left simultaneously.<br>
Users can undo or redo some data cleaning steps by simply click on the steps they want to restore.<br>
<img src="https://lh3.googleusercontent.com/3MdbpsvGT3yOfqP2RmBk_Id2g0I5s9uESa-g5VVaiGIctw36cthqNUOkglbBSc4lz0gzow3uoQZJ=s8000" alt="enter image description here" title="operations choose OR"><br>
2). Perform a few data cleaning operations, both generalizable and non-generalizable.<br>
Here there are 6 steps in all recorded in the <strong>Undo/Redo</strong> operation history sidebar.<br>
<img src="https://lh3.googleusercontent.com/tNyZfTed6Hmct84Fh5t9IGZXmybBIv6sKFVymxbmjQ9kCgyvScdSwRBjZ4n3v7xXxoi3MDgxYQky=s8000" alt="enter image description here" title="demo0 part1 operations"></li>
</ul>
<p>3). View the operation <strong>history</strong>(H1)<br>
<img src="https://lh3.googleusercontent.com/VRjrxEMg6JbuI7BNf-SeNqKka6wC4Plih8_9dQdYAqWTg1UZ0rAhjFCZ-Cm0XUd1R05grC5Kr9SY=s1000" alt="enter image description here" title="demo0_part1_OH"><br>
4). Undo all data cleaning steps, then redo all the operations.<br>
Click on the first step: “0. Create project”, which can help undo all data cleaning steps and initialize the project status.<br>
Then click back on the final step to redo all the operations.<br>
<img src="https://lh3.googleusercontent.com/Pt0yJw06e30eTDacgq-iMC0lMSFJZqchsQjyr6LkxP-Jkma__Vc6RD0clJervE6jbo1p8n7_h9sT=s8000" alt="enter image description here" title="undo-all"><br>
5). Export the cleaned data set C1.<br>
Click on “Export” button, and choose “Comma-separated value” which can generate a csv file.<br>
<img src="https://lh3.googleusercontent.com/i6FK_OJYAHSxtaltGyj2X480FqBNUnx8ppLp2SIa2cYOUQZMvPALffR1hjWiJEBPUAfrbVCuzcl9=s8000" alt="enter image description here" title="export_csv"></p>
<pre class=" language-csv"><code class="prism  language-csv">Column,id,name,sponsor,event,venue,place,physical_description 1,physical_description 2,physical_description 3,physical_description 4,physical_description 5,occasion,notes,call_number,keywords,language,date,location,location_type,currency,currency_symbol,status,page_count,dish_count
0,12463,,hotel eastman,breakfast,commercial,"HOT SPRINGS, AR",CARD, 4.75X7.5,,,,EASTER;,,1900-2822,,,1900-04-15,Hotel Eastman,,,,complete,2,67
1,12464,,republican house,dinner;,commercial,"MILWAUKEE, [WI];",CARD, ILLUS, COL, 7.0X9.0,,EASTER;,"WEDGEWOOD BLUE CARD; WHITE EMBOSSED GREEK KEY BORDER; ""EASTER SUNDAY"" EMBOSSED IN WHITE; VIOLET COLORED SPRAY OF FLOWERS IN UPPER LEFT CORNER;",1900-2825,,,1900-04-15,Republican House,,,,complete,2,34
2,12465,,norddeutscher lloyd bremen,fruhstuck/breakfast;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,CARD, ILLU, COL, 5.5X8.0,,,"MENU IN GERMAN AND ENGLISH; ILLUS, STEAMSHIP AND SAILING VESSEL;",1900-2827,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,84
3,12466,,norddeutscher lloyd bremen,lunch;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,CARD, ILLU, COL, 5.5X8.0,,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH SAILING VESSEL;",1900-2828,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,63
4,12467,,norddeutscher lloyd bremen,dinner;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,FOLDER, ILLU, COL, 5.5X7.5,,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH ROCKS AND LIGHTHOUSE; STEAMSHIP AND SAILING VESSELS; CONCERT PROGRAM; DATES:  ON GERMAN SIDE OF MENU ""MONTAG, DEN 16 APRIL 1900""; ON ENGLISH SIDE OF MENU ""MONDAY, APRIL 15TH, 1900"";",1900-2829,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,4,33

</code></pre>
<p><img src="https://lh3.googleusercontent.com/zfr5RqXEC8UaDMm5dk0lKgCsydAUETqq7YGLYmlvzEqS3TebX6KU6RDrhC4XUmhmEY0dMCmFmx4Q=s8000" alt="enter image description here" title="demo0_part1_output"><br>
6). Export the project and save as an archive A, a tarball.<br>
Click on “Export” and choose “Export project”, a <em>tar.gz</em> compressed folder will be generated.<br>
<img src="https://lh3.googleusercontent.com/hQ6iuEK18Qf89kRoCmwXR2OazSMsNuX5P8M1k0FOqWPXGfeMrgr0LcA8s832O9aOMRb1Mt-V6Gtl=s8000" alt="enter image description here" title="export_tar"><br>
Part 2:<br>
1). Create a new OpenRefine project (P2), importing the exported archive (A).<br>
Import Project steps:<br>
Click on “Import Project” on the left, then choose the archive file and re-name project (optional choice).<br>
<img src="https://lh3.googleusercontent.com/MI0ZK7qxj9sVt62xFrKK03BRHUMusXck5mWmciPvZzFJ5gpPK0y2sJ2iyqW4XCSKiIi8qpV8OANX=s8000" alt="enter image description here" title="demo0_part2 import archive"><br>
2). View the operation <strong>history</strong> (H2) and check that it looks like H1<br>
The <strong>operation history</strong> on the left is H2, and H1 is on the right. We can see that H2 is the same as H1.<br>
<img src="https://lh3.googleusercontent.com/2Ok_a9JlVCtu8w3PHmEVpSu-R60rGnsjLUmzfPr68D-yBjPbg8Q33iwKb6SROsJT3_Mi4jaDDGvF=s8000" alt="enter image description here" title="compare OH1 and OH2"><br>
3). Undo all data cleaning steps, then redo all the operations.<br>
4). Export the cleaned data set C2.<br>
This is C2:</p>
<pre class=" language-csv"><code class="prism  language-csv">Column,id,name,sponsor,event,venue,place,physical_description 1,physical_description 2,physical_description 3,physical_description 4,physical_description 5,occasion,notes,call_number,keywords,language,date,location,location_type,currency,currency_symbol,status,page_count,dish_count
0,12463,,hotel eastman,breakfast,commercial,"HOT SPRINGS, AR",CARD, 4.75X7.5,,,,EASTER;,,1900-2822,,,1900-04-15,Hotel Eastman,,,,complete,2,67
1,12464,,republican house,dinner;,commercial,"MILWAUKEE, [WI];",CARD, ILLUS, COL, 7.0X9.0,,EASTER;,"WEDGEWOOD BLUE CARD; WHITE EMBOSSED GREEK KEY BORDER; ""EASTER SUNDAY"" EMBOSSED IN WHITE; VIOLET COLORED SPRAY OF FLOWERS IN UPPER LEFT CORNER;",1900-2825,,,1900-04-15,Republican House,,,,complete,2,34
2,12465,,norddeutscher lloyd bremen,fruhstuck/breakfast;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,CARD, ILLU, COL, 5.5X8.0,,,"MENU IN GERMAN AND ENGLISH; ILLUS, STEAMSHIP AND SAILING VESSEL;",1900-2827,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,84
3,12466,,norddeutscher lloyd bremen,lunch;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,CARD, ILLU, COL, 5.5X8.0,,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH SAILING VESSEL;",1900-2828,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,63
4,12467,,norddeutscher lloyd bremen,dinner;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,FOLDER, ILLU, COL, 5.5X7.5,,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH ROCKS AND LIGHTHOUSE; STEAMSHIP AND SAILING VESSELS; CONCERT PROGRAM; DATES:  ON GERMAN SIDE OF MENU ""MONTAG, DEN 16 APRIL 1900""; ON ENGLISH SIDE OF MENU ""MONDAY, APRIL 15TH, 1900"";",1900-2829,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,4,33

</code></pre>
<p><img src="https://lh3.googleusercontent.com/xveKW4Y6GjWHubejCSMC1k9svbxYoHosII0NJrhkSd-s3WeJlQXT2UcLxIF04b-YjgMEhAQ18d9t=s8000" alt="enter image description here" title="demo0_part2_output"><br>
5). Show that C1 and C2 are the <strong>same</strong>.</p>
<pre class=" language-console"><code class="prism  language-console">wirelessprv-10-194-219-248:demo_all barbaralee$  diff demo0_part1/demo0_part1_partMenu.csv demo0_part2/demo0_part2.csv

wirelessprv-10-194-219-248:demo_all barbaralee$
</code></pre>
<p>We use <em>diff</em> to test C1 and C2, and there is no return here. Thus, C1 and C2 are the same.</p>
<h2 id="demo-1a">Demo 1a</h2>
<p>This demo shows that OpenRefine recipes suffice when all operations are <strong>generalizable</strong>.</p>
<p>Part 1:<br>
1). Create new OpenRefine project (P3) importing test data set (T).<br>
(Follow the instructions in Demo 0 part 1)<br>
<img src="https://lh3.googleusercontent.com/SyVrZ3nsG2R2LxpsMBmqlNPUWX9smF_woDehrxaI-jw_DKof-yJOw38sTv603a90XQd4BlX9m3aP=s8000" alt="enter image description here" title="demo1a_part1 initial"><br>
2). Perform a few data cleaning operations where all operations are generalizable.<br>
There are 5 steps in all.<br>
<img src="https://lh3.googleusercontent.com/C1dOSuBociCHFCbGQ1Bsu1pqCOVZkMetgyBFwpPZstH1TVUu1ORJetWiIdYhTXVtr7bXmxKCuhc7=s8000" alt="enter image description here" title="demo1a_part1 OH"><br>
3). Export the operation history and save as a <strong>recipe</strong>  R.<br>
Click on “Extract…” and then copy and paste the json-format contents from the right red box.<br>
<img src="https://lh3.googleusercontent.com/XuBQEoFwyvrFEhjTVwX4lLRTOj3xswyWOJnC6bqsistf7S-qtlxghrKbc85z_nAFTO9VlqkutpYq=s8000" alt="enter image description here" title="extract Recipe"><br>
This is the recipe R:</p>
<pre class=" language-json"><code class="prism  language-json"><span class="token punctuation">[</span>
  <span class="token punctuation">{</span>
    <span class="token string">"op"</span><span class="token punctuation">:</span> <span class="token string">"core/text-transform"</span><span class="token punctuation">,</span>
    <span class="token string">"description"</span><span class="token punctuation">:</span> <span class="token string">"Text transform on cells in column id using expression value.toNumber()"</span><span class="token punctuation">,</span>
    <span class="token string">"engineConfig"</span><span class="token punctuation">:</span> <span class="token punctuation">{</span>
      <span class="token string">"facets"</span><span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
      <span class="token string">"mode"</span><span class="token punctuation">:</span> <span class="token string">"row-based"</span>
    <span class="token punctuation">}</span><span class="token punctuation">,</span>
    <span class="token string">"columnName"</span><span class="token punctuation">:</span> <span class="token string">"id"</span><span class="token punctuation">,</span>
    <span class="token string">"expression"</span><span class="token punctuation">:</span> <span class="token string">"value.toNumber()"</span><span class="token punctuation">,</span>
    <span class="token string">"onError"</span><span class="token punctuation">:</span> <span class="token string">"keep-original"</span><span class="token punctuation">,</span>
    <span class="token string">"repeat"</span><span class="token punctuation">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
    <span class="token string">"repeatCount"</span><span class="token punctuation">:</span> <span class="token number">10</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token punctuation">{</span>
    <span class="token string">"op"</span><span class="token punctuation">:</span> <span class="token string">"core/text-transform"</span><span class="token punctuation">,</span>
    <span class="token string">"description"</span><span class="token punctuation">:</span> <span class="token string">"Text transform on cells in column sponsor using expression value.toLowercase()"</span><span class="token punctuation">,</span>
    <span class="token string">"engineConfig"</span><span class="token punctuation">:</span> <span class="token punctuation">{</span>
      <span class="token string">"facets"</span><span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
      <span class="token string">"mode"</span><span class="token punctuation">:</span> <span class="token string">"row-based"</span>
    <span class="token punctuation">}</span><span class="token punctuation">,</span>
    <span class="token string">"columnName"</span><span class="token punctuation">:</span> <span class="token string">"sponsor"</span><span class="token punctuation">,</span>
    <span class="token string">"expression"</span><span class="token punctuation">:</span> <span class="token string">"value.toLowercase()"</span><span class="token punctuation">,</span>
    <span class="token string">"onError"</span><span class="token punctuation">:</span> <span class="token string">"keep-original"</span><span class="token punctuation">,</span>
    <span class="token string">"repeat"</span><span class="token punctuation">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
    <span class="token string">"repeatCount"</span><span class="token punctuation">:</span> <span class="token number">10</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token punctuation">{</span>
    <span class="token string">"op"</span><span class="token punctuation">:</span> <span class="token string">"core/text-transform"</span><span class="token punctuation">,</span>
    <span class="token string">"description"</span><span class="token punctuation">:</span> <span class="token string">"Text transform on cells in column event using expression value.toLowercase()"</span><span class="token punctuation">,</span>
    <span class="token string">"engineConfig"</span><span class="token punctuation">:</span> <span class="token punctuation">{</span>
      <span class="token string">"facets"</span><span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
      <span class="token string">"mode"</span><span class="token punctuation">:</span> <span class="token string">"row-based"</span>
    <span class="token punctuation">}</span><span class="token punctuation">,</span>
    <span class="token string">"columnName"</span><span class="token punctuation">:</span> <span class="token string">"event"</span><span class="token punctuation">,</span>
    <span class="token string">"expression"</span><span class="token punctuation">:</span> <span class="token string">"value.toLowercase()"</span><span class="token punctuation">,</span>
    <span class="token string">"onError"</span><span class="token punctuation">:</span> <span class="token string">"keep-original"</span><span class="token punctuation">,</span>
    <span class="token string">"repeat"</span><span class="token punctuation">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
    <span class="token string">"repeatCount"</span><span class="token punctuation">:</span> <span class="token number">10</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token punctuation">{</span>
    <span class="token string">"op"</span><span class="token punctuation">:</span> <span class="token string">"core/text-transform"</span><span class="token punctuation">,</span>
    <span class="token string">"description"</span><span class="token punctuation">:</span> <span class="token string">"Text transform on cells in column venue using expression value.toLowercase()"</span><span class="token punctuation">,</span>
    <span class="token string">"engineConfig"</span><span class="token punctuation">:</span> <span class="token punctuation">{</span>
      <span class="token string">"facets"</span><span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
      <span class="token string">"mode"</span><span class="token punctuation">:</span> <span class="token string">"row-based"</span>
    <span class="token punctuation">}</span><span class="token punctuation">,</span>
    <span class="token string">"columnName"</span><span class="token punctuation">:</span> <span class="token string">"venue"</span><span class="token punctuation">,</span>
    <span class="token string">"expression"</span><span class="token punctuation">:</span> <span class="token string">"value.toLowercase()"</span><span class="token punctuation">,</span>
    <span class="token string">"onError"</span><span class="token punctuation">:</span> <span class="token string">"keep-original"</span><span class="token punctuation">,</span>
    <span class="token string">"repeat"</span><span class="token punctuation">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
    <span class="token string">"repeatCount"</span><span class="token punctuation">:</span> <span class="token number">10</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token punctuation">{</span>
    <span class="token string">"op"</span><span class="token punctuation">:</span> <span class="token string">"core/column-split"</span><span class="token punctuation">,</span>
    <span class="token string">"description"</span><span class="token punctuation">:</span> <span class="token string">"Split column physical_description by separator"</span><span class="token punctuation">,</span>
    <span class="token string">"engineConfig"</span><span class="token punctuation">:</span> <span class="token punctuation">{</span>
      <span class="token string">"facets"</span><span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
      <span class="token string">"mode"</span><span class="token punctuation">:</span> <span class="token string">"row-based"</span>
    <span class="token punctuation">}</span><span class="token punctuation">,</span>
    <span class="token string">"columnName"</span><span class="token punctuation">:</span> <span class="token string">"physical_description"</span><span class="token punctuation">,</span>
    <span class="token string">"guessCellType"</span><span class="token punctuation">:</span> <span class="token boolean">true</span><span class="token punctuation">,</span>
    <span class="token string">"removeOriginalColumn"</span><span class="token punctuation">:</span> <span class="token boolean">true</span><span class="token punctuation">,</span>
    <span class="token string">"mode"</span><span class="token punctuation">:</span> <span class="token string">"separator"</span><span class="token punctuation">,</span>
    <span class="token string">"separator"</span><span class="token punctuation">:</span> <span class="token string">";"</span><span class="token punctuation">,</span>
    <span class="token string">"regex"</span><span class="token punctuation">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
    <span class="token string">"maxColumns"</span><span class="token punctuation">:</span> <span class="token number">0</span>
  <span class="token punctuation">}</span>
<span class="token punctuation">]</span>
</code></pre>
<p>4). Export the cleaned data set (C3).<br>
This is the output csv file C3:</p>
<pre class=" language-csv"><code class="prism  language-csv">Column,id,name,sponsor,event,venue,place,physical_description 1,physical_description 2,physical_description 3,physical_description 4,physical_description 5,occasion,notes,call_number,keywords,language,date,location,location_type,currency,currency_symbol,status,page_count,dish_count
0,12463,,hotel eastman,breakfast,commercial,"HOT SPRINGS, AR",CARD, 4.75X7.5,,,,EASTER;,,1900-2822,,,1900-04-15,Hotel Eastman,,,,complete,2,67
1,12464,,republican house,[dinner],commercial,"MILWAUKEE, [WI];",CARD, ILLUS, COL, 7.0X9.0,,EASTER;,"WEDGEWOOD BLUE CARD; WHITE EMBOSSED GREEK KEY BORDER; ""EASTER SUNDAY"" EMBOSSED IN WHITE; VIOLET COLORED SPRAY OF FLOWERS IN UPPER LEFT CORNER;",1900-2825,,,1900-04-15,Republican House,,,,complete,2,34
2,12465,,norddeutscher lloyd bremen,fruhstuck/breakfast;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,CARD, ILLU, COL, 5.5X8.0,,,"MENU IN GERMAN AND ENGLISH; ILLUS, STEAMSHIP AND SAILING VESSEL;",1900-2827,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,84
3,12466,,norddeutscher lloyd bremen,lunch;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,CARD, ILLU, COL, 5.5X8.0,,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH SAILING VESSEL;",1900-2828,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,63
4,12467,,norddeutscher lloyd bremen,dinner;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,FOLDER, ILLU, COL, 5.5X7.5,,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH ROCKS AND LIGHTHOUSE; STEAMSHIP AND SAILING VESSELS; CONCERT PROGRAM; DATES:  ON GERMAN SIDE OF MENU ""MONTAG, DEN 16 APRIL 1900""; ON ENGLISH SIDE OF MENU ""MONDAY, APRIL 15TH, 1900"";",1900-2829,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,4,33

</code></pre>
<p><img src="https://lh3.googleusercontent.com/Y24T2WT4J6FTDr4A84eacUVD4JxSQdMaKfWEey68MhKW5odBg8h0sV4fIKgiAv6HbgsdMhi_VjyQ=s8000" alt="enter image description here" title="demo1a output"></p>
<p>Part 2:<br>
1). Create a new OpenRefine project (P4) importing test data set (T). (Follow the instructions in Demo 0 part 1)<br>
<img src="https://lh3.googleusercontent.com/onQUOKBdadZ9s1gwkGBJ-Ix1_Y4uxJfxYV_riklfANye0AV201IP3YHX8GxzSSppZLGcvVLxSEio=s8000" alt="enter image description here" title="demo1a_part2"><br>
2). Execute <strong>recipe</strong> R through the OR interface.<br>
Click on the button “Apply…”, and paste the contents of R into the box, then click on “Perform Operations”.<br>
<img src="https://lh3.googleusercontent.com/qgW3QTBfm4k5HbMFZe10TXlRy-flygKVPI9VdNfZUfpAb6RC5xN2BtGPokwJci-ZOU5Xz_QLhhXS=s8000" alt="enter image description here" title="demo 1a apply"><br>
3). Export the cleaned data set C4.<br>
This is the output csv file C4:</p>
<pre class=" language-csv"><code class="prism  language-csv">Column,id,name,sponsor,event,venue,place,physical_description 1,physical_description 2,physical_description 3,physical_description 4,physical_description 5,occasion,notes,call_number,keywords,language,date,location,location_type,currency,currency_symbol,status,page_count,dish_count
0,12463,,hotel eastman,breakfast,commercial,"HOT SPRINGS, AR",CARD, 4.75X7.5,,,,EASTER;,,1900-2822,,,1900-04-15,Hotel Eastman,,,,complete,2,67
1,12464,,republican house,[dinner],commercial,"MILWAUKEE, [WI];",CARD, ILLUS, COL, 7.0X9.0,,EASTER;,"WEDGEWOOD BLUE CARD; WHITE EMBOSSED GREEK KEY BORDER; ""EASTER SUNDAY"" EMBOSSED IN WHITE; VIOLET COLORED SPRAY OF FLOWERS IN UPPER LEFT CORNER;",1900-2825,,,1900-04-15,Republican House,,,,complete,2,34
2,12465,,norddeutscher lloyd bremen,fruhstuck/breakfast;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,CARD, ILLU, COL, 5.5X8.0,,,"MENU IN GERMAN AND ENGLISH; ILLUS, STEAMSHIP AND SAILING VESSEL;",1900-2827,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,84
3,12466,,norddeutscher lloyd bremen,lunch;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,CARD, ILLU, COL, 5.5X8.0,,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH SAILING VESSEL;",1900-2828,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,63
4,12467,,norddeutscher lloyd bremen,dinner;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,FOLDER, ILLU, COL, 5.5X7.5,,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH ROCKS AND LIGHTHOUSE; STEAMSHIP AND SAILING VESSELS; CONCERT PROGRAM; DATES:  ON GERMAN SIDE OF MENU ""MONTAG, DEN 16 APRIL 1900""; ON ENGLISH SIDE OF MENU ""MONDAY, APRIL 15TH, 1900"";",1900-2829,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,4,33

</code></pre>
<p><img src="https://lh3.googleusercontent.com/cq_BLpIDGk5b7QvWWqoxlLCxPbeM2SerciZHv4kiWM4IYO870dpGQn2VWj_EiVUUqd2vutqAG7KZ=s8000" alt="enter image description here" title="demo 1a part2 output"><br>
4). Show that C3 and C4 are the <strong>same</strong> (data cleaning was reproduced).<br>
Here C3 is named as <em>demo1a_part1_partMenu.csv</em> file, C4 is <em>demo1a_part2_partMenu.csv</em> file. We use <em>diff</em> to test the difference between these two files.</p>
<pre class=" language-console"><code class="prism  language-console">wirelessprv-10-194-219-248:demo_all barbaralee$ diff demo1a_part1/demo1a_part1_partMenu.csv demo1a_part2/demo1a_part2_partMenu.csv

wirelessprv-10-194-219-248:demo_all barbaralee$
</code></pre>
<p>It shows that there is no difference between C3 and C4</p>
<h2 id="demo-1b">Demo 1b</h2>
<p>This demo shows that OpenRefine recipes do not suffice when operations <strong>not generalizable</strong>.</p>
<p>Part 1:<br>
1). Create a new OpenRefine project (P5) importing test data set (T). (Follow the instructions in Demo 0 part 1)<br>
<img src="https://lh3.googleusercontent.com/jP9h-_SyJ_0teAiaFMqv2hFISUA24sM1EB5k71DGXFOIWPHzWrIRDa3rDyw7jqV6LuQQlfFFleug=s8000" alt="enter image description here" title="demo1b part1 initial"><br>
2). Perform a few data cleaning operations where <strong>one</strong> operation is non-generalizable.<br>
3). View the operation <strong>history</strong> (H1).<br>
There are six steps in all, where the 4th step is a non-generalizable operation, “Edit single cell on row 2, column event”.<br>
<img src="https://lh3.googleusercontent.com/seOXIp-kvEIbo8BnQi-aoCpGyaNf9U4h7esUwfS1P3dcZ3DVwLh34vFOXlFD7cyI0bxl9EdD6zPM=s8000" alt="enter image description here" title="demo 1b part1 OH"><br>
4). Export the operation <strong>history</strong> and save as a <strong>recipe</strong> R via copy and paste to a file.<br>
When we check this JSON file, there are only five operations recorded in it.<br>
<strong>recipe</strong> R:<br>
This is the R:</p>
<pre class=" language-json"><code class="prism  language-json"><span class="token punctuation">[</span>
  <span class="token punctuation">{</span>
    <span class="token string">"op"</span><span class="token punctuation">:</span> <span class="token string">"core/text-transform"</span><span class="token punctuation">,</span>
    <span class="token string">"description"</span><span class="token punctuation">:</span> <span class="token string">"Text transform on cells in column id using expression value.toNumber()"</span><span class="token punctuation">,</span>
    <span class="token string">"engineConfig"</span><span class="token punctuation">:</span> <span class="token punctuation">{</span>
      <span class="token string">"facets"</span><span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
      <span class="token string">"mode"</span><span class="token punctuation">:</span> <span class="token string">"row-based"</span>
    <span class="token punctuation">}</span><span class="token punctuation">,</span>
    <span class="token string">"columnName"</span><span class="token punctuation">:</span> <span class="token string">"id"</span><span class="token punctuation">,</span>
    <span class="token string">"expression"</span><span class="token punctuation">:</span> <span class="token string">"value.toNumber()"</span><span class="token punctuation">,</span>
    <span class="token string">"onError"</span><span class="token punctuation">:</span> <span class="token string">"keep-original"</span><span class="token punctuation">,</span>
    <span class="token string">"repeat"</span><span class="token punctuation">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
    <span class="token string">"repeatCount"</span><span class="token punctuation">:</span> <span class="token number">10</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token punctuation">{</span>
    <span class="token string">"op"</span><span class="token punctuation">:</span> <span class="token string">"core/text-transform"</span><span class="token punctuation">,</span>
    <span class="token string">"description"</span><span class="token punctuation">:</span> <span class="token string">"Text transform on cells in column sponsor using expression value.toLowercase()"</span><span class="token punctuation">,</span>
    <span class="token string">"engineConfig"</span><span class="token punctuation">:</span> <span class="token punctuation">{</span>
      <span class="token string">"facets"</span><span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
      <span class="token string">"mode"</span><span class="token punctuation">:</span> <span class="token string">"row-based"</span>
    <span class="token punctuation">}</span><span class="token punctuation">,</span>
    <span class="token string">"columnName"</span><span class="token punctuation">:</span> <span class="token string">"sponsor"</span><span class="token punctuation">,</span>
    <span class="token string">"expression"</span><span class="token punctuation">:</span> <span class="token string">"value.toLowercase()"</span><span class="token punctuation">,</span>
    <span class="token string">"onError"</span><span class="token punctuation">:</span> <span class="token string">"keep-original"</span><span class="token punctuation">,</span>
    <span class="token string">"repeat"</span><span class="token punctuation">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
    <span class="token string">"repeatCount"</span><span class="token punctuation">:</span> <span class="token number">10</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token punctuation">{</span>
    <span class="token string">"op"</span><span class="token punctuation">:</span> <span class="token string">"core/text-transform"</span><span class="token punctuation">,</span>
    <span class="token string">"description"</span><span class="token punctuation">:</span> <span class="token string">"Text transform on cells in column event using expression value.toLowercase()"</span><span class="token punctuation">,</span>
    <span class="token string">"engineConfig"</span><span class="token punctuation">:</span> <span class="token punctuation">{</span>
      <span class="token string">"facets"</span><span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
      <span class="token string">"mode"</span><span class="token punctuation">:</span> <span class="token string">"row-based"</span>
    <span class="token punctuation">}</span><span class="token punctuation">,</span>
    <span class="token string">"columnName"</span><span class="token punctuation">:</span> <span class="token string">"event"</span><span class="token punctuation">,</span>
    <span class="token string">"expression"</span><span class="token punctuation">:</span> <span class="token string">"value.toLowercase()"</span><span class="token punctuation">,</span>
    <span class="token string">"onError"</span><span class="token punctuation">:</span> <span class="token string">"keep-original"</span><span class="token punctuation">,</span>
    <span class="token string">"repeat"</span><span class="token punctuation">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
    <span class="token string">"repeatCount"</span><span class="token punctuation">:</span> <span class="token number">10</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token punctuation">{</span>
    <span class="token string">"op"</span><span class="token punctuation">:</span> <span class="token string">"core/text-transform"</span><span class="token punctuation">,</span>
    <span class="token string">"description"</span><span class="token punctuation">:</span> <span class="token string">"Text transform on cells in column venue using expression value.toLowercase()"</span><span class="token punctuation">,</span>
    <span class="token string">"engineConfig"</span><span class="token punctuation">:</span> <span class="token punctuation">{</span>
      <span class="token string">"facets"</span><span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
      <span class="token string">"mode"</span><span class="token punctuation">:</span> <span class="token string">"row-based"</span>
    <span class="token punctuation">}</span><span class="token punctuation">,</span>
    <span class="token string">"columnName"</span><span class="token punctuation">:</span> <span class="token string">"venue"</span><span class="token punctuation">,</span>
    <span class="token string">"expression"</span><span class="token punctuation">:</span> <span class="token string">"value.toLowercase()"</span><span class="token punctuation">,</span>
    <span class="token string">"onError"</span><span class="token punctuation">:</span> <span class="token string">"keep-original"</span><span class="token punctuation">,</span>
    <span class="token string">"repeat"</span><span class="token punctuation">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
    <span class="token string">"repeatCount"</span><span class="token punctuation">:</span> <span class="token number">10</span>
  <span class="token punctuation">}</span><span class="token punctuation">,</span>
  <span class="token punctuation">{</span>
    <span class="token string">"op"</span><span class="token punctuation">:</span> <span class="token string">"core/column-split"</span><span class="token punctuation">,</span>
    <span class="token string">"description"</span><span class="token punctuation">:</span> <span class="token string">"Split column physical_description by separator"</span><span class="token punctuation">,</span>
    <span class="token string">"engineConfig"</span><span class="token punctuation">:</span> <span class="token punctuation">{</span>
      <span class="token string">"facets"</span><span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">,</span>
      <span class="token string">"mode"</span><span class="token punctuation">:</span> <span class="token string">"row-based"</span>
    <span class="token punctuation">}</span><span class="token punctuation">,</span>
    <span class="token string">"columnName"</span><span class="token punctuation">:</span> <span class="token string">"physical_description"</span><span class="token punctuation">,</span>
    <span class="token string">"guessCellType"</span><span class="token punctuation">:</span> <span class="token boolean">true</span><span class="token punctuation">,</span>
    <span class="token string">"removeOriginalColumn"</span><span class="token punctuation">:</span> <span class="token boolean">true</span><span class="token punctuation">,</span>
    <span class="token string">"mode"</span><span class="token punctuation">:</span> <span class="token string">"separator"</span><span class="token punctuation">,</span>
    <span class="token string">"separator"</span><span class="token punctuation">:</span> <span class="token string">";"</span><span class="token punctuation">,</span>
    <span class="token string">"regex"</span><span class="token punctuation">:</span> <span class="token boolean">false</span><span class="token punctuation">,</span>
    <span class="token string">"maxColumns"</span><span class="token punctuation">:</span> <span class="token number">0</span>
  <span class="token punctuation">}</span>
<span class="token punctuation">]</span>
</code></pre>
<p>5). Export the cleaned data set C1.<br>
This is the output csv file C1:</p>
<pre class=" language-csv"><code class="prism  language-csv">Column,id,name,sponsor,event,venue,place,physical_description 1,physical_description 2,physical_description 3,physical_description 4,physical_description 5,occasion,notes,call_number,keywords,language,date,location,location_type,currency,currency_symbol,status,page_count,dish_count
0,12463,,hotel eastman,breakfast,commercial,"HOT SPRINGS, AR",CARD, 4.75X7.5,,,,EASTER;,,1900-2822,,,1900-04-15,Hotel Eastman,,,,complete,2,67
1,12464,,republican house,dinner;,commercial,"MILWAUKEE, [WI];",CARD, ILLUS, COL, 7.0X9.0,,EASTER;,"WEDGEWOOD BLUE CARD; WHITE EMBOSSED GREEK KEY BORDER; ""EASTER SUNDAY"" EMBOSSED IN WHITE; VIOLET COLORED SPRAY OF FLOWERS IN UPPER LEFT CORNER;",1900-2825,,,1900-04-15,Republican House,,,,complete,2,34
2,12465,,norddeutscher lloyd bremen,fruhstuck/breakfast;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,CARD, ILLU, COL, 5.5X8.0,,,"MENU IN GERMAN AND ENGLISH; ILLUS, STEAMSHIP AND SAILING VESSEL;",1900-2827,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,84
3,12466,,norddeutscher lloyd bremen,lunch;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,CARD, ILLU, COL, 5.5X8.0,,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH SAILING VESSEL;",1900-2828,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,63
4,12467,,norddeutscher lloyd bremen,dinner;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,FOLDER, ILLU, COL, 5.5X7.5,,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH ROCKS AND LIGHTHOUSE; STEAMSHIP AND SAILING VESSELS; CONCERT PROGRAM; DATES:  ON GERMAN SIDE OF MENU ""MONTAG, DEN 16 APRIL 1900""; ON ENGLISH SIDE OF MENU ""MONDAY, APRIL 15TH, 1900"";",1900-2829,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,4,33
 
</code></pre>
<p><img src="https://lh3.googleusercontent.com/qvziV8seQnPjbQIGrywMYalExQtbiv8WMwzXloXTgWSqxvWB3OkZiyNZxqSpJHejCVr_YltyFcMB=s8000" alt="enter image description here" title="demo1b part1 output"></p>
<p>Part 2:<br>
1). Create a new OpenRefine project (P6) importing test data set (T). (Follow the instructions in Demo 0 part 1)<br>
<img src="https://lh3.googleusercontent.com/gXTMZ59ei1BlwlJqDeLFcoheGsdQgjiymK3qCqvgJhiMWDl-7CFg-Us8Yzc6OEWR_DEyKtKmTtW9=s8000" alt="enter image description here" title="demo1b part2 initial"><br>
2). Execute <strong>recipe</strong> R through the OR interface.<br>
Click on “Apply…” and copy and paste the contents of R into the box, then click on “Perform Operations”.<br>
<img src="https://lh3.googleusercontent.com/jpu7AD9eQ7fDqAS2OxNnXsUql9OTOKqeGQYq96DR-X3t409dsM4GeJfdLXo0Pvkn0aT6op0Yhnp0=s8000" alt="enter image description here" title="apply OH1 to demo1b part2"><br>
3). View the operation <strong>history</strong> (H2) and note that H2 lacks the non-generalizable steps from H1.<br>
As it shows below, Step 4 “Edit single cell on row 2, column event” recorded in H1 disappears in H2.<br>
<img src="https://lh3.googleusercontent.com/_4pVb62ALjfjM5Xnas19Qp225h89f49GBRFFIGnc9KFaeA0Bpz8TmZDaQK-t9H_jVnuD0h05p139=s8000" alt="enter image description here" title="compare OH1 and OH2"><br>
3). Export the cleaned data set C2.<br>
This is the output csv file C2:</p>
<pre class=" language-csv"><code class="prism  language-csv">Column,id,name,sponsor,event,venue,place,physical_description 1,physical_description 2,physical_description 3,physical_description 4,physical_description 5,occasion,notes,call_number,keywords,language,date,location,location_type,currency,currency_symbol,status,page_count,dish_count
0,12463,,hotel eastman,breakfast,commercial,"HOT SPRINGS, AR",CARD, 4.75X7.5,,,,EASTER;,,1900-2822,,,1900-04-15,Hotel Eastman,,,,complete,2,67
1,12464,,republican house,[dinner],commercial,"MILWAUKEE, [WI];",CARD, ILLUS, COL, 7.0X9.0,,EASTER;,"WEDGEWOOD BLUE CARD; WHITE EMBOSSED GREEK KEY BORDER; ""EASTER SUNDAY"" EMBOSSED IN WHITE; VIOLET COLORED SPRAY OF FLOWERS IN UPPER LEFT CORNER;",1900-2825,,,1900-04-15,Republican House,,,,complete,2,34
2,12465,,norddeutscher lloyd bremen,fruhstuck/breakfast;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,CARD, ILLU, COL, 5.5X8.0,,,"MENU IN GERMAN AND ENGLISH; ILLUS, STEAMSHIP AND SAILING VESSEL;",1900-2827,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,84
3,12466,,norddeutscher lloyd bremen,lunch;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,CARD, ILLU, COL, 5.5X8.0,,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH SAILING VESSEL;",1900-2828,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,2,63
4,12467,,norddeutscher lloyd bremen,dinner;,commercial,DAMPFER KAISER WILHELM DER GROSSE;,FOLDER, ILLU, COL, 5.5X7.5,,,"MENU IN GERMAN AND ENGLISH; ILLUS, HARBOR SCENE WITH ROCKS AND LIGHTHOUSE; STEAMSHIP AND SAILING VESSELS; CONCERT PROGRAM; DATES:  ON GERMAN SIDE OF MENU ""MONTAG, DEN 16 APRIL 1900""; ON ENGLISH SIDE OF MENU ""MONDAY, APRIL 15TH, 1900"";",1900-2829,,,1900-04-16,Norddeutscher Lloyd Bremen,,,,complete,4,33

</code></pre>
<p><img src="https://lh3.googleusercontent.com/uFRUDXIkHo091En2uirSMi1ffV4R07xNgwmbH9ziAce8XTavV-7ZbLsNyBb1-JXqZORBS2-eKdEQ=s8000" alt="enter image description here" title="demo 1b part 2 output"><br>
4). Show that C1 and C2 are <strong>different</strong> (data cleaning <strong>not</strong> reproduced)<br>
C1 here is named as <em>demo1b_part1.csv</em> file, C2 is named as <em>demo1b_part2_partMenu.csv</em> file.</p>
<pre class=" language-console"><code class="prism  language-console">wirelessprv-10-194-219-248:demo_all barbaralee$ diff demo1b_part1/demo1b_part1.csv demo1b_part2/demo1b_part2_partMenu.csv

3c3

&lt; 1,12464,,republican house,dinner;,commercial,"MILWAUKEE, [WI];",CARD, ILLUS, COL, 7.0X9.0,,EASTER;,"WEDGEWOOD BLUE CARD; WHITE EMBOSSED GREEK KEY BORDER; ""EASTER SUNDAY"" EMBOSSED IN WHITE; VIOLET COLORED SPRAY OF FLOWERS IN UPPER LEFT CORNER;",1900-2825,,,1900-04-15,Republican House,,,,complete,2,34

---

&gt; 1,12464,,republican house,[dinner],commercial,"MILWAUKEE, [WI];",CARD, ILLUS, COL, 7.0X9.0,,EASTER;,"WEDGEWOOD BLUE CARD; WHITE EMBOSSED GREEK KEY BORDER; ""EASTER SUNDAY"" EMBOSSED IN WHITE; VIOLET COLORED SPRAY OF FLOWERS IN UPPER LEFT CORNER;",1900-2825,,,1900-04-15,Republican House,,,,complete,2,34
</code></pre>
<p>As it shows, there is <strong>one</strong> difference between C1 and C2  which is stored in column 3 and row 3. In C1, the value is “dinner;”, whereas the value in C2 is “[dinner]”. This difference is exactly caused by the missing non-generalizable operation <strong>Step 4 “Edit single cell on row 2, column event”</strong>.</p>

