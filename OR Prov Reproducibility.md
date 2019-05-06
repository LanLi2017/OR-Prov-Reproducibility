---


---

<h1 id="openrefine-reproducibility-demo">OpenRefine Reproducibility Demo</h1>
<p>These four demos are to test the OpenRefine <strong>reproducibility</strong><br>
Dataset is first 5 rows of Menu.csv from <a href="http://menus.nypl.org/data">New York Public Library</a>.<br>
<img src="https://lh3.googleusercontent.com/UZI3YMHsf9V20E0kv7Qrjh-d4D92Hnoi1SolehurTe1pjlkElsQJHoY6gozs9yzFCOPY6qwNYLzM=s8000" alt="enter image description here" title="Dataset for demo"></p>
<h2 id="demo-0">Demo 0</h2>
<p>This demo is supported by OpenRefine natively, should always work.<br>
Part 1:<br>
1). Create new OpenRefine project (P1) importing test data set (T).</p>
<p><img src="https://lh3.googleusercontent.com/T1AhCiSnEZbv8l6br8VOiP5Vm1L44bJyZbM7Iopn7_faRfmjMcRSjg1uVvU2X9WzX1YpHhkmGw2x=s8000" alt="enter image description here" title="demo0_part1_initial"><br>
2). Perform a few data cleaning operations, both generalizable and non-generalizable.<br>
<img src="https://lh3.googleusercontent.com/s3KDyv_mM1VK43xoB-IJiy3EnWxbWTYkRMdaz-naA_myIGek2m2vqujPPVr-TyhF19BTrpG7iN2R=s8000" alt="enter image description here" title="demo0_part1_operations"></p>
<p>3). View the operation <strong>history</strong>(H1)<br>
<img src="https://lh3.googleusercontent.com/VRjrxEMg6JbuI7BNf-SeNqKka6wC4Plih8_9dQdYAqWTg1UZ0rAhjFCZ-Cm0XUd1R05grC5Kr9SY=s1000" alt="enter image description here" title="demo0_part1_OH"><br>
4). Undo all data cleaing steps, then redo all the operations.</p>
<p>5). Export the cleaned data set C1.<br>
<img src="https://lh3.googleusercontent.com/zfr5RqXEC8UaDMm5dk0lKgCsydAUETqq7YGLYmlvzEqS3TebX6KU6RDrhC4XUmhmEY0dMCmFmx4Q=s8000" alt="enter image description here" title="demo0_part1_output"><br>
6). Export the project and save as an archive A, a tarball.</p>
<p>Part 2:<br>
1). Create a new OpenRefine project (P2), importing the exported archive (A).<br>
<img src="https://lh3.googleusercontent.com/MI0ZK7qxj9sVt62xFrKK03BRHUMusXck5mWmciPvZzFJ5gpPK0y2sJ2iyqW4XCSKiIi8qpV8OANX=s8000" alt="enter image description here" title="demo0_part2 import archive"><br>
2). View the operation <strong>history</strong> (H2) and check that it looks like H1<br>
<img src="https://lh3.googleusercontent.com/2Ok_a9JlVCtu8w3PHmEVpSu-R60rGnsjLUmzfPr68D-yBjPbg8Q33iwKb6SROsJT3_Mi4jaDDGvF=s8000" alt="enter image description here" title="compare OH1 and OH2"><br>
3). Undo all data cleaning steps, then redo all the operations.<br>
4). Export the cleaned data set C2.<br>
<img src="https://lh3.googleusercontent.com/xveKW4Y6GjWHubejCSMC1k9svbxYoHosII0NJrhkSd-s3WeJlQXT2UcLxIF04b-YjgMEhAQ18d9t=s8000" alt="enter image description here" title="demo0_part2_output"><br>
5). Show that C1 and C2 are the <strong>same</strong>.</p>
<pre class=" language-console"><code class="prism  language-console">wirelessprv-10-194-219-248:demo_all barbaralee$  diff demo0_part1/demo0_part1_partMenu.csv demo0_part2/demo0_part2.csv

