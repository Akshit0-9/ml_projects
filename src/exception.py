import sys
import logging

# pushing own custom message when an error occurs
# All information in custom handling exception documentation

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()  # will give only last information about error in which line and what error
    file_name = exc_tb.tb_frame.f_code.co_filename # file name 
    error_message = "Error occured in python script name [{0} line number [{1}] error message [{2}]".format(
    # filling the placeholders
    file_name,exc_tb.tb_lineno,str(error))
    
    return error_message
    
    
class customException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    
# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#        logging.info("Divide by zero error")
#        raise customException(e,sys)
