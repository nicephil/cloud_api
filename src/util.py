def debug_echo (req, resp):
    """
    echo request content
    """
    payload = req.stream.read().decode('utf-8')
    if payload:
        data_in = json.loads(payload)
    else:
        data_in = {}
    result = {
        #'attribute': dir(req),
        'params': req.params,
        'path': req.path,
        'relative_uri': req.relative_uri,
        'uri': req.uri,
        'prefix': req.prefix,
        'headers': req.headers,
        'return_code': 'debug',
        'return_message' : 'echo back some fields and payload',
        'payload_echo' : data_in
    }
    resp.status = falcon.HTTP_200
    resp.body= json.dumps (result, sort_keys=True, indent=4, separators=(',', ': '))

def is_positive_int (string):
    try:
        val = int(string)
        if val < 0:
            return False
    except ValueError:
            return False
    return True

