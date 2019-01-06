# -*- coding: cp936 -*-

#导入随机数模块
import random

#导入win32com模块,用来操作Word
import win32com
from win32com.client import Dispatch, constants

#创建新的WORD文档
w = win32com.client.Dispatch('Word.Application')
w.Visible = 0#0表示在后台操作。设为1则在前端能看到Word界面。
w.DisplayAlerts = 0#不显示警告
doc = w.Documents.Add()

#准备对文档头部进行操作
myRange = doc.Range(0,0)#从第0行第0个字开始：
myRange.Style.Font.Name = "宋体"#设置字体
myRange.Style.Font.Size = "16"#设置为三号

#========以下为文章的内容部分=======

#文章标题（用\n来控制文字的换行操作）
title='XXXXX会\n会议时间: '

#会议时间
timelist=['1月9日','1月16日','1月23日','1月30日',
          '2月6日','2月13日','2月20日','2月27日',
          '3月6日','3月13日','3月20日','3月27日',
          '4月3日','4月10日','4月17日','4月24日',
          '5月8日','5月15日','5月22日','5月29日',
          '6月5日','6月12日','6月19日','6月26日',
          '7月3日','7月10日','7月17日','7月24日'
          ]

#会议地点
addrlist=['\n会议地点: 地点AXXX\n主持人: 张X\n',
         '\n会议地点: 地点BXXXX主持人: 吴X\n',
         '\n会议地点: 地点CXXXX\n主持人: 王X\n',
         '\n会议地点: 地点DXXXX\n主持人: 冉X\n',
         '\n会议地点: 地点EXXXX\n主持人: 李X\n',
         ]
#参加人员
member='参加人员: XXX,XXX,XXX,XXX,XXX,XXX,XXX。\n会议内容：\n '

#四段文字
list1=['第一段(A型)\n','第一段(B型)\n','第一段(C型)\n','第一段(D型)\n']
list2=['第二段(A型)\n','第二段(B型)\n','第二段(C型)\n','第二段(D型)\n']
list3=['第三段(A型)\n','第三段(B型)\n','第三段(C型)\n','第三段(D型)\n']
list4=['第四段(A型)\n','第四段(B型)\n','第四段(C型)\n','第四段(D型)\n']


#开始循环操作，往Word里面写文字

    #先开始遍历地点（A,B,C,D,E四个地区）
for addr in addrlist:

        #遍历28个日期
    for time in timelist:

        #随机生成四个数（范围0-3）
        aa=random.randint(0,3)
        bb=random.randint(0,3)
        cc=random.randint(0,3)
        dd=random.randint(0,3)

        #从文件开头依次插入标题、时间、地点、人物
        myRange.InsertAfter(title)
        myRange.InsertAfter(time)
        myRange.InsertAfter(addr)
        myRange.InsertAfter(str3)

        #在后面继续添加随机选取的四段文字
        myRange.InsertAfter(list1[aa])
        myRange.InsertAfter(list2[bb])
        myRange.InsertAfter(list3[cc])
        myRange.InsertAfter(list4[dd])

#循环完毕，保存为 D:\d.doc
doc.SaveAs(r'D:\d.doc')

#退出操作
doc.Close()
w.Quit()