#!/usr/bin/python3

""" checkoAPI - python module to searching information about Russian buisness
API: https://checko.ru 
Github: https://github.com/webcartel-https
checkoAPI docs: https://github.com/webcartel-https/checkoAPI/wiki


Email for issues and questions: project-checkoAPI@gmail.com
Developer email: prvtangl@gmail.com
"""


""" THIS IS ALPHA-DEMO VERSION OF CHECKOAPI!"""
""" IN THIS VERION CHECKOAPI CAN: FIND ENTEPRENEURS,FIND FINANCIAL DOCUMENTS, FIND DATA BY LINK ON CHECKOAPI"""
""" IF YOU FACING SOME BUGS OR OTHER PROBLEMS, PLEASE CONTACT ME: project-checkoAPI@gmail.com"""
import requests as rq
import os,sys,platform
from datetime import date
import json as js

try:    
    import __version__
    import format as f
    import exeptions as e
except ImportError as FILE_ERR: print(f"Критическая ошибка, отсутствуют файлы \n {repr(FILE_ERR)}") 

class Company: # work in progress

    """https://checko.ru/integration/api/company"""

    def __init__(self,key:str,search:str,parameters:str):
        self.search = search
        self.key = key
        self.parameters = parameters

    def GetData(self,savefile:bool,final:str):
        try:
            result = rq.get(url=f"https://api.checko.ru/v2/company?key={self.key}&{self.search}={self.parameters}")
            result_json = result.json()
            fData = result_json["data"]
            f.Fcompany(_fdata=fData,_resultjson=result_json,_result=result,_final=final)
        except rq.exceptions.ConnectionError: print("[checkoapierror] Не удалось получить запрос. ")
            
class Finances: # Done
    " https://checko.ru/integration/api/finances"

    def __init__(self,key,search,parameters,download=False):
        self.key = key
        self.search = search
        self.parameters = parameters

    def download_pdf(self,url,file_path):
        response = rq.get(url)
        with open(file_path, "wb") as PDF:
            PDF.write(response.content)
    
    def GetLinks(self,year="all",download=False):
        try:
            result = rq.get(url=f"https://api.checko.ru/v2/finances?key={self.key}&{self.search}={self.parameters}")
            finJson = result.json()
            fData = finJson["data"]
            nalogRU = finJson["bo.nalog.ru"]["Отчет"]
        except rq.exceptions.ConnectionError: print("Не удалось выполнить запрос, проверьте подключение к интернету")
        if year == "all":
            try:
                link_2019 = nalogRU["2019"]
                print(f"Отчёт за 2019: {link_2019}")
                """ 
                if download == True:
                    try:
                        PDFfile = wget.download(link_2019)
                        print("Отчётность за 2019 год успешно загружена:" + PDFfile)
                    except Exception as e:
                        print("Ошибка при загрузке файла:",str(e))
                """

            except KeyError:
                print("2019 год - не найдено.")
                pass
            except ConnectionRefusedError:
                print("[checkoAPI] Ошибка. Подключение не установлено, так как сервер отверг подключение.(ConnectionRefusedError)(WinError 10061)")
                print("[checkoAPI] Если вы используете прокси, убедитесь в том, что подключение работает корректно.")
            except rq.exceptions.ProxyError:
                print("[checkoAPI] Не удалось подключиться к прокси серверу. Проверьте настройки прокси и попробуйте ещё раз.")

            try:
                link_2020 = nalogRU["2020"]
                print(f"Отчёт за 2020: {link_2020}")

            except KeyError:
                print("2020 год - не найдено.")
                pass
            except ConnectionRefusedError:
                print("[checkoAPI] Ошибка. Подключение не установлено, так как сервер отверг подключение.(ConnectionRefusedError)(WinError 10061)")
                print("[checkoAPI] Если вы используете прокси, убедитесь в том, что подключение работает корректно.")
            except rq.exceptions.ProxyError:
                print("[checkoAPI] Не удалось подключиться к прокси серверу. Проверьте настройки прокси и попробуйте ещё раз.")

            try:
                link_2021 = nalogRU["2021"]
                print(f"Отчёт за 2021: {link_2021}")

            except KeyError:
                print("2021 год - не найдено.")
                pass
            except ConnectionRefusedError:
                print("[checkoAPI] Ошибка. Подключение не установлено, так как сервер отверг подключение.(ConnectionRefusedError)(WinError 10061)")
                print("[checkoAPI] Если вы используете прокси, убедитесь в том, что подключение работает корректно.")
            except rq.exceptions.ProxyError:
                print("[checkoAPI] Не удалось подключиться к прокси серверу. Проверьте настройки прокси и попробуйте ещё раз.")

            try:
                link_2022 = nalogRU["2022"]
                print(f"Отчёт за 2022: {link_2022}")

            except KeyError:
                print("2022 год - не найдено.")
                pass
            except ConnectionRefusedError:
                print("[checkoAPI] Ошибка. Подключение не установлено, так как сервер отверг подключение.(ConnectionRefusedError)(WinError 10061)")
                print("[checkoAPI] Если вы используете прокси, убедитесь в том, что подключение работает корректно.")
            except rq.exceptions.ProxyError:
                print("[checkoAPI] Не удалось подключиться к прокси серверу. Проверьте настройки прокси и попробуйте ещё раз.")
        else:
            try:
                customYear = nalogRU[year]
                print(f"Отчётность за {year} год: {customYear}")
            except KeyError:
                print(f"Данные за {year} не найдены!")
            except ConnectionRefusedError:
                print("[checkoAPI] Ошибка. Подключение не установлено, так как сервер отверг подключение.(ConnectionRefusedError)(WinError 10061)")
                print("[checkoAPI] Если вы используете прокси, убедитесь в том, что подключение работает корректно.")
            except rq.exceptions.ProxyError:
                print("[checkoAPI] Не удалось подключиться к прокси серверу. Проверьте настройки прокси и попробуйте ещё раз.")

