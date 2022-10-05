import json
import re
from collections import OrderedDict
from datetime import datetime
from django.http import HttpResponse
# from ai import ai
from ai.ai import Ai

# Create your views here.


def talk(request):
    request_str = request.body.decode('utf-8')
    print(request_str)
    request_obj = json.loads(request_str)

    answer_text = Ai.nanako_answer(request_obj['question'])

    answer = {
        "answer" : answer_text,
        "timestamp" : datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }
    return HttpResponse(json.dumps(answer),
     content_type='application/json; charset=UTF-8',
     status=None)
