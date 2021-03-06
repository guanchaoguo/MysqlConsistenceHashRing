#coding=utf-8
from  consistent import MysqlHashClient
from settings import host_config
import time
import logging

class BaseLayout(object):
    #mysql consistence ring static class object
    client = MysqlHashClient(host_config)
    #mysql table name must extent
    TABLE_NAME = ""

    def __init__(self, guid, value):
        self.guid = guid
        self.value = value

    def set(self):
        return self.client.set(key=self.guid,\
                        value=self.value, table_name=self.TABLE_NAME)

    @classmethod
    def delete(cls, guid):
        return cls.client.delete(guid, table_name=cls.TABLE_NAME)


    @classmethod
    def get(cls, guid):
        return cls.client.get(guid, table_name=cls.TABLE_NAME)


class UserHomeLayout(BaseLayout):
    TABLE_NAME = "user_home_layout"
    
    def __init__(self, guid, value):
        super(UserHomeLayout, self).__init__(guid, value)


class UserChannelLayout(BaseLayout):
    TABLE_NAME = "user_channel_layout"
    
    def __init__(self, guid, value):
        super(UserChannelLayout, self).__init__(guid, value)


if __name__ == "__main__":

    now = time.time()
    guid = "35aee8e85ffb518e70e44ee06bcc4479"
    value = [1, 2, 3, 4]
    user_layout = UserHomeLayout(guid, value)
    print "initial use:", time.time() - now

    now = time.time()
    user_layout.set()
    print "set use:", time.time() - now
    print "result:", UserHomeLayout.get(guid)

    now = time.time()
    value = [1, 2, 3, 6]
    user_layout = UserHomeLayout(guid, value)
    user_layout.set()
    print "set dup use:", time.time() - now

    now = time.time()
    print "result:", UserHomeLayout.get(guid)
    print "get use:", time.time() - now

    now = time.time()
    UserHomeLayout.delete(guid)
    print "del use:", time.time() - now

    now = time.time()
    print "result:", UserHomeLayout.get(guid)
    print "get use:", time.time() - now
