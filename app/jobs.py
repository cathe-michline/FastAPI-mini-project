from apscheduler.schedulers.background import BackgroundScheduler
from app.database import SessionLocal
from app import models

def update_tasks():
    db = SessionLocal()
    tasks = db.query(models.Task).filter(models.Task.status == "pending").all()

    for task in tasks:
        task.status = "completed"

    db.commit()
    db.close()

scheduler = BackgroundScheduler()
scheduler.add_job(update_tasks, "interval", seconds=60)
scheduler.start()