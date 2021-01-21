# Generators generate custom sequence of values but using yield function

def remote_control_next():
    yield 'a'
    yield 'b'

for r in remote_control_next():
    print(r)
##r = remote_control_next()
##print r.next()
##print r.next()
##print r.next()
