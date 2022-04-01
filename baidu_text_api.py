
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# OCR通用文字识别标准版 Python示例代码
if __name__ == '__main__':
    url = 'http://bdycharacterrecognition.api.bdymkt.com/ocr/general-basic'
    
    data = 'imageType=1&image=https:\/\/apisown-test.bj.bcebos.com\/general-basic.jpg'
    headers = {
        
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Bce-Signature': 'AppCode/您的AppCode'
    }
    r = requests.request("POST", url, data=data, headers=headers)
    print(r.content)