wirelessprv-10-194-219-248:demo_all barbaralee$
</code></pre>
<p>We use <em>diff</em> to test C1 and C2, and there is no return here. Thus, C1 and C2 are the same.</p>
<h2 id="demo-1a">Demo 1a</h2>
<p>This demo shows that OpenRefine recipes suffice when all operations are <strong>generalizable</strong>.</p>
<p>Part 1:<br>
1). Create new OpenRefine project (P3) importing test data set (T).<br>
<img src="https://lh3.googleusercontent.com/SyVrZ3nsG2R2LxpsMBmqlNPUWX9smF_woDehrxaI-jw_DKof-yJOw38sTv603a90XQd4BlX9m3aP=s8000" alt="enter image description here" title="demo1a_part1 initial"><br>
2). Perform a few data cleaing operations where all operations are generalizable.<br>
<img src="https://lh3.googleusercontent.com/C1dOSuBociCHFCbGQ1Bsu1pqCOVZkMetgyBFwpPZstH1TVUu1ORJetWiIdYhTXVtr7bXmxKCuhc7=s8000" alt="enter image description here" title="demo1a_part1 OH"><br>
3). Export the operation history and save as a <strong>recipe</strong> ®.</p>
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
<img src="https://lh3.googleusercontent.com/Y24T2WT4J6FTDr4A84eacUVD4JxSQdMaKfWEey68MhKW5odBg8h0sV4fIKgiAv6HbgsdMhi_VjyQ=s8000" alt="enter image description here" title="demo1a output"></p>
<p>Part 2:<br>
1). Create a new OpenRefine project (P4) importing test data set (T).<br>
<img src="https://lh3.googleusercontent.com/onQUOKBdadZ9s1gwkGBJ-Ix1_Y4uxJfxYV_riklfANye0AV201IP3YHX8GxzSSppZLGcvVLxSEio=s8000" alt="enter image description here" title="demo1a_part2"><br>
2). Execute <strong>recipe</strong> R through the OR interface.<br>
<img src="https://lh3.googleusercontent.com/qgW3QTBfm4k5HbMFZe10TXlRy-flygKVPI9VdNfZUfpAb6RC5xN2BtGPokwJci-ZOU5Xz_QLhhXS=s8000" alt="enter image description here" title="demo 1a apply"><br>
3). Export the cleaned data set C4.<br>
<img src="https://lh3.googleusercontent.com/cq_BLpIDGk5b7QvWWqoxlLCxPbeM2SerciZHv4kiWM4IYO870dpGQn2VWj_EiVUUqd2vutqAG7KZ=s8000" alt="enter image description here" title="demo 1a part2 output"><br>
4). Show that C3 and C4 are the <strong>same</strong> (data cleaning was reproduced).<br>
Here C3 is  demo1a_part1_partMenu.csv file, C4 is demo1a_part2_partMenu.csv file. We use <span class="katex--inline"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>d</mi><mi>i</mi><mi>f</mi><mi>f</mi></mrow><annotation encoding="application/x-tex">diff</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.88888em; vertical-align: -0.19444em;"></span><span class="mord mathit">d</span><span class="mord mathit">i</span><span class="mord mathit" style="margin-right: 0.10764em;">f</span><span class="mord mathit" style="margin-right: 0.10764em;">f</span></span></span></span></span> to test the difference between these two files.</p>
<pre class=" language-console"><code class="prism  language-console">wirelessprv-10-194-219-248:demo_all barbaralee$ diff demo1a_part1/demo1a_part1_partMenu.csv demo1a_part2/demo1a_part2_partMenu.csv

