from locust import HttpLocust, TaskSet, task

class UserTasks(TaskSet):

    @task
    def index(self):
        self.client.get("/?p=1") # Realiza um get na url <HOST_DO_WORDPRESS>/?p=1


class WebsiteUser(HttpLocust):
    task_set = UserTasks