def call():
    print('calling someone')
    return 'call done'


class phone:
    price = 1200
    color = 'red'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print('calling one person')\
    
    def send_sms(self, phone, sms):
        text = f'sending sms to {phone} and message {sms}'
        return text

my_phone = phone()
print(my_phone.features)

print(my_phone.send_sms(123, 'i miss you'))