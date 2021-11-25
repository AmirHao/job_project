import logging
from uuid import uuid4

from django.utils.deprecation import MiddlewareMixin

from utils.middleware import local

logger = logging.getLogger("django")


class RemoteIpFilter(logging.Filter):
    def filter(self, record):
        record.remote_ip = getattr(local, "remote_ip", "no remote ip")
        record.request_id = getattr(local, "request_id", "no request id")
        return True


class RequestIDMiddleware(MiddlewareMixin):
    # 权限、限流、白名单、添加部分信息
    def process_request(self, request):  # noqa
        """
        :param request:
        :return:
            返回值是 None 的话，按正常流程继续走，交给下一个中间件处理
            返回值是 HttpResponse 对象，将不执行后续，直接以该中间件为起点，倒序执行中间件，且执行的是视图函数之后执行的方法
        """
        # print("请求进来啦，快来处理 😊 ")
        local.remote_ip = (
            request.META.get("HTTP_X_FORWARDED_FOR")
            or request.META.get("HTTP_X_REAL_IP")
            or request.META.get("REMOTE_ADDR")
        )
        request.META["HTTP_X_REQUEST_ID"] = local.request_id = request.META.get(
            "HTTP_X_REQUEST_ID", uuid4().hex
        )
        logger.info(
            "[request] method: %s, path: %s", request.method, request.get_full_path()
        )

    def process_view(self, request, view_func, view_args, view_kwargs):  # noqa
        """
        :param request: HttpRequest 对象
        :param view_func: Django 即将使用的视图函数
        :param view_args: 传递给视图的位置参数的列表
        :param view_kwargs: 传递给视图的关键字参数的字典
        :return:
            返回值是 None 的话，按正常流程继续走
            返回值是 HttpResponse 对象，不执行后续，直接以该中间件为起点，倒序执行中间件，且执行的是视图函数之后执行的方法
            返回值是 view_func(request)，不执行后续，提前执行视图函数，然后再倒序执行视图函数之后执行的方法
        """
        # print("找到视图啦，快来看 😬 ")
        pass

    def process_exception(self, request, exception):  # noqa
        """
        在视图函数之后，在 process_response 方法之前执行。
        :param request: HttpRequest 对象
        :param exception: 视图函数异常产生的 Exception 对象
        :return:
            返回值是 None，页面会报 500 状态码错误，视图函数不会执行
            返回值是 HttpResponse 对象，页面不会报错，返回状态码为 200
        """
        # print("好失望啊，出错了 😭 ")
        return exception

    def process_response(self, request, response):  # noqa
        """
        process_response 方法是在视图函数之后执行的
        :param request:
        :param response:
        :return: response
        """
        # print("撤啦撤啦，by ~ ")
        try:
            response.content
        except:  # noqa
            logger.info(
                "[response] status_code:%s, content: FileResponse"
                % response.status_code
            )
            return response
        logger.info("[response] status_code:%s, content: ..." % (response.status_code,))
        return response

    def process_template_response(self, request, response):  # noqa
        """
        在视图函数执行完成后立即执行，它有一个前提条件，视图函数返回的对象有一个render()方法（或者表明该对象是一个TemplateResponse对象或等价方法
        :param request: HttpRequest对象
        :param response: TemplateResponse对象（由视图函数或者中间件产生）
        :return:
        """
        # *** 暂时有问题，任何情况下都走这里
        # print("模板函数执行完成啦 👋")
        return response
