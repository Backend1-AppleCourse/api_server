from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
import time
import logging

# Create a named logger
logger = logging.getLogger('httpLogger')

# Configure this logger
handler = logging.FileHandler('logs/http_requests.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class LogRequestsMiddleware(BaseHTTPMiddleware):
    '''
    Middleware class to log incoming HTTP requests
    '''
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = (time.time() - start_time) * 1000
        logger.info(f"Request: {request.method} {request.url} - Completed in {process_time:.2f}ms - Status code: {response.status_code}")
        return response