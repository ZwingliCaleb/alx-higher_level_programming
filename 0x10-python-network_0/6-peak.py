#!/usr/bin/python3
""" Function that finds the peak in a list of unsorted arrays """

def find_peak(list_of_integers):
    ''' Find peak in list '''
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
