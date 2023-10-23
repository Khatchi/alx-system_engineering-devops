#!/usr/bin/python3
"""
A script that accesses a REST API for employees' todo lists.
"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    employeeUrl = f"{baseUrl}/{employeeId}"

    response = requests.get(employeeUrl)
    employeeName = response.json().get('name')

    todosUrl = f'{employeeUrl}/todos'
    todosResponse = requests.get(todosUrl)
    todosItems = todosResponse.json()

    doneLists = []
    done = 0

    for item in todosItems:
        if item.get('completed'):
            doneLists.append(item)
            done += 1

    print(f'Employee {employeeName} is done with tasks({done}/{len(todosItems)}):')

    for item in doneLists:
        print(f"\t{item['title']}")
