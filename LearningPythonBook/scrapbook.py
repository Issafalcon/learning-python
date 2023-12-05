#!/usr/bin/python3

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')

if not 'height' in bob:
    print('missing height, adding')
    bob['height'] = 100

# Sort the keys
for key in sorted(bob):
    print(key, '=>', bob[key])
