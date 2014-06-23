#!/usr/bin/env python3
import binascii
import re
import os
import sys
 
def new_text2bin(mtext):
        result = [ bin(ord(ch))[2:].zfill(8) for ch in mtext ]
        return ''.join(result)
 
def switch_bit(bit, my_list ):
        result_list = my_list[:]
        if result_list[bit] == '1':
                result_list[bit] = '0'
        else:
                result_list[bit] = '1'
        return result_list
 
def generate_similar( domain ):
        domains = []
        domain_list = list(domain)
        for i in range(len(domain)):
                print(switch_bit(i, domain_list))
        return domains
 
def binstr_to_ascii( binstr ):
        binstr = -len(binstr) % 8 * '0' + binstr
        string_blocks = (binstr[i:i+8] for i in range(0, len(binstr), 8))
        string = ''.join(chr(int(char, 2)) for char in string_blocks)
        return string
 
if len(sys.argv) != 2:
        sys.exit("Not enough args")
else:
        domain=str(sys.argv[1])
 
        domain_list = list(new_text2bin(domain))
 
        for i in range(len(domain_list)):
                new_d = (''.join(switch_bit(i, domain_list)))
 
                new_d_str = binstr_to_ascii(new_d)
                corect_domain = re.match("^(((([a-z0-9]+){1,63}\.)|(([a-z0-9]+(\-)+[a-z0-9]+){1,63}\.))+){1,255}$", new_d_str + "." )
 
                if ( corect_domain is not None and len(corect_domain.string) > 1 and (corect_domain.string).index(".") < len(corect_domain.string)-1 ):
                        print(new_d_str, end="\n")
 
        print(" ")