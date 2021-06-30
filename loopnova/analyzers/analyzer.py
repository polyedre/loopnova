#!/usr/bin/env python3

def discover_ports(target, controller):
    print(f"Scanning {target}")
    last_digit = target.split('.')[-1]
    try:
        number = int(last_digit)
        if number % 2 == 0:
            controller.add_target('ip', f'666.666.666.{number+1}')
    except TypeError as error:
        print(error)