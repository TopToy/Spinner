def add_missing(proto_msg, data):
    orig_keys = proto_msg.DESCRIPTOR.fields_by_name.keys()
    for key in orig_keys:
        if key not in data.keys():
            data[key] = 0
    return data
