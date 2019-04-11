Script backup mysql sử dụng python3

# Yêu cầu 
- Ubuntu / CentOS
- python 3
- git 
- crontab
- rsync (optional)

# Tính năng 

- Backup mysql database.
- Gửi thông báo backup đến Slack, Telegram, Email
- Tự động sync đến FTP server.
- Xóa các folder backup cũ trong vòng **x** ngày

# Ví dụ (Thực hiện trên CentOS 7)

### 1. Cài đặt các gói cần thiết

```
yum groupinstall "Development Tools" -y
yum install git -y
```

### 2. Cài đặt python 3.6

```
yum install https://centos7.iuscommunity.org/ius-release.rpm -y
yum install python-devel -y
yum install python36-devel -y
yum install python36 -y

yum install python-pip -y
yum install python36u-pip -y
pip3.6 install virtualenv
```

### 3. Clone repo

```
cd /opt/
https://github.com/nhanhoadocs/backup-mysql-with-python3.git
```

### 4. Tạo virtual environmet và cài đặt thư viện cần thiết

```
cd /opt/backup_mysql
virtualenv env
source env/bin/activate
pip install -r requirement.txt
```

### 5. Sửa file setting

> Một số ví dụ setting mẫu tại đây: [Ví dụ](https://github.com/nhanhoadocs/backup-mysql-with-python3/blob/master/example/example.md)

Sửa file setting tại  `/opt/backup_mysql/settings/settings.json`. Trong đó

```json
{
    "mysql": {
        "user": "MYSQL_USER",
        "password": "MYSQL_PASSWORD",
        "backup_type": "table", 
        "database": "MYSQL_DATABASE",
        "tables": "table1, table2, table3"
    },
    "backup": {
        "backup_folder": "/your/backup/folder",
        "backup_file_name": "your_back_up_file_name"
    },
    "delete_old_file": {
        "delete_old_file": true,
        "remove_days": 10
    },
    "sync": {
        "sync": false,
        "ftp_server": "10.10.10.10",
        "remote_sync_path": "/backup/folder/in/ftp/server"
    },
    "telegram": {
        "send_notify": true,
        "token": "your_telegram_token",
        "chat_id": "your_telegram_chat_id"
    },
    "slack": {
        "send_notify": true,
        "token": "your_slack_token",
        "channel": "your_slack_channel"
    },
    "email": {
        "send_notify": true,
        "smtp_server": "your_smtp_server",
        "smtp_user": "your_user_email@your_smtp_server",
        "smtp_password": "your_email_password",
        "smtp_from": "This is sender <your_user_email@your_smtp_server>",
        "smtp_TLS": true,
        "smtp_port": 587,
        "email_subject": "Test backup report {}",
        "receiver_email": "to_email"
    }
}
```

(Trong đó)

**a. backup_type - setting của các loại backup_type (kiểu backup) gồm:**

- all : `Backup tất cả database.`

- database : `Backup một database.`

- table : `Backup một (hoặc nhiều) table.`

**b. Tính năng mở rộng - setting của các tính năng mở rộng gồm:**

- "sync": true / false 

    ```
    Có hoặc không sync dữ liệu. Nếu chọn true, 2 server phải được cài đặt rsync và phải SSH less không cần password với nhau.
    ```

- "send_notify": true / false 

    ```
    Có hoặc không gửi thông báo Slack hoặc Telegram.
    ```

- "delete_old_file": true / false

    ```
    Có hoặc không xóa các file backup cũ trên server chạy script. Nếu có, xóa trong vòng "remove_days" ngày.
    ```


### 6. Thêm script vào crontab

```
crontab -e
```

Thêm crontab, chú ý đường dẫn của `env` và file `run_backup.py`


```
0 */2 * * * source /opt/backup_mysql/env/bin/activate && python /opt/backup_mysql/run_backup.py
```

