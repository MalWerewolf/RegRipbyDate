reg_rip_by_date
============

This code intends to provide an elegant solution for searching through the
Windows Registry Hives based upon the 'modified date.'

This work is based upon the 'printall.py' sample found below:

    https://github.com/williballenthin/python-registry/blob/master/samples/

Outputs the timestamp and full registry paths either to the console, or
a CSV file.

-----

### Usage

This program accepts an input file path (Registry Hive), a range of time (earliest/latest),
and optionally, an output file path (CSV).

```
usage: reg_rip_by_date.py [-h] -e YYYY-MM-DD HH:MM:SS -l YYYY-MM-DD HH:MM:SS
                          -i FILE PATH [-o FILE PATH]

Query Registry Hives by 'modified date'

optional arguments:
  -h, --help                                              show this help message and exit
  -e YYYY-MM-DD HH:MM:SS, --earliest YYYY-MM-DD HH:MM:SS  Earliest Date/Time.
  -l YYYY-MM-DD HH:MM:SS, --latest YYYY-MM-DD HH:MM:SS    Latest Date/Time.
  -i FILE PATH, --input FILE PATH                         Full Path to Registry Hive.
  -o FILE PATH, --output FILE PATH                        Optional Output to CSV.
```

-----

### Examples

 ```
python reg_rip_by_date.py -earliest "2014-03-01 00:00:00" -latest "2014-03-30 00:00:00" -input "/Users/username/Desktop/SYSTEM"
 ```

 OR

 ```
python reg_rip_by_date.py --earliest "2014-03-01 00:00:00" --latest "2014-03-02 00:00:00" --input "/Users/username/Desktop/SYSTEM" --output "/Users/username/Desktop/TEST.csv"
 ```

-----


### Sources

https://github.com/williballenthin/python-registry

```
    Copyright 2014

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
```
