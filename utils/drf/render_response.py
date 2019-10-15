from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            if isinstance(data,dict):
                msg = data.pop('msg', '请求成功')
                code = data.pop('code', 0)
                count = data.pop('count',0)

            else:
                msg = '请求成功'
                code = 0
                count = 0
            response = renderer_context['response']
            response.status_code = 200
            res = {
                "code":code,
                "msg":msg,
                "count":count,
                "data":data["results"]
            }
            return super().render(res, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)