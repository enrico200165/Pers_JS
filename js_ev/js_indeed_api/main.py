'''

indeed-python
A client library for using the Indeed Jobsearch API

 Install from PyPi using pip, a package manager for Python.
$ pip install indeed

The Indeed API needs to be called with your Indeed publisher number.
get here:  https://ads.indeed.com/jobroll/xmlfeed
You must pass this to the IndeedClient constructor.

from indeed import IndeedClient

client = IndeedClient(publisher = YOUR_PUBLISHER_NUMBER)


'''


from indeed import indee

# Performing a Job Search


client = IndeedClient('YOUR_PUBLISHER_NUMBER')

params = {
    'q' : "python",
    'l' : "austin",
    'userip' : "1.2.3.4",
    'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)"
}

search_response = client.search(**params)