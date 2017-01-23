#!/usr/bin/env python

ip_address = raw_input("Please enter IP address: ")
ip_address = ip_address.split(".")

print
print "{:<12} {:<12} {:<12} {:<12}".format(*ip_address)
print

