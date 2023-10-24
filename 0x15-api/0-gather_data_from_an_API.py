#!/usr/bin/python3
"""
A script that accesses a REST API for employees' todo lists.
"""

import requests
import sys


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

    strr = 'is done with tasks'
    e = 'Employee'
    print('e {} {}({}/{}):'.format(employeeName, strr, done, len(todosItems)))

    for item in doneLists:
        print('\t{}'.format(item['title']))
