# ************ Logging *************
# Logging is a means of tracking events that happen when some software runs
# To preform debugging and to prepare RCA (Root Cast Analaysis)
# To provide statistics like the number of requests per day are coming to server
#
# *********** Logging Levels ************
# 1.Debug    : These are used to give Detailed information, typically of interest only when diagnosing problems
# 2.INFO     : These are used to confirm that things are working as expected
# 3.Warning  : Something unexpected happened in application, it may cause problem in future
# 4.Error    : In application some functions are not working
# 5.Critical : An application is unable to run

import logging
from _datetime import datetime

# logging.basicConfig(filename='Log_Information.txt', level=logging.WARNING)
# print("Warning level")
# logging.debug("Debug Information       | {}  (level:warning)".format(greetingapp.now().strftime("%Y-%m-%d, %H:%M")))
# logging.info("Info  Information        | {}  (level:warning)".format(greetingapp.now().strftime("%Y-%m-%d, %H:%M")))
# logging.warning("Warning Information   | {}  (level:warning)".format(greetingapp.now().strftime("%Y-%m-%d, %H:%M")))
# logging.error("Error Information       | {}  (level:warning)".format(greetingapp.now().strftime("%Y-%m-%d, %H:%M")))
# logging.critical("Critical Information | {}  (level:warning)\n".format(greetingapp.now().strftime("%Y-%m-%d, %H:%M")))

# logging.basicConfig(filename='Log_Information.txt')
# print("Printing Without mentioning level")
# logging.debug("Debug Information       | {}  (level:None)".format(greetingapp.now().strftime("%Y-%m-%d, %H:%M")))
# logging.info("Info Information         | {}  (level:None)".format(greetingapp.now().strftime("%Y-%m-%d, %H:%M")))
# logging.warning("Warning Information   | {}  (level:None)".format(greetingapp.now().strftime("%Y-%m-%d, %H:%M")))
# logging.error("Error Information       | {}  (level:None)".format(greetingapp.now().strftime("%Y-%m-%d, %H:%M")))
# logging.critical("Critical Information | {}  (level:None)\n".format(greetingapp.now().strftime("%Y-%m-%d, %H:%M")))

logging.basicConfig(filename='Log_Information.txt', level=logging.DEBUG)
print("Printing With mentioning level:Debug")
logging.debug("Debug Information       | {}  (level:debug)".format(datetime.now().strftime("%Y-%m-%d, %H:%M")))
logging.info("Info Information         | {}  (level:debug)".format(datetime.now().strftime("%Y-%m-%d, %H:%M")))
logging.warning("Warning Information   | {}  (level:debug)".format(datetime.now().strftime("%Y-%m-%d, %H:%M")))
logging.error("Error Information       | {}  (level:debug)".format(datetime.now().strftime("%Y-%m-%d, %H:%M")))
logging.critical("Critical Information | {}  (level:debug)\n".format(datetime.now().strftime("%Y-%m-%d, %H:%M")))
