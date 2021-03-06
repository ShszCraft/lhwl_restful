"""
Django settings for Retailers project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import os
from django.middleware.cache import UpdateCacheMiddleware
from django.middleware.cache import FetchFromCacheMiddleware

from lhwill.util.loggingFilter import skip_unreadable_post

'''
网站设置
:
# HTTP_HOST: 站点域名[后面不加杠]
HTTP_API_HOST: API地址
SECRET_KEY: 站点密匙[建议定期更换]
'''
HTTP_HOST = 'http://127.0.0.1:8000'
DATABASES_HOST = '127.0.0.1'
HTTP_API_HOST = '{}/{}'.format(HTTP_HOST, 'api')
SECRET_KEY = '%%lfj...........'
'''
Email设置
:
EMAIL_USE_SSL: 启用SSL
EMAIL_HOST: 邮箱服务器地址
EMAIL_PORT: 端口
EMAIL_HOST_USER: 帐号
EMAIL_HOST_PASSWORD: 密码
DEFAULT_FROM_EMAIL: 帐号
'''
EMAIL_USE_SSL = True
EMAIL_HOST = ''
EMAIL_PORT = 465
EMAIL_HOST_USER = ''  # 帐号
EMAIL_HOST_PASSWORD = ''  # 密码
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

'''
国采登录
'''
CLIENT_ID = '4a2ff26e5979427faa89670114e3ffed'
CLIENT_SEC = ''
REDIRECT_URI = 'https://www.lhwill.com/auth/login/oauth2/zycg/'

'''
配置QQ开放平台授权
'''
SOCIAL_AUTH_QQ_KEY = ''
SOCIAL_AUTH_QQ_SECRET = ''

'''
配置微信开放平台授权
'''
SOCIAL_AUTH_WEIXIN_KEY = ''
SOCIAL_AUTH_WEIXIN_SECRET = ''
ALIPAY_URL = 'https://openapi.alipay.com/gateway.do'

'''
设置时区
:
LANGUAGE_CODE: 语言
TIME_ZONE: 时区
USE_I18N: 国际化[翻译]
USE_L10N: 国际化[翻译]
USE_TZ: UTC本地时间的转换
'''
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

'''
缓存设置
'''

# CACHE_MIDDLEWARE_ALIAS = 'default'  # 用来存储的缓存别名
# CACHE_MIDDLEWARE_SECONDS = 3600  # 所有页面默认缓存时间,默认600
# CACHE_MIDDLEWARE_KEY_PREFIX = 'www.lhwil.com'  # 关键的前缀，当多个站点使用同一个配置的时候，这个可以设置可以避免发生冲突,一般设置为网站域名
# # CACHE_MIDDLEWARE_ANONYMOUS_ONLY = False  # 那么只有匿名的请求会被缓存，这是一个禁用缓存非匿名用户页面的最简单的做法，注意确保已经启用了Django用户认证中间件
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     }
# }

'''
跨域
'''  # 跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

'''
ETag的支持
'''
USE_ETAG = True

'''
其他设置
:
DEBUG: 调试模式
ALLOWED_HOSTS: 设置域名白名单
'''
DEBUG = True
ALLOWED_HOSTS = ['192.168.137.1', '127.0.0.1', '192.168.1.106', '127.0.0.1:8080', '*']
# ALLOWED_HOSTS = ['www.lhwill.com', '59.110.137.64']
LOGIN_URL = '/auth/login/'

'''
系统默认
##############################
#     注意： 下面不必修改    #
##############################
'''
ROOT_URLCONF = 'lhwill.urls'

WSGI_APPLICATION = 'lhwill.wsgi.application'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''
第三方第一次登录成功后跳转页面[禁止修改]
'''
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/auth/register/auto'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# 生产环境需要开启STATIC_ROOT，作用于合同签章
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT_PDF = os.path.join(BASE_DIR, 'static')

MEDIA = '/media'
# 搜索引擎 媒体资源文件夹名称，非路径

MEDIA_URL = '{}/'.format(MEDIA)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

'''
购物车
'''
CART_SESSION_ID = 'shopping'

'''
数据库设置
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': DATABASES_HOST,
        'PORT': '3306',
        'CHARSET': 'utf8',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine = INNODB',
        }
    }
}

'''
设置rest api分页器
: 启用会导致后台或者前台很多接口不一致，最后数据拿不出来
'''

REST_FRAMEWORK = {
    # 配置默认的认证方式 base:账号密码验证
    # session：session_id认证
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # drf的这一阶段主要是做验证,middleware的auth主要是设置session和user到request对象
        # 默认的验证是按照验证列表从上到下的验证
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ]
}
# 页码
PAGE_SIZE_LIMIT = 2

# 一页展示数据量
PAGE_SIZE = 60

# ?limit=20
DEFAULT_LIMIT = PAGE_SIZE


import datetime

JWT_AUTH = {
    # 指明token的有效期
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'api.util.jwt.jwt_response_payload_handler',
    'JWT_PAYLOAD_HANDLER': 'api.util.jwt.jwt_payload_handlers',
    'JWT_ENCODE_HANDLER':
        'rest_framework_jwt.utils.jwt_encode_handler',
    'JWT_DECODE_HANDLER':
        'rest_framework_jwt.utils.jwt_decode_handler',
    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
        'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,
}

'''
App应用
'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'rest_framework',
    'rest_framework_jwt',
    'django_filters',
    'stock',
    'search',

    'image_thumbs',

    'corsheaders',
    'haystack',
    'sorl.thumbnail',
    'api',
    'OAuth2',
    'account',
    'app',
    'home',

    'managestage',
    'shopping',
    'social_django',

    'plate'
]

AUTH_USER_MODEL = 'account.User'

MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware', # 缓存
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 拦截请求，设置session到request
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 再次拦截请求，判断是否有session(上面已加入)，设置user到request
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'django.middleware.cache.FetchFromCacheMiddleware',  # 缓存 必须设置在最后一个位置
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                # 'django.template.loaders.app_directories.Loader',
                'shopping.context_processors.template_defaule',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'lhwill.context_processors.template_defaule'
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

'''搜索引擎'''
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        'ENGINE': 'search.backend.whoosh_cn_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}
# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 搜索展示商品个数
HAYSTACK_SEARCH_RESULTS_PER_PAGE = DEFAULT_LIMIT
'''
设置要使用的第三方登录
'''

AUTHENTICATION_BACKENDS = (
    'social_django.social_core.backends.weixin.WeixinOAuth2',  # 使用微信登录
    'social_django.social_core.backends.qq.QQOAuth2',  # 使用QQ登录
    'django.contrib.auth.backends.ModelBackend',
    'account.util.authentication.EmailAuthBackend',  # 邮箱登陆
)

''''''

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s : %(message)s'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s %(module)s %(process)d %(thread)d : %(message)s'
        },
        'standard': {
            'format': '[%(asctime)s] [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
        'error': {
            'format': '[%(asctime)s] [%(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d] %(levelname)s: %(message)s'
        }
    },
    'filters': {
        'skip_unreadable_posts': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': skip_unreadable_post,
        },
        # 此过滤器仅在settings.DEBUG为True时传递记录 【require_debug_true】django.utils.log.RequireDebugTrue，其传递记录时 DEBUG是True
        # 此过滤器仅在settings.DEBUG为False时传递记录 【require_debug_false】django.utils.log.RequireDebugFalse，其传递记录时 DEBUG是False
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },

        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins_ERROR': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            # 'filters': ['require_debug_false'],
        },
        'mail_admins_CRITICAL': {
            'level': 'CRITICAL',
            'class': 'django.utils.log.AdminEmailHandler',
            # 'filters': ['require_debug_false'],
        },

        'INFO': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/', 'django_INFO.log'),
            # 'filters': ['require_debug_false'],
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },

        'WARNING': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/', 'django_WARNING.log'),
            # 'filters': ['require_debug_false'],
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'ERROR': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/', 'django_ERROR.log'),
            # 'filters': ['require_debug_false'],
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'error',
        },

        'CRITICAL': {
            'level': 'CRITICAL',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/', 'django_CRITICAL.log'),
            # 'filters': ['require_debug_false'],
            'formatter': 'error',
        },
        'DEBUG': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'error',
            'filename': os.path.join(BASE_DIR, 'logs/', 'django_DEBUG.log'),
            'filters': ['require_debug_true'],
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'INFO', 'WARNING'],
            'level': 'INFO',
            'propagate': True,
        },

        'django.server': {
            'handlers': ['console', 'DEBUG', 'WARNING'],
            'level': 'INFO',
            'propagate': True,
        },

        'django.request': {
            'handlers': ['console', 'ERROR', 'CRITICAL', 'mail_admins_ERROR', 'mail_admins_CRITICAL'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}
