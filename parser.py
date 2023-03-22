

def parse_message(msg):
    m_number = None
    f_number = None
    for i in range(len(msg)):
        if msg[i] == 'm':
            try:
                m_number = int(msg[i+1])
            except (ValueError, IndexError):
                print("Error: Invalid number after 'm'")
        elif msg[i] == 'f':
            try:
                f_number = int(msg[i+1])
            except (ValueError, IndexError):
                print("Error: Invalid number after 'f'")
    return m_number, f_number


def is_forwarded(id_gen, id_fwd):
    if id_gen != id_fwd:
        return True
    else:
        return False


def update_stats(generator, forwarder, _json,shrange):
    if shrange == 'c' or shrange == 'C':        
        if is_forwarded(generator, forwarder):
            _json["forward"][forwarder] += 1
        else:
            _json["regular"][forwarder] += 1
    elif shrange == 'a' or shrange == 'A':        
        if is_forwarded(generator, forwarder):
            _json["forward"][forwarder-1] += 1
        else:
            _json["regular"][forwarder-1] += 1
    elif shrange == 'b' or shrange == 'B':        
        if is_forwarded(generator, forwarder):
            _json["forward"][bool(forwarder)] += 1
        else:
            _json["regular"][bool(forwarder)] += 1
    

    _json["last_event"] = update_last_event(generator, forwarder)
    return _json


def update_last_event(generator, forwarder):
    return "New message {} by meter {}. Content from meter {}".format(
        "forwarded" if is_forwarded(generator, forwarder) else "received",
        forwarder,
        generator)
