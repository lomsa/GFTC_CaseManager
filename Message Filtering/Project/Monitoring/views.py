from django.http import HttpResponseRedirect


from django.shortcuts import render, render_to_response
# -*- coding: utf-8 -*-
import os
import shutil
from datetime import datetime

from Project.Monitoring.models import *

dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')

array20 = []

try:
    os.mkdir("c:\MSG")
    os.chdir("c:\MSG")
    os.mkdir("Success")
    os.mkdir("Failed")
    os.chdir("c:\MSG\Success")
    os.mkdir("Mt192")
    os.mkdir("Mt195")
    os.mkdir("Mt196")
    os.mkdir("Mt199")
except:
    try:
        os.chdir("c:\MSG")
        os.mkdir("Success")
        os.chdir("c:\MSG\Success")
        os.mkdir("Mt192")
        os.mkdir("Mt195")
        os.mkdir("Mt196")
        os.mkdir("Mt199")
    except:
        try:
            os.chdir("c:\MSG\Success")
            os.mkdir("Mt192")
            os.mkdir("Mt195")
            os.mkdir("Mt196")
            os.mkdir("Mt199")
        except:
            try:
                os.chdir("c:\MSG\Success")
                os.mkdir("Mt195")
                os.mkdir("Mt196")
                os.mkdir("Mt199")
            except:
                try:
                    os.chdir("c:\MSG\Success")
                    os.mkdir("Mt196")
                    os.mkdir("Mt199")
                except:
                    try:
                        os.chdir("c:\MSG\Success")
                        os.mkdir("Mt199")
                    except:
                        print "Success Arsebobs", "192, 195, 196, 199, Arsebobs"
    try:
        os.chdir("c:\MSG")
        os.mkdir("Failed")
    except:
        print "Failed arsebobs"



def index(request):
    filter()
    filter_message_mt()
    mt195()
    message = MSG.objects.all()
    return render(request, 'index.html', {'message':message})

def detail(request, detail_id):
    message = MSG.objects.filter(id=detail_id)
    return render(request, 'form.html', {'message':message, 'detail_id':detail_id, })


def filter():
    Folder = "c:\MSG"
    os.chdir(Folder)
    file_names = os.listdir(os.curdir)
    for file in file_names:
        if file.endswith(".out"):
            reader = open(file,'r')
            if ":20:" and ":21:" in reader.read():
                direction ='C:\MSG\Success' + '\\' + dirname + file
                reader.close()
                shutil.move(file, direction)
            else:
                direction ='C:\MSG\Failed' + '\\' + file
                reader.close()
                shutil.move(file, direction)

def filter_message_mt():
    Folder = "c:\MSG\Success"
    os.chdir(Folder)
    file_names = os.listdir(os.curdir)
    for file in file_names :
        if file.endswith(".out"):
            reader = open(file,'r')
            readFirstLine = reader.readlines()[0]
            start = readFirstLine.find('{2:')
            end = readFirstLine.find('}', start)
            result = readFirstLine[start:end+1]
            if "{2:O195"  in result:
                direction ='C:\MSG\Success\Mt195'
                reader.close()
                shutil.move(file, direction)
            elif "{2:I195" in result:
                direction ='C:\MSG\Success\Mt195'
                reader.close()
                shutil.move(file, direction)
            elif "2:I192" in result:
                direction ='C:\MSG\Success\Mt192'
                reader.close()
                shutil.move(file, direction)
            elif "2:O192" in result:
                 direction ='C:\MSG\Success\Mt192'
                 reader.close()
                 shutil.move(file, direction)
            elif "2:I196" in result:
                direction ='C:\MSG\Success\Mt196'
                reader.close()
                shutil.move(file, direction)
            elif "2:O196" in result:
                 direction ='C:\MSG\Success\Mt196'
                 reader.close()
                 shutil.move(file, direction)
            elif "2:I199" in result:
                direction ='C:\MSG\Success\Mt199'
                reader.close()
                shutil.move(file, direction)
            elif "2:O199" in result:
                 direction ='C:\MSG\Success\Mt199'
                 reader.close()
                 shutil.move(file, direction)


def mt195():
    Folder = "C:\MSG\Success\Mt195"
    os.chdir(Folder)
    file_names = os.listdir(os.curdir)
    for file in file_names:
        if file.endswith(".out"):
            reader = open(file,'r')
            result = reader.readlines()[0]
            if "2:I195" in result:
                i195 = MSG195()
                i195.sender = result[7:19]
                start = result.find('{2:I195')
                end = result.find('N}', start)
                reciver = result[start:end+1]
                i195.reciver = reciver[7:19]
                i195.input_output = reciver[3]
                reader.close()
                referance20 = open(file, 'r')
                result_referance = referance20.readlines()[1]
                i195.reference20 = result_referance[4:]
                referance20.close()
                referance21 = open(file , 'r')
                result_referance21 = referance21.readlines()[2]
                i195.reference21 = result_referance21[4:]
                referance21.close()
                reader_name75 = open(file , 'r')
                name75_results = reader_name75.readlines()
                start = name75_results.find(':75:')
                end = name75_results.find(':77')
                name_75 = reader_name75[start+3:end-3]
                i195.name75 = name_75
                reader_name75.close()
                reader_name77a = open(file , 'r').readlines()
                start = reader_name77a.find(':77A:')
                end = reader_name77a.find(':11S:')
                name77a = reader_name77a[start+4:end-4]
                i195.comment77a = name77a
                reader_name77a.close()


