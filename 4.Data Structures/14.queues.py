from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# remove from the front of the queue
queue.popleft()
print(queue)

if not queue:
    print("queue is empty")