1.并发与并行
    并发: 单个 CPU 处理多个任务,各个任务交替执行一段时间
    并行: 多个 CPU 同时执行多个任务

    同步: 多个任务排队执行
    异步: 多个任务同时执行,各自执行各的,相互之间互不影响

2.多进程
    进程
        进程是操作系统进行资源分配的基本单位
        操作系统中一个正在运行的程序或软件就是一个进程
        每个进程都有自己独立的一块内存空间
        一个进程崩溃后,在保护模式下不会对其他进程产生影响
        多进程指在操作系统中同时运行多个程序

    创建
        Unix/Linux 操作系统提供了一个 os.fork() 系统调用,
        普通的函数调用,执行一次,返回一次.
        调用 fork() 一次,返回两次,因为操作系统会字典把当前进程(父进程)复制了一份(子进程),然后,分别在父进程和子进程内返回.
        使用 multiprocessing.Process 创建进程
            语法
                multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

            说明
                group: 应当始终为 None, 其存在仅仅是为了与 thread.Thread 兼容
                target: 由 run() 方法发起调用的可调用对象,默认为 None
                name: 进程名,默认为 None 时自动分配
                args: 参数元组
                kwargs: 关键字参数字典
                daemon: 是否为守护进程, True|False, 默认为 None 时则继承父进程

            Process 的属性和方法与其他常用方法
                name: 获取进程名
                pid: 获取进程号
                daemon: 判断或设置进程是否为守护进程
                exitcode: 获取子进程的退出状态码
                start(): 启动进程, 调用传入 target 的对象. start() 只能被调用一次
                run(): 默认调用传入 target 的对象,如果子类化了 Process, 可以重写此方法来定义行为
                join([timeout]): 阻塞主进程,直至子进程结束或超时. timeout 意为阻止多少秒
                terminate(): 强制终止子进程
                kill(): 杀死进程,与 terminate() 类似,但是更彻底.
                is_alive(): 检查进程是否仍在运行
                os.getpid(): 获取当前进程编号
                os.getppid(): 获取当前进程的父进程编号

        创建方式
            multiprocessing.Process(target=进程执行的对象,由 run 方法发起调用的可调用对象)

            创建进程子类,通过子类创建进程对象
                子类需要重写 run 方法

            通过进程池创建进程对象,当需要启动大量子进程时,可以使用进程池
                语法
                    multiprocess.Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])

                说明
                    processes: 要使用的进程数, 默认使用 os.cpu_count() 的值
                    initializer: 如果不为 None, 则每个工作进程将会在启动时调用 initializer(*initargs)
                    maxtasksperchild: 进程池的最多工作任务数,默认工作进程寿与池齐
                    context: 用于指定启动的工作进程的上下文.通常一个进程池是使用函数 multiprocessing.Pool() 或者一个上下文对象的 Pool() 方法创建的.

                    注意:进程池对象的方法只有创建它的进程能够调用
                    使用时一般只指定 processes 参数.

                常用方法:
                    apply(func[,args[,kwds]]): 使用 args 参数以及 kwds 命名参数同步调用 func,在返回结果前阻塞.
                        另外 func 只会在一个进程池中的一个工作进程执行
                    apply_async(func[, args[, kwds[, callback[, error_callback]]]]): 异步调用 func,并立即返回一个 AsyncResult 对象,不会阻塞
                        可以通过 callback 获取结果和通过 error_callback 处理异常
                    close(): 阻止后续任务提交到进程池,当所有任务执行完成后,工作进程会退出
                    terminate():不必等待未完成的任务,立即停止工作进程.当进程池对象被垃圾回收时,会立即调用 terminate().
                    join(): 阻塞主进程,等待工作进程结束.调用 join() 前必须先调用 close() 或者 terminate()

    进程间通信
        进程间不共享全局变量
            子进程向传入的列表中添加元素，最终发现主进程与子进程之间的列表结果不同
        使用 Queue 通信
            Python 的 multiprocessing 模块包装了底层的机制,提供了 Queue, Pipes 等多种方式交换数据
            multiprocessing.Queue([maxsize]) 返回一个使用一个管道和少量锁和信号量实现的共享队列(先进先出)实例.
                当一个进程将一个对象放进队列中时,一个写入线程会启动并将对象从缓冲区写入管道中.
                默认队列是无限大小的,可以通过 maxsize 参数限制.

            Queue 常用方法
                qsize(): 返回队列的大致长度,结果不可靠
                empty(): 判断队列是否为空,结果不可靠
                full(): 判断队列是否已满,结果不可靠
                put(obj[,block[,timeout]]): 将 obj 放入队列中
                    block: True | False
                        True:
                            timeout 为 None 时, 会阻塞当前进程,直至有空的缓存槽
                            timeout 为正数时, 阻塞最多 timeout 秒之后还是没有可用的缓冲区,抛出 queue.Full 异常
                        False:
                            仅当有可用的缓冲槽时,才会放入对象,否则抛出 queue.Full 异常(此时会忽略 timeout 参数)

                put_nowait(obj): 相当于 put(obj, False)
                get([block[, timeout]]): 从队列中取出并返回对象
                    block: True | False
                        True:
                            timeout 为 None 时, 会阻塞当前进程,直至有可用的对象
                            timeout 为正数时, 阻塞最多 timeout 秒之后还是没有可用的对象,抛出 queue.Empty 异常
                        False:
                            仅当有可用的对象能够被取出并返回,否则抛出 queue.Empty 异常(此时会忽略 timeout 参数)
                get_nowait(): 相当于 get(False)

            注意: multiprocessing.Queue存在兼容性问题，如果要使用进程池，可以使用Mananger().Queue

        进程池之间使用 Manager().Queue 通信

