# Dumps KOTC2 character hoster data file - WIP to become an editor
#
# author: Zappastuff (a.k.a. ThyWoof)

import sys
import os
import argparse

def get_args():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('character_hoster_file', type=str)
    return my_parser.parse_args()

def get_number(stream, count):
    return int.from_bytes(stream.read(count), byteorder = 'little', signed = False)

def get_string(stream, count):
    r = stream.read(count).decode('ascii')
    stream.read(1) # bypass 0x00 terminator on strings
    return r

def dump_actor(stream):
    header_len = get_number(stream, 4)
    header = get_string(stream, header_len)
    print(header)

    level = get_number(stream, 1)
    print(f'INFO: Level: {level}')

    actor_name_len = get_number(stream, 4)
    actor_name = get_string(stream, actor_name_len)
    print(f'INFO: Name: {actor_name}')

    actor_name_len = get_number(stream, 4)
    actor_name = get_string(stream, actor_name_len)
    print(f'INFO: Name: {actor_name}')

    class_desc_len = get_number(stream, 4)
    class_desc = get_string(stream, class_desc_len)
    print(f'INFO: Description: {class_desc}')

    race_name_len = get_number(stream, 4)
    race_name = get_string(stream, race_name_len)
    print(f'INFO: Race: {race_name}')

    token_file_len = get_number(stream, 4)
    token_file = get_string(stream, token_file_len)
    print(f'INFO: Token: {token_file}')

    actor_type_len = get_number(stream, 4)
    actor_type = get_string(stream, actor_type_len)
    print(f'INFO: Type: {actor_type}')

    stream.read(4) # NO IDEA WHAT THAT IS

    gender_len = get_number(stream, 4)
    gender = get_string(stream, gender_len)
    print(f'INFO: Gender: {gender}')

    _class_len = get_number(stream, 4)
    _class = get_string(stream, _class_len)
    print(f'INFO: Class: {_class}')

    # need to check the right order here
    current_hp = get_number(stream, 4)
    max_hp = get_number(stream, 4)
    other_hp_data = get_number(stream, 4)

    # bypass these bytes I still need to make sense off
    stream.read(21)

    actor_str = get_number(stream, 1)
    actor_dex = get_number(stream, 1)
    actor_con = get_number(stream, 1)
    actor_int = get_number(stream, 1)
    actor_wiz = get_number(stream, 1)
    actor_cha = get_number(stream, 1)

    print(f'INFO: Attributes: {actor_str}/{actor_dex}/{actor_con}/{actor_int}/{actor_wiz}/{actor_cha}')

def dump_character_hoster(filename):
    with open(filename, 'rb') as stream:
        actor_count = get_number(stream, 4)
        print(f'INFO: found {actor_count} actors on character hoster')
        # for actor in range(actor_count):
            # print(f'INFO: starting dump actor {actor+1}')
        dump_actor(stream)
    
def main():
    args = get_args()
    if args.dump:
        dump_character_hoster(args.character_hoster_file)

if __name__ == '__main__':
    main()