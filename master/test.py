class MasterBOOMER(object):
    """
    Runner used to run distributed load tests across multiple processes and/or machines.

    MasterRunner doesn't spawn any user greenlets itself. Instead it expects
    :class:`WorkerRunners <WorkerRunner>` to connect to it, which it will then direct
    to start and stop user greenlets. Stats sent back from the
    :class:`WorkerRunners <WorkerRunner>` will aggregated.
    """

    def __init__(self, environment, master_bind_host, master_bind_port):
        """
        :param environment: Environment instance环境实例
        :param master_bind_host: Host/interface to use for incoming worker connections主机地址
        :param master_bind_port: Port to use for incoming worker connections主机接口
        """

        self.worker_cpu_warning_emitted = False
        self.master_bind_host = master_bind_host
        self.master_bind_port = master_bind_port
        #嵌套类，这个类可以被作为一个方法被父类调用
        class WorkerNodesDict(dict):
            def get_by_state(self, state):
                return [c for c in self.values() if c.state == state]

            @property
            def all(self):
                return self.values()

            @property
            def ready(self):
                return self.get_by_state(STATE_INIT)

            @property
            def spawning(self):
                return self.get_by_state(STATE_SPAWNING)

            @property
            def running(self):
                return self.get_by_state(STATE_RUNNING)

            @property
            def missing(self):
                return self.get_by_state(STATE_MISSING)

        self.clients = WorkerNodesDict()
        print(dir(self.clients))
if __name__ == '__main__':
    e = []
    runner = MasterBOOMER(e,'127.0.0.1','8989')
        
    