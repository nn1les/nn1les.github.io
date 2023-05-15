from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


knopka1 = KeyboardButton('🅽🅰🅿🆁🅰🆅🅻🅴🅽🅸🆈🅰')
knopka2 = KeyboardButton('🆁🅰🆂🅿🅸🆂🅰🅽🅸🅴')
knopka3 = KeyboardButton('🅺🅾🅽🆃🅰🅺🆃_🅿🅴🅳')
knopka4 = KeyboardButton('🅺🅾🅽🆃🅰🅺🆃_🅻🅰🅱')
knopka5 = KeyboardButton('🅺🅾🅽🆃🅰🅺🆃_🅰🅳🅼')
knopka6 = KeyboardButton('🅶🅸🅶🅸🅴🅽🅰')
knopka7 = KeyboardButton('🅿🆁🅾🅼🅳🅸🆉🅰🆈🅽')
knopka8 = KeyboardButton('🅿🆈🆃🅷🅾🅽')
knopka9 = KeyboardButton('🆆🅴🅱')
knopka10 = KeyboardButton('🅲🆈🅰🆉🆈🅺')
knopka11 = KeyboardButton('🆁🅰🆉🆁🆅🆁🅰🆁')
knopka12 = KeyboardButton('🆁🅾🅱🅾🆃')
knopka13 = KeyboardButton('🆁🅰🆉🆁🅼🅾🅱')
knopka14 = KeyboardButton('🆄🆄🅰🆇🅼🅰🆃')
knopka15 = KeyboardButton('Список команд')
knopka16 = KeyboardButton('Виды направлений')
knopka17 = KeyboardButton('🅺🅾🅽🆃🅰🅺🆃_🅽🅾🅼')
knopka18 = KeyboardButton('Вернуться в начало')
knopka19 = KeyboardButton('Контактные номера')
knopka20 = KeyboardButton('Подкоманды')


knopkao = ReplyKeyboardMarkup(
   resize_keyboard=True, one_time_keyboard=True).add(knopka15).add(knopka1).add(knopka2).add(knopka17)

knopkat = ReplyKeyboardMarkup(
   resize_keyboard=True, one_time_keyboard=True).add(knopka16).add(knopka6).add(knopka7).add(knopka8).add(knopka9).add(knopka10).add(knopka11).add(knopka12).add(knopka13).add(knopka14).add(knopka18)

knopkaf = ReplyKeyboardMarkup(
   resize_keyboard=True, one_time_keyboard=True).add(knopka19).add(knopka3).add(knopka4).add(knopka5).add(knopka18)

inline_0 = InlineKeyboardButton('Список команд', callback_data='knopka15')
inline_1 = InlineKeyboardButton('🅽🅰🅿🆁🅰🆅🅻🅴🅽🅸🆈🅰', callback_data='knopka1')
inline_2 = InlineKeyboardButton('🆁🅰🆂🅿🅸🆂🅰🅽🅸🅴', callback_data='knopka2')
inline_3 = InlineKeyboardButton('🅺🅾🅽🆃🅰🅺🆃_🅽🅾🅼', callback_data='knopka17')
inline_4 = InlineKeyboardButton('Вернуться в начало', callback_data='knopka18')
inline_kn1 = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(inline_0).add(inline_1).add(inline_2).add(inline_3).add(inline_4).add(inline_4)
inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_0).add(inline_1).add(inline_2).add(inline_3).add(inline_4)
