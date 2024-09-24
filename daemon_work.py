# import time
# from daemon import runner

# class App():
#     def __init__(self):
#         self.stdin_path = '/dev/null'
#         self.stdout_path = '/dev/tty'
#         self.stderr_path = '/dev/tty'
#         self.pidfile_path =  '/tmp/foo.pid'
#         self.pidfile_timeout = 5
#     def run(self):
#         while True:
#             print("Howdy!  Gig'em!  Whoop!")
#             time.sleep(10)

# app = App()
# daemon_runner = runner.DaemonRunner(app)
# daemon_runner.do_action()

from threading import Thread
import time




def func():
    # for i in range(5):
    #     print(f"from child thread: {i}")
    while True:
        print ("li")
        time.sleep(3)
th = Thread(target=func)
th.start()

def func2():
    # for i in range(5):
    #     print(f"from child thread: {i}")
    while True:
        print ("li2")
        time.sleep(3)
th2 = Thread(target=func2)
th2.start()
# print("App stop")

