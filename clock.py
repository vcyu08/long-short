from apscheduler.schedulers.blocking import BlockingScheduler
from long_short import LongShort

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=9, minute=57, timezone='US/Eastern')
def timed_job():
	print("Start Long-short...")
	ls = LongShort()
	ls.run()
	print("End Long-short...")

sched.start()