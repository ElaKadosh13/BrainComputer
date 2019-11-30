import socket   
import struct
import time
import calendar

from braincomputer.cli import CommandLineInterface

cli = CommandLineInterface()

def pack_message_protocol(user_id, thought):
    struct_obj = struct.Struct('LLI') 
    time_stamp = calendar.timegm(time.gmtime())
    return struct_obj.pack(user_id, time_stamp, len(thought))   

@cli.command
def upload_thought(address, user, thought):
    connection = socket.socket()
    tuple_address = address.split(":")
    arg_address = (tuple_address[0], int(tuple_address[1]))
    connection.connect(arg_address)
    message_protocol = pack_message_protocol(int(user), thought)
    message = message_protocol + thought.encode()
    connection.sendall(message)
    print("done")
    connection.close()

def main(argv):
    cli.main()


if __name__ == '__main__':
    import sys
    cli.main()
    sys.exit()
