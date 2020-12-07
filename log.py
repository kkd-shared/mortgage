"""
Kristian K. Damsgaard, 2019.

Class for logging messages.
"""

import datetime

class Log:
    def __init__(self):
        self.__log = []

    @property
    def log(self) -> list:
        return self.__log
    
    def append_message(self, a_sender, a_message):
        """
        Logs sender, date and time plus appended message.

        @type a_sender: str
        @param a_sender: Tag of the sending class
        @type a_message: str
        @param a_message: The message to log.
        """
        if a_sender is None:
            message = "Unknown object >>> " + str(datetime.datetime.now()) + " >>> "
        else:
            message = a_sender.__class__.__name__ + " >>> " + str(datetime.datetime.now()) + " >>> "

        if isinstance(a_message, str) :
            if a_message is not "":
                message += a_message
            else:
                message += "Tried to log an empty string."
        else: 
            message += "Tried to log a non-string message."

        print(message)
        self.__log.append(message)
        
    def print_log_to_console(self):
        """
        Prints the log to the console.
        """
        if self.__log:
            for message in self.__log:
                print(message)
        
    def write_log_to_file(self):
        """
        Writes the log to "log.txt". Creates "log.txt" if the file does not exist 
        in program parent folder.
        """
        if self.__log:
            f = open("log.txt", "a+")
            for message in self.__log:
                f.write(message + "\n")
            f.close()

    
