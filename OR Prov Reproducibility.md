<h1 id="openrefine-reproducibility-demo">OpenRefine Reproducibility Demo</h1>
<p>These four demos are to test the OpenRefine <strong>reproducibility</strong></p>
<h2 id="demo-0">Demo 0</h2>
<p>This demo is supported by OpenRefine natively, should always work.<br>
Part 1:<br>
1). Create new OpenRefine project (P1) importing test data set (T).<br>
<img src="https://lh3.googleusercontent.com/9We-m-vdid5iYV3d-RfToCDOPfXGaXrqPS4jik8Bhn9mJkO5B6PgZnEeXWsPz55kfC4nrPEuNyc" alt="Data set is from Menu.csv version 04/16/19 from New York Public Library " title="Create project P1" width="800"><br>
2). Perform a few data cleaning operations, both generalizable and non-generalizable.<br>
<img src="https://lh3.googleusercontent.com/4cvlYjKTXMBeKutAfOfhKC7pXWF6ClpoPEWHwrXA_vyPZ3PjSHkM90eJJ4IIUVfOnQA_ZgbAhp0" alt="enter image description here" title="Perform data cleaning operations"><br>
3). View the operation <strong>history</strong>(H1)<br>
<img src="https://lh3.googleusercontent.com/_oXqoZYRCPsmFRGamo72RmeCwOacojL08GH6LDIkv4wYs9jR-OfvCvWwBYEE-HTy9no-sAAH4sA" alt="enter image description here" title="Extract Operation History"><br>
4). Undo all data cleaing steps, then redo all the operations.<br>
5). Export the cleaned data set (<a href="https://drive.google.com/open?id=1zg3jDYuXNblminVmdQ5VEJyXrGdKFziW">C1</a>).<br>
6). Export the project and save as an archive (<a href="https://drive.google.com/open?id=1RfEqHDCGtii3R3XD_BDHZMNwVzy-NRZq">A</a>), a tarball.</p>
<p>Part 2:<br>
1). Create a new OpenRefine project (P2), importing the exported archive (A).<br>
<img src="https://lh3.googleusercontent.com/vKUv6TVcxbL7CVPRxnC3Ck6SQSCEIE0I-Rv9XqaMslAGikVCTaa1xiJXzoc_QdDUq9jNM8EFSSM" alt="Create a new project by imporing archive(A) from part1 of demo0" title="create a new project P2"><br>
2). View the operation <strong>history</strong> (H2) and check that it looks like H1<br>
<img src="https://lh3.googleusercontent.com/8Fafs_2agkPlaVQ84AUTlV6sehoP0C0x2WtqE5mnG0IouWNtsQBxZRMtG_TSOabr4SeThjXMgUY" alt="H1 and H2 are the same" title="Compare H1 and H2"><br>
3). Undo all data cleaning steps, then redo all the operations.<br>
4). Export the cleaned data set (<a href="https://drive.google.com/open?id=1cN2svCY3V2vyNblXzPB07MSLvqPMZwOJ">C2</a>).<br>
5). Show that C1 and C2 are the <strong>same</strong>.</p>
<pre><code>script Diff_C1_C2.log
</code></pre>
<p>Get a <a href="https://drive.google.com/open?id=16qeTfN9Cx9QGeRkyn2-tXsntcVyr0t90">log</a> file :</p>
<pre><code>Script started on Sun Apr 28 17:09:01 2019
 [?1034hbash-3.2$ diff demo_0_1/C1_cleaned_Dataset.csv demo0_2  [K  [K  [K_0_2/Openrefine_demo0_2_C2.cs 
v &gt;&gt; Diff_C1_C2.txt
bash-3.2$ exit
exit

Script done on Sun Apr 28 17:10:07 2019
</code></pre>
<p>And the difference of C1 and C2 are record in <a href="https://drive.google.com/open?id=1mNd6cVXzweOuqE0rZVuLmyb7pKM0y1if">Diff_C1_C2.txt</a>, where it shows C1 and C2 are the same</p>
<h2 id="demo-1a">Demo 1a</h2>
<p>This demo shows that OpenRefine recipes suffice when all operations are <strong>generalizable</strong>.</p>
<p>Part 1:<br>
1). Create new OpenRefine project (P3) importing test data set (T).<br>
2). Perform a few data cleaing operations where all operations are generalizable.<br>
<img src="https://lh3.googleusercontent.com/81QHE_FdPgmVXTWfu_U_WHW94-zKaQSYljUA8LRRhX1yvNnbhKoHiHrMGQ-OHTab_g77uXIHUQo" alt="enter image description here" title="Generalized operations"><br>
3). Export the operation history and save as a <strong>recipe</strong> (<a href="https://drive.google.com/open?id=18Cb606OWsgt11sn5Kwr6DcBzfsP4_xFJ">R</a>) via copy and paste to a file.<br>
4). Export the cleaned data set (<a href="https://drive.google.com/open?id=14NaoCElH9Qr5Aaw8YaPDC8gHoprz8MTY">C3</a>)</p>
<p>Part 2:<br>
1). Create a new OpenRefine project (P4) importing test data set (T).<br>
2). Execute <strong>recipe</strong> R through the OR interface.<br>
<img src="https://lh3.googleusercontent.com/jQTMQ53cVJVoUwtw5zWB-OJN3D_nsrf-VwVZGy2Wt2e806K6VM-xTBgFy7vrgxdPDKuNWNrb7V8" alt="enter image description here" title="Apply recipe R to Project P4"><br>
3). Export the cleaned data set (<a href="https://drive.google.com/open?id=1norLAD0mhMzlYtmDOrkLv8vhyWFnLCwO">C4</a>)<br>
4). Show that C3 and C4 are the <strong>same</strong> (data cleaning was reproduced).</p>
<pre><code>script Diff_C3_C4.log
</code></pre>
<p>Get a <a href="https://drive.google.com/open?id=1Ga9Zx3CMZqUX2YFYr9s-c_X1VTPkZVRe">log</a> file:</p>
<pre><code>Script started on Sun Apr 28 16:48:39 2019
 [?1034hbash-3.2$ diff  [K  [K  [K  [Kdiff demo_1a_2/Openrefine_1a_2_C4.csv demo_1a_1/openrefine_demo1a1_C3. 
csv &gt;&gt; Diff_C3_C4.txt
bash-3.2$ exit
exit

Script done on Sun Apr 28 16:49:01 2019
</code></pre>
<p>And the diffrences of C3 and C4 are recorded in <a href="https://drive.google.com/open?id=1wSQFwzV6jsNqXuOTOKIfqCS_gvDYFWCi">Diff_C3_C4.txt</a>, where it shows that C3 and C4 are the same.</p>
<h2 id="demo-1b">Demo 1b</h2>
<p>This demo shows that OpenRefine recipes do not suffice when operations <strong>not generalizable</strong>.</p>
<p>Part 1:<br>
1). Create a new OpenRefine project (P5) importing test data set (T).<br>
2). Perform a few data cleaning operations where <strong>one</strong> operation is non-generalizable.<br>
3). View the operation <strong>history</strong> (H1).<br>
<img src="https://lh3.googleusercontent.com/SCY0kpxeGMz00ZGdzteDGaVzCXZlkhcVqj4rBPiTUbJ0A08NoZtAg4TJdkivo3QvF5wjWl3k15Me" alt="enter image description here" title="Non-generalizable Operation"><br>
4). Export the operation <strong>history</strong> and save as a <strong>recipe</strong> (<a href="https://drive.google.com/open?id=1lZ0c_hBq6ISoklrqpLRvgK1YCsfnCxYT">R</a>) via copy and paste to a file.<br>
5). Export the cleaned data set (<a href="https://drive.google.com/open?id=1bUdEoTALvkAOr71dWgZBRpWGnMrHZOE5">C1</a>)</p>
<p>Part 2:<br>
1). Create a new OpenRefine project (P6) importing test data set (T).<br>
2). Execute <strong>recipe</strong> R through the OR interface.<br>
<img src="https://lh3.googleusercontent.com/QksTjtBgqkNZKbL4DqXjprG4EyMP7Bpw88Kc0WQHYfJF0BLtfOwcFKJbLVYz9tEfXlGLfo5pq6QQ" alt="enter image description here" title="Apply R to P2"><br>
2). View the operation <strong>history</strong> (H2) and note that H2 lacks the non-generalizable steps from H1.<br>
<img src="https://lh3.googleusercontent.com/j-ibXPDJ_zEQNdpSDw2mmffdq5tMu_dJJ1T_CgKQCyJ7OHBSvVe6GKFF6BjlA2JiefhU1XMa_c6-" alt="Missing operation for single edit" title="Compare H1_H2"><br>
3). Export the cleaned data set (<a href="https://drive.google.com/open?id=10YyART-zao33U4hYA_ormS0c8cxfibeB">C2</a>)<br>
4). Show that C1 and C2 are <strong>different</strong> (data cleaning <strong>not</strong> reproduced)</p>
<pre><code>script Diff_demo1b_C1_C2.log
</code></pre>
<p>Get a <a href="https://drive.google.com/open?id=1aKeOSRXnLBnItij4xHPVGcz24Dby4z8Y">log</a> file:</p>
<pre><code> Script started on Mon Apr 29 13:57:45 2019
     [?1034hbash-3.2$ diff downloads/demo1b_part2.csv downloads/demo1b_part1.csv &gt;&gt; Diff_dem 
    o1b_C1_c  [KC2.txt
    bash-3.2$
</code></pre>
<p>And the difference between C1 and C2 are stored in the <a href="https://drive.google.com/open?id=1bVgzUvtpMqDRic1i03DJXIKCvEZhS7KB">Diff_demo1b_C1_C2.txt</a>, where it shows there is one row are different:</p>
<pre><code>&lt; 21083,,leonard lewisohn,complimentary dinner to the fellow passengers of the normannia to meet mr. robert m. thompson,private party;,"DELMONICO'S, [NEW YORK]",FOLDER, ILL, 7.5X5.5,,,,,SEE ABOVE EVENT;,FASTENED AT TOP IN TWO PLACES BY RIBBONS; FRENCH MENU; WINES AND LIQUERS,1892-115,,,1891-10-10T00:00:00Z,Leonard Lewisohn,,,,complete,4,28
---
&gt; 21083,,leonard lewisohn,complimentary dinner to the fellow passengers of the normannia to meet mr. robert m. thompson,private party,"DELMONICO'S, [NEW YORK]",FOLDER, ILL, 7.5X5.5,,,,,SEE ABOVE EVENT;,FASTENED AT TOP IN TWO PLACES BY RIBBONS; FRENCH MENU; WINES AND LIQUERS,1892-115,,,1891-10-10T00:00:00Z,Leonard Lewisohn,,,,complete,4,28
</code></pre>
<p>The difference occurs in column 5:  column"venue", and one is “private party;” whereas the other is “private party”.  C1 and C2 are different.</p>
<h2 id="demo-2">Demo 2</h2>
<p>This demo shows augmenting OpenRefine with additional scripts can create “extended”/“completed” recipes that are “fully reproducible”, i.e. will obtain C1=C2 …)</p>
<p>Part 1:<br>
1). Create a new OpenRefine project (P7) importing test data set (T).<br>
2). Perform a few data cleaning operations where one operaiton is non-generalizable.<br>
3). View the operation <strong>history</strong> (H1).<br>
<img src="https://lh3.googleusercontent.com/5GKiJBxJK0toZFmimXxDaZfG-P2eZoNJ78B5WTa2sNgJfPjnsrSt2ez0E8fFcM66XIXPEzkoPGTz" alt="enter image description here" title="Operation History Demo2 part1"><br>
4). Export the operation history as a recipe (<a href="https://drive.google.com/open?id=1TKVte-JiNCXJOu1QC6n32bj8Mwg5t3u7">R</a>) via copy and paste to a file.<br>
5). Export the project as archive <a href="https://drive.google.com/open?id=1UvHgpBUplqr-rh-R7UL6IHxiiAHXYHxh">A2</a>.<br>
6). Run <strong>Complete-History-Extractor</strong> script with A2 as input, and get as output JSON file representing the extended recipe (<a href="https://drive.google.com/open?id=12SrTmNmRQUTpQi0g8emeMZzuj8l5HmvQ">ER</a>) associated with A2.<br>
7). Show that R and ER differ (using jsondiff), where the differences correspond exactly to non-generalizable operations which are not represented in R, but are represented in ER.</p>
<pre><code>screen Diff_OH_ER.log
</code></pre>
<p>Get a <a href="https://drive.google.com/open?id=1XvTEEpICJE1bdyaRkCup2RbQTTfZzzWZ">log</a> file:</p>
<pre><code>Script started on Mon Apr 29 15:33:05 2019 
[?1034hbash-3.2$ df [Kiff  [Kjson  [Kdiff demo2_part1_OH.json demo2_part1_ [K_ER.. [Kjson &gt;&gt; Diff_OH_ER.txt 
bash-3.2$ exit 
exit 
Script done on Mon Apr 29 15:33:39 2019
</code></pre>
<p>The differences between R and ER recorded in <a href="https://drive.google.com/open?id=1uEK84O_Uooz1SvIdzOV4F04GC2ZoX45l">Diff_OH_ER.txt</a> :</p>
<pre><code>{"$insert": [[8, {"cell": "3", "new": "{\"v\":\"middag/dinner\"}", "row": "8643", "old": "{\"v\":\"middag-dinner\"}", "op": "custom/single-edit"}]]}
</code></pre>
<p>ER has extract information about the <strong>single-edit</strong>.<br>
8). Exported the cleaned data set (<a href="https://drive.google.com/open?id=17MIkIfqPzYzGqI74uZffvsQ9_0PjnuRe">C1</a>).</p>
<p>Part 2:<br>
1). Create a new OpenRefine project (P2) importing test data set (T) through the OR interface.<br>
2). Run the <strong>Complete-History-Application</strong> script giving it ER as input.<br>
3). The script connects to the running OR instance with P2 loaded, and applies the extended recipe.</p>
<p>4). After a refresh of the OR web interface.<br>
5). Export the cleaned data set (C2)<br>
6). Show that C1 and C2 are <strong>same</strong> (data cleaning <strong>was</strong> reproduced)</p>

