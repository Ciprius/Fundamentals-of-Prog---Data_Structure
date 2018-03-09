'''
Created on Dec 5, 2016

@author: Cipri
'''
class ControllerException(Exception):
    """
    Exception class for controller errors
    """
    def __init__(self, message):
        """
        Constructor for controller exception class
        message - A string representing the exception message
        """
        self.__message = message

    def __str__(self):
        return self.__message

    def getMessage(self):
        return  self.__message