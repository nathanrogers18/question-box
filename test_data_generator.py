import requests

URL = 'http://127.0.0.1:8000/api/'


def create_test_data(user1, user2):
    create_user_profile(user1)
    create_user_profile(user2)
    create_tags()
    create_questions(user1, user2)
    create_answers(user1, user2)
    create_comments(user1, user2)
    return


def create_user_profile(user):
    data = {
        'user': user['id'],
        'score': 0
    }
    url = URL + 'user/'
    requests.post(url, data)
    print("User profiles created")
    return


def create_tags():
    data1 = {'topic': 'django'}
    data2 = {'topic': 'python'}
    data3 = {'topic': 'sharks'}
    url = URL + 'tag/'
    requests.post(url, data1)
    requests.post(url, data2)
    requests.post(url, data3)
    print("Tags created")
    return


def create_questions(user1, user2):
    data1 = {
        'user': user1['id'],
        'title': 'Are sharks superior to tigresses?',
        'text': 'Asking for a friend.',
        'tag': 'sharks',
    }
    data2 = {
        'user': user2['id'],
        'title': 'When is the best time to use the Druyvestian model?',
        'text': "I normally use a maxwell-boltzmann distribution. When would I not?",
        'tag': 'python',
    }
    url = URL + 'question/'
    requests.post(url, data1)
    requests.post(url, data2)
    print("Questions created")
    return


def create_answers(user1, user2):
    data1 = {
        'user': user2['id'],
        'question': 1,
        'text': 'Definitely. Tigresses are lame.',
    }
    data2 = {
        'user': user1['id'],
        'question': 2,
        'text': "Primarily for low-pressure plasma regimes. the maxwell-boltzmann distribution will take care of the rest."
    }
    url = URL + 'answer/'
    requests.post(url, data1)
    requests.post(url, data2)
    print("Answers created")
    return


def create_comments(user1, user2):
    data1 = {
        'user': user2['id'],
        'question': 1,
        'text': 'Is this the appropriate place?'
    }
    data2 = {
        'user': user1['id'],
        'answer': 1,
        'text': "Yeah, you're right. Thanks."
    }
    url = URL + 'comment/'
    requests.post(url, data1)
    requests.post(url, data2)
    print("Comments created")
    return


def main():
    user1 = {'id': 1}
    user2 = {'id': 2}
    create_test_data(user1, user2)
    print("Data created.")

if __name__ == '__main__':
    main()
