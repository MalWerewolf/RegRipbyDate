RegRipbyDate
============

A script very similar to William Ballenthin's print all sample script @ https://github.com/williballenthin/python-registry/blob/master/samples/printall.py, but this allows for a more elegant way to do a refined search of the registry to happen based upon the modified date.


Prerequisite
------------

You need to have the python-registry library from https://github.com/williballenthin/python-registry setup to use this and this script must be located in that folder.

The script below takes in 3 required arguments (Earliest Date, Latest Date, and File Location) and 1 optional argument (Output to CSV or not). 


Examples
------------

MAC Example: RegRipbyDate.py -e '2014-01-26 12:00:00' -l '2014-01-28 00:00:00' -i /Users/Someone/Desktop/Temp/SYSTEM. (Note the single Quotes for MAC)

Windows: Windows Example: RegRipbyDate.py -e "2014-01-20 00:00:00" -l "2014-01-27 00:00:00" -i C:\Users\SomeUser\Desktop\SYSTEM (Note the double Quotes for Windows)

Sources
-------
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
