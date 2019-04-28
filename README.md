ToDo app for learning Django
---
```shell
git clone https://github.com/190ikp/learnning-django.git
cd learning-django
docker-compose run app python manage.py migrate todo
docker-compose up -d
```
then access http://localhost:8000/ .

## Issue
- タスク追加・編集時，期限の入力で`2019-04-29 23:59`のように決まったフォーマットで入力しないといけない
  adminサイトみたいにカレンダーから選べるようにしたい
- ToDoの編集ページが開けない(NoReverseMatchエラー)
- WebPush実装