
<img src="assets/bg-masthead3.jpg" alt="SOCIB">

# What is SOCIB API?

An API (Application Programming Interface) is basically a programmatic tool that is used to interact with a system; in this case, the Balearic Islands Coastal Ocean Observing System (SOCIB). In other words, [SOCIB API](http://api.socib.es/) offers the possibility of discovering SOCIB data catalog and retrieving the data it contains. A success story is the development of the [SOCIB Data Catalog](http://apps.socib.es/data-catalog/) web that fully relies on the capacity of this API.

This API is a REST API, which means that the requests are issued with an usual HTTP client (available in any programming language) and on the notebooks in this repository users will find useful code snippets in python for doing so.

# What's new?

SOCIB API is meant to replace the services provided by the <i>soon-to-be-deprecated</i> <a href="http://apps.socib.es/DataDiscovery/index.jsp" target="_blank">SOCIB Data Discovery API</a>. Among the significants improvements of SOCIB API over SOCIB Data Disocvery API users will find:
<ul>
	<li>Extended data discovery and retrieval capabilities. Unlike SOCIB Data Discovery API, SOCIB API do not limit the data retrieval to the last 60 days: users can now request further data (no temporal restrictions). In adidtion, a most complete set of parameters have been enabled so that users stablish different filtering criterias over the data in the requests.</li>
	<li>New types of data, SOCIB API now handles gridded-like data in addition to time series, profiles and trajectory-like data. So far, this gridded data only applies to the observations produced by SOCIB High Frequency Radar system</li>
	<li>New data-<i>entities</i>. SOCIB API distinguishes a total of 3 data-<i>entities</i>: entries (files), sources (files comming from the same instrument/platform) and products (files from different instrument/platforms sharing a given context: i.e produced in the frame of a given project, campaing etc).</li>
	<li>Authentication. SOCIB API supports user authenticatio via API keys. This way users activity can be properly tracked.</li>
	<li>New dictionaries. SOCIB API now provides a wider range of dictionaries with descriptive fields to introduce the users the available types of platfoms, instruments, procesing levels, variables etc</li>
</ul>
Finally, in future releases the new API will allow responding with new data types such as operational data models or even media data.

# Who is addressed to?

SOCIB API is addressed to two different types of users: the IT (software developer) user and the scientists. IT experts will find the use of the API almost trivial. Scientiests with no previous experience on APIs usage, will need some training. 

# Get your API key
Go to the [API home page](http://api.socib.es/home/) and request an API key (form at the bottom of the page) to be able to dicover and retrieve SOCIB data by means of the API.


# API examples (python notebooks)

* Data streams ([Static](01-Getting-started.ipynb) | [Live](https://gesis.mybinder.org/binder/v2/gh/pazrg/SOCIB_API/ca0639283248e34ae7c46741872dbf5e401ddbaa?filepath=01-Getting-started.ipynb)):
    - *Origin*: Platform-types and instruments-types managed by SOCIB Observing System.
	- *Content*: standard variables managed by SOCIB Observing System
	- *Representations*: data-modes, data-levels and features

* Data entities ([Static](02-Hands-on-data.ipynb) | [Live](https://gesis.mybinder.org/binder/v2/gh/pazrg/SOCIB_API/ca0639283248e34ae7c46741872dbf5e401ddbaa?filepath=02-Hands-on-data.ipynb)):
	- *Discovery*: find data produced in a given area, time range, containing a certain variable and involving a given instrument or/and platform type.
	- *Download*: download data from the above discovery results.

# Quick setup
* Export search results to CSV - for later download or sharing purposes ([quickSetup1.zip](quickSetups/quickSetup1.zip))

# Contact
This material has been developed by [Paz Rotllan](https://github.com/pazrg). Email: protllan@socib.es

# Copyright
Copyright (c) 2017 ICTS SOCIB - Servei d'observació i predicció costaner de les Illes Balears.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.