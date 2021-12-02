# -*- coding: utf8 -*-
# by Sharapov Ilya
import telebot
from telebot import types

token = ''

bot = telebot.TeleBot(token)

def gen_markup():
	markup = types.InlineKeyboardMarkup(row_width = 1)
	item1 = types.InlineKeyboardButton("Хочу арендовать кальян! 🤪", callback_data = '1')
	item2 = types.InlineKeyboardButton("На какое время я могу арендовать кальян? ⌛️", callback_data = '2')
	item3 = types.InlineKeyboardButton("Расскажи о доставке! 🤔🚘", callback_data = '3')
	item4 = types.InlineKeyboardButton("Какой табак я могу использовать для кальяна? 😋", callback_data = '4')
	item5 = types.InlineKeyboardButton("Как я могу забить чашу для кальяна? 🍃", callback_data = '5')
	item6 = types.InlineKeyboardButton("Наши контакты! 📞", callback_data = '6')
	markup.add(item1, item2, item3, item4, item5, item6)
	return markup


@bot.message_handler(commands = ['start'])
def welcome(message):
	bot.send_message(872839024, f"\n\nДанные о пользователе который выполнил команду \"/start\" в Telegram:\nID: @{message.from_user.id}\nFirstname and Lastname: {message.from_user.first_name} {message.from_user.last_name}\nUsername: @{message.from_user.username}")
	sticker = open('welcome.tgs', 'rb')
	bot.send_sticker(message.chat.id, sticker)
	bot.send_message(message.chat.id,"Привет, {0.first_name}! 👋\nМеня зовут <b>{1.first_name}</b>, я помогу тебе заказать дымный и вкусный кальян! ❤️💨".format(message.from_user, bot.get_me()), parse_mode = 'html')
	bot.send_message(message.chat.id,"Выберите действие!", reply_markup = gen_markup())



