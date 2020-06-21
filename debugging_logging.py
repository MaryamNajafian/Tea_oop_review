"""
writes logging `events` to file or the terminal screen
Messages are written and logged at levels of `severity`: logging.INFO:severity level 20
    1- (debug()) : DIAGNOSTIC MESSAGES FOR DEVELOPMENT: logging.debug:severity level 30
    2- (info()): STANDARD PROGRESS MESSAGES
    3- (warning()): DETECTED A NON-SERIOUS ISSUE
    4- (error()): ENCOUNTERED AN ERROR, POSSIBLY SEIOUS
    5- (critical()): USUALLY A FATAL ERROR (PROGRAM STOPS)
if we don't set a level with `logging.basicConfig(level=logging.INFO)`
 the default is (warning())

"""

# import logging

# we are logging messages with severity level of (info()) or above
# logging.basicConfig(level=logging.INFO)
# store log messages in a file instead of the screen

#logging.basicConfig(level=logging.DEBUG, filename='example.log')
#logging.basicConfig(filename='example.log', format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

#
# logging.debug('This message will be igored')
# logging.info('This should be logged')
# logging.warning('And, this too')