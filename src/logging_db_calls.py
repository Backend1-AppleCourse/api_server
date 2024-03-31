import functools
import time
import logging

# Create a named logger
logger = logging.getLogger('functionLogger')

# Configure this logger
handler = logging.FileHandler('logs/function_logs.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def log_function_data(func):
    '''
    Decorator function to log function name, input values, execution time and 
    output byte length
    '''
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        # Log function name and input values
        logger.info(f"Called function: {func.__name__} with args: {args} and kwargs: {kwargs}")
        
        start_time = time.time()
        result = await func(*args, **kwargs)  # Assuming the function might be async
        execution_time = time.time() - start_time
        
        # Log execution time and output byte length
        output_byte_length = len(str(result).encode('utf-8'))
        logger.info(f"Function: {func.__name__} executed in {execution_time:.4f}s with output byte length: {output_byte_length}")
        
        return result
    return wrapper
