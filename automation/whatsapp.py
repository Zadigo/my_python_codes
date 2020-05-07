from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers import blocking

def test():
    print('Great')

# schedule = BlockingScheduler()
# schedule.add_job(test, minutes=1)
# schedule.start()
# schedule.shutdown()

s = blocking.BlockingScheduler()
s.add_job(test, 'interval', seconds=3)
s.start()
s.shutdown()