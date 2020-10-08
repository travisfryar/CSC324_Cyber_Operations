# ==========================================================================
# PROGRAM:........... search CVE database for subject
# AUTHOR:............ Travis Fryar
# COURSE:............ CSC 324
# TERM:.............. Fall 2020
# ==========================================================================
import textwrap, wget, os
# return list of known vulnerabilities per given subject
def search_CVE_database(filename, subject):
    results = []
    with open(filename, 'r', errors='ignore') as file:
        for line in file:
            if 'CVE-' in line:
                if int(line.split('-')[1]) >= 2017 and subject in line:
                    results.append(line)
    return results
print('┌─────────────────────┐')
print('│  CVE fetch utility  │')
print('└─────────────────────┘')
print('Downloading latest CVE database...', end='')
url = 'https://cve.mitre.org/data/downloads/allitems.csv'
if os.path.isfile('allitems.csv'):
    os.remove('allitems.csv')
    filename = wget.download(url)
else:
    filename = wget.download(url)
print('\rDownloading latest CVE database...done!')
print('------')
# windows
search_results = search_CVE_database('allitems.csv', 'Windows')
print('Number of known vulnerabilities in Windows OS (2018-present): ', len(search_results))
print('------')
# iOS
search_results = search_CVE_database('allitems.csv', 'iOS')
print('Number of known vulnerabilities in iOS (2018-present): ', len(search_results))
print('------')
# chrome
search_results = search_CVE_database('allitems.csv', 'Google Chrome')
print('The latest vulnerability in Google Chrome: ')
print('\n'.join(textwrap.wrap(search_results[-1],80,break_long_words=False)))