@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
	if call.message:

		global lease_time
		global lease_time_price
		global delivery_method
		global delivery_method_price
		global our_service
		global our_service_price
		global tobacco
		global summa


		markup1 = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton("Хочу арендовать кальян на 4 часа. ✅", callback_data = '11')
		item2 = types.InlineKeyboardButton("Хочу арендовать кальян на сутки. ✅", callback_data = '12')
		item3 = types.InlineKeyboardButton("Назад.", callback_data = '13')
		item4 = types.InlineKeyboardButton("Главное меню.", callback_data = '14')
		markup1.add(item1, item2, item3, item4)

		markup2 = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton("Нужна доставка в нижнюю часть города. 🏙", callback_data = '21')
		item2 = types.InlineKeyboardButton("Нужна доставка в верхнюю часть города. 🐥", callback_data = '22')
		item3 = types.InlineKeyboardButton("Хочу забрать кальян самостоятельно. 💪🚀", callback_data = '23')
		item4 = types.InlineKeyboardButton("Назад.", callback_data = '24')
		item5 = types.InlineKeyboardButton("Главное меню.", callback_data = '25')
		markup2.add(item1, item2, item3, item4, item5)

		markup3 = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton("Хочу использовать свой табак. ✅", callback_data = '31')
		item2 = types.InlineKeyboardButton("Хочу заказать табак у Вас. ✅", callback_data = '32')
		item3 = types.InlineKeyboardButton("Назад.", callback_data = '33')
		item4 = types.InlineKeyboardButton("Главное меню.", callback_data = '34')
		markup3.add(item1, item2, item3,item4)

		markup4 = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton("Хочу воспользоваться услугой. ✅", callback_data = '41')
		item2 = types.InlineKeyboardButton("Хочу забить кальян самостоятельно. ✅", callback_data = '42')
		item3 = types.InlineKeyboardButton("Хочу арендовать электроплитку. ✅", callback_data = '43')
		item4 = types.InlineKeyboardButton("Назад.", callback_data = '44')
		item5 = types.InlineKeyboardButton("Главное меню.", callback_data = '45')
		markup4.add(item1, item2, item3, item4, item5)

		markup5 = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton("Да, всё верно! ✅", callback_data = '51')
		item2 = types.InlineKeyboardButton("Нет, нужно исправить! ❌", callback_data = '52')
		item3 = types.InlineKeyboardButton("Назад.", callback_data = '53')
		item4 = types.InlineKeyboardButton("Главное меню.", callback_data = '54')
		markup5.add(item1, item2, item3, item4)

		markup6 = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton("Назад.", callback_data = '61')
		markup6.add(item1)

		markup7 = types.InlineKeyboardMarkup(row_width = 1)
		item1 = types.InlineKeyboardButton("Хочу арендовать кальян на 4 часа. ✅", callback_data = '11')
		item2 = types.InlineKeyboardButton("Хочу арендовать кальян на сутки. ✅", callback_data = '12')
		item3 = types.InlineKeyboardButton("Назад.", callback_data = '73')
		item4 = types.InlineKeyboardButton("Главное меню.", callback_data = '14')
		markup7.add(item1, item2, item3, item4)


		if call.data == '1':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Хочу арендовать кальян! 🤪")
			bot.send_message(call.message.chat.id, "На какое время Вы хотите арендовать кальян?\n\n•Аренда кальяна на 4 часа = 700 ₽ 😊\n•Аренда на сутки = 850 ₽ 😉\n Если вы хотите арендовать кальян на сутки, то Вам нужно оставить залог в размере 1000 ₽. Залог возвращается, когда мы получаем кальян. ✅\n\nВыберите действие!", reply_markup = markup1)
		if call.data == '2':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: На какое время я могу арендовать кальян? ⌛️\n\n•Аренда кальяна на 4 часа = 700 ₽ 😊\n•Аренда на сутки = 850 ₽ 😉\n Если вы хотите арендовать кальян на сутки, то Вам нужно оставить залог в размере 1000 ₽. Залог возвращается, когда мы получаем кальян. ✅\n\nВыберите действие!", reply_markup = markup6)
		if call.data == '3':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Расскажи о доставке! 🤔🚘\n\nДоставка до вашего дома стоит:\n•150 ₽ по нижней части города 🏙\n•200 ₽ по верхней части города 🐥\n•Вы можете так же забрать кальян самостоятельно 💪🚀\n\nВыберите действие!", reply_markup = markup6)
		if call.data == '4':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Какой табак я могу использовать? 😋\n\n•Табак можете использовать Ваш личный\n•Либо заказать у нас, и мы доставим его вместе с кальяном.\n (Вкус и крепость Вы сможете уточнить у нашего кальянного мастера) 😋\n\nВыберите действие!", reply_markup = markup6)
		if call.data == '5':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Как я могу забить чашу для кальяна? 🍃\n\nВы можете воспользоваться услугой \"Забивка чаши от нашего кальянного мастера\". Услуга стоит 150 ₽, в неё входит:\n•Грамотное распределение табака в чаше 🍃\n•Разогревание углей при помощи плитки 🔥\n•Раскур кальяна 🌬\n\nЛибо Вы можете арендовать только электроплитку для разогрева углей:\n•Аренда стоит 100 ₽, вне зависмости от времени аренды самого кальяна (4 часа или сутки) 😃\n\nВыберите действие!", reply_markup = markup6)
		if call.data == '6':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Наши контакты! 📞\n\n📸 Instagram:\ninstagram.com/kalyanvnntop\n🎵 TikTok:\ntiktok.com/@kalyanvnn\n✉️ Telegram:\nt.me/kalyanvnn\n🗑 Vk:\n(будет как наладим всё)\n\nВыберите действие!", reply_markup = markup6)


		if call.data == '11':
			lease_time_price = 0;
			lease_time_price = 700;
			lease_time = 0;
			lease_time = "Вы выбрали: Хочу арендовать кальян на 4 часа. ✅";
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Хочу арендовать кальян на 4 часа. ✅")
			bot.send_message(call.message.chat.id, "Как вы желаете получить кальян?\n\nДоставка до вашего дома стоит:\n•150 ₽ по нижней части города 🏙\n•200 ₽ по верхней части города 🐥\n•Вы можете также забрать кальян самостоятельно 💪🚀\n\nВыберите действие!", reply_markup =markup2)
		if call.data == '12':
			lease_time_price = 0;
			lease_time_price = 850;
			lease_time = 0;
			lease_time = "Вы выбрали: Хочу арендовать кальян на на сутки. ✅";
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Хочу арендовать кальян на сутки. ✅")
			bot.send_message(call.message.chat.id, "Как вы желаете получить кальян?\n\nДоставка до вашего дома стоит:\n•150 ₽ по нижней части города 🏙\n•200 ₽ по верхней части города 🐥\n•Вы можете также забрать кальян самостоятельно 💪🚀\n\nВыберите действие!", reply_markup =markup2)
		if call.data == '13':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Назад\n\nВыберите действие!", reply_markup = gen_markup())
		if call.data == '14':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Главное меню.\n\nВыберите действие!", reply_markup = gen_markup())


		if call.data == '21':
			delivery_method_price = 0;
			delivery_method_price = 150;
			delivery_method = 0;
			delivery_method = "Вы выбрали: Нужна доставка в нижнюю часть города. 🏙";
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Нужна доставка в нижнюю часть города. 🏙")
			bot.send_message(call.message.chat.id, "Какой табак Вы желаете использовать для кальяна?\n\n•Табак можете использовать Ваш личный\n•Либо заказать у нас, и мы доставим его вместе с кальяном. (Вкус и крепость Вы сможете уточнить у нашего кальянного мастера) 😋\n\nВыберите действие!", reply_markup = markup3)
		if call.data == '22':
			delivery_method_price = 0;
			delivery_method_price = 200;
			delivery_method = 0;
			delivery_method = "Вы выбрали: Нужна доставка в верхнюю часть города. 🐥";
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Нужна доставка в верхнюю часть города. 🐥")
			bot.send_message(call.message.chat.id, "Какой табак Вы желаете использовать для кальяна?\n\n•Табак можете использовать Ваш личный\n•Либо заказать у нас, и мы доставим его вместе с кальяном. (Вкус и крепость Вы сможете уточнить у нашего кальянного мастера) 😋\n\nВыберите действие!", reply_markup = markup3)
		if call.data == '23':
			delivery_method_price = 0;
			delivery_method = 0;
			delivery_method = "Вы выбрали: Хочу забрать кальян самостоятельно. 💪🚀";
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Хочу забрать кальян самостоятельно. 💪🚀")
			bot.send_message(call.message.chat.id, "Какой табак Вы желаете использовать для кальяна?\n\n•Табак можете использовать Ваш личный\n•Либо заказать у нас, и мы доставим его вместе с кальяном. (Вкус и крепость Вы сможете уточнить у нашего кальянного мастера) 😋\n\nВыберите действие!", reply_markup = markup3)
		if call.data == '24':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Назад\n\nНа какое время Вы хотите арендовать кальян?\n\n•Аренда кальяна на 4 часа = 700 ₽ 😊\n•Аренда на сутки = 850 ₽ 😉\n Если вы хотите арендовать кальян на сутки, то Вам нужно оставить залог в размере 1000 ₽. Залог возвращается, когда мы получаем кальян. ✅\n\nВыберите действие!", reply_markup = markup1)
		if call.data == '25':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Главное меню.\n\nВыберите действие!", reply_markup = gen_markup())


		if call.data == '31':
			tobacco = 0;
			tobacco = "Вы выбрали: Хочу использовать свой табак. ✅";
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Хочу использовать свой табак. ✅")
			bot.send_message(call.message.chat.id, "Вам понадобиться услуга \"Забивка чаши от нашего кальянного мастера\"? Услуга стоит 150 ₽, в неё входит:\n•Грамотное распределение табака в чаше 🍃\n•Разогревание углей при помощи электроплитки 🔥\n•Раскур кальяна 🌬\n\nЛибо Вы можете арендовать только электроплитку для разогрева углей:\n•Аренда стоит 100 ₽, вне зависмости от времени аренды самого кальяна (4 часа или сутки) 😃\n\nВыберите действие!", reply_markup = markup4)
		if call.data == '32':
			tobacco = 0;
			tobacco = "Вы выбрали: Хочу попросить Вас купить для меня табак. ✅";
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Хочу попросить Вас купить для меня табак. ✅")
			bot.send_message(call.message.chat.id, "Вам понадобиться услуга \"Забивка чаши от нашего кальянного мастера\"? Услуга стоит 150 ₽, в неё входит:\n•Грамотное распределение табака в чаше 🍃\n•Разогревание углей при помощи электроплитки 🔥\n•Раскур кальяна 🌬\n\nЛибо Вы можете арендовать только электроплитку для разогрева углей:\n•Аренда стоит 100 ₽, вне зависмости от времени аренды самого кальяна (4 часа или сутки) 😃\n\nВыберите действие!", reply_markup = markup4)
		if call.data == '33':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Назад.\n\nКак вы желаете получить кальян?\n\nДоставка до вашего дома стоит:\n•150 ₽ по нижней части города 🏙\n•200 ₽ по верхней части города 🐥\n•Вы можете так же забрать кальян самостоятельно 💪🚀\n\nВыберите действие!", reply_markup = markup2)
		if call.data == '34':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Главное меню.\n\nВыберите действие!", reply_markup = gen_markup())


		if call.data == '41':
			our_service_price = 0;
			our_service_price = 150;
			summa = lease_time_price + delivery_method_price + our_service_price;
			our_service = 0;
			our_service = "Вы выбрали: Хочу воспользоваться услугой. ✅";
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Хочу воспользоваться услугой. ✅")
			bot.send_message(call.message.chat.id, "Прекрасно! Проверьте, пожалуйста, правильность введённых данных:\n\n"+lease_time+" "+str(lease_time_price)+"₽\n"+delivery_method+" "+str(delivery_method_price)+"₽\n"+tobacco+"\n"+our_service+" "+str(our_service_price)+"₽\n\nОбщая цена без учёта табака: " +str(summa)+ " ₽.\n\nВыберите действие!", reply_markup =markup5)
		if call.data == '42':
			our_service_price = 0;
			summa = lease_time_price + delivery_method_price + our_service_price;
			our_service = 0;
			our_service = "Вы выбрали: Хочу забить кальян самостоятельно. ✅";
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Хочу забить кальян самостоятельно. ✅")
			bot.send_message(call.message.chat.id, "Прекрасно! Проверьте, пожалуйста, правильность введённых данных:\n\n"+lease_time+" "+str(lease_time_price)+"₽\n"+delivery_method+" "+str(delivery_method_price)+"₽\n"+tobacco+"\n"+our_service+" "+str(our_service_price)+"₽\n\nОбщая цена без учёта табака: " +str(summa)+ " ₽.\n\nВыберите действие!", reply_markup =markup5)
		if call.data == '43':
			our_service_price = 0;
			our_service_price = 100;
			summa = lease_time_price + delivery_method_price + our_service_price;
			our_service = 0;
			our_service = "Вы выбрали: Хочу арендовать электроплитку. ✅";
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Хочу арендовать электроплитку. ✅")
			bot.send_message(call.message.chat.id, "Прекрасно! Проверьте, пожалуйста, правильность введённых данных:\n\n"+lease_time+" "+str(lease_time_price)+"₽\n"+delivery_method+" "+str(delivery_method_price)+"₽\n"+tobacco+"\n"+our_service+" "+str(our_service_price)+"₽\n\nОбщая цена без учёта табака: " +str(summa)+ " ₽.\n\nВыберите действие!", reply_markup =markup5)
		if call.data == '44':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Назад.\n\nКакой табак Вы желаете использовать для кальяна?\n\n•Табак можете использовать Ваш личный\n•Либо заказать у нас, и мы доставим его вместе с кальяном. (Вкус и крепость Вы сможете уточнить у нашего кальянного мастера) 😋\n\nВыберите действие!", reply_markup = markup3)
		if call.data == '45':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Главное меню.\n\nВыберите действие!", reply_markup = gen_markup())


		if call.data == '51':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Да, всё верно! ✅")
			msg = bot.send_message(call.message.chat.id, "Напишите Ваш номер телефона, чтобы мы могли с Вами связаться.")
			bot.register_next_step_handler(msg, get_number)
		if call.data == '52':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Нет, нужно исправить! ❌")
			bot.send_message(call.message.chat.id, "Oooops. Давайте попробуем сначала. На какое время Вы хотите арендовать кальян?\n\n•Аренда кальяна на 4 часа = 700 ₽ 😊\n•Аренда на сутки = 850 ₽ 😉\n Если вы хотите арендовать кальян на сутки, то Вам нужно оставить залог в размере 1000 ₽. Залог возвращается, когда мы забираем кальян ✅\nНа какое время Вы хотите арендовть кальян?\n\nВыберите действие!", reply_markup =markup7)
		if call.data == '53':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Назад.\n\nВам понадобиться услуга \"Забивка чаши от нашего кальянного мастера\"? Услуга стоит 150 ₽, в неё входит:\n•Грамотное распределение табака в чаше 🍃\n•Разогревание углей при помощи электроплитки 🔥\n•Раскур кальяна 🌬\n(Услугу нельзя выбрать, если Вы решили забрать кальян самостоятельно😢)\n\nЛибо Вы можете арендовать только электроплитку для разогрева углей:\n•Аренда стоит 100 ₽, вне зависмости от времени аренды самого кальяна (4 часа или сутки) 😃\n\nВыберите действие!", reply_markup = markup4)
		if call.data == '54':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Главное меню.\n\nВыберите действие!", reply_markup = gen_markup())


		if call.data == '61':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Назад.\n\nВыберите действие!", reply_markup = gen_markup())


		if call.data == '73':
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы выбрали: Назад.\n\nПроверьте, пожалуйста, правильность введённых данных:\n\n"+lease_time+" "+str(lease_time_price)+"₽\n"+delivery_method+" "+str(delivery_method_price)+"₽\n"+tobacco+"\n"+our_service+" "+str(our_service_price)+" ₽\n\nОбщая цена без учёта табака: " +str(summa)+ "₽.\n\nВыберите действие!", reply_markup =markup5)


