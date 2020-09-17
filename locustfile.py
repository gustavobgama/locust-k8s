#!/usr/bin/env python
# -*- coding: utf-8 -*-

from locust import HttpUser, task, between

class MyUser(HttpUser):
    @task
    def home(self):
        self.client.get("/")

    wait_time = between(5, 15)