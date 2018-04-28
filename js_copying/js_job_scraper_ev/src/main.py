# -*- coding: utf-8 -*-
import os
try:
    os.chdir(r'C:\Users\chase\Documents\GitHub\job_scrape\src')
except:
    pass
from scrape_linkedin import linkedinJob
from scrape_indeed import indeedJob

def parseAuthkey(authkey):
    result = {}
    with open(authkey, 'r') as file:
        for cnt, line in enumerate(file):
            string = list(map(str.strip, line.split(' ')))
            result[string[0]] = {'email':string[1], 'password':string[2]}
    return result

def scrape(website, email, password, job_keyword, location, filterByDate, sortBy):
    websiteList = {'linkedin':linkedinJob, "indeed":indeedJob}
    jobType = websiteList[website]
    global job_scrape
    job_scrape = jobType(homePath)
    job_scrape.logIn(email, password)
    job_scrape.search(job_keyword, location)
    job_scrape.customSearch(filterByDate, sortBy)
    job_scrape.scroll()
    job_scrape.job_list.toJSON()
    job_scrape.job_list.toMarkdown()
    job_scrape.driverQuit()


if __name__ == "__main__":
    from settings import config
    website             = config['website']
    homePath           = config['homePath']
    authkey            = config['authkey']
    if authkey:
        email              = parseAuthkey(authkey)['indeed']['email']
        password           = parseAuthkey(authkey)['indeed']['password']
    else:
        email = config['username']
        password = config['password']
    job_keyword        = config['keywords']
    location           = config['locations']
    date_range         = config['date_range']
    sort_by            = config['sort_by']

    for web in website:
        for i in range(len(job_keyword)):
            scrape(web, email, password, job_keyword[i], location[i], date_range[web], sort_by)
