import base64

x = 'ibc'
y = 'IBC'

encoded_small   = base64.b64encode(x)
encoded_cap     = base64.b64encode(y)

print encoded_small
print encoded_cap
