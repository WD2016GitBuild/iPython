appid = 1400088485;
appkey = "86268a0cb01a9cb6ce86efe0cf328669";
phone_numbers = ["13880608926"];
template_id = 7839;

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

ssender = SmsSingleSender(appid, appkey)
try:
    result = ssender.send(0, 86, phone_numbers[0],
        "测试短信，普通单发，深圳，小明，上学。")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)