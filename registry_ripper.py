#!/usr/bin/env python

"""
-------------------------------------------------------------------------------
Copyright 2014 CaptainCrabnasty

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-------------------------------------------------------------------------------

This code intends to provide an elegant solution for searching through the
Windows Registry Hives based upon a given time frame.

This work is based upon the 'printall.py' sample found below:

    https://github.com/williballenthin/python-registry/blob/master/samples/
"""

__program__ = "reg_rip_by_date.py"
__author__ = "CaptainCrabnasty"
__copyright__ = "Copyright 2014, CaptainCrabnasty"
__license__ = "Apache License 2.0"
__version__ = "0.0.1"
__status__ = "Development"

import argparse
import csv
import os
import sys
from datetime import datetime

try:
    from Registry import Registry

except ImportError:
    sys.exit(
        """
        Missing 'Registry' Module! Get it here:
        https://github.com/williballenthin/python-registry
        """
    )


def format_date(user_input):
    """Returns a properly formatted time string."""

    try:
        formatted_date = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")

    except ValueError:

        sys.exit(
            """
            Incorrect Time Format or Range! Expecting: 'YYYY-MM-DD HH:MM:SS'

            You provided: %s
            """ % user_input
        )

    return formatted_date


def input_file(user_input):
    """Returns file path if the file exists."""

    if not os.path.isfile(user_input):

        sys.exit(
            """
            Invalid File Path: %s
            """ % user_input
        )

    return user_input


def get_keys_in_range(key, earliest_time, latest_time, results_dict):
    """Return keys modified between earliest and latest times provided."""

    if earliest_time <= key.timestamp() <= latest_time:

        results_dict[str(key.timestamp())] = key.path()

    for sub_key in key.subkeys():

        get_keys_in_range(sub_key, earliest_time, latest_time, results_dict)


def main():
    """Where the automagic happens..."""

    # For Argparse, see: http://docs.python.org/dev/library/argparse.html
    parser = argparse.ArgumentParser(
        prog="reg_rip_by_date.py",
        description="Query Registry Hives by 'modified date'",
        epilog="Thanks for using this program!",
        formatter_class=lambda prog: argparse.RawTextHelpFormatter(
            prog, max_help_position=100)
    )

    parser.add_argument(
        "-e", "--earliest", type=format_date, required=True,
        metavar="YYYY-MM-DD HH:MM:SS", help="Earliest Date/Time."
    )

    parser.add_argument(
        "-l", "--latest", type=format_date, required=True,
        metavar="YYYY-MM-DD HH:MM:SS", help="Latest Date/Time."
    )

    parser.add_argument(
        "-i", "--input", type=input_file, required=True,
        metavar="FILE PATH", help="Full Path to Registry Hive."
    )

    parser.add_argument(
        "-o", "--output", type=str, required=False,
        metavar="FILE PATH", help="Optional Output to CSV."
    )

    args = parser.parse_args()

    data = open(args.input, 'rb')

    hive = Registry.Registry(data)

    root = hive.root()

    results_dict = {}

    get_keys_in_range(root, args.earliest, args.latest, results_dict)

    if args.output:

        with open(args.output, 'wb') as outfile:

            writer = csv.writer(
                outfile, results_dict, quoting=csv.QUOTE_ALL
            )

            writer.writerow(['Timestamp', 'Key Path'])

            for timestamp, registry_key in results_dict.iteritems():

                writer.writerow([timestamp, registry_key])

        print("\n\tDone! Find Your Results Here: %s\n" % args.output)

    else:

        count = 0  #USED FOR TESTING

        for timestamp, registry_key in results_dict.iteritems():

            print("%s, %s" % (timestamp, registry_key))

            count+=1

        print count
if __name__ == "__main__":
    """The proper way to run this code..."""

    main()
