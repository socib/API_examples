
<img src="images/bg-masthead3.jpg" alt="SOCIB">

# What is SOCIB API?

API stands for Application Programming Interface. An API is basically a programmatic tool that is used to interact with a system. More specifically, the new SOCIB API offers the possibility of discovering our data catalog and retrieving the data it contains. This API is a REST API, which means that the requests are issued with an usual HTTP client (available with any programming language). 

# What's new?

One of the main new features is the possibility of discovering and retrieving data without temporal restrictions, unlike Data Discovery API, that only lets you retrieve the latest 60 days of data, at most. Also important is that the data can be filtered with new sets of criteria and retrieved with several resampling methods. 

Gridded data type is now also supported (currently only for HF Radar data). Another important breakthrough has been achieved introducing the concept of "data products", that let us provide grouped data in almost any way. The API also supports authentication via API keys, so the tracking of users will now be possible (it was not with the old one). 

Finally, in future releases the new API will allow responding with new data types such as operational data models or even media data.

# Who is addressed to?

The new SOCIB API is addressed to two different types of users: the IT (software developer) user and the data scientific user. For the IT expert, the use will be almost trivial. For  scientific data experts, with no experience on this kind of tool, some training will be needed. 

A success story is the development of the [SOCIB Data Catalog](http://apps.socib.es/data-catalog/) web that fully relies on the capacity of this API, that will be published on the new SOCIB website.

# How to interact with SOCIB API?
Go to the [API home page](http://api.socib.es/home/) and request an API key (bottom of the page)


# API examples (python notebooks)

* [Quick start](tips/quick_start.ipynb) - SOCIB API main concepts

* [SOCIB data-sources](data_sources): SOCIB deployments metadata & data

	- What is a data-source? ([Example 1](data_sources/what_is_a_data_source.ipynb))

	- Searching for certain data-sources ([Example 2](data_sources/searching_for_certain_data_sources.ipynb))

	- Requesting a data-source's data ([Example 3](data_sources/requesting_a_data_sources_data.ipynb))

	- Subsetting a data-source's data: by time-range, by elevation-range and by bounding-box ([Example 4](data_sources/subsetting_a_data_sources_data.ipynb))

	- Resampling a data-source's data: ([Example 5](data_sources/resampling_a_data_sources_data.ipynb))
 
* [SOCIB data-platforms](data_platforms): SOCIB platforms metadata & data
	- What is a data-platform? ([Example 6](data_platforms/what_is_a_data_platform.ipynb))

	- Searching for certain data-platform ([Example 7](data_platforms/searching_for_certain_data_platforms.ipynb)) by platform type.

	- Requesting a data-plaform's historical files ([Example 8](data_platforms/requesting_a_data_platforms_historical_files.ipynb))

	- Requesting a data-plaform's latest files ([Example 9](data_platforms/requesting_a_data_platforms_latest_files.ipynb))

* [SOCIB data-products](data_products): SOCIB products metadata & data
	- What is a data-product? ([Example 10](data_products/what_is_a_data_product.ipynb))

	- Searching for certain data-products ([Example 11](data_products/searching_for_certain_data_products.ipynb)) by coverage_bounding_box, type, status, instrument, product, initial_time, end_time, processing levels etc.

	- Requesting a data-product's files ([Example 12](data_products/requesting_a_data_product_files.ipynb))


# Quick hands-on
* Getting SOCIB platforms full-list - by platform type and status ([hands on 1](hands_on/hands_on_1.ipynb))
* Getting SOCIB platforms latest data - download ([hands on 2](hands_on/hands_on_2.ipynb))
* Getting SOCIB platforms historical data - download ([hands on 3](hands_on/hands_on_3.ipynb))


# Legacy
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
