import threading
import time
class TicketBooking:
    def __init__(self, available_tickets):
        self.available_tickets = available_tickets
        self.lock = threading.Lock()
    def book_tickets(self, name):
        with self.lock:
            if self.available_tickets > 0:
                time.sleep(1)
                self.available_tickets -= 1
                print(f"{name} successful ticket booking. Remaining: {self.available_tickets}")
            else:
                print(f"sorry {name}, no tickets available")
                
tic = TicketBooking(1)
threads = []
users = ["alice", "bob"]
for user in users:
    t = threading.Thread(target=tic.book_tickets, args=(user,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()