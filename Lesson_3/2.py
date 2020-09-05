def user_detail(**kwargs):
    for key, val in kwargs.items():
        print(val, end=" ")
    return


user_detail(name='Иван', surname='Иванов', birthday='01.01.2000', city='Moscow', email='iv@iv.com', phone='999111111')
