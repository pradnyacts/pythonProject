def logger(msg):
    def log_message():
        print("Log: ", msg)
    return  log_message    #return function
log_hi=logger('Hi')
log_hi()