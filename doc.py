# -*- coding: cp936 -*-

#���������ģ��
import random

#����win32comģ��,��������Word
import win32com
from win32com.client import Dispatch, constants

#�����µ�WORD�ĵ�
w = win32com.client.Dispatch('Word.Application')
w.Visible = 0#0��ʾ�ں�̨��������Ϊ1����ǰ���ܿ���Word���档
w.DisplayAlerts = 0#����ʾ����
doc = w.Documents.Add()

#׼�����ĵ�ͷ�����в���
myRange = doc.Range(0,0)#�ӵ�0�е�0���ֿ�ʼ��
myRange.Style.Font.Name = "����"#��������
myRange.Style.Font.Size = "16"#����Ϊ����

#========����Ϊ���µ����ݲ���=======

#���±��⣨��\n���������ֵĻ��в�����
title='XXXXX��\n����ʱ��: '

#����ʱ��
timelist=['1��9��','1��16��','1��23��','1��30��',
          '2��6��','2��13��','2��20��','2��27��',
          '3��6��','3��13��','3��20��','3��27��',
          '4��3��','4��10��','4��17��','4��24��',
          '5��8��','5��15��','5��22��','5��29��',
          '6��5��','6��12��','6��19��','6��26��',
          '7��3��','7��10��','7��17��','7��24��'
          ]

#����ص�
addrlist=['\n����ص�: �ص�AXXX\n������: ��X\n',
         '\n����ص�: �ص�BXXXX������: ��X\n',
         '\n����ص�: �ص�CXXXX\n������: ��X\n',
         '\n����ص�: �ص�DXXXX\n������: ȽX\n',
         '\n����ص�: �ص�EXXXX\n������: ��X\n',
         ]
#�μ���Ա
member='�μ���Ա: XXX,XXX,XXX,XXX,XXX,XXX,XXX��\n�������ݣ�\n '

#�Ķ�����
list1=['��һ��(A��)\n','��һ��(B��)\n','��һ��(C��)\n','��һ��(D��)\n']
list2=['�ڶ���(A��)\n','�ڶ���(B��)\n','�ڶ���(C��)\n','�ڶ���(D��)\n']
list3=['������(A��)\n','������(B��)\n','������(C��)\n','������(D��)\n']
list4=['���Ķ�(A��)\n','���Ķ�(B��)\n','���Ķ�(C��)\n','���Ķ�(D��)\n']


#��ʼѭ����������Word����д����

    #�ȿ�ʼ�����ص㣨A,B,C,D,E�ĸ�������
for addr in addrlist:

        #����28������
    for time in timelist:

        #��������ĸ�������Χ0-3��
        aa=random.randint(0,3)
        bb=random.randint(0,3)
        cc=random.randint(0,3)
        dd=random.randint(0,3)

        #���ļ���ͷ���β�����⡢ʱ�䡢�ص㡢����
        myRange.InsertAfter(title)
        myRange.InsertAfter(time)
        myRange.InsertAfter(addr)
        myRange.InsertAfter(str3)

        #�ں������������ѡȡ���Ķ�����
        myRange.InsertAfter(list1[aa])
        myRange.InsertAfter(list2[bb])
        myRange.InsertAfter(list3[cc])
        myRange.InsertAfter(list4[dd])

#ѭ����ϣ�����Ϊ D:\d.doc
doc.SaveAs(r'D:\d.doc')

#�˳�����
doc.Close()
w.Quit()