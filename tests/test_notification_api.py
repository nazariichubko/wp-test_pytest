import pytest
import requests
import json

with open('test.json') as json_file:
    data_file = json.load(json_file)

def test_login_student():
    """Return token for student type user"""
    data = dict(email='ncteststudent3@mailinator.com', password='Qwerty1!')
    response = requests.post('https://dev.api.teachme.com.ua/v1/login', data)
    res = response.json()
    clean_token = res['data']['token']
    print(f'Student token is: {clean_token}')

def test_get_student_lessons():
    """Generate student's link to enter lessonn room."""
    clean_token = '5024|sPrnP31mZRtQnJCmfbMprwQhSVmkRaFXRFB8wCgu'
    users_token = f'Bearer {clean_token}'
    response = requests.get(
        'https://dev.api.teachme.com.ua/v1/profile/student/lessons',
        params= {'date': '2022-07-21'},
        headers={'accept':'application/json','Authorization': users_token })
    print(response.content)
    res = response.json()
    lesson_val = res[8]
    lesson_uuid = lesson_val['uuid']
    print(f'https://dev.lesson.teachme.com.ua/init/{clean_token}:{lesson_uuid}')

def test_login_tutor():
    """Return tutor's security token."""
    data = dict(email='nctesttutor5@mailinator.com', password='Qwerty1!')
    response = requests.post('https://dev.api.teachme.com.ua/v1/login', data)
    res = response.json()
    token = res['data']['token']
    print(f'Tutor token is: {token}')

def test_get_tutors_lessons():
    """Generate tutor's link to enter lesson room."""
    clean_token = '5025|KOQ9LegK6hmthvoEiOfcKK4I7Thp6Lqax5QJ0Dde'
    users_token = f'Bearer {clean_token}'
    response = requests.get(
        'https://dev.api.teachme.com.ua/v1/profile/tutor/lessons',
        params= {'date': '2022-07-21'},
        headers={'accept':'application/json','Authorization': users_token })
    print(response.content)
    res = response.json()
    lesson_val = res[0]
    lesson_uuid = lesson_val['uuid']
    print(f'https://dev.lesson.teachme.com.ua/init/{clean_token}:{lesson_uuid}')

def test_notifications():
    "Return user's notifications settings"
    clean_token = '4426|n5PTZ5eUdbwRspX9pgvUvKaX1M5flHi3Agq5K4bQ'
    users_token = f'Bearer {clean_token}'
    response = requests.get('https://dev.api.teachme.com.ua/v1/profile/notifications',
                            headers={'accept':'application/json', 'Authorization': users_token})
    print(response.text)
    print(response.status_code)




