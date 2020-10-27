def remote_control_next():
    yield 'a'
    yield 'b'

for r in remote_control_next():
    print(r)
r = remote_control_next()
print(r.__next__())
print(r.__next__())
print(r.__next__())
