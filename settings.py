#coding=utf-8


host_config = {

    "hosts": [{
        'db': 'youku_mobile_user', # Or path to database file if using sqlite3.
        'user': 'root', # Not used with sqlite3.
        'passwd': '', # Not used with sqlite3.
        'host': 'localhost', # Set to sempty string for localhost. Not used with sqlite3.
        'port': 3306, # Set to empty string for default. Not used with sqlite3.
        'init_command': 'SET storage_engine=INNODB;set SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED; set autocommit=0;set  names "utf8";'
        ,
        'partitions': [1, 2],
        },
            {
            'db': 'youku_mobile_user', # Or path to database file if using sqlite3.
            'user': 'test', # Not used with sqlite3.
            'passwd': 'test', # Not used with sqlite3.
            'host': '10.10.140.27', # Set to sempty string for localhost. Not used with sqlite3.
            'port': 3306, # Set to empty string for default. Not used with sqlite3.
            'init_command': 'SET storage_engine=INNODB;set SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED; set autocommit=0;set  names "utf8";'
            ,
            'partitions': [1, 2],
            },
            {
            'db': 'youku_mobile_user', # Or path to database file if using sqlite3.
            'user': 'test', # Not used with sqlite3.
            'passwd': 'test', # Not used with sqlite3.
            'host': '10.10.116.88', # Set to sempty string for localhost. Not used with sqlite3.
            'port': 3306, # Set to empty string for default. Not used with sqlite3.
            'init_command': 'SET storage_engine=INNODB;set SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED; set autocommit=0;set  names "utf8";'
            ,
            'partitions': [1, 2],
            },
         ]
}

old_host_config = {
    "hosts": [{
        'db': 'youku_mobile_user', # Or path to database file if using sqlite3.
        'user': 'root', # Not used with sqlite3.
        'passwd': '', # Not used with sqlite3.
        'host': 'localhost', # Set to sempty string for localhost. Not used with sqlite3.
        'port': 3306, # Set to empty string for default. Not used with sqlite3.
        'init_command': 'SET storage_engine=INNODB;set SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED; set autocommit=0;set  names "utf8";'
        ,
        'partitions': [1, 2],
        },
            {
            'db': 'youku_mobile_user', # Or path to database file if using sqlite3.
            'user': 'test', # Not used with sqlite3.
            'passwd': 'test', # Not used with sqlite3.
            'host': '10.10.140.27', # Set to sempty string for localhost. Not used with sqlite3.
            'port': 3306, # Set to empty string for default. Not used with sqlite3.
            'init_command': 'SET storage_engine=INNODB;set SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED; set autocommit=0;set  names "utf8";'
            ,
            'partitions': [1, 2],
            },
         ]
}

rebalance_db_table = "user_home_layout"