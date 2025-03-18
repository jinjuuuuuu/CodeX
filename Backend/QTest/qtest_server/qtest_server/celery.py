import os
from celery import Celery

# Django의 settings 모듈을 Celery의 기본 설정으로 사용
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qtest_server.settings')

# Celery 앱 생성
celery_app = Celery('qtest_server')

# 설정을 Django의 settings에서 가져오도록 지정 (CELERY_ 로 시작하는 설정을 자동으로 가져옴)
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# 등록된 앱에서 task를 자동으로 탐색
celery_app.autodiscover_tasks()

@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')