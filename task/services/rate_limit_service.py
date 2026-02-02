import time
import threading
from collections import defaultdict, deque
from task.core.config import RATE_LIMIT, WINDOW_SIZE


class RateLimiter:
    def __init__(self):
        self.requests = defaultdict(deque)
        self.lock = threading.Lock()

    def is_allowed(self, ip: str) -> bool:
        now = time.time()

        with self.lock:
            timestamps = self.requests[ip]

            while timestamps and timestamps[0] <= now - WINDOW_SIZE:
                timestamps.popleft()

            if len(timestamps) >= RATE_LIMIT:
                return False

            timestamps.append(now)
            return True


rate_limiter = RateLimiter()
