from locust import task, between, SequentialTaskSet, FastHttpUser
from common.logger_handler import get_logger
from common.prometheus_exporter import usernames
from common.redis_store import redis_store

logger = get_logger('chenqg', file=True)


class RedisTest(SequentialTaskSet):
    # item = {}

    @task
    def login(self):
        username = self.user.username
        redis_store.set(f"{username}1", "6FB9AED05F10D1EA18C39498E10AA519")
        redis_store.set(f"{username}2", "6FB9AED05F10D1EA18C39498E10AA519")
        redis_store.set(f"{username}3", "6FB9AED05F10D1EA18C39498E10AA519")
        redis_store.set(f"{username}4", "6FB9AED05F10D1EA18C39498E10AA519")
        redis_store.set(f"{username}5", "6FB9AED05F10D1EA18C39498E10AA519")

        redis_store.get(f"{username}1")
        redis_store.get(f"{username}2")
        redis_store.get(f"{username}3")
        redis_store.get(f"{username}4")
        redis_store.get(f"{username}5")


class RedisTestUser(FastHttpUser):
    wait_time = between(1, 3)
    host = "https://www.baidu.com"

    # pool = redis.ConnectionPool(host='123.123.123.123', port=6379, password='password', db=0)
    # redis_store = redis.Redis(connection_pool=pool, decode_responses=True)
    def __init__(self, parent):
        self.username = usernames.pop()
        super().__init__(parent)

    tasks = [RedisTest]