wirelessprv-10-194-219-248:demo_all barbaralee$
</code></pre>
<p>There is no difference between C3 and C4</p>
<h2 id="demo-1b">Demo 1b</h2>
<p>This demo shows that OpenRefine recipes do not suffice when operations <strong>not generalizable</strong>.</p>
<p>Part 1:<br>
1). Create a new OpenRefine project (P5) importing test data set (T).<br>
<img src="https://lh3.googleusercontent.com/jP9h-_SyJ_0teAiaFMqv2hFISUA24sM1EB5k71DGXFOIWPHzWrIRDa3rDyw7jqV6LuQQlfFFleug=s8000" alt="enter image description here" title="demo1b part1 initial"><br>
2). Perform a few data cleaning operations where <strong>one</strong> operation is non-generalizable.<br>
3). View the operation <strong>history</strong> (H1).<br>
<img src="https://lh3.googleusercontent.com/seOXIp-kvEIbo8BnQi-aoCpGyaNf9U4h7esUwfS1P3dcZ3DVwLh34vFOXlFD7cyI0bxl9EdD6zPM=s8000" alt="enter image description here" title="demo 1b part1 OH"><br>
4). Export the operation <strong>history</strong> and save as a <strong>recipe</strong> R via copy and paste to a file.</p>
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
<img src="https://lh3.googleusercontent.com/qvziV8seQnPjbQIGrywMYalExQtbiv8WMwzXloXTgWSqxvWB3OkZiyNZxqSpJHejCVr_YltyFcMB=s8000" alt="enter image description here" title="demo1b part1 output"></p>
<p>Part 2:<br>
1). Create a new OpenRefine project (P6) importing test data set (T).<br>
<img src="https://lh3.googleusercontent.com/gXTMZ59ei1BlwlJqDeLFcoheGsdQgjiymK3qCqvgJhiMWDl-7CFg-Us8Yzc6OEWR_DEyKtKmTtW9=s8000" alt="enter image description here" title="demo1b part2 initial"><br>
2). Execute <strong>recipe</strong> R through the OR interface.<br>
<img src="https://lh3.googleusercontent.com/jpu7AD9eQ7fDqAS2OxNnXsUql9OTOKqeGQYq96DR-X3t409dsM4GeJfdLXo0Pvkn0aT6op0Yhnp0=s8000" alt="enter image description here" title="apply OH1 to demo1b part2"><br>
3). View the operation <strong>history</strong> (H2) and note that H2 lacks the non-generalizable steps from H1.<br>
Step 4 “Edit single cell on row 2, column event” recorded in H1 disappears in H2.<br>
<img src="https://lh3.googleusercontent.com/_4pVb62ALjfjM5Xnas19Qp225h89f49GBRFFIGnc9KFaeA0Bpz8TmZDaQK-t9H_jVnuD0h05p139=s8000" alt="enter image description here" title="compare OH1 and OH2"><br>
3). Export the cleaned data set C2.<br>
<img src="https://lh3.googleusercontent.com/uFRUDXIkHo091En2uirSMi1ffV4R07xNgwmbH9ziAce8XTavV-7ZbLsNyBb1-JXqZORBS2-eKdEQ=s8000" alt="enter image description here" title="demo 1b part 2 output"><br>
4). Show that C1 and C2 are <strong>different</strong> (data cleaning <strong>not</strong> reproduced)<br>
C1 here is demo1b_part1.csv file, C2 is demo1b_part2_partMenu.csv file.</p>
<pre class=" language-console"><code class="prism  language-console">wirelessprv-10-194-219-248:demo_all barbaralee$ diff demo1b_part1/demo1b_part1.csv demo1b_part2/demo1b_part2_partMenu.csv

3c3

&lt; 1,12464,,republican house,dinner;,commercial,"MILWAUKEE, [WI];",CARD, ILLUS, COL, 7.0X9.0,,EASTER;,"WEDGEWOOD BLUE CARD; WHITE EMBOSSED GREEK KEY BORDER; ""EASTER SUNDAY"" EMBOSSED IN WHITE; VIOLET COLORED SPRAY OF FLOWERS IN UPPER LEFT CORNER;",1900-2825,,,1900-04-15,Republican House,,,,complete,2,34

---

