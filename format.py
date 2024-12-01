""" Parsing and formatting data """
import os,sys,platform 
from datetime import date 
import json as js

def Fcompany(_fdata,_resultjson,_result,_final): # In dev, work in progress and etc 
    """ Описание всех данных и формат ответа API вы можете посмотреть здесь: 
    https://checko.ru/integration/api/company
    """
    fData = _fdata
    result_json = _resultjson
    final = _final
    try:
        d_OGRN = fData["ОГРН"] 
        d_INN = fData["ИНН"]
        d_KPP = fData["КПП"]
        d_OKPO = fData["ОКПО"]
        d_FULLNAME = fData["НаимПолн"]
        d_SOKRNAME = fData["НаимСокр"]
        d_DATAREG = fData["ДатаРег"]
    except KeyError as JSONKEY:
        print(repr(JSONKEY))
    if final == "Data":
        finalData = [
            f"Основная информация о {d_FULLNAME}",
            f"ОГРН: {d_OGRN}",
            f"ИНН: {d_INN}",
            f"КПП: {d_KPP}",
            f"ОКПО: {d_OKPO}",
            f"Полное имя: {d_FULLNAME}",
            f"Имя сокращённое: {d_SOKRNAME}",
            f"Дата регистрации: {d_DATAREG}"
        ]
        for id in finalData:
            try:
                print(id + "\n")
            except UnboundLocalError as PRINTERR: break
                #repr?
    try:
        # right now this is not working, idk why 
        d_STATUS = fData["Статус"]
        d_STATUS_access = fData["Статус"]["ОгрДоступ"] 
        d_STATUS_code = fData["Статус"]["Код"]
        d_STATUS_naim = fData["Статус"]["Наим"]
        d_STATUS_data = fData["Статус"]["Дата"]
    except KeyError as JSONKEY:
        print(repr(JSONKEY))
        pass
    if final == "Status":
        finalStatus = [
            f"Статус {d_FULLNAME}",
            f"Сведения об ограничении доступа: {d_STATUS_access}",
            f"Код: {d_STATUS_code}",
            f"Наименование: {d_STATUS_naim}",
        ]
        for id in finalStatus:
            try:
                print(id + "\n")
            except UnboundLocalError as PRINTERR: print("[checkoAPI:UnboundLocalError] Не удалось получить данные")
    try:
        d_LIKVID = fData["Ливкид"]["Дата"]
        d_LIKVID_reason = fData["Ливкид"]["Наим"]
    except KeyError as JSONKEY:
        print("[checkoAPI:KeyError]. Какие-то данные отсутствуют. блок: [Ликвид]")
        print(repr(JSONKEY))
        pass
            
    try:
        d_REGION = fData["Регион"]["Наим"]
        d_REGION_code = fData["Регион"]["Код"]
    except KeyError:
        print("[checkoAPI:KeyError]. Какие-то данные отсутствуют. блок: [Регион]")
        pass
        try:
            d_ADRESS = fData["ЮрАдрес"]
            d_ADRESS_city = d_ADRESS["НасПункт"]
            d_ADRESS_ADRESSrf = d_ADRESS["АдресРФ"]
            d_ADRESS_idGAR = d_ADRESS["ИдГАР"] 
            d_ADRESS_nottrue = d_ADRESS["Недост"] 
            d_ADRESS_nottrue_reason = d_ADRESS["НедостОпис"]
        except KeyError:
            print("[checkoAPI:KeyError]. Какие-то данные отсутствуют. блок: [ЮрАдрес]")
            pass
        try:
            d_OKVED_code = fData["ОКВЭД"]["Код"]
            d_OKVED_naim = fData["ОКВЭД"]["Наим"]
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [ОКВЭД]")
            pass
        try:
            d_OKDOP = fData["ОКВЭДДоп"]
            for d in d_OKDOP:
                d_OKDOP_code = d["Код"]
                d_OKDOP_naim = d["Наим"]
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [ОКВЭДДоп]")
            pass

        try:
            d_OKOPF = fData["ОКОПФ"] # Организационно-правовая форма 
            d_OKOPF_code = d_OKOPF["Код"]
            d_OKOPF_naim = d_OKOPF["Наим"]
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [ОКОПФ]")
            pass

        try:
            d_OKFS = fData["ОКФС"] # Форма собстенности
            d_OKFS_code = d_OKFS["Код"]
            d_OKFS_naim = d_OKFS["Наим"]
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [ОКФС]")
            pass

        try:
            d_OKOGU = fData["ОКОГУ"] # Общероссийский классификатор органов государственной власти и управления 
            d_OKOGU_code = d_OKOGU["Код"]
            d_OKOGU_naim = d_OKOGU["Наим"]
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [ОКОГУ]")
            pass
                    # ------

        try:
            d_OKATO = fData["ОКАТО"] # Общероссийский классификатор объектов административно-территориального деления 
            d_OKATO_code = d_OKATO["Код"]
            d_OKATO_naim = d_OKATO["Наим"]
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [ОКАТО]")
            pass
            
        try:
            d_OKTMO = fData["ОКТМО"]
            d_OKTMO_code = d_OKTMO["Код"]
            d_OKTMO_naim = d_OKTMO["Наим"]
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [ОКТМО]")
            pass

        try:
            d_FNS = fData["РегФНС"] # Регистрация в налоговом органе
            d_FNS_code = d_FNS["КодОрг"]
            d_FNS_naim = d_FNS["НаимОрг"]
            d_FNS_adress = d_FNS["АдресОрг"]
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [РегФНС]")
            pass

        try:
            d_FNS_tek = fData["ТекФНС"]
            d_FNS_tek_code = d_FNS_tek["КодОрг"]
            d_FNS_tek_naim = d_FNS_tek["НаимОрг"]
            d_FNS_tek_data = d_FNS_tek["Дата"]
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [ТекФНС]")
            pass

        try:
            d_CAPITAL = fData["УстКап"]
            d_CAPITAL_type = d_CAPITAL["Тип"]
            d_CAPITAL_sum = d_CAPITAL["Сумма"]
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [УстКапитал]")
            pass
                    # ------

        try:
            d_UPR = fData["УпрОрг"] # Управляющая организация 
            d_UPR_access = d_UPR["ОгрДоступ"]
            d_UPR_ogrn = d_UPR["ОГРН"]
            d_UPR_inn = d_UPR["ИНН"]
            d_upr_fullname = d_UPR["НаимПолн"]
            d_upr_sokrname = d_UPR["НаимСокр"]
            d_UPR_incountry = d_UPR["ИнСтрана"]
            d_UPR_inadress = d_UPR["ИнАдрес"]
            d_UPR_inregnumber = d_UPR["ИнРегНомер"]
            d_UPR_indatareg = d_UPR["ИнДатаРег"]
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [УпрОгр]")
            pass
                    # ------

        try:
            d_BOSS = fData["Руковод"]
            for items in d_BOSS:
                try:
                    d_BOSS_access = items["ОгрДоступ"]
                    d_BOSS_name = items["ФИО"]
                    d_BOSS_inn = items["ИНН"]
                    d_BOSS_dol = items["ВидДолжн"]
                    d_BOSS_naim_dol = items["НаимДолжн"]
                    d_BOSS_nedost = items["Недост"]
                    d_BOSS_nedost_desr = items["НедостОпис"]
                    d_BOSS_massboss = items["МассРуковод"]
                    d_BOSS_discval = items["ДисквЛицо"]
                    d_BOSS_other_boss = items["СвязРуковод"]
                    d_boss_other_ucherd = items["СвязУчред"]
                except KeyError:
                    print("[CheckoAPI Error] Данные отсутствует в списке: Руковод")
                    pass
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [Руковод]")
            pass

        try:
            d_meta = result_json["meta"]
            m_request = d_meta["today_request_count"]
            m_balance = d_meta["balance"]
        except KeyError:
            print("[checkoAPI:KeyError]. Данные отсутствуют. блок: [Meta]")
            pass
