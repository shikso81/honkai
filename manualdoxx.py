import os

manualdoxx = """Взято с канала HackMe! https://t.me/+IYKMHp0NqKNmMTAy

1. @phonenumberinformation_bot
2. @Quick_osintik_bot
3. @UniversalSearchRobot
4. @search_himera_bot
5. @Solaris_Search_Bot
6. @Zernerda_bot
7. @t_sys_bot
8. @OSINTInfoRobot
9. @LBSE_bot
10. @SovaAppBot
11. @poiskorcombot
12. @SEARCHUA_bot
13. @helper_inform_bot
14. @infobazaa_bot
15. @declassified_bot
16. @GHack_search_bot
17. @osint_databot
18. @Informator_BelBot
19. @HowToFindRU_Robot
20. @SEARCH2UA_bot
21. @UsersSearchBot
22. @BITCOlN_BOT
23. @ce_poshuk_bot
24. @BlackatSearchBot
25. @dataisbot
26. @n3fm4xw2rwbot
27. @cybersecdata_bot
28. @safe_search_bot
29. @getcontact_real_bot
30. @PhoneLeaks_bot
31. @useridinfobot 
32. @mailcat_s_bot
33. @last4mailbot
34. @holehe_s_bot
35. @bmi_np_bot
36. @clerkinfobot
37. @kolibri_osint_bot
38. @getcontact_premium_bot
39. @phone_avito_bot
40. @pyth1a_0racle_bot
41. @olx_phone_bot
42. @ap_pars_bot
43. @SPOwnerBot
44. @regdatebot
45. @ibhldr_bot
46. @TgAnalyst_bot
47. @cryptoscanning_bot
48. @LinkCreatorBot
49. @telesint_bot
50. @Checknumb_bot
51. @TelpoiskBot_bot
52. @TgDeanonymizer_bot
53. @protestchat_bot
54. @locatortlrm_bot
55. @GetCont_bot
56. @usinfobot
57. @SangMataInfo_bot
58. @creationdatebot
59. @tgscanrobot
60. @InfoVkUser_bot
61. @getfb_bot
62. @GetOK2bot
63. @VKHistoryRobot
64. @detectiva_robot
65. @FindNameVk_bot
66. @vk2017robot
67. @AgentFNS_bot
68. @OpenDataUABot
69. @egrul_bot
70. @Bumz639bot
80. @ogrn_bot
90. @ShtrafKZBot
91. @egrnrobot
92. @VipiskaEGRNbot
93. @Search_firm_bot
94. @geomacbot
95. @pwIPbot
96. @ipscorebot
97. @ip_score_checker_bot
98. @FakeSMI_bot
99. @ipinfo_check_bot
100. @Search_IPbot
101. @WhoisDomBot
102. @vimebasebot
103. @maigret_osint_bot
104. @PasswordSearchBot
105. @ddg_stresser_bot
106. @BotAvinfo_bot
107. @reverseSearch2Bot
108. @pimeyesbot
109. @findfacerobot
110. @CarPlatesUkraineBot
111. @nomerogrambot
112. @ShtrafyPDRbot
113. @cerbersearch_bot
@GetOK2bot (Одноклассники)
@poiskorcombot
@cybersecdata_bot
@bmi_np_bot
@ip_score_checker_bot (Чекер IP / думаю лучший бот)
@UsersSearchBot (Один из лучших)
@safe_search_bot
@VKHistoryRobot (Лучший бот для нахождения инфы по Вк)
@GTA_searchBot (Гта,один из лучших) 
@Euyiy999_bot (Глаз Бога,один из лучших)
@SovaAppBot
@PhoneLeaks_bot ( утечки номера)
@Detecta_bot
@search_himera_bot
@Zernerda_bot
@TeleSkan_bot (Чек тг)
@helper_inform_bot ( Очень хороший,подписка на 24ч - 24₽)
@BlackatSearchBot
@test_sys_tank_bot (Дорогой но хороший)
@Qu1ckosint_robot (Дорогой но хороший)
@clerkinfobot
@getcontact_real_bot
@AntiParkonBot
@OpenDataUABot
@cryptoscanning_bot
@Probiwfepix_bot
@SovaAppBot
@oko_ua_bot
@QUICKHAKAbot
@clubdev_bot
@VipiskaEGRNbot
@ShtrafKZBot
@pyth1a_0racle_bot
@ce_poshuk_bot
@InfoVkUser_bot
@mailcat_s_bot
@n3fm4xw2rwbot
@get_caller_bot
@WhoisDomBot
@find_caller_bot
@t3_avtootvetchik_bot
@Search_firm_bot
@BlackatSearchBot
@userinfobot
@oomanuals_bot
@PhoneLeaks_bot
@ibhldr_bot
@HowToFindRU_Robot
@declassified_bot
@GetOK2bot
@UsersSearchBot
@mnp_bot
@userinfobot
@no_secret_bot
@PhoneLeaks_bot
@creationdatebot
@telesint_bot
@getfb_bot
@info_baza_bot – бaза данных нoмеров телефона, email
@get_caller_bot - Ищет только пo нoмеру телефoна. На выходе: ФИО, дата рoждения, пoчта и «ВКoнтакте»
@OpenDataUABot – по кoду ЕДРПOУ возвращает данные о компaнии из реeстра, по ФИО — наличие регистрации ФОП
@YouControlBot - полное досье на каждую компанию Украины
@Dosie_Bot – создатели «Досье» пошли дальше и по номеру телефона отдают ИНН и номер паспорта
@UAfindbot – База данных Украины
@FindClonesBot – Поиск человека по фото
@MsisdnInfoBot - Получение сведений о номере телефона
@antiparkon_bot - Поиск сведений об автовладельце
@friendsfindbot - Поиск человека по местоположению
@egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта России
@last4mailbot (Mail2Phone) — по почте показывает статус: есть ли аккаунт в «Одноклассниках» и «Сбербанке», или нет.
@bmi_np_bot - По номеру телефона определяет регион и оператора.
@VKUserInfo_bot — по ID «ВКонтакте» возвращает расширенную информацию о профиле.
@GetGmail_bot (GetGmail — OSINT email search) — по gmail-почте отдает Google ID, зная который, можно получить архив альбомов Google, а также редактирования и отзывы на Google-картах


https://t.me/FroxSoftprobivBot
https://t.me/WhiteQuickbot
https://t.me/UniversalSearchRobot
https://t.me/kolibri_osint_bot
https://t.me/Qu1ck0s11nt_bot
https://t.me/PhoneLeaks_bot
https://t.me/fandorin_search_bot
https://t.me/clerkinfobot
https://t.me/telesint_bot
https://t.me/Mrsotss_bot
https://t.me/maigret_osint_bot
https://t.me/MsisdnInfoBot
https://t.me/egrul_bot
https://t.me/darknetfinderbot
https://t.me/getfb_bot
https://t.me/holehe_s_bot
https://t.me/Probivio_bot
https://t.me/Pika4y_bot
https://t.me/Zernerda_bot
https://t.me/probiv_Ukraina_bot
https://t.me/OpenDataUABot
https://t.me/detectiva_robot
https://t.me/maigret_s_bot
https://t.me/nanoprobiv4_bot
https://t.me/telescan_osint_robot
https://t.me/ProstoyPoiskBot
https://t.me/VKHistoryRobot
https://t.me/LBSE_bot
https://t.me/buzzim_alerts_bot
https://t.me/leakscheckerbot
https://t.me/SovaAppBot
https://t.me/poisk_gps_calls_bot
https://t.me/eyegodsearchnewbot
https://t.me/Search_firm_bot
https://t.me/AngelSearchBot
https://t.me/egrul_bot
https://t.me/mailcat_s_bot
https://t.me/HowToFindRU_Robot_bot
https://t.me/phonenumberinformation_bot
https://t.me/jqc2bgj9mbot_bot
https://t.me/AviinfoBot
https://t.me/vin01bot
https://t.me/getcontact_real_bot
https://t.me/tgscanrobot
https://t.me/ArnoldShvarcenegger_bot
https://t.me/Himera_Search_net_bot
https://t.me/bmi_np_bot
https://t.me/helper_inform_bot
https://t.me/imole_bot
https://t.me/MotherSearchBot
https://t.me/findmenow_bot
https://t.me/getcontact_premium_bot
https://t.me/a11_1n_bot
https://t.me/darova_osint_bot
https://t.me/maigret_s2_bot
https://t.me/userinfobot
https://t.me/Probiv_VK_Bot
https://t.me/RBares_bot
https://t.me/v34a89dsa_bot_bot
https://t.me/ip_score_checker_bot
https://t.me/The_New_Get_Contact_Bot
https://t.me/phonebook_space_bot
https://t.me/deadghoul_zxc_bot
https://t.me/cryptoscanning_bot
https://t.me/CheckID_AIDbot




@PhoneLeaks_bot
@getmyid_bot

@egrnrobot — Бот для получения легальной информации о недвижимости из ЕГРН.
• @indiapeoplebot — по номеру найдёт FaceBook,VK и т.д
• @FindGitHubUserEmailBot - поиск по аккаунту GitHub
• @egrul_bot ищет информацию о юридических и физических лицах, учредителях, связях, местах регистрации. 
• @last4mailbotl → Last4mail ← находит связь почтового адреса к одноклассникам и сбербанку.
• @telesint_bot → Telesint ← даёт информацию о том, в каких чатах сидит пользователь.
• @ibhldr_bot → ibhldr ← показывает предпочтения юзера на основе собранный информации по чатам, каналам и т.п.
• @mailsearchbot — ищет по базе, дает часть пароля
• @AvinfoBot — найдет аккаунт в ВК
• @GetGmail_bot — Полезнейший инструмент, способный узнать ФИ по почте Gmail
• @clerkinfobot — Номер телефона.
• @BusinkaBusya — хороший селлер, рекомендую (Пробив Solaris)
• @InfoVkUser_bot — выдает информацию про пользователя вк.
• @FindNameVk_bot — старые имена вк. 
• @phone_avito_bot — пробив по номеру, выдаст Avito
• @Quick_OSINT_bot — различные серверные пробивы по данным критериям (почте, номеру, номеру машины, ip-адресу, паспортным данным, по Telegram и т.п) +analog @EyeGodsBot +analog @AvinfoBot
• @getfb_bot — при помощи номера сможем найти аккаунт в Facebok
• @GetYandexBot — пробив по почте выдает различные данные
• @clerkinfobot — Номер телефона.
• @leakcheck_bot — есть в списке указанного в первом сообщении бота. Ищет утекшие в сеть пароли от email. На тест забил пару своих заброшенных с mail.ru. прихуел Был неприятно удивлён




@egrnrobot — Бот для получения легальной информации о недвижимости из ЕГРН.
• @indiapeoplebot — по номеру найдёт FaceBook,VK и т.д
• @FindGitHubUserEmailBot - поиск по аккаунту GitHub
• @egrul_bot ищет информацию о юридических и физических лицах, учредителях, связях, местах регистрации. 
• @last4mailbotl → Last4mail ← находит связь почтового адреса к одноклассникам и сбербанку.
• @telesint_bot → Telesint ← даёт информацию о том, в каких чатах сидит пользователь.
• @ibhldr_bot → ibhldr ← показывает предпочтения юзера на основе собранный информации по чатам, каналам и т.п.
• @mailsearchbot — ищет по базе, дает часть пароля
• @AvinfoBot — найдет аккаунт в ВК
• @GetGmail_bot — Полезнейший инструмент, способный узнать ФИ по почте Gmail
• @clerkinfobot — Номер телефона.
• @BusinkaBusya — хороший селлер, рекомендую (Пробив Solaris)
• @InfoVkUser_bot — выдает информацию про пользователя вк.
• @FindNameVk_bot — старые имена вк. 
• @phone_avito_bot — пробив по номеру, выдаст Avito
• @Quick_OSINT_bot — различные серверные пробивы по данным критериям (почте, номеру, номеру машины, ip-адресу, паспортным данным, по Telegram и т.п) +analog @EyeGodsBot +analog @AvinfoBot
• @getfb_bot — при помощи номера сможем найти аккаунт в Facebok
• @GetYandexBot — пробив по почте выдает различные данные
• @clerkinfobot — Номер телефона.
• @leakcheck_bot — есть в списке указанного в первом сообщении бота. Ищет утекшие в сеть пароли от email. На тест забил пару своих заброшенных с mail.ru. прихуел Был неприятно удивлён

@Avnumbot

@WhoisDomBot

@lnfoVkUser_bot

@Finding_caller_id_bot

@find_caller_bot

@Eoododofkcjjdbot

@Zernerda_bot

@eyeofbeholder_bot

@Poisk_nomeru_bot

@InfoVkUser_bot

@Euyiy999_bot

@deanon_infobot

@Poisk_ID_bot

@LeakedInfoBot

@UniversalSearchRobot

@maigret_osint_bot

@nanoprobiv4_bot

@n8a7x6gkybot_bot

@bedoxymap44380461bot

@l2k5e4daw_kss_bot

@eyegod11_bot

@cerbersearch_bot

@probovpobazerf_bot

@QuickOSINT_bot

@sms_activ_3bot

@GreedySMSbot

@SMSBest_bot

@Info_BazaXbot

@UsersSearchBot

@ku06l61fzcheke_bot

@SovaAppBot

@cerber_robot

@Zernerda_bot

полезные боты для пробивов


@getcontact_real_bot - идеально подойдёт для проверки номера(Вирт или не Вирт)
@UsersSearchBot - найдет не мало хорошей информации по номеру, так же возможны другие методы поиска
@detectiva_bot - найдет информации по номеру и другим методам поиска(так же по номеру ищет соц-сети)
@vk2017robot - найдет информации по странице которая была зарегестрироваться в 17 и ранее году
@EyeCultist_bot - зеркало оригинального глаза бога
@n3fm4xw2rwbot - найдет информацию по почте, номеру, авто
@BotAvinfo_bot - найдет информации по авто
@helper_inform_bot - найдет чу чуть информации по номеру, так же присутствуют разные методы пробива
@Quickosintfast_bot - зеркало осинта. находит информации по чему угодно, только придется чу чуть оплачивать поиск
@vin01bot - найдет информации по ГОС или VIN номеру
@TgAnalyst_bot - найдет всю возможную информацию по айди телеграмм аккаунта
@Zernerda_bot - соберёт много информации по номеру телефона
@ip_score_checker_bot - найдет информации по айпи человека
@maigret_osint_bot - найдет информации по юзернейму телеграмм аккаунта
@UniversalSearchRobot - найдет информации по номеру телефона
@CultustDoxed_bot - зеркало баз ГТА
@PasswordSearchBot - найдет утерянные пароли в базах
@usinfobot - находит информации по юзеру/айди
@clerkinfobot - находит информации разными методами
@last4mailbot - найдет много полезной инфы по электронной почте

@QuickOSINT_bot- Хороший бот с большим ассортиментом найдет вам фулл инфу даже больше чем фулл инфу

@eyessofgodbot-Обычный всеми известный Гб тоже не плохой

@UniversalSearchRobot- Достаточно хороший бот тем что он ищет соц-сети так же находит Ф.И

@telesint_bot-Бот ищет в каких чатах находиться пользователь 

@userbox_boxbot- Замечательный бот для доксера очень хорошо работает 

@getcontact_real_bot- Не плохой Бот 50/50

@gta_search_bot- Бот найдет ФИО и остальные данные 


Список нормальных бомберов:
1) @bomber_calls_bot (бесплатный тест)

2) @miraibomber_bot (бесплатный тест)

3) @smsbomberosvip_bot (бесплатный тест)

4) @adscii_bomber_bot (бесплатный тест)

5) @SmsBomberat_bot (бесплатный тест)

6) @privateBloodLust_bot 

7) @sms_call_bomber2023_bot

8) @freez3_bomber_bot 

9) @TG_NoNameBot

10) @elderly_bot


"""

print(manualdoxx)