def mt199():
    Folder = "C:\MSG\Success\Mt199"
    os.chdir(Folder)
    file_names = os.listdir(os.curdir)
    for file in file_names:
        if file.endswith(".out"):
            reader = open(file, 'r')
            result = reader.readlines()[0]
            if "2:I199" in result or "2:O199" in result :
                i199 = MSG199()
                i199.sender = result[7:19]
                start = result.find('{2:I199')
                end = result.find('N}', start)
                reciver = result[start:end + 1]
                i199.reciver = reciver[start:end + 1]
                i199.input_output = reciver[3]
                reader.close()
                referance20 = open(file, 'r')
                result_referance = referance20.readlines()[1]
                i199.reference20 = result_referance[4:]
                referance20.close()
                referance21 = open(file, 'r')
                result_referance21 = referance21.readlines()[2]
                i199.reference21 = result_referance21[4:]
                referance21.close()
                reader_name79 = open(file, 'r')
                name79_results = reader_name79.readlines()
                start = name79_results.find(':79:')
                end = name79_results.find('-}')
                name_79 = reader_name79[start + 3:end - 3]
                i199.name75 = name_79
                reader_name79.close()
                i199.save()

def mt196():
    Folder = "C:\MSG\Success\Mt196"
    os.chdir(Folder)
    file_names = os.listdir(os.curdir)
    for file in file_names:
        if file.endswith(".out"):
            reader = open(file, 'r')
            result = reader.readlines()[0]
            if "2:I196" in result or "2:O196" in result:
                i196 = MSG196()
                i196.sender = result[7:19]
                start = result.find('{2:I199')
                end = result.find('N}', start)
                reciver = result[start:end + 1]
                i196.reciver = reciver[start:end + 1]
                i196.input_output = reciver[3]
                reader.close()
                referance20 = open(file, 'r')
                result_referance = referance20.readlines()[1]
                i196.reference20 = result_referance[4:]
                referance20.close()
                referance21 = open(file, 'r')
                result_referance21 = referance21.readlines()[2]
                i196.reference21 = result_referance21[4:]
                referance21.close()
                reader_name76 = open(file, 'r')
                name76_results = reader_name76.readlines()
                start = name76_results.find(':76:')
                end = name76_results.find(':77A:')
                result = reader_name76[start + 3:end - 3]
                i196.field_76 = result
                reader_name76.close()
                reader_name77 = open(file, 'r')
                reader_name77_read = reader_name77.readlines()
                start = reader_name77_read.find(':77A:')
                end = reader_name77_read.find(':11S:')
                result = reader_name77_read[start+3:end-4]
                i196.field_77 = result
                reader_name77.close()
                reader_date= open(file, 'r')
                date_11 = reader_date.readlines()
                start = date_11.find(':11S:')
                end = date_11.find(':79:')
                result = date_11[start+8:end-4]
                i196.date_11 = result
                reader_date.close()
                field_79_reader = open(file, 'r')
                field_79_read = field_79_reader.readlines()
                start = field_79_read.find(':79:')
                end = field_79_read.find('-}')
                result = field_79_read[start+4:end-2]
                i196.field_79 =result
                field_79_reader.close()
                i196.save()



def mt192():
    Folder = "C:\MSG\Success\Mt192"
    os.chdir(Folder)
    file_names = os.listdir(os.curdir)
    for file in file_names:
        if file.endswith(".out"):
            reader = open(file, 'r')
            result = reader.readlines()[0]
            if "2:I196" in result or "2:O196" in result:
                i192 = MSG192()
                i192.sender = result[7:19]
                start = result.find('{2:I199')
                end = result.find('N}', start)
                reciver = result[start:end + 1]
                i192.reciver = reciver[start:end + 1]
                i192.input_output = reciver[3]
                reader.close()
                referance20 = open(file, 'r')
                result_referance = referance20.readlines()[1]
                i192.reference20 = result_referance[4:]
                referance20.close()
                referance21 = open(file, 'r')
                result_referance21 = referance21.readlines()[2]
                i192.reference21 = result_referance21[4:]
                referance21.close()
                reader_name79 = open(file, 'r')
                name79_results = reader_name79.readlines()
                start = name79_results.find(':79:')
                end = name79_results.find('-}')
                name_79 = reader_name79[start + 3:end - 3]
                i192.name79 = name_79
                reader_name79.close()
                i192.save()







