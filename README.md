# PAPI Hello World Python Code Snippets
The following Python code snippets are intended to help Python developers new to the Akamai Property Manager API (aka PAPI), get up and running and gain confidence within about an hour.<br>
<br>
While the sample code snippets are written in Python, developers using other programming languages can follow these examples and adapt to their programming environments.<br>
<br>

Prerequisites:
- An Akamai portal login userid and password (https://control.akamai.com)<br>
- Python 2 or 3 installed<br>
<br>

We recommended going through the sample snippets above in the order of step1, step2, etc.  While you can jump ahead to whichever code snippet you want, it may be easier to follow in the intended order.<br>

After you download the snippets or clone this repository, open the files, review all the comments, and edit the lines between -- REPLACE BEGIN -- and -- REPLACE END --

These code snippets are not intended to:
- Teach you everything about PAPI.  These are very simple code snippets intended to get you up and running quickly, ready to explore more.  See further PAPI code samples here:  https://github.com/akamai/api-kickstart
- Other Open APIs besides PAPI.  While PAPI is central to most Akamai onboarding and configuration automation, other Open APIs are often also used.  These include Purge, CPS, SPS, FastDNS, Reporting, Billing, Diagnostics and various Cloudlets.

PAPI Intro Video<br>
[![PAPI Sample Code](https://img.youtube.com/vi/3YMJdhjVh8Y/0.jpg)](https://www.youtube.com/embed/videoseries?list=PL01azkzCBGf8AqL7aDnCZRFjqzuVbOXc1 "PAPI Sample Code")

For more information about Akamai APIs, see the [{OPEN} Developer Site](https://developer.akamai.com/).

## Quick Install

Install required python modules (For python 2, use `pip` instead of `pip3`):

```bash
$pip3 install requests
$pip3 install edgegrid-python
```

Clone this repository (alternatively you can also just copy/save the code samples to a local directory), then _create a new file called `.edgerc` in the main directory of the project_ with your own PAPI credentials (create "New API Client for me" from the Akamai portal / Configure/Manage APIs menu).  Watch the video above for details):

```plaintext
[default]
host = akaa-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.luna.akamaiapis.net/
client_token = akab-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
client_secret = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=
access_token = akab-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
max-body = 131072
```

For each sample code file, review the code until you understand what it does, then edit each file and replace values in the REPLACE BEGIN and REPLACE END section with your information if necessary.  Pay special attention to the credentials which are specified in the `edgerc` and `section` variables.

Finally, to run the sample code:

```bash
$./step1_papisample_listgroups.py
$./step2_papisample_listproperties.py
$./step3_papisample_listpropertydetails.py
$./step4_papisample_updatepropertyruletree.py
```


## License

> Copyright 2015 Akamai Technologies, Inc. All Rights Reserved.
> 
> Licensed under the Apache License, Version 2.0 (the "License");
> you may not use this file except in compliance with the License.
>
> A copy of the License is distributed with this software, or you
> may obtain a copy of the License at 
>
>    http://www.apache.org/licenses/LICENSE-2.0
>
> Unless required by applicable law or agreed to in writing, software
> distributed under the License is distributed on an "AS IS" BASIS,
> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> See the License for the specific language governing permissions and
> limitations under the License.
