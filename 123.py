# # -*- coding: utf-8 -*-
#
# # print "I am %(name)s, i am %(age)d years old" % {'name':'weiyq','age':24}
# '''
# %s    字符串 (采用str()的显示)
#
# %r    字符串 (采用repr()的显示)
#
# %c    单个字符
#
# %b    二进制整数
#
# %d    十进制整数
#
# %i    十进制整数
#
# %o    八进制整数
#
# %x    十六进制整数
#
# %e    指数 (基底写为e)
#
# %E    指数 (基底写为E)
#
# %f    浮点数
#
# %F    浮点数，与上相同
#
# %g    指数(e)或浮点数 (根据显示长度)
#
# %G    指数(E)或浮点数 (根据显示长度)
#
#
#
# %%    字符"%"
# 可以用如下的方式，对格式进行进一步的控制：
#
# %[(name)][flags][width].[precision]typecode
#
# (name)为命名
#
# flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。
# ' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
#
# width表示显示宽度
#
# precision表示小数点后精度
# '''
#
# # print ("%+10x" % 10)
# # print ("%04d" % 5)
# # print ("%+6.2f" % 2.3)
# # # print  "asd" + "adasd"
# # formatter = "%r %r %r %r"
# #
# # print formatter % (1,2,3,4)
#
#
# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#
# print "Here are the days: ",days
# print "Here are the months: ",months
# print """
# There`s something going on herer.
# with the three double-quoters.
# we`ll be able to type as much as we like.
# Even 4 lines if we want, or ,or 6.
# """
#
# print "I`m 6`2\" tall"
# print 'I am 6\'2" tall.'
#
# fat_cat ='''
# I'll do a list:
# \t* Cat food
# \t* Finishes
# \t* Catnip\n\t* Grass
# '''
#
# print fat_cat
#
#
#
#
# print "How old are you?"
# age = raw_input()
# print "How tall are you?",
# height = raw_input()
# print "How much do you weight?",
# weight = raw_input()
# print "So, you are %r old,%r tall and %r heavy." % (age,height,weight)

# print "input a string",
# myword = raw_input()
# print myword
# name=raw_input("please input your name?")
# height = raw_input("please input your age")
# weight = raw_input("please input your weight")
# print "your name is :%s,\nyour height is %s,\nyour weight is %s." % (name,height,weight)

from sys import argv

# script,first,second,third = argv
#
# print "The acript is called:",script
# print "The first variable is: ",first
# print "the second variable is ",second
# print "the third variable is ",third

# 18:46
# script ,user_name  = argv
#
# prompt ='> '
#
# print "Hi %s,I'm the %s script" % (user_name,script)
# print "I'd like to ask you a few questons."
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)
#
# print "Where do you live %s?" % user_name
# lives = raw_input(prompt)
#
# print "what kind of computer do you have ?"
# computer = raw_input(prompt)
#
# print """
# Alright ,so you  have said %r about liking me.
# You live in %r, Not sure where thst is.
# And you have a %r computer. Nice.
# """ % (likes,lives,computer)

# 15 读取文件
# script,file_name=argv
# txt = open(file_name)
# print "Here is your file ",txt.name  #% file_name
# print txt.read(5) #读取的字符数
# txt.close()
#
# print "type the file name again"
# file_again = raw_input('>')
# txtagain = open(file_again)
# print "Here is what in your file just typed:"
# print txtagain.read()
# txtagain.close()

#16读写文件
import os
# script,filename = argv
# print "we're going to erase %r ." % filename
# print "If you don't want that,hit cutr_c."
# print "if you do want that hit return."
# raw_input("?")
# print "Opening the file..."
# target = open(filename,"r+")
# # print target.read() #??为什么显示不出来
#
# print "Truncating the file. Goodbye！"
# target.truncate()
#
# print "Now I'm going to ask you for three lines."
#
# line1 = raw_input("line 1:")
# line2 = raw_input("line 2:")
# line3 = raw_input("line 3:")
#
# print "I'm going to write these to the file."
#
# target.write(line1+'\n'+line2+'\n'+line3+'\n')
# print "this is the new file "
# #target=open("15.txt") #不写这一行就没有显示啦，应该是文件指针移动到了文件的末尾
# target.seek(0,os.SEEK_SET)#定位指针到文件起始位置
# target.flush()
# print target.read()
# target.close()

#17更多文件操作