def get_number(message):
	try:
		global number
		number = message.text
		if not number.isdigit():
			msg = bot.send_message(message.chat.id, 'Номер телефона должен состоять из 11 цифр, попробуйте, пожалуйста, ещё раз.')
			bot.register_next_step_handler(msg, get_number)
			return
		if not len(number) == 11:
			msg = bot.send_message(message.chat.id, 'Номер телефона должен состоять из 11 цифр, попробуйте, пожалуйста, ещё раз.')
			bot.register_next_step_handler(msg, get_number)
			return
		msg = bot.send_message(message.from_user.id, 'Как Вас зовут?')
		bot.register_next_step_handler(msg, get_name)
	except Exception as e:
		print(repr(e))


def get_name(message):
	try:

		global name;
		name = message.text
		bot.send_message(message.chat.id, "Спасибо за заказ, " +name+ "! Скоро с Вами свяжется наша команда по этому номеру телефона: " +number+ ".\n\n"+lease_time+" "+str(lease_time_price)+"₽\n"+delivery_method+" "+str(delivery_method_price)+"₽\n"+tobacco+"\n"+our_service+" "+str(our_service_price)+"₽\n\nОбщая цена без учёта табака: " +str(summa)+ " ₽.")
		bot.send_message(message.chat.id, "Возвращаю Вас в главное меню!", reply_markup = gen_markup())
		bot.send_message(id1, "Новый заказ!\n\nИмя: " +name+ "\nНомер телефона: " +number+ "\n\n" +lease_time+" "+str(lease_time_price)+"₽\n"+delivery_method+" "+str(delivery_method_price)+"₽\n"+tobacco+"\n"+our_service+" "+str(our_service_price)+"₽\n\nОбщая цена без учёта табака: " +str(summa)+ " ₽." f"\n\nДанные о пользователе в Telegram:\nID: @{message.from_user.id}\nFirstname and Lastname: {message.from_user.first_name} {message.from_user.last_name}\nUsername: @{message.from_user.username}")
		bot.send_message(id2, "Новый заказ!\n\nИмя: " +name+ "\nНомер телефона: " +number+ "\n\n" +lease_time+" "+str(lease_time_price)+"₽\n"+delivery_method+" "+str(delivery_method_price)+"₽\n"+tobacco+"\n"+our_service+" "+str(our_service_price)+"₽\n\nОбщая цена без учёта табака: " +str(summa)+ " ₽." f"\n\nДанные о пользователе в Telegram:\nID: @{message.from_user.id}\nFirstname and Lastname: {message.from_user.first_name} {message.from_user.last_name}\nUsername: @{message.from_user.username}")
	except Exception as e:
		print(repr(e))


bot.polling(none_stop=True)