&gt; 1,12464,,republican house,[dinner],commercial,"MILWAUKEE, [WI];",CARD, ILLUS, COL, 7.0X9.0,,EASTER;,"WEDGEWOOD BLUE CARD; WHITE EMBOSSED GREEK KEY BORDER; ""EASTER SUNDAY"" EMBOSSED IN WHITE; VIOLET COLORED SPRAY OF FLOWERS IN UPPER LEFT CORNER;",1900-2825,,,1900-04-15,Republican House,,,,complete,2,34
</code></pre>
<p>And the difference between C1 and C2 are stored in the column 3 and row 3, where in C1, the value is “dinner;”, but the value in C2 is “[dinner]”.</p>
<h2 id="demo-2">Demo 2</h2>
<p>This demo shows augmenting OpenRefine with additional scripts can create “extended”/“completed” recipes that are “fully reproducible”, i.e. will obtain C1=C2 …)</p>
<p>Part 1:<br>
1). Create a new OpenRefine project (P7) importing test data set (T).<br>
<img src="https://lh3.googleusercontent.com/n9o6bpXDTr7gtWKhBdpQV0H6S7XZoo9JzpD9T7AnjD9JIpykC0EnHOA0gaDqQOycmdfkzGqMj2ei=s8000" alt="enter image description here" title="demo2 part1 initial"><br>
2). Perform a few data cleaning operations where <strong>one</strong> operaiton is non-generalizable.<br>
3). View the operation <strong>history</strong> (H1).<br>
<img src="https://lh3.googleusercontent.com/6b8Gz-O9-yFQGuM61OegZm2jpZR-7BK_UT6zaOHwgyHfKF2hXX9yQREvQRu795ETc5lppH838NPH=s8000" alt="enter image description here" title="demo2 part1 OH"><br>
4). Export the operation history as a recipe R via copy and paste to a file.</p>
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
<p>5). Export the project as archive A2.<br>
6). Run <strong>Complete-History-Extractor</strong> script with A2 as input, and get as output JSON file representing the extended recipe (<a href="https://drive.google.com/open?id=12SrTmNmRQUTpQi0g8emeMZzuj8l5HmvQ">ER</a>) associated with A2.<br>
7). Show that R and ER differ (using jsondiff), where the differences correspond exactly to non-generalizable operations which are not represented in R, but are represented in ER.</p>
<p>ER has extract information about the <strong>single-edit</strong>.<br>
8). Exported the cleaned data set (<a href="https://drive.google.com/open?id=17MIkIfqPzYzGqI74uZffvsQ9_0PjnuRe">C1</a>).</p>
<p>Part 2:<br>
1). Create a new OpenRefine project (P2) importing test data set (T) through the OR interface.<br>
<img src="https://lh3.googleusercontent.com/8NM7iYuxixKqcuGQdYJXIRZRxYSlimNGZg3o3Nec3p7abIBqfbJkJCjg3r7fT5u22rQLHlr-lXl4=s8000" alt="demo2 project" title="demo2 project"><br>
2). Run the <strong>Complete-History-Application</strong> script giving it ER as input.</p>
<pre><code>   $ python run_or_script.py -i ./JSON/Enhanced_Recipe.json -pname "demo2_part2"
   recipe ./JSON/Enhanced_Recipe.json executed on project: demo2_part2
</code></pre>
<p><img src="https://lh3.googleusercontent.com/TE43WR55TI3wccjhcAU5IA-Av4sjz2zFaMFOfhZQm6bjouW9X7qlgaPinf7sIfhMvUZmiDz8CvjW=s8000" alt="enter image description here" title="Demo2 project refresh"></p>
<p>3). The script connects to the running OR instance with P2 loaded, and applies the extended recipe.<br>
4). After a refresh of the OR web interface.<br>
5). Export the cleaned data set (<a href="https://drive.google.com/open?id=1DnETG_JMXXiwGhILvYhhjC8kvvlzQbsz">C2</a>)<br>
6). Show that C1 and C2 are <strong>same</strong> (data cleaning <strong>was</strong> reproduced)</p>
<pre><code>script Diff_C1_C2
</code></pre>
<p>Get the <a href="https://drive.google.com/open?id=1-2vQp3xR_qFY6Qtz3fidW4iz4bVBlEZv">log</a> file:</p>
<pre><code>Script started on Mon Apr 29 17:24:45 2019 
[?1034hbash-3.2$ diff demo [Kdemo2_part1.csv demo2_part2.csv &gt;&gt; Diff_C1_D [KC2.gt [Ktxt 
bash-3.2$ exit 
exit 
Script done on Mon Apr 29 17:25:05 2019
</code></pre>
<p>The difference between C1 and C2 is stored in <a href="https://drive.google.com/open?id=1hCIMx-5vz_4qsOoPDpOei6AnKSnEiUIt">Diff_C1_C2.txt</a>, which it shows that C1 is the same as C2.</p>

