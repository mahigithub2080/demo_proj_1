## common code which will be used in entire project..
import sys

def error_message_details(error,error_details:sys): # defining custom msg..
    _,_,exc_tb=error_details.exc_info() # getting last parameter of errror which is exc_tb
    file_name=exc_tb.tb_frame.f_code.co_filename # fetching filename from exc_tb
    error_message=' Error occured in python script name [{0}] line number [{1}] error message [{2}] '.format(file_name,exc_tb.tb_lineno,str(error)) 
    # the error  msg should print 
    return error_message # returning error msg

class CustomException(Exception): # class defination inherited by Exception class
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message   

    


