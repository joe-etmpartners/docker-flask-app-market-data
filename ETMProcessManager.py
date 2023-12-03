import threading
from time import sleep


def nullProcess(thisProcess, **kwargs):
    thisProcess.set_status('Running')
    print('nullProcess called with kwargs: {}'.format(kwargs))

    iterations = kwargs['iterations']
    delay = kwargs['delay']

    for i in range(iterations):
        thisProcess.set_status('Running iteration {}'.format(i))
        thisProcess.set_progress(((i+1)*100)/iterations)
        sleep(delay)

    sleep(3)
    thisProcess.set_status('Finishing')
    sleep(3)
    print('nullProcess completed successfully')
    return ("nullProcess completed successfully")

class ETMProcess(object):
    """
    This is the base class for all ETM processes.
    """
    def __init__(self, process_name, process_description, function, **kwargs):
        self.process_name = process_name
        self.process_description = process_description
        self.function = function
        self.kwargs = kwargs
        self.status = 'Zero-State'
        self.progress = 0
        self.last_run_result = None
        self.lock = threading.Lock()

    def info(self):
        """
        This method is called to get the info of the process.
        """
        self.lock.acquire()
        rtn = { 'name': self.process_name, 
                'description': self.process_description, 
                'status': self.status, 
                'kwargs': self.kwargs, 
                'progress': self.progress, 
                'last_run_result': self.last_run_result
                }
        self.lock.release()
        return rtn
    
    def set_status(self, status):
        """
        This method is called to set the status of the process.
        """
        self.lock.acquire()
        self.status = status
        self.lock.release()
        pass

    def get_status(self):
        """
        This method is called to get the status of the process.
        """
        self.lock.acquire()
        status = self.status
        self.lock.release()
        return status
    
    def set_progress(self, progress):
        """
        This method is called to set the progress of the process.
        """
        self.lock.acquire()
        self.progress = progress
        self.lock.release()
        pass

    def get_progress(self):
        """
        This method is called to get the progress of the process.
        """
        self.lock.acquire()
        progress = self.progress
        self.lock.release()
        return progress

    def run(self):
        """
        This method is called to run the process.
        """
        self.set_status('About to start')

        last_run_result=self.function(self, **self.kwargs)

        self.lock.acquire()
        self.last_run_result = last_run_result
        self.lock.release()

        self.set_status('Stopped')
        pass

    


    # def get_start_time(self):
    #     """
    #     This method is called to get the start time of the process.
    #     """
    #     pass

    # def get_end_time(self):
    #     """
    #     This method is called to get the end time of the process.
    #     """
    #     pass

    # def get_last_run_time(self):
    #     """
    #     This method is called to get the last run time of the process.
    #     """
    #     pass

    # def get_last_run_exit_status(self):
    #     """
    #     This method is called to get the last run status of the process.
    #     """
    #     pass

    # def get_last_run_duration(self):
    #     """
    #     This method is called to get the last run duration of the process.
    #     """
    #     pass


class ETMProcessManager(object):

    etm_processes = []
    lock = threading.Lock()

    def __init__(self):
        pass

    def register_process(self, process):
        """
        Registers a process with the process manager.
        """
        self.lock.acquire()
        self.etm_processes.append(process)
        self.lock.release()

    def run_process(self, process_name):
        """
        Runs a process in a separate
        """
        self.lock.acquire()
        for process in self.etm_processes:
            if process.process_name == process_name:
                new_thread = threading.Thread(target=process.run, args=())
                new_thread.start()
                self.lock.release()
                return True
        self.lock.release()
        return False
    
    def get_all_process_info(self):
        """
        Returns a list of dictionaries containing the info for each process.
        """
        rtn = []
        self.lock.acquire()
        for process in self.etm_processes:
            rtn.append(process.info())
        self.lock.release()
        return rtn

if __name__ == '__main__':
    print('This is the ETMProcessManager module.')
    print('It is not meant to be run directly.')
    print('Running units tests instead.')

    pm = ETMProcessManager()
    process1 = ETMProcess('Process1', 'This is process 1', nullProcess, iterations=50, delay=1)
    process2 = ETMProcess('Process2', 'This is process 2', nullProcess, iterations=20, delay=3)

    pm.register_process(process1)
    pm.register_process(process2)

    print('All process info: {}'.format(pm.get_all_process_info()))
    sleep(1)

    print('Process 1 info: {}'.format(process1.info()))
    print('Process 2 info: {}'.format(process2.info()))

    print('About to start process 1')
    pm.run_process('Process1')

    print('About to start process 2')
    pm.run_process('Process2')

    from pprint import pprint
    for i in range(30):
        pprint(pm.get_all_process_info())
        sleep(2)