3.多线程
    线程
        线程是处理器任务调度和执行的基本单位
        一个进程至少有一个线程,也可以运行多个线程
        多个线程之间可共享数据
        线程运行出错异常后,如果没有捕获,会导致整个进程崩溃
        多线程是指在同一进程中同时执行多个任务

    创建
        threading.Thread 创建线程

        语法
            threading.Thread(group=None, target=None, name=None, args(), kwargs={}, *, daemon=None)
        说明
            group：应为 None，保留给将来实现 ThreadGroup 类的扩展使用。
            target：用于 run() 方法调用的可调用对象。默认是 None，表示不需要调用任何方法。
            name：线程名称。 在默认情况下，会以 “Thread-N” 的形式构造唯一名称，其中 N 为一个较小的十进制数值，或是 "Thread-N (target)" 的形式，其中 “target” 为 target.__name__，如果指定了 target 参数的话。
            args：用于发起调用目标函数的参数列表或元组。 默认为 ()。
            kwargs：用于调用目标函数的关键字参数字典。默认是 {}。
            daemon：True 或 False 来设置该线程是否为守护模式。如果是 None （默认值），线程将继承当前线程的守护模式属性。

        Thread 的属性和方法与其他常用方法
            name: 线程名
            daemon: 线程是否为守护线程
            ident: 线程标识符
            native_id: 此线程的线程 id(tid),由 OS(内核) 分配
            start(): 启动线程, 调用线程的 run() 方法
            run(): 定义线程的行为, 默认调用传入的 target 对象
            join([timeout=None]): 阻塞主线程,直至当前线程运行完成或达到超时时间
            is_alive(): 线程是否仍在运行
            threading.enumerate(): 查看有哪些线程
            threading.current_thread(): 返回当前线程实例

        创建方式
            threading.Thread()
            自定义 Thread 子类创建线程
                子类继承 thread.Thread,重写 run 方法
            线程池
                ThreadPoolExecutor 是 concurrent.futures 模块中的线程池实现,允许我们将任务提交到线程池,并管理任务的执行和结果

                语法
                    concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix="", initializer=None, initargs=())
                说明
                    max_workers：线程池的最大线程数（默认取决于系统资源）。
                    thread_name_prefix：线程名称前缀。
                    initializer：可选的初始化函数。
                    initargs：传递给初始化函数的参数。
                常用方法
                    submit(fn, *args, **kwargs): 提交一个任务到线程池,返回一个 Future 对象.可使用 Future.result() 获取任务结果
                    map(func, *iterables, timeout=None, chunksize=1):类似于内置 map() 函数,但在线程池中并行执行.Iterables 为可迭代对象,
                        传递给目标函数.chunksize 对 ThreadPoolExecutor 没有效果.
                    shutdown(wait=True,cancel_futures=False):关闭线程池,等待所有任务完成.
                        wait 表示是否等待线程池的所有线程完成任务
                        cancel_futures 表示是否取消尚未开始的任务.

        互斥锁
            线程安全问题
                线程之间共享数据会存在线程安全的问题

            互斥锁的概念
                某个线程要更改共享数据时,先将其锁定,此时其他线程不能更改该共享数据.直至该线程释放资源,将资源的状态变为"非锁定",
                    其他线程才能再次锁定该资源.
                互斥锁保证了每次只有一个线程进行写入操作,从而保证了多线程情况下数据的正确性

            互斥锁的使用
                通过 threading.Lock() 创建互斥锁
                使用 lock.acquire([blockint=True],[, timeout=-1])来获取锁
                    blocking 若为 True, 线程会阻塞直至获取到锁
                             若为 False, 线程立即返回.
                    获取锁成功返回 True,否则返回 False
                    timeout 为等待的超时时间,单位为秒.如果超时仍未获取到锁,返回 False
                使用 lock.release() 释放锁

        CIL
            Python 全局解释器(Global Interpreter Lock, 简称 CIL) 是一个锁, 同一时间只允许一个线程保持 Python 解释器的控制权.
            执行单线程程序时看不到 GIL 的影响,但它可能是 CPU 密集型和多线程代码的性能瓶颈.
            GIL 并不是 Python 的特性,它是实现 Python 解析器(CPython)时引入的一个概念
            GIL 的存在会对多线程的效率有不小的影响,甚至几乎等于 Python 是个单线程的程序.
            总之,当程序需要进行大量的 CPU 计算时, GIL 会成为性能的瓶颈. 即使有多个线程,GIL也会阻止它们在多个 CPU 核心上并行执行.
            实际上,多个线程会轮流获取 GIL,这样就不能真正并行地使用多个处理器核心.
            而对于 IO 操作(如文件读写,网络请求等)地程序, GIL 影响较小,因为在 IO 操作时,线程会释放 GIL,其他线程可以在此时执行,使得多线程在 IO 密集型任务中能够更有效地并发.


4.线程VS进程
                                                线程                                                                                  进程
    资源分配            共享所属进程的内存空间和资源,同一进程内的线程之间可用直接访问共享内存                             拥有独立的内存空间和系统资源,每个进程都有自己的代码段,数据段和堆栈等
    开销                 只需要在所属进程的内存空间内进行少量资源分配,开销较小                                                  需要分配独立的内存和系统资源,开销较大
    并发性(多核CPU)     在单核心 CPU 上是通过时间片轮转实现"伪异步".多核CPU上,因CPython的CIL存在,不是真正的异步                      多核CPU下,可以实现真正的异步操作
    独立性                 同一进程内的线程之间相互影响,一个线程出现问题可能导致整个进程崩溃                                 进程之间相互独立,一个进程的崩溃通常不会影响其他进程
    通信                  线程间通信相对简单,它们共享内存,可以直接访问共享变量                                            进程之间通信相对复杂,需要使用特殊的机制(如管道,消息队列,共享内存等)


    适用场景
        多线程:
            IO 密集型任务
            对资源共享要求高
        多进程:
            CPU 密集型任务
            需要隔离地任务