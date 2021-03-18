class UserSchema:
    def __init__(self, mobile_number, user_id, email_verified=False, mobile_number_verified=False):
        self.mobile_number = mobile_number
        self.user_id = user_id
        self.email_verified = email_verified
        self.mobile_number_verified = mobile_number_verified

    def __repr__(self):
        return f'User(mobile_number={self.mobile_number},user_id={self.user_id},email_verified={self.email_verified},mobile_number_verified={self.mobile_number_verified}) '

    def to_dict(self):
        user_object = {
            u'mobile_number': self.mobile_number,
            u'mobile_number_verified': self.mobile_number_verified,
            u'email_verified': self.email_verified,
            u'user_id': self.user_id
        }

        if self.mobile_number:
            user_object[u'mobile_number'] = self.mobile_number

        if self.mobile_number_verified:
            user_object[u'mobile_number_verified'] = self.mobile_number_verified

        if self.email_verified:
            user_object[u'email_verified'] = self.email_verified

        if self.user_id:
            user_object[u'user_id'] = self.user_id

        return user_object
