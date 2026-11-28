"""
    创建线程对象的方式2
    定义类继承 thread.Thread
"""
import threading
import time

class Worker(threading.Thread):
    def run(self):
        flag = 0
        while True:
            print(f"线程{threading.current_thread().name}", f"{flag}" * 5)
            flag = flag ^ 1 # 替换0和1
            time.sleep(0.5)

if __name__ == '__main__':
    t1 = Worker(name="thread-1")
    t2 = Worker(name="thread-2")

    t1.start()
    t2.start()