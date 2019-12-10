import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR=os.path.join(BASE_DIR,'blog/templates/')


ALLOWED_HOSTS=['localhost','127.0.0.1','[::1]']
TEMPLATE=[
    {
        'BACKEND':'django.template.backends.django.DjangoTemplates',
        'DIRS':[TEMPLATE_DIR],
        'APP_DIRS':True,
        'OPTIONS':{
            'context_processors':[
                'django.template.context_procesors.debug',
                'django.template.context_procesors.request',
                'django.contrib.auth.context_procesors.auth',
                'django.contrib.messages.context_procesors.messages',
            ],
        },
    },
]