## Creating a new django project

```python
$ django-admin startproject mysite
```

## Start the server

```python
$ python manage.py runserver
```

## Django Models

To create a new table:

1) Create a new class in models.py (Note: 1 app can have many table)
2) Specify relations, fields (Data Type)
3) python manage.py makemigrations [app_name]
4) python manage.py migrate --plan
5) python manage.py migrate

Voila! Your new column new added!

When jango run, it will run `settings.py` first.

(January - May 2023)
1. Complete 7 basic tutorials
2. Django Rest framework [https://www.django-rest-framework.org/tutorial/quickstart/](https://www.django-rest-framework.org/tutorial/quickstart/)
3. Graphin Framework Django 3.2 [https://docs.graphene-python.org/projects/django/en/latest/](https://docs.graphene-python.org/projects/django/en/latest/)
4. GraphQL

(June 2023)
5. Mini Project

(October 2023)
6. Portfolio Project 

Voila, graduate from DJango. 






# Idea Bucket
1. Bill Splitter


Command to check what file will get affected by migration.
```python
python manage.py migrate --plan
```





## References: 
- How to commit docker images after changes

```cmd
$ sudo docker ps -a
$ sudo docker commit [CONTAINER_ID] [new_image_name]
```




https://phoenixnap.com/kb/how-to-commit-changes-to-docker-image