#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dragon Mania Store Bot - Professional Multi-Language Telegram Bot
Owner: @JUSTHOHOHO
"""

import logging
import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from telegram.constants import ParseMode

# ==================== CONFIG ====================
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables!")

OWNER_USERNAME = "JUSTHOHOHO"
OWNER_LINK = f"https://t.me/{OWNER_USERNAME}"

# ==================== FULL ACCOUNTS ====================
ACCOUNTS = [
    {
        "id": "acc1",
        "emoji": "💎",
        "price": 130,
        "title": {
            "ar": "حساب جديد - 2 مليار جوهرة",
            "en": "New Account - 2 Billion Gems",
            "pt": "Conta Nova - 2 Bilhões de Gemas",
            "es": "Cuenta Nueva - 2 Mil Millones de Gemas",
            "ru": "Новый аккаунт - 2 миллиарда гемов",
        },
        "desc": {
            "ar": "• حساب جديد تمامًا\n• يحتوي على **2 مليار جوهرة**\n• مثالي للبدء القوي\n• جاهز للاستخدام فورًا",
            "en": "• Brand new account\n• Contains **2 Billion Gems**\n• Perfect for a strong start\n• Ready to use immediately",
            "pt": "• Conta completamente nova\n• Contém **2 Bilhões de Gemas**\n• Perfeita para um início forte\n• Pronta para uso imediato",
            "es": "• Cuenta completamente nueva\n• Contiene **2 Mil Millones de Gemas**\n• Perfecta para un inicio fuerte\n• Lista para usar inmediatamente",
            "ru": "• Совершенно новый аккаунт\n• Содержит **2 миллиарда гемов**\n• Идеально для сильного старта\n• Готов к использованию сразу",
        },
    },
    {
        "id": "acc2",
        "emoji": "🐉",
        "price": 160,
        "title": {
            "ar": "حساب مميز - 2 مليار جوهرة + 90% تنانين",
            "en": "Premium Account - 2B Gems + 90% Dragons",
            "pt": "Conta Premium - 2B Gemas + 90% Dragões",
            "es": "Cuenta Premium - 2B Gemas + 90% Dragones",
            "ru": "Премиум аккаунт - 2B гемов + 90% драконов",
        },
        "desc": {
            "ar": "• **2 مليار جوهرة**\n• أكثر من **90% من تنانين اللعبة**\n• Habitats كثيرة جدًا\n• جميعها موجودة في الـ Storage\n• حساب قوي ومتوازن",
            "en": "• **2 Billion Gems**\n• More than **90% of all dragons**\n• Lots of Habitats\n• All stored in Storage\n• Strong and balanced account",
            "pt": "• **2 Bilhões de Gemas**\n• Mais de **90% de todos os dragões**\n• Muitos Habitats\n• Todos no Storage\n• Conta forte e equilibrada",
            "es": "• **2 Mil Millones de Gemas**\n• Más del **90% de todos los dragones**\n• Muchos Habitats\n• Todos en el Storage\n• Cuenta fuerte y equilibrada",
            "ru": "• **2 миллиарда гемов**\n• Более **90% всех драконов**\n• Много хабитатов\n• Все в Storage\n• Сильный и сбалансированный аккаунт",
        },
    },
    {
        "id": "acc3",
        "emoji": "🔥",
        "price": 250,
        "title": {
            "ar": "حساب أسطوري - أقوى حساب متاح",
            "en": "Legendary Account - Strongest Available",
            "pt": "Conta Lendária - A Mais Forte Disponível",
            "es": "Cuenta Legendaria - La Más Fuerte Disponible",
            "ru": "Легендарный аккаунт - Самый сильный",
        },
        "desc": {
            "ar": "• **جميع تنانين الفئة S مفتوحة**\n• جميع الأراضي مفتوحة\n• **ملياري طعام**\n• جميع المساكن تم وضعها\n• أكثر من **90% من التنانين** في المخزن\n• أقوى التنانين **مستوى 130**\n• حساب خارق جاهز للسيطرة",
            "en": "• **All S-Class dragons unlocked**\n• All lands unlocked\n• **2 Billion Food**\n• All habitats placed\n• More than **90% of dragons** in storage\n• Strongest dragons at **Level 130**\n• God-tier account ready to dominate",
            "pt": "• **Todos os dragões Classe S desbloqueados**\n• Todas as terras desbloqueadas\n• **2 Bilhões de Comida**\n• Todos os habitats colocados\n• Mais de **90% dos dragões** no storage\n• Dragões mais fortes no **Nível 130**\n• Conta de nível divino pronta para dominar",
            "es": "• **Todos los dragones Clase S desbloqueados**\n• Todas las tierras desbloqueadas\n• **2 Mil Millones de Comida**\n• Todos los habitats colocados\n• Más del **90% de los dragones** en el storage\n• Dragones más fuertes en **Nivel 130**\n• Cuenta de nivel dios lista para dominar",
            "ru": "• **Все драконы S-класса открыты**\n• Все земли открыты\n• **2 миллиарда еды**\n• Все хабитаты размещены\n• Более **90% драконов** на складе\n• Сильнейшие драконы **уровень 130**\n• Аккаунт божественного уровня готов к доминированию",
        },
    },
]

# ==================== SERVICES ====================
DRAGON_PACKS = [
    {"id": "d300", "emoji": "🐉", "qty": 300, "price": 35},
    {"id": "d500", "emoji": "🐉", "qty": 500, "price": 50},
    {"id": "d1000", "emoji": "🐉", "qty": 1000, "price": 90},
    {"id": "d1400", "emoji": "🐉", "qty": 1400, "price": 130},
]

HABITAT_PACKS = [
    {"id": "h30", "emoji": "🏡", "qty": 30, "price": 30},
    {"id": "h50", "emoji": "🏡", "qty": 50, "price": 45},
    {"id": "h100", "emoji": "🏡", "qty": 100, "price": 80},
    {"id": "h150", "emoji": "🏡", "qty": 150, "price": 130},
]

# ==================== TRANSLATIONS ====================
TEXTS = {
    "ar": {
        "welcome": "🔥 *مرحبًا بك في متجر Dragon Mania* 🔥\n\nاختر لغتك المفضلة:",
        "main_menu": "🏠 *القائمة الرئيسية*\n\nاختر من القائمة التالية:",
        "contact_dev": "📞 *التواصل مع مطور البوت*\n\nاضغط الزر بالأسفل للتواصل معي مباشرة على تيليجرام.",
        "support": "🛠 *الدعم الفني*\n\nلأي استفسار أو مشكلة، تواصل معي مباشرة:",
        "payment": "💳 *طرق الدفع المتاحة*\n\n"
                   "🟡 *Binance ID:*\n`1202669996`\n\n"
                   "📱 *Vodafone Cash:*\n`+201061724535`\n\n"
                   "🎁 *بطاقات هدايا Binance*\n(مقبولة)\n\n"
                   "بعد التحويل أرسل صورة الإيصال للدعم الفني.",
        "accounts_list": "🐉 *الحسابات الكاملة المتاحة*\n\nاختر الحساب اللي عايزه:",
        "account_details": "{emoji} *{title}*\n\n{desc}\n\n💰 *السعر: ${price}*",
        "buy_now": "✅ عايز تشتري؟\nاضغط الزر وتواصل معايا فورًا.",
        "services": "🛠 *الخدمات*\n\nاختر نوع الخدمة:",
        "dragons_services": "🐉 *باقات التنانين العشوائية*\n\nاختر الباقة:",
        "habitats_services": "🏡 *باقات الموائل العشوائية*\n\nاختر الباقة:",
        "pack_details": "{emoji} *{qty} {item} عشوائي*\n\n💰 السعر: *${price}*\n\n✅ جاهز للتسليم فورًا بعد الدفع.",
        "guide": "📖 *دليل الاستخدام*\n\nهنا هتلاقي فيديو توضيحي لطريقة استخدام الحسابات والخدمات.\n\n(الفيديو هيضاف قريبًا)\n\nلو عندك أي سؤال تواصل مع الدعم.",
        "readme": "⚠️ *اقرأني مهم - قواعد الشراء*\n\n"
                  "⚡ *اصرف بسرعة:* عشان تاخد أقصى استفادة، اصرف الجواهر بأسرع ما يمكن بعد تسجيل الدخول! ارفع كل الأراضي ومزارع الطعام والتنانين والمعابد (هواء، أرض، ماء...).\n\n"
                  "💎 *نصيحة ذهبية للاحتفاظ بالجواهر:* لو عايز تحتفظ بكمية كبيرة من الجواهر حتى بعد الريسيت، اشتري بطاقات Starfall بالجواهر فورًا. بعد ما الرصيد الأولي يتصفر، لف/استرد بطاقات Starfall وهترجع لك كمية كبيرة وآمنة من الجواهر!\n\n"
                  "🛡 *السلامة وضمان الحظر:*\n"
                  "• استخدام الحساب آمن 100% ومفيش خطر حظر من الاستخدام العادي.\n"
                  "• في حالة الحظر المؤقت 7 أيام (نادر جدًا)، استنى المدة والحساب هيرجع سليم بكل التقدم.\n"
                  "• لو حصل حظر نهائي خلال أول 7 أيام من الشراء → هتستلم حساب بديل *مجاني 100%*.\n"
                  "• لو حصل حظر نهائي بعد 7 أيام → تقدر تاخد حساب بديل كامل مقابل *30 دولار* فقط.\n\n"
                  "💰 *السعر والاستفسارات:*\n"
                  "• السعر قابل للتفاوض، لكن *للمشترين الجادين فقط*.\n"
                  "• اقرأ الوصف كامل قبل ما تراسل. لو جاهز تشتري، يلا نخلص الموضوع!\n\n"
                  "🚫 *سياسة الاسترجاع:*\n"
                  "• مفيش استرجاع بعد تسليم بيانات الحساب.\n"
                  "• لو مش موافق على الشروط، ألغِ الطلب قبل إرسال البيانات وهتسترد فلوسك فورًا.",
        "back": "🔙 رجوع",
        "main_menu_btn": "🏠 القائمة الرئيسية",
        "contact_btn": "📞 التواصل مع المطور",
        "buy_btn": "🐉 شراء حسابات",
        "services_btn": "🛠 خدمات",
        "payment_btn": "💳 طرق الدفع",
        "support_btn": "🛠 الدعم الفني",
        "guide_btn": "📖 الدليل",
        "readme_btn": "⚠️ اقرأني مهم",
        "dragons_btn": "🐉 باقات التنانين",
        "habitats_btn": "🏡 باقات الموائل",
        "buy_this": "🛒 اشتري الآن",
        "contact_me": "💬 تواصل معي الآن",
        "footer": "\n\n━━━━━━━━━━━━━━\nمتجر Dragon Mania | @JUSTHOHOHO",
    },
    "en": {
        "welcome": "🔥 *Welcome to Dragon Mania Store* 🔥\n\nChoose your preferred language:",
        "main_menu": "🏠 *Main Menu*\n\nPlease select an option:",
        "contact_dev": "📞 *Contact Bot Developer*\n\nClick the button below to contact me directly on Telegram.",
        "support": "🛠 *Technical Support*\n\nFor any questions or issues, contact me directly:",
        "payment": "💳 *Available Payment Methods*\n\n"
                   "🟡 *Binance ID:*\n`1202669996`\n\n"
                   "📱 *Vodafone Cash:*\n`+201061724535`\n\n"
                   "🎁 *Binance Gift Cards*\n(Accepted)\n\n"
                   "After payment, send the receipt screenshot to support.",
        "accounts_list": "🐉 *Available Full Accounts*\n\nSelect an account:",
        "account_details": "{emoji} *{title}*\n\n{desc}\n\n💰 *Price: ${price}*",
        "buy_now": "✅ Want to buy?\nClick the button and contact me now.",
        "services": "🛠 *Services*\n\nChoose service type:",
        "dragons_services": "🐉 *Random Dragons Packages*\n\nSelect a package:",
        "habitats_services": "🏡 *Random Habitats Packages*\n\nSelect a package:",
        "pack_details": "{emoji} *{qty} Random {item}*\n\n💰 Price: *${price}*\n\n✅ Ready for instant delivery after payment.",
        "guide": "📖 *Usage Guide*\n\nHere you will find a tutorial video on how to use the accounts and services.\n\n(Video will be added soon)\n\nIf you have any questions, contact support.",
        "readme": "⚠️ *Important - Purchase Rules*\n\n"
                  "⚡ *Spend Fast:* To get the maximum value, spend your gems as fast as you can right after login! Max out all lands, food farms, dragons, and temples (Air, Earth, Water, etc.).\n\n"
                  "💎 *Keep Gems Forever (Golden Tip):* If you want to keep a massive amount of gems even after a reset, buy Starfall cards with your gems immediately. After the initial gem balance resets, simply spin/redeem your Starfall cards to get a huge, safe stack of gems back!\n\n"
                  "🛡 *SAFETY & BAN GUARANTEE:*\n"
                  "• Using this account is completely safe, and there is NO BAN RISK from normal usage.\n"
                  "• In the rare event of a 7-day temporary ban, simply wait it out—your account and all progress will remain completely intact after 7 days.\n"
                  "• If a permanent ban occurs within the first 7 days of purchase, you will receive a 100% FREE replacement account.\n"
                  "• If a permanent ban occurs after 7 days, you can get a full replacement account for just $30.\n\n"
                  "💰 *PRICE & INQUIRIES:*\n"
                  "• Price: Negotiable, but ONLY for serious buyers.\n"
                  "• Please read the full description carefully before messaging. If you are ready to buy, let's get straight to business!\n\n"
                  "🚫 *REFUND POLICY:*\n"
                  "• No Refunds After Delivery: Once account details are delivered and terms are agreed upon, all sales are final.\n"
                  "• If you do not agree to these terms, please cancel your order before the account data is sent for an instant refund.",
        "back": "🔙 Back",
        "main_menu_btn": "🏠 Main Menu",
        "contact_btn": "📞 Contact Developer",
        "buy_btn": "🐉 Buy Accounts",
        "services_btn": "🛠 Services",
        "payment_btn": "💳 Payment Methods",
        "support_btn": "🛠 Technical Support",
        "guide_btn": "📖 Guide",
        "readme_btn": "⚠️ Read Me Important",
        "dragons_btn": "🐉 Dragons Packages",
        "habitats_btn": "🏡 Habitats Packages",
        "buy_this": "🛒 Buy Now",
        "contact_me": "💬 Contact Me Now",
        "footer": "\n\n━━━━━━━━━━━━━━\nDragon Mania Store | @JUSTHOHOHO",
    },
    "pt": {
        "welcome": "🔥 *Bem-vindo à Loja Dragon Mania* 🔥\n\nEscolha seu idioma preferido:",
        "main_menu": "🏠 *Menu Principal*\n\nSelecione uma opção:",
        "contact_dev": "📞 *Contatar Desenvolvedor do Bot*\n\nClique no botão abaixo para me contatar diretamente no Telegram.",
        "support": "🛠 *Suporte Técnico*\n\nPara qualquer dúvida ou problema, entre em contato comigo:",
        "payment": "💳 *Métodos de Pagamento Disponíveis*\n\n"
                   "🟡 *Binance ID:*\n`1202669996`\n\n"
                   "📱 *Vodafone Cash:*\n`+201061724535`\n\n"
                   "🎁 *Cartões Presente Binance*\n(Aceitos)\n\n"
                   "Após o pagamento, envie o comprovante para o suporte.",
        "accounts_list": "🐉 *Contas Completas Disponíveis*\n\nSelecione uma conta:",
        "account_details": "{emoji} *{title}*\n\n{desc}\n\n💰 *Preço: ${price}*",
        "buy_now": "✅ Quer comprar?\nClique no botão e fale comigo agora.",
        "services": "🛠 *Serviços*\n\nEscolha o tipo de serviço:",
        "dragons_services": "🐉 *Pacotes de Dragões Aleatórios*\n\nSelecione um pacote:",
        "habitats_services": "🏡 *Pacotes de Habitats Aleatórios*\n\nSelecione um pacote:",
        "pack_details": "{emoji} *{qty} {item} Aleatórios*\n\n💰 Preço: *${price}*\n\n✅ Pronto para entrega imediata após o pagamento.",
        "guide": "📖 *Guia de Uso*\n\nAqui você encontrará um vídeo tutorial sobre como usar as contas e serviços.\n\n(O vídeo será adicionado em breve)\n\nSe tiver alguma dúvida, entre em contato com o suporte.",
        "readme": "⚠️ *Importante - Regras de Compra*\n\n"
                  "⚡ *Gaste Rápido:* Para obter o máximo valor, gaste suas gemas o mais rápido possível após o login! Maximize todas as terras, fazendas de comida, dragões e templos.\n\n"
                  "💎 *Dica de Ouro para Manter Gemas:* Se quiser manter uma grande quantidade de gemas mesmo após o reset, compre cartas Starfall com suas gemas imediatamente. Depois que o saldo inicial resetar, gire/resgate suas cartas Starfall para recuperar um grande estoque seguro de gemas!\n\n"
                  "🛡 *SEGURANÇA E GARANTIA CONTRA BAN:*\n"
                  "• Usar esta conta é completamente seguro, sem risco de ban por uso normal.\n"
                  "• Em caso raro de ban temporário de 7 dias, apenas aguarde — sua conta e progresso permanecerão intactos.\n"
                  "• Se ocorrer ban permanente nos primeiros 7 dias → você receberá uma conta de reposição *100% GRÁTIS*.\n"
                  "• Se ocorrer ban permanente após 7 dias → você pode obter uma conta completa de reposição por apenas *$30*.\n\n"
                  "💰 *PREÇO E CONSULTAS:*\n"
                  "• Preço negociável, mas APENAS para compradores sérios.\n"
                  "• Leia a descrição completa antes de enviar mensagem.\n\n"
                  "🚫 *POLÍTICA DE REEMBOLSO:*\n"
                  "• Sem reembolso após a entrega dos dados da conta.\n"
                  "• Se não concordar com os termos, cancele o pedido antes do envio dos dados para reembolso imediato.",
        "back": "🔙 Voltar",
        "main_menu_btn": "🏠 Menu Principal",
        "contact_btn": "📞 Contatar Desenvolvedor",
        "buy_btn": "🐉 Comprar Contas",
        "services_btn": "🛠 Serviços",
        "payment_btn": "💳 Métodos de Pagamento",
        "support_btn": "🛠 Suporte Técnico",
        "guide_btn": "📖 Guia",
        "readme_btn": "⚠️ Leia-me Importante",
        "dragons_btn": "🐉 Pacotes de Dragões",
        "habitats_btn": "🏡 Pacotes de Habitats",
        "buy_this": "🛒 Comprar Agora",
        "contact_me": "💬 Fale Comigo Agora",
        "footer": "\n\n━━━━━━━━━━━━━━\nLoja Dragon Mania | @JUSTHOHOHO",
    },
    "es": {
        "welcome": "🔥 *Bienvenido a la Tienda Dragon Mania* 🔥\n\nElige tu idioma preferido:",
        "main_menu": "🏠 *Menú Principal*\n\nSelecciona una opción:",
        "contact_dev": "📞 *Contactar al Desarrollador del Bot*\n\nHaz clic en el botón de abajo para contactarme directamente en Telegram.",
        "support": "🛠 *Soporte Técnico*\n\nPara cualquier consulta o problema, contáctame directamente:",
        "payment": "💳 *Métodos de Pago Disponibles*\n\n"
                   "🟡 *Binance ID:*\n`1202669996`\n\n"
                   "📱 *Vodafone Cash:*\n`+201061724535`\n\n"
                   "🎁 *Tarjetas de Regalo Binance*\n(Aceptadas)\n\n"
                   "Después del pago, envía la captura del recibo al soporte.",
        "accounts_list": "🐉 *Cuentas Completas Disponibles*\n\nSelecciona una cuenta:",
        "account_details": "{emoji} *{title}*\n\n{desc}\n\n💰 *Precio: ${price}*",
        "buy_now": "✅ ¿Quieres comprar?\nHaz clic en el botón y contáctame ahora.",
        "services": "🛠 *Servicios*\n\nElige el tipo de servicio:",
        "dragons_services": "🐉 *Paquetes de Dragones Aleatorios*\n\nSelecciona un paquete:",
        "habitats_services": "🏡 *Paquetes de Hábitats Aleatorios*\n\nSelecciona un paquete:",
        "pack_details": "{emoji} *{qty} {item} Aleatorios*\n\n💰 Precio: *${price}*\n\n✅ Listo para entrega inmediata después del pago.",
        "guide": "📖 *Guía de Uso*\n\nAquí encontrarás un video tutorial sobre cómo usar las cuentas y servicios.\n\n(El video se agregará pronto)\n\nSi tienes alguna pregunta, contacta al soporte.",
        "readme": "⚠️ *Importante - Reglas de Compra*\n\n"
                  "⚡ *Gasta Rápido:* Para obtener el máximo valor, gasta tus gemas lo más rápido posible después de iniciar sesión. Maximiza todas las tierras, granjas de comida, dragones y templos.\n\n"
                  "💎 *Consejo Dorado para Conservar Gemas:* Si quieres conservar una gran cantidad de gemas incluso después del reinicio, compra cartas Starfall con tus gemas inmediatamente. Después de que se reinicie el saldo inicial, gira/canjea tus cartas Starfall para recuperar una gran cantidad segura de gemas.\n\n"
                  "🛡 *SEGURIDAD Y GARANTÍA CONTRA BAN:*\n"
                  "• Usar esta cuenta es completamente seguro, sin riesgo de ban por uso normal.\n"
                  "• En el raro caso de un ban temporal de 7 días, simplemente espera: tu cuenta y progreso permanecerán intactos.\n"
                  "• Si ocurre un ban permanente en los primeros 7 días → recibirás una cuenta de reemplazo *100% GRATIS*.\n"
                  "• Si ocurre un ban permanente después de 7 días → puedes obtener una cuenta completa de reemplazo por solo *$30*.\n\n"
                  "💰 *PRECIO E INQUIRIES:*\n"
                  "• Precio negociable, pero SOLO para compradores serios.\n"
                  "• Lee la descripción completa antes de enviar mensaje.\n\n"
                  "🚫 *POLÍTICA DE REEMBOLSO:*\n"
                  "• Sin reembolsos después de la entrega de los datos de la cuenta.\n"
                  "• Si no estás de acuerdo con los términos, cancela el pedido antes del envío de los datos para un reembolso instantáneo.",
        "back": "🔙 Atrás",
        "main_menu_btn": "🏠 Menú Principal",
        "contact_btn": "📞 Contactar Desarrollador",
        "buy_btn": "🐉 Comprar Cuentas",
        "services_btn": "🛠 Servicios",
        "payment_btn": "💳 Métodos de Pago",
        "support_btn": "🛠 Soporte Técnico",
        "guide_btn": "📖 Guía",
        "readme_btn": "⚠️ Léeme Importante",
        "dragons_btn": "🐉 Paquetes de Dragones",
        "habitats_btn": "🏡 Paquetes de Hábitats",
        "buy_this": "🛒 Comprar Ahora",
        "contact_me": "💬 Contáctame Ahora",
        "footer": "\n\n━━━━━━━━━━━━━━\nTienda Dragon Mania | @JUSTHOHOHO",
    },
    "ru": {
        "welcome": "🔥 *Добро пожаловать в магазин Dragon Mania* 🔥\n\nВыберите предпочитаемый язык:",
        "main_menu": "🏠 *Главное меню*\n\nВыберите опцию:",
        "contact_dev": "📞 *Связь с разработчиком бота*\n\nНажмите кнопку ниже, чтобы связаться со мной напрямую в Telegram.",
        "support": "🛠 *Техническая поддержка*\n\nПо любым вопросам или проблемам свяжитесь со мной напрямую:",
        "payment": "💳 *Доступные способы оплаты*\n\n"
                   "🟡 *Binance ID:*\n`1202669996`\n\n"
                   "📱 *Vodafone Cash:*\n`+201061724535`\n\n"
                   "🎁 *Подарочные карты Binance*\n(Принимаются)\n\n"
                   "После оплаты отправьте скриншот чека в поддержку.",
        "accounts_list": "🐉 *Доступные полные аккаунты*\n\nВыберите аккаунт:",
        "account_details": "{emoji} *{title}*\n\n{desc}\n\n💰 *Цена: ${price}*",
        "buy_now": "✅ Хотите купить?\nНажмите кнопку и свяжитесь со мной сейчас.",
        "services": "🛠 *Услуги*\n\nВыберите тип услуги:",
        "dragons_services": "🐉 *Пакеты случайных драконов*\n\nВыберите пакет:",
        "habitats_services": "🏡 *Пакеты случайных хабитатов*\n\nВыберите пакет:",
        "pack_details": "{emoji} *{qty} случайных {item}*\n\n💰 Цена: *${price}*\n\n✅ Готово к мгновенной доставке после оплаты.",
        "guide": "📖 *Руководство по использованию*\n\nЗдесь будет обучающее видео о том, как использовать аккаунты и услуги.\n\n(Видео будет добавлено скоро)\n\nЕсли у вас есть вопросы, свяжитесь с поддержкой.",
        "readme": "⚠️ *Важно - Правила покупки*\n\n"
                  "⚡ *Тратьте быстро:* Чтобы получить максимальную пользу, тратьте гемы как можно быстрее после входа! Максимально улучшите все земли, фермы еды, драконов и храмы.\n\n"
                  "💎 *Золотой совет по сохранению гемов:* Если хотите сохранить большое количество гемов даже после сброса, сразу купите карты Starfall на гемы. После сброса начального баланса просто крутите/обменивайте карты Starfall и получите обратно большой безопасный запас гемов!\n\n"
                  "🛡 *БЕЗОПАСНОСТЬ И ГАРАНТИЯ ОТ БАНА:*\n"
                  "• Использование аккаунта полностью безопасно, риска бана при обычном использовании нет.\n"
                  "• В редком случае временного бана на 7 дней просто подождите — аккаунт и весь прогресс останутся целыми.\n"
                  "• Если произойдет перманентный бан в первые 7 дней после покупки → вы получите аккаунт на замену *100% БЕСПЛАТНО*.\n"
                  "• Если перманентный бан произойдет после 7 дней → вы можете получить полный аккаунт на замену всего за *$30*.\n\n"
                  "💰 *ЦЕНА И ВОПРОСЫ:*\n"
                  "• Цена договорная, но ТОЛЬКО для серьезных покупателей.\n"
                  "• Пожалуйста, внимательно прочитайте описание перед сообщением.\n\n"
                  "🚫 *ПОЛИТИКА ВОЗВРАТА:*\n"
                  "• Возврат после передачи данных аккаунта невозможен.\n"
                  "• Если вы не согласны с условиями, отмените заказ до отправки данных аккаунта для мгновенного возврата.",
        "back": "🔙 Назад",
        "main_menu_btn": "🏠 Главное меню",
        "contact_btn": "📞 Связаться с разработчиком",
        "buy_btn": "🐉 Купить аккаунты",
        "services_btn": "🛠 Услуги",
        "payment_btn": "💳 Способы оплаты",
        "support_btn": "🛠 Техподдержка",
        "guide_btn": "📖 Руководство",
        "readme_btn": "⚠️ Прочитай важно",
        "dragons_btn": "🐉 Пакеты драконов",
        "habitats_btn": "🏡 Пакеты хабитатов",
        "buy_this": "🛒 Купить сейчас",
        "contact_me": "💬 Связаться со мной",
        "footer": "\n\n━━━━━━━━━━━━━━\nМагазин Dragon Mania | @JUSTHOHOHO",
    },
}

# ==================== HELPERS ====================
def get_lang(context: ContextTypes.DEFAULT_TYPE) -> str:
    return context.user_data.get("lang", "ar")


def t(key: str, lang: str = "ar") -> str:
    return TEXTS.get(lang, TEXTS["ar"]).get(key, key)


def get_lang_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🇪🇬 العربية", callback_data="lang_ar"),
            InlineKeyboardButton("🇺🇸 English", callback_data="lang_en"),
        ],
        [
            InlineKeyboardButton("🇧🇷 Português", callback_data="lang_pt"),
            InlineKeyboardButton("🇪🇸 Español", callback_data="lang_es"),
        ],
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(t("contact_btn", lang), callback_data="menu_contact")],
        [InlineKeyboardButton(t("buy_btn", lang), callback_data="menu_accounts")],
        [InlineKeyboardButton(t("services_btn", lang), callback_data="menu_services")],
        [InlineKeyboardButton(t("payment_btn", lang), callback_data="menu_payment")],
        [InlineKeyboardButton(t("guide_btn", lang), callback_data="menu_guide")],
        [InlineKeyboardButton(t("readme_btn", lang), callback_data="menu_readme")],
        [InlineKeyboardButton(t("support_btn", lang), callback_data="menu_support")],
        [InlineKeyboardButton(t("main_menu_btn", lang), callback_data="back_to_lang")],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_services_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(t("dragons_btn", lang), callback_data="services_dragons")],
        [InlineKeyboardButton(t("habitats_btn", lang), callback_data="services_habitats")],
        [InlineKeyboardButton(t("back", lang), callback_data="back_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_accounts_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = []
    for acc in ACCOUNTS:
        title = acc["title"].get(lang, acc["title"]["en"])
        btn_text = f"{acc['emoji']} {title} — ${acc['price']}"
        keyboard.append([InlineKeyboardButton(btn_text, callback_data=f"acc_{acc['id']}")])
    keyboard.append([InlineKeyboardButton(t("back", lang), callback_data="back_main")])
    return InlineKeyboardMarkup(keyboard)


def get_dragon_packs_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = []
    item = {"ar": "تنين", "en": "Dragons", "pt": "Dragões", "es": "Dragones", "ru": "драконов"}.get(lang, "Dragons")
    for pack in DRAGON_PACKS:
        btn_text = f"{pack['emoji']} {pack['qty']} {item} — ${pack['price']}"
        keyboard.append([InlineKeyboardButton(btn_text, callback_data=f"pack_{pack['id']}")])
    keyboard.append([InlineKeyboardButton(t("back", lang), callback_data="menu_services")])
    return InlineKeyboardMarkup(keyboard)


def get_habitat_packs_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = []
    item = {"ar": "موئل", "en": "Habitats", "pt": "Habitats", "es": "Hábitats", "ru": "хабитатов"}.get(lang, "Habitats")
    for pack in HABITAT_PACKS:
        btn_text = f"{pack['emoji']} {pack['qty']} {item} — ${pack['price']}"
        keyboard.append([InlineKeyboardButton(btn_text, callback_data=f"pack_{pack['id']}")])
    keyboard.append([InlineKeyboardButton(t("back", lang), callback_data="menu_services")])
    return InlineKeyboardMarkup(keyboard)


def get_contact_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(t("contact_me", lang), url=OWNER_LINK)],
        [InlineKeyboardButton(t("back", lang), callback_data="back_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_back_main_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton(t("back", lang), callback_data="back_main")]])


# ==================== HANDLERS ====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.clear()
    await update.message.reply_text(
        TEXTS["ar"]["welcome"],
        reply_markup=get_lang_keyboard(),
        parse_mode=ParseMode.MARKDOWN,
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data
    lang = get_lang(context)

    # Language selection
    if data.startswith("lang_"):
        lang = data.split("_")[1]
        context.user_data["lang"] = lang
        text = t("main_menu", lang) + t("footer", lang)
        await query.edit_message_text(text=text, reply_markup=get_main_menu_keyboard(lang), parse_mode=ParseMode.MARKDOWN)
        return

    if data == "back_to_lang":
        context.user_data.clear()
        await query.edit_message_text(text=TEXTS["ar"]["welcome"], reply_markup=get_lang_keyboard(), parse_mode=ParseMode.MARKDOWN)
        return

    if data == "back_main":
        text = t("main_menu", lang) + t("footer", lang)
        await query.edit_message_text(text=text, reply_markup=get_main_menu_keyboard(lang), parse_mode=ParseMode.MARKDOWN)
        return

    # Contact
    if data == "menu_contact":
        text = t("contact_dev", lang) + t("footer", lang)
        await query.edit_message_text(text=text, reply_markup=get_contact_keyboard(lang), parse_mode=ParseMode.MARKDOWN)
        return

    # Support
    if data == "menu_support":
        text = t("support", lang) + t("footer", lang)
        await query.edit_message_text(text=text, reply_markup=get_contact_keyboard(lang), parse_mode=ParseMode.MARKDOWN)
        return

    # Payment
    if data == "menu_payment":
        text = t("payment", lang) + t("footer", lang)
        await query.edit_message_text(text=text, reply_markup=get_back_main_keyboard(lang), parse_mode=ParseMode.MARKDOWN)
        return

    # Guide
    if data == "menu_guide":
        text = t("guide", lang) + t("footer", lang)
        await query.edit_message_text(text=text, reply_markup=get_back_main_keyboard(lang), parse_mode=ParseMode.MARKDOWN)
        return

    # Readme
    if data == "menu_readme":
        text = t("readme", lang) + t("footer", lang)
        await query.edit_message_text(text=text, reply_markup=get_back_main_keyboard(lang), parse_mode=ParseMode.MARKDOWN)
        return

    # Accounts list
    if data == "menu_accounts":
        text = t("accounts_list", lang) + t("footer", lang)
        await query.edit_message_text(text=text, reply_markup=get_accounts_keyboard(lang), parse_mode=ParseMode.MARKDOWN)
        return

    # Specific account
    if data.startswith("acc_"):
        acc_id = data.split("_")[1]
        acc = next((a for a in ACCOUNTS if a["id"] == acc_id), None)
        if not acc:
            return
        title = acc["title"].get(lang, acc["title"]["en"])
        desc = acc["desc"].get(lang, acc["desc"]["en"])
        text = t("account_details", lang).format(emoji=acc["emoji"], title=title, desc=desc, price=acc["price"])
        text += "\n\n" + t("buy_now", lang) + t("footer", lang)
        keyboard = [
            [InlineKeyboardButton(t("buy_this", lang), url=OWNER_LINK)],
            [InlineKeyboardButton(t("back", lang), callback_data="menu_accounts")],
        ]
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN)
        return

    # Services menu
    if data == "menu_services":
        text = t("services", lang) + t("footer", lang)
        await query.edit_message_text(text=text, reply_markup=get_services_keyboard(lang), parse_mode=ParseMode.MARKDOWN)
        return

    # Dragons packages
    if data == "services_dragons":
        text = t("dragons_services", lang) + t("footer", lang)
        await query.edit_message_text(text=text, reply_markup=get_dragon_packs_keyboard(lang), parse_mode=ParseMode.MARKDOWN)
        return

    # Habitats packages
    if data == "services_habitats":
        text = t("habitats_services", lang) + t("footer", lang)
        await query.edit_message_text(text=text, reply_markup=get_habitat_packs_keyboard(lang), parse_mode=ParseMode.MARKDOWN)
        return

    # Specific pack
    if data.startswith("pack_"):
        pack_id = data.split("_")[1]
        pack = next((p for p in DRAGON_PACKS + HABITAT_PACKS if p["id"] == pack_id), None)
        if not pack:
            return

        is_dragon = pack_id.startswith("d")
        item_name = {
            "ar": "تنين" if is_dragon else "موئل",
            "en": "Dragons" if is_dragon else "Habitats",
            "pt": "Dragões" if is_dragon else "Habitats",
            "es": "Dragones" if is_dragon else "Hábitats",
            "ru": "драконов" if is_dragon else "хабитатов",
        }.get(lang, "items")

        text = t("pack_details", lang).format(
            emoji=pack["emoji"],
            qty=pack["qty"],
            item=item_name,
            price=pack["price"],
        )
        text += "\n\n" + t("buy_now", lang) + t("footer", lang)

        back_data = "services_dragons" if is_dragon else "services_habitats"
        keyboard = [
            [InlineKeyboardButton(t("buy_this", lang), url=OWNER_LINK)],
            [InlineKeyboardButton(t("back", lang), callback_data=back_data)],
        ]
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode=ParseMode.MARKDOWN)
        return


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_lang(context)
    await update.message.reply_text(
        t("main_menu", lang),
        reply_markup=get_main_menu_keyboard(lang),
        parse_mode=ParseMode.MARKDOWN,
    )

async def get_media_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    message = update.effective_message

    if not user or user.username != OWNER_USERNAME or not message:
        return

    if message.video:
        file_id = message.video.file_id
    elif message.photo:
        file_id = message.photo[-1].file_id
    else:
        return

    await message.reply_text(f"File ID:\n{file_id}")


def main() -> None:
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logger = logging.getLogger(__name__)

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
application.add_handler(
    MessageHandler(
        (filters.VIDEO | filters.PHOTO) & filters.ChatType.PRIVATE,
        get_media_file_id
    )
)
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))
    logger.info("Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
