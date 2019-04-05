
## Ví dụ cho setting

### 1 Ví dụ Backup **tất cả** database và **xóa** các file trong vòng 10 ngày: 

```
...
    "mysql": {
        "user": "MYSQL_USER",
        "password": "MYSQL_PASSWORD",
        "backup_type": "all", 
    ...

    "delete_old_file": {
        "delete_old_file": true,
        "remove_days": 10
    },
```

### 2. Ví dụ Backup 1 database và gửi thông báo đến slack:

```
...
    "mysql": {
        "user": "MYSQL_USER",
        "password": "MYSQL_PASSWORD",
        "backup_type": "database",
        "database": "my_database",
        "tables": ""
    ...
    
    "slack": {
        "send_notify": true,
        "token": "your_slack_token",
        "channel": "your_slack_channel"
    }
```

### 3. Ví dụ Backup 3 table, sync sang ftp server, gửi thông báo đến telegram

```
...
    "mysql": {
        "user": "MYSQL_USER",
        "password": "MYSQL_PASSWORD",
        "backup_type": "table",
        "database": "my_database",
        "tables": "table1, table2, table3"
    ...

    "sync": {
        "sync": true,
        "ftp_server": "10.10.10.10",
        "remote_sync_path": "/backup/folder/in/ftp/server"
    },

    ...
    "telegram": {
        "send_notify": true,
        "token": "your_telegram_token",
        "chat_id": "your_telegram_chat_id"
    },
```

### 4. Ví dụ Backup 1 table, gửi thông báo đến telegram, không gửi thông báo đến slack

```
...
    "mysql": {
        "user": "MYSQL_USER",
        "password": "MYSQL_PASSWORD",
        "backup_type": "table",
        "database": "my_database",
        "tables": "table1, table2, table3"
    ...

    "sync": {
        "sync": true,
        "ftp_server": "10.10.10.10",
        "remote_sync_path": "/backup/folder/in/ftp/server"
    },

    ...
    "telegram": {
        "send_notify": true,
        "token": "your_telegram_token",
        "chat_id": "your_telegram_chat_id"
    },
    ...

    "slack": {
        "send_notify": false,
        "token": "your_slack_token",
        "channel": "your_slack_channel"
    }
```
