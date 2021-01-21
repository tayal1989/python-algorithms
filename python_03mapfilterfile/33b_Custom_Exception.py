class OverTheLimitException(Exception):
    def __init__(self, msg):
        self.msg = msg

def withdrawal(amount):
    try:
        if amount > 500:
            raise OverTheLimitException("You are not allowed to enter more than 500")
    except OverTheLimitException:
                print("Value entered is larger than 500")

withdrawal(501)
