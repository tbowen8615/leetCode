from collections import deque

class RecentCounter:
    def __init__(self):
        # Initialize a queue to store timestamps of requests
        self.requests = deque()

    def ping(self, t: int) -> int:
        """
        :type t: int
        :rtype: int
        """
        # Add the current request's timestamp to the queue
        self.requests.append(t)

        # Remove timestamps older than t - 3000
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        # Return the number of valid requests in the range
        return len(self.requests)


# Example usage
# Create an instance of RecentCounter
recentCounter = RecentCounter()

# Add requests and print the number of recent requests
print(recentCounter.ping(1))      # Output: 1
print(recentCounter.ping(100))    # Output: 2
print(recentCounter.ping(3001))   # Output: 3
print(recentCounter.ping(3002))   # Output: 3
