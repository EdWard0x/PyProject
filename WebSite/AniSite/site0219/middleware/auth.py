from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class Auth(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info in ['/login/', '/imgcode/','/index/']:
            return
        info_session = request.session.get('info')
        if info_session:
            return
        return redirect('/login/')
