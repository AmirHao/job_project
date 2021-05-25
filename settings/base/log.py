import logging
import os

from settings.base import BASE_DIR

BASE_LOG_DIR = os.path.join(BASE_DIR, "log_file")

LOGGING = {
    'version': 1,  # 保留字
    'disable_existing_loggers': False,  # 禁用已经存在的logger实例
    # 日志文件的格式
    'formatters': {
        'verbose': {  # 详细
            'format': '[%(levelname)1.1s %(asctime)s - %(module)s.%(funcName)s:%(lineno)d] - '
                      'pid:%(process)d - %(thread)d - %(message)s',  # %(request_id)s,%(remote_ip)s 暂不可用
        },
        'standard': {  # 标准
            'format': '[%(asctime)s] - [%(levelname)s] - %(message)s'
        },
    },
    # 过滤器
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'request_id_remote_ip': {
            '()': 'utils.middleware.request.RemoteIpFilter'
        },
    },
    # 处理器
    'handlers': {
        # 在终端打印
        'console': {
            'level': 'DEBUG',
            'filters': ['request_id_remote_ip'],  # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',  #
            'formatter': 'verbose',
        },
        # 默认的
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "job_info.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 3,  # 最多备份几个
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        # 默认的logger应用如下配置
        'django': {
            'handlers': ['default', 'console'],  # 上线之后可以把'console'移除
            'level': 'INFO',
            'propagate': False,  # 向不向更高级别的logger传递
        },
    },
}

LOGGING_OBJ = logging.getLogger('django')
