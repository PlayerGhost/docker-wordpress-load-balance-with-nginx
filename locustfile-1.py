from locust import HttpUser, TaskSet, task

BASE_URL = 'http://localhost:80'

file_300kb = '/2022/05/14/300kb/'
file_400kb = '/2022/05/14/400kb/'
file_1mb = '/2022/05/14/1mb/'

class DockerUser(HttpUser):
    @task(1)
    def post_1mb_img(self):
        self.client.get(BASE_URL + file_1mb)