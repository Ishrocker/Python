import socket
import time


def ping(host, port=80, timeout=5):
    '''
    Simple ping of a host:port

    params:
    host <str>: a string representation of the host
          for example and IP address or domain name.
          127.0.0.1 or www.google.com
    port <int>: The port of the host.
    timeout <int>: the amount of seconds to wait before
            the socket closes the connection and raises
            a TimeoutError.
    '''
    
    s = socket.socket()
    s.settimeout(timeout)
    end = None
    start = time.time()
    try:
        s.connect((host, port))
    except TimeoutError as e:
        print(e)
    except OSError as e:
        print(e)
    finally:
        end = time.time()
        s.shutdown(socket.SHUT_RDWR)
        s.close()


    end = time.time()
    ms = 1000 * (end - start)
    return round(ms, 2)
