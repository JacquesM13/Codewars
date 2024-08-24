'''
Description:

Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.
Examples

* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246
'''

# My solution
def ips_between(start, end):
    output = []
    sum = 0
    start = start.split('.')
    end = end.split('.')
    for i in range(len(start)):
        output.append(int(end[i]) - int(start[i]))
    
    for i in range(len(output)):
        if i == 0:
            output[i] = output[i] * 256 * 256 * 256
        if i == 1:
            output[i] = output[i] * 256 * 256
        if i == 2:
            output[i] = output[i] * 256
    for i in output:
        sum += i
    return sum

'''
Good solution(s)

from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))


def ips_between(start, end):
    a = sum([int(e)*256**(3-i) for i, e in enumerate(start.split('.'))])
    b = sum([int(e)*256**(3-i) for i, e in enumerate(end.split('.'))])
    return abs(a-b)
'''
