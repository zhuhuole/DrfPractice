from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, data_status, data_msg, results=None, status=None, header=None, content_type=None, **kwargs):
        data = {
            'status': data_status,
            'msg': data_msg,
        }
        if results:
            data[results]=results
            data.update(kwargs)
        super().__init__(data=data, status=status, header=header, content_type=content_type)