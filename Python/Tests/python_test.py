#!/usr/bin/python3
import sys
import os
import unittest
import argparse
import importlib

# Get module directore names:
cwd = sys.path[0]

data_structures_dir = cwd + '/../Data Structures'
data_structures_test_dir = cwd + '/../Tests/data-structures'

sorting_dir = cwd + '/../Sorting'
sorting_test_dir = cwd + '/../Tests/sorting-algos'

dynamic_programming_dir = cwd + '/../Dynamic Programming'
dynamic_programming_test_dir = cwd + '/../Tests/dynamic-programming'

graphs_dir = cwd + '/../Graphs'
graphs_test_dir = cwd + '/../Tests/graphs'

# Extend sys.path to include module directories
sys.path.extend([data_structures_dir, data_structures_test_dir, sorting_dir, sorting_test_dir,
                 dynamic_programming_dir, dynamic_programming_test_dir, graphs_dir, graphs_test_dir])

# print(sys.path)

def main():
    parser = argparse.ArgumentParser(
        description='Run unit tests on algorithm implementations in python')
    parser.add_argument('tests', metavar='<test-name>', type=str, nargs='*',
                        help='Specify which test to run by their names. \nValid names include: "data-structures," "sorting," "graphs," "dynamic-programming."  \nIf no tests are specificed then all tests will run.')
    tests_list = parser.parse_args().tests
    # print(tests_list)

    if len(tests_list) is 0:
        return
    else:
        [runTest(test) for test in tests_list]


def runTest(test):
    group_tests = ['sorting', 'data-structures', 'graphs', 'dynamic-programming']
    if test in group_tests:
        runGroupTest(test)
        return

    try:
        this_test = importlib.import_module(test + '_test')
        if this_test is None:
            print('Cannot find module', this_test)
        else:
            this_test.main()
            return
    except ImportError:
        print('No such test module as: ', test)


def runGroupTest(group):
    if group == 'data-structures':
        [runTest(test) for test in ['stack', 'linked-list', 'heap', 'bst', 'avl', 'hash-table']]
    elif group == 'sorting':
        [runTest(test) for test in ['bubble', 'insertion', 'selection', 'heap-sort', 'merge', 'quick', 'counting', 'radix']]    
    elif group == 'graphs':
        return
    elif group == 'dynamic-programming':
        return
    else:
        raise ValueError('No such test group')

if __name__ == '__main__':
    main()
