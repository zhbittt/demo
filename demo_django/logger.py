import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_LOG_DIR = os.path.join(BASE_DIR, "logs")


LOGGING = {
    'version': 1,  # 保留的参数，默认是1
    'disable_existing_loggers': False,  # 是否禁用已经存在的logger实例
    # 日志输出格式的定义
    'formatters': {
        'standard': {  # 标准的日志格式化
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'error': {     # 错误日志输出格式
            'format': '%(levelname)s %(asctime)s %(pathname)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'collect': {
            'format': '%(message)s'
        }
    },
    # 处理器：需要处理什么级别的日志及如何处理
    'handlers': {
        # 将日志打印到终端
        'console': {
            'level': 'DEBUG',                  # 日志级别
            'class': 'logging.StreamHandler',  # 使用什么类去处理日志流
            'formatter': 'simple'              # 指定上面定义过的一种日志输出格式
        },
        # 默认日志处理器
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "default.log"),  # 日志文件路径
            'maxBytes': 1024 * 1024 * 100,  # 日志大小 100M
            'backupCount': 5,  # 日志文件备份的数量
            'formatter': 'standard',  # 日志输出格式
            'encoding': 'utf-8',
        },
        # 日志处理级别warn
        'warn': {
            'level': 'WARN',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "warn.log"),  # 日志文件路径
            'maxBytes': 1024 * 1024 * 100,  # 日志大小 100M
            'backupCount': 5,  # 日志文件备份的数量
            'formatter': 'standard',  # 日志格式
            'encoding': 'utf-8',
        },
        # 日志级别error
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "error.log"),  # 日志文件路径
            'maxBytes': 1024 * 1024 * 100,  # 日志大小 100M
            'backupCount': 5,
            'formatter': 'error',  # 日志格式
            'encoding': 'utf-8',
        },
    },

    'loggers': {
        # 默认的logger应用如下配置
        'default': {
            'handlers': ['default', 'warn', 'error'],
            'level': 'DEBUG',
            'propagate': True,  # 如果有父级的logger示例，表示不要向上传递日志流
        },
        'collect': {
            'handlers': ['console', 'default', 'warn', 'error'],
            'level': 'INFO',
        }
    },
}