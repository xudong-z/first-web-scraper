1. How to run your code (what command-line switches they are, what happens when you invoke the code, etc.)
This program is for you to extract the information about Academy Awarded films

positional arguments:
  source_type      Input the source: 'remote' or 'local'

optional arguments:
  -h, --help       show this help message and exit
  --source SOURCE  Input an integer for Source: 1/2/3!
  --nfilm NFILM    Any integer between 0-170, nfilm = 5 by default

1) first, you have specify the local source or remote source.
2) second, you can specify which particular source you would like to check (source1/2/3), and it will return a dafaframe with certain rows. If you don’t specify this parameter, it will return an aggregated(source1&2&3) data frame,as well as the visualisation plots
3) third, you can specify the nrows() you want. If you don’t do this, it will return a 5-row data frame by default

2. Any major “gotchas” to the  code (i.e. things that don’t work, go slowly, could be improved, etc.)
1)  please note that the remote source3 is time-consuming, probably 5 seconds for a record. and the response speed is kind of unstable. It is usually faster in the early morning. thing can be improved with a faster API.
2) in addition, if writing the data to a SQL, it will be faster.

3. Anything else you feel is relevant to your project.
