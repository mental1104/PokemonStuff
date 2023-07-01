'''
Date: 2023-07-01 00:18:43
Author: mental1104 mental1104@gmail.com
LastEditors: mental1104 mental1104@gmail.com
LastEditTime: 2023-07-01 16:18:40
'''

import db
import sys
sys.path.append('/home/espeon/Pokemon')


from storage.parse import ParseData

db.startup()
ParseData.init()