"""
    演示了线程的创建方式1 threading.Thread()
"""
import threading
import time

# 两个线程分别交替打印
def func():
    flag = 0
    while True:
        with lock:
            print(f"线程{threading.current_thread().name}",f"{flag}" * 5)
        flag = flag ^ 1
        time.sleep(0.5)


if __name__ == '__main__':
    lock = threading.Lock()

    t1 = threading.Thread(target=func, name="线程1")
    t2 = threading.Thread(target=func, name="线程2")

    t1.start()
    t2.start()

    # p1 = multiprocessing.Process(target=func)
    # p2 = multiprocessing.Process(target=func)
    # p1.start()
    # p2.start()