class Ent: # 80 % is done
# > Collect data about entrepreneurs by ogrn,inn,kpp,okpo

    def __init__(self,key:str,search:str,parameters:str):
        self.key = key 
        self.search = search 
        self.parameters = parameters 

    def GetData(self,savefile:bool,final:str): 
        try:
            result = rq.get(url=f"https://api.checko.ru/v2/entrepreneur?key={self.key}&{self.search}={self.parameters}")
            result_json = result.json()
            fData = result_json["data"]
            try: msg = result_json["meta"]["message"],print(msg),sys.exit()
            except (UnboundLocalError,KeyError): pass
        except rq.exceptions.ConnectionError as CONN_ERR: print(f"[checkoAPI] Не удалось подключится к серверу: \n {repr(CONN_ERR)}"),sys.exit()
        except KeyError: pass
        try:
            if result.status_code == 200: print("[checkoAPI] Запрос выполнен успешно.")
            if result.status_code == 401: print("[checkoAPI] Неправильно введён API-ключ!"), sys.exit()
            if result.status_code == 400: print("[checkoAPI] Ошибка. Неправильно указаны параметры. Проверьте параметры search"),sys.exit()
        except UnboundLocalError: pass
        f.Fent(_fdata = fData,_resultjson = result_json,_result=result,_final=final) # format.py

"""    
class GenerateLink:
    def __init__(self,type:str,surname:str,name:str,ogrn:str):
        self.name = name
        self.ogrn = ogrn
        self.surname = surname
        self.type = type

    def GetLink(self):
        from translation import dictionary
        fName = self.name 
        fSurname = self.surname
        fData = self.ogrn
        english_fName = ''
        fullname = f"{fSurname}-{fName}"
        for key in fullname:
            linkname = dictionary[key]
        link = f"https://checko.ru/{self.type}/{linkname}-{self.ogrn}"
        print(link)
"""

class Parselink: # work only with entepreneurs 
# > Collect data on buissness profiles on checko.ru by link
    def __init__(self,link:str,final:str,key:str):
        self.link = link
        self.parse = final
        self.key = key

    def Parse(self,savefile=None):
        try:
            keyword = ["entrepreneur","company","finances"]
            for i in keyword:
                if i in self.link:
                    parsebylink = int(''.join(filter(str.isdigit,self.link)))
                    parsetype = i
            _url_ = f"https://api.checko.ru/v2/{parsetype}?key={self.key}&ogrn={parsebylink}"
            try:
                result = rq.get(url=_url_)
                result_json = result.json()
                fData = result_json["data"]
            except rq.exceptions.ConnectionError as CONN_ERR: print(f"[checkoAPI] Не удалось подключится к серверу: \n {repr(CONN_ERR)}"),sys.exit()
            except (KeyError,UnboundLocalError): raise e.DataNotFound("Данные не найдены.")
            f.Fent(_fdata = fData,_resultjson=result_json,_result=result,_final="All")
            #if savefile is True: f.savefile(_filename)
        except KeyError: pass 
        

class SearchName:

    def __init__(self,by,obj,query):
        pass           