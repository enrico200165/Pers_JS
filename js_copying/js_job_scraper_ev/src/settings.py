config = {
    # website to scrape, only linkedin & indeed are supported now
    'website'          : ['linkedin', 'indeed'],
    # path where program located
    'homePath'         : r'C:\Users\chase\Documents\GitHub\job_scrape',
    # specify username & password
    # or specify an authkey file
    "username"         :  "",
    "password"         :  "",
    "authkey"          : r"C:\Users\chase\_authinfo",
    "keywords"         :  ["SAS Programmer", "SAS"],
    "locations"        :  ["China", "China"],

    # specify date range:
    # for linkedin: 'Past 24 hours', 'Past Week', 'Past Month', 'Any Time'
    # for indeed: 'any', '15', '7', '3', '1', 'last'
    "date_range"       :  {'linkedin': "Past Month", 'indeed': "15"},

    # sort by either 'relevance' or 'post date'
    "sort_by"          :  "post date"
}
