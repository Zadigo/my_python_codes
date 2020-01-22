from apscheduler.schedulers.blocking import BlockingScheduler

def test():
    pass

schedule = BlockingScheduler()
schedule.add_job(test, minutes=15)
schedule.start()
schedule.shutdown()