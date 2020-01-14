from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from demo_app.models import UserInfo
from demo_app.form import LoginForm
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import time
# Create your views here.
import logging


logger = logging.getLogger('collect')


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/demo/index')
        return render(request, 'login.html', {'form': form})
    return HttpResponse("hello world")


def index(request):
    return render(request, 'index.html')


def get_url_response(url, method='GET', param=None, data=None):
    if method == 'GET':
        response = requests.get(url, params=param)
    else:
        response = requests.post(url, data=data, params=param, )
    print(response.url)
    return json.loads(response.text)


def gettoken(request):
    """获取access_token"""
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    params = {
        'corpid': 'ww3035220e283065a8',
        'corpsecret': 'KPAJ-x46km4-bOXDVyXzVW7ChokG1-tugKj8wpjWIqg'
    }
    data = get_url_response(url, param=params)
    request.session['access_token'] = data.get('access_token')
    logging.info(data)
    return JsonResponse(data)


def getapprovaldetail(request):
    """获取审批申请详情"""
    url = 'https://qyapi.weixin.qq.com/cgi-bin/oa/getapprovaldetail?access_token=%s' % request.session.get('access_token')
    print(url)
    data = {
        "sp_no": 202001130002
    }
    response = get_url_response(url, method='POST', data=json.dumps(data))
    print(response)
    # request.session['template_id'] = response['info'].get('template_id')
    logging.info(response)
    return JsonResponse(response)


def applyevent(request):
    """提交审批申请"""
    url = 'https://qyapi.weixin.qq.com/cgi-bin/oa/applyevent?access_token=%s' % request.session.get('access_token')

    data = {
        "creator_userid": "test",
        "template_id": "Bs5MftA28SL8rSEQewAarjoAzBEwuXqo3XuFgqomM",
        "approver": [
            {
                "attr": 2,
                "userid": ["test", "LuoMinWen"]
            }
        ],
        "notifyer":[ "LuoMinWen", "test"],
        "notify_type" : 1,
        "apply_data": {
             "contents": [
                    {
                        "control": "Date",
                        "id": "Date-1578905704636",
                        "title": [
                            {
                                "text": "申请日期",
                                "lang": "zh_CN"
                            }
                        ],
                        "value": {
                            "date": {
                                "type": "day",
                                "s_timestamp": time.time()
                            }
                        }
                    },
                    {
                        "control": "Selector",
                        "id": "Selector-1578905723150",
                        "title": [
                            {
                                "text": "文件类型",
                                "lang": "zh_CN"
                            }
                        ],
                        "value": {
                            "selector": {
                                "type": "single",
                                "options": [
                                    {
                                        "key": "option-1578905769690"
                                    }
                                ]
                            }
                        }
                    },
                    {
                        "control": "Table",
                        "id": "Table-1578905946804",
                        "title": [
                            {
                                "text": "明细",
                                "lang": "zh_CN"
                            }
                        ],
                        "value": {
                            "children": [
                                {
                                    "list": [
                                        {
                                            "control": "Selector",
                                            "id": "Selector-1578906004681",
                                            "title": [
                                                {
                                                    "text": "所属公司",
                                                    "lang": "zh_CN"
                                                }
                                            ],
                                            "value": {
                                                "selector": {
                                                    "type": "single",
                                                    "options": [
                                                        {
                                                            "key": "option-1578906004682"
                                                        }
                                                    ]
                                                }
                                            }
                                        },
                                        {
                                            "control": "Text",
                                            "id": "Text-1578906037718",
                                            "title": [
                                                {
                                                    "text": "所属项目",
                                                    "lang": "zh_CN"
                                                }
                                            ],
                                            "value": {
                                                "text": "Test合作 (二次)"
                                            }
                                        },
                                        {
                                            "control": "Text",
                                            "id": "Text-1578906053751",
                                            "title": [
                                                {
                                                    "text": "对方单位",
                                                    "lang": "zh_CN"
                                                }
                                            ],
                                            "value": {
                                                "text": "Test公司"
                                            }
                                        },
                                        {
                                            "control": "Selector",
                                            "id": "Selector-1578906073218",
                                            "title": [
                                                {
                                                    "text": "盖章类型",
                                                    "lang": "zh_CN"
                                                }
                                            ],
                                            "value": {
                                                "selector": {
                                                    "type": "multi",
                                                    "options": [
                                                        {
                                                            "key": "option-1578906073218"
                                                        }
                                                    ]
                                                }
                                            }
                                        },
                                        {
                                            "control": "Textarea",
                                            "id": "Textarea-1578906248819",
                                            "title": [
                                                {
                                                    "text": "情况说明",
                                                    "lang": "zh_CN"
                                                }
                                            ],
                                            "value": {
                                                "text": "Test公司合作(二次)......情况说明"
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ]
        },
        "summary_list": [
            {
                "summary_info": [{
                    "text": "申请日期: 2020/1/14",
                    "lang": "zh_CN"
                }]
            },
            {
                "summary_info": [{
                    "text": "文件类型：合同类",
                    "lang": "zh_CN"
                }]
            },
            {
                "summary_info": [{
                    "text": "明细： 明细",
                    "lang": "zh_CN"
                }]
            }
        ]
    }
    response = get_url_response(url, method="POST", data=json.dumps(data))
    logging.info(response)
    return JsonResponse(response)


@csrf_exempt
def applyeventcallback(request):
    print(request.body)
    logger.info(request.body)
    return HttpResponse('200')


def wechat(request):
    access_token = request.session.get('access_token')
    return HttpResponse(access_token)

