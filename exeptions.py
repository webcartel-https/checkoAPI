import os,sys,platform 

""" Work in progress """


class checkoAPIException(Exception):
    """ Base exception """




class DataNotFound(checkoAPIException): ...


class ConnectionError(checkoAPIException): ...