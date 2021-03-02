# BigPy

A Python Library designed to interact with iControl REST API and provide OOP principles to access various F5 Objects 

## Features

### F5 LTM Objects are now Python Objects

#### Example - Get all Virtual Servers
```py
import bigpy

my_f5 = bigpy.Bigip(address="127.0.0.1")

virtual_cursor = my_f5.ltm.Virtual()
for virtual in virtual_cursor.get_virtual_servers:
    print(virtual.destination)
    print(virtual.generation)
    ...etc


>> "/Common/127.0.0.1:443"
>> 87938
>>> ...etc
```

#### Example - Get a specified Virtual Server

```py
import bigpy

my_f5 = bigpy.Bigip(address="127.0.0.1")

virtual_cursor = my_f5.ltm.Virtual()
virtual = virtual_cursor.get_virtual_server("/Common/VirtualServerName")

print(virtual.destination)
print(virtual.generation)
...etc

>> "/Common/127.0.0.1:443"
>> 87938
>>> ...etc
```

##### Supported LTM Objects

bigpy.Bigip.ltm.Virtual
bigpy.Bigip.ltm.Pool