def Fent(_fdata, _resultjson, _result, _final):
    fData = _fdata
    final = _final
    result_json = _resultjson
    result = _result
    try:
        ent_OGRN = fData["ОГРНИП"]
        ent_INN = fData["ИНН"]
        ent_OKPO = fData["ОКПО"]
        ent_datareg = fData["ДатаРег"]
        ent_fullname = fData["ФИО"]
        ent_type = fData["Тип"]
        ent_sex = fData["Пол"]
        # доделать функцию final
        if final == "Data":
            finalData = [
                f"Основная информация о {ent_fullname}",
                f"ОГРН: {ent_OGRN}",
                f"ИНН: {ent_INN}",
                f"ОКПО: {ent_OKPO}",
                f"Дата регистрации:{ent_datareg}",
                f"ФИО: {ent_fullname}",
                f"Тип: {ent_type}",
                f"Пол: {ent_sex}",
            ]
            for id in finalData:
                try:
                    print(id + "\n")
                except UnboundLocalError:
                    print(
                        "[checkoAPI] Данные отсутствовали или их не удалось получить."
                    )
            # print(finalData)
    except KeyError as JSONDATA_ERROR :
        print(f"[checkoAPI] Некоторые данные в блоке data отсутствуют \n {repr(JSONDATA_ERROR)} ")
    except UnboundLocalError:
        print(
            "[checkoAPI] Не удалось получить данные, возможно вы неправильно указали параметры или сервер не дал ответ."
        )
        print("HTTPS response:", result.status_code)
        os.abort()
    try:
        fStatus = fData["Статус"]
        ent_status_code = fStatus["Код"]
        ent_status_naim = fStatus["Наим"]
    except KeyError: pass 
    try:
        ent_status_access = fStatus["ОгрДоступ"]
        if final == "Status":
            finalStatus = [
                f"Блок: Статус",
                f"Сведения об ограничении доступа: {ent_status_access}",
                f"Код: {ent_status_code}",
                f"Наименование:{ent_status_naim}",
            ]
            for id in finalStatus:
                try:
                    print(id + "\n")
                except UnboundLocalError:
                    print(
                        "[checkoAPI] Данные отсутствовали или их не удалось получить."
                    )
                    pass
    except KeyError as JSONDATA_ERROR:
        print(f"[checkoAPI] Некоторые данные в блоке Статус отсутствуют \n {repr(JSONDATA_ERROR)} ")
        pass
    try:
        fClosed = fData["Прекращ"]
        ent_if_closed = fClosed["Дата"]
        ent_closed_reason = fClosed["Наим"]
        if final == "Closed":
            try:
                finalClosed = [
                    "Данные о прекращенни деятельности:",
                    f"Дата:{ent_if_closed}",
                    f"Причина:{ent_closed_reason}",
                ]
                for id in finalClosed:
                    print(id + "\n")
            except UnboundLocalError:
                print("[checkoAPI] Данные отсутствовали или их не удалось получить.")
    except KeyError:
        print("[chekoAPI] Не найдено сведений о прекращении деятельности")
        pass
    try:
        fRegion = fData["Регион"]
        ent_region_code = fRegion["Код"]
        ent_region_name = fRegion["Наим"]
        if final == "Region":
            try:
                finalRegion = [
                    "Данные о регионе",
                    f"Код региона: {ent_region_code}",
                    f"Регион: {ent_region_name}",
                ]
                for id in finalRegion:
                    print(id + "\n")
            except UnboundLocalError:
                print("[checkoAPI] Данные отсутствовали или их не удалось получить.")
    except KeyError:
        print("[checkoAPI] Данные о регионе не найдены")
        pass
    try:
        fOKVED = fData["ОКВЭД"]
        ent_okved_code = fOKVED["Код"]
        ent_okved_name = fOKVED["Наим"]
        ent_okved_version = fOKVED["Версия"]
        if final == "OKVED":
            try:
                finalOKVED = [
                    "Данные о видах деятельности:",
                    f"Код ОКВЭД: {ent_okved_code}",
                    f"Наименование:{ent_okved_name}",
                    f"Версия ОКВЭД: {ent_okved_version}",
                ]
                for id in finalOKVED:
                    print(id + "\n")
            except UnboundLocalError:
                print("[checkoAPI] Данные отсутствовали или их не удалось получить.")
    except KeyError:
        print("[checkoAPI] Некоторые данные ОКВЭД не найдены. ")
        pass

    try:
        fFNS = fData["РегФНС"]
        ent_FNS_code = fFNS["Код"]
        ent_FNS_name = fFNS["НаимОрг"]
        ent_FNS_adress = fFNS["АдресОрг"]
        finalFNS = [
            "Данные о регистрации в ФНС:",
            f"Код: {ent_FNS_code}",
            f"Наименование организации: {ent_FNS_name}",
            f"Адрес организации: {ent_FNS_adress}",
        ]
    except KeyError:
        print("[checkoAPI] некоторые данные о регистрации в ФНС не найдены")
        pass
    try:
        fOrganisations = fData["СвязРуковод"]
        for org_item in fOrganisations:
            i = 0
            try:
                for i in range(i + 1):
                    ent_org_ogrn = fOrganisations[i]["ОГРН"]
                    ent_org_inn = fOrganisations[i]["ИНН"]
                    ent_org_name = fOrganisations[i]["НаимПолн"]
                    ent_org_datareg = fOrganisations[i]["ДатаРег"]
                    ent_org_status = fOrganisations[i]["Статус"]
                    ent_org_region = fOrganisations[i]["РегионКод"]
                    ent_org_adress = fOrganisations[i]["ЮрАдрес"]
                    ent_org_okved = fOrganisations[i]["ОКВЭД"]
            except IndexError:
                pass
    except KeyError:
        print("[checkoAPI] некоторые данные в блоке [СвязРуковод]")
        pass
    try:
        fUchreditel = fData["СвязУчред"]
        for uch_item in fUchreditel:
            i = 0
            try:
                for i in range(i + 1):
                    ent_uch_ogrn = fUchreditel[i]["ОГРН"]
                    ent_uch_inn = fUchreditel[i]["ИНН"]
                    ent_uch_name = fUchreditel[i]["НаимПолн"]
                    ent_uch_datareg = fUchreditel[i]["ДатаРег"]
                    ent_uch_status = fUchreditel[i]["Статус"]
                    ent_uch_region = fUchreditel[i]["РегионКод"]
                    ent_uch_adress = fUchreditel[i]["ЮрАдрес"]
                    ent_uch_okved = fUchreditel[i]["ОКВЭД"]
            except IndexError:
                pass
    except KeyError:
        print("[checkoAPI] некоторые данные в блоке [СвязУчред] отсутствуют")
        pass
    try:
        fLicenses = fData["Лиценз"]
        for lic_items in fLicenses:
            ent_license_number = fLicenses["Номер"]
            ent_license_data = fLicenses["Дата"]
            ent_license_given = fLicenses["ЛицОрг"]
            ent_license_type = fLicenses["ВидДеят"]
    except KeyError:
        print("[checkoAPI] некоторые данные о  Лицензиях отсутствуют")
        pass
    try:
        fTovarZnak = fData["ТоварЗнак"]
        for tovar_items in fTovarZnak:
            tovar_id = fTovarZnak["ID"]
            tovar_url = fTovarZnak["URL"]
    except KeyError:
        print("[checkoAPI] некоторые данные о Товарном знаке отсутствуют")
        pass
    try:
        fMeta = result_json["meta"]
        fMeta_status = fMeta["status"]
        fMeta_count = fMeta["today_request_count"]
        fMeta_balance = fMeta["balance"]
    except KeyError:
        pass
    if final == "All":
        try:
            # print(fData)
            print("Основная информация:")
            print(f"    Сведения о {ent_fullname}")
            print(f"    ОГРН: {ent_OGRN}")
            print(f"    ИНН: {ent_INN}")
            print(f"    ОКПО: {ent_OKPO}")
            print(f"    Дата регистрации: {ent_datareg}")
            print(f"    ФИО: {ent_fullname}")
            print(f"    Тип: {ent_type}")
            print(f"    Пол: {ent_sex}")
            print("------------------------")
        except UnboundLocalError:
            print("[Данные отсутствуют]")
            print("------------------------")
            pass
        try:
            print("Статус:")
            print(f"    Признаки ограничения доступа: {ent_status_access}")
            print(f"    Код: {ent_status_code}")
            print(f"    Описание: {ent_status_naim}")
            print("------------------------")
        except UnboundLocalError:
            print("[Данные отсутствуют]")
            print("------------------------")
            pass
        try:
            print("Сведения о прекращении деятельности")
            print(f"    Дата: {ent_if_closed}")
            print(f"    Причина: {ent_closed_reason}")
            print("------------------------")
        except UnboundLocalError:
            print("[Данные отсутствуют]")
            print("------------------------")
            pass
        try:
            print("Регион:")
            print(f"    Код региона: {ent_region_code}")
            print(f"    Регион: {ent_region_name}")
            print("------------------------")
        except UnboundLocalError:
            print("[Данные отсутствуют]")
            print("------------------------")
            pass
        try:
            print("ОКВЭД:")
            print(f"    Код: {ent_okved_code}")
            print(f"    Наименование: {ent_okved_name}")
            print(f"    Версия ОКВЭД: {ent_okved_version}")
            print("------------------------")
        except UnboundLocalError:
            print("[Данные отсутствуют]")
            print("------------------------")
            pass
        try:
            print("Руководитель в следующих организациях:")
            print(f"    ОГРН: {ent_org_ogrn}")
            print(f"    ИНН: {ent_org_inn}")
            print(f"    Наименование: {ent_org_name}")
            print(f"    Дата регистрации: {ent_org_datareg}")
            print(f"    Статус: {ent_org_status}")
            print(f"    Регион: {ent_org_region}")
            print(f"    Юридический адрес: {ent_org_adress}")
            print("------------------------")
        except UnboundLocalError:
            print("[Данные отсутствуют]")
            print("------------------------")
            pass
        try:

            print("Учредитель в следующих организациях")
            print(f"    ОГРН: {ent_uch_ogrn}")
            print(f"    ИНН: {ent_uch_inn}")
            print(f"    Наименование: {ent_uch_name}")
            print(f"    Дата регистрации: {ent_uch_datareg}")
            print(f"    Статус: {ent_uch_status}")
            print(f"    Регион: {ent_uch_region}")
            print(f"    Адрес: {ent_uch_adress}")
            print(f"    ОКВЭД: {ent_uch_okved}")
            print("------------------------")
        except UnboundLocalError:
            print("[Данные отсутствуют]")
            print("------------------------")
            pass
        try:
            print(f"Количество запросов сегодня: {fMeta_count}")
            print(f"Баланс: {fMeta_balance}")
        except UnboundLocalError:
            pass
def savefile(_filename=None,resultjson=None,path=None):
        try:
            if path == "current":
                current_path = os.path.abspath(f"{_filename}.json") 
                #print(current_path)
            else:
                current_path = path 
            with open(current_path,"w",encoding="utf-8") as json_file:
                js.dump(resultjson,json_file,ensure_ascii=False,indent=2)
                print(f"Файл {_filename}.json создан в директории {current_path}")
        except PermissionError:
                print("[checkoAPI] Не удалось записать данные в файл (Недостаточно прав)")
                pass
