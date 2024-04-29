'''
Author: liusuxian 382185882@qq.com
Date: 2024-04-26 21:01:03
LastEditors: liusuxian 382185882@qq.com
LastEditTime: 2024-04-27 00:12:01
Description: 

Copyright (c) 2024 by liusuxian email: 382185882@qq.com, All Rights Reserved.
'''
from modelscope import snapshot_download
model_dir = snapshot_download('baicai003/llama-3-8b-Instruct-chinese_v2')
print(model_dir)
