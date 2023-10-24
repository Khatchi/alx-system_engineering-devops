#!/usr/bin/python3
"""
A script that accesses a REST API for employees' todo lists,
and  exports data in csv format.
"""

import requests
import sys
import csv


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    employeeUrl = '{}/{}'.format(baseUrl, employeeId)

    response = requests.get(employeeUrl)
    employeeName = response.json().get('name')

    todosUrl = '{}/todos'.format(employeeUrl)
    todosResponse = requests.get(todosUrl)
    todosItems = todosResponse.json()

    doneLists = []
    done = 0

    for item in todosItems:
        if item.get('completed'):
            doneLists.append(item)
            done += 1

    fileName = '{}.csv'.format(employeeId)
    with open(fileName, 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        for item in doneLists:
            csvWriter.writerow([employeeId, employeeName, 'completed', item['title']])

    s = 'is done with tasks'
    e = 'Employee'
    print('{} {} {}({}/{}):'.format(e, employeeName, s, done, len(todosItems)))
