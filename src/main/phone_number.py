# Created by Leon Hunter at 9:54 AM 10/23/2020
import re

class PhoneNumber(object):
    def __init__(self, phone_number):
        regex_string = "\\(\\d{3}\\)-\\d{3}-\\d{4}" # validate phone number with format `(###)-###-####`
        regex_pattern = re.compile(regex_string)
        if not regex_pattern.match(phone_number):
            raise ValueError("save must be True if recurse is True")
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number