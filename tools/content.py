# -*- coding: utf-8 -*-
"""All site copy in one place. English is the master language (business English);
AZ and RU are translations. Edit here, then run `python3 tools/build.py`.
"""

LANGS = ["az", "en", "ru"]
DEFAULT_LANG = "az"   # served at the site root; others under /en/, /ru/
LANG_LABEL = {"en": "EN", "az": "AZ", "ru": "RU"}
LANG_HTML = {"en": "en", "az": "az", "ru": "ru"}


def T(en, az, ru):
    return {"en": en, "az": az, "ru": ru}


COMPANY = {
    "brand": "BIONUT",
    "legal": T("Gilan Gabala Food Products Manufacturing OJSC",
               "“Gilan Qəbələ Qida Məhsullarının İstehsalı” ASC",
               "ОАО «Гилан Габала по производству пищевых продуктов»"),
    "address": T("4 A. Aliyev St., Zaragan village, Gabala District, AZ3630, Azerbaijan",
                 "Ə.Əliyev 4, Zarağan kəndi, Qəbələ rayonu, AZ3630, Azərbaycan",
                 "ул. А. Алиева 4, с. Зараган, Габалинский район, AZ3630, Азербайджан"),
    "phones": ["+994 50 290 20 70", "+994 50 290 19 95"],
    "emails": ["info@bionut.az", "rahib.rahimov@bionut.az", "anar.ismayilov@bionut.az"],
    "map_query": "Zarağan, Qəbələ, Azerbaijan",
    "copyright": "© 2026 Bionut. All rights reserved.",
}

# ---------------------------------------------------------------- navigation
NAV = [
    ("home", T("Home", "Ana səhifə", "Главная")),
    ("about", T("About Us", "Haqqımızda", "О компании")),
    ("products", T("Products", "Məhsullar", "Продукция")),
    ("process", T("Process & Quality", "Proses və Keyfiyyət", "Процесс и качество")),
    ("certifications", T("Certifications", "Sertifikatlar", "Сертификаты")),
    ("contact", T("Contact", "Əlaqə", "Контакты")),
]

UI = {
    "skip": T("Skip to content", "Məzmuna keç", "Перейти к содержанию"),
    "menu": T("Menu", "Menyu", "Меню"),
    "close": T("Close", "Bağla", "Закрыть"),
    "contact_btn": T("Contact Sales", "Satış şöbəsi", "Отдел продаж"),
    "insights": T("Insights", "Bilgi Mərkəzi", "Аналитика"),
    "read_more": T("Read article", "Məqaləni oxu", "Читать статью"),
    "view_product": T("View product", "Məhsula bax", "Подробнее"),
    "all_products": T("View all products", "Bütün məhsullar", "Вся продукция"),
    "moisture": T("Moisture", "Nəmlik", "Влажность"),
    "calibers": T("Calibers", "Kalibrlər", "Калибры"),
    "sizes": T("Particle sizes", "Kalibrlər", "Размер частиц"),
    "packaging": T("Packaging", "Qablaşdırma", "Упаковка"),
    "applications": T("Applications", "İstifadə sahələri", "Области применения"),
    "upon_request": T("Upon request", "Sorğu əsasında", "По запросу"),
    "download_spec": T("Download Product Specification (PDF)", "Məhsul spesifikasiyasını yüklə (PDF)", "Скачать спецификацию (PDF)"),
    "request_quote": T("Request a Quote", "Qiymət təklifi istə", "Запросить предложение"),
    "related": T("Related products", "Oxşar məhsullar", "Похожие продукты"),
    "moq_title": T("Minimum Order Quantity", "Minimum sifariş həcmi", "Минимальный объём заказа"),
    "moq": T("Minimum Order Quantity (MOQ): Starting from 1 MT (1,000 kg). For international export shipments, full pallet or container loads (FCL/LCL) are recommended to optimize logistics efficiency.",
             "Minimum sifariş həcmi (MOQ): 1 MT-dan (1 000 kq) başlayaraq. Beynəlxalq ixrac daşımaları üçün logistik səmərəliliyi artırmaq məqsədilə tam palet və ya konteyner yükləri (FCL/LCL) tövsiyə olunur.",
             "Минимальный объём заказа (MOQ): от 1 MT (1 000 кг). Для международных экспортных поставок рекомендуются полные паллеты или контейнерные партии (FCL/LCL) для оптимизации логистики."),
    "spec_table": T("Technical specification", "Texniki spesifikasiya", "Техническая спецификация"),
    "origin": T("Origin", "Mənşə", "Происхождение"),
    "origin_val": T("Gabala, Azerbaijan (own orchards)", "Qəbələ, Azərbaycan (öz bağlarımız)", "Габала, Азербайджан (собственные сады)"),
    "breadcrumb_home": T("Home", "Ana səhifə", "Главная"),
    "back_insights": T("All insights", "Bütün məqalələr", "Все статьи"),
    "source": T("Source", "Mənbə", "Источник"),
    "sources": T("Sources", "Mənbələr", "Источники"),
    "published": T("Published", "Dərc edilib", "Опубликовано"),
    "min_read": T("min read", "dəq oxu", "мин чтения"),
    "footer_tag": T("Premium hazelnut ingredients from our own orchards in Gabala, Azerbaijan, cultivated, processed and supplied to food manufacturers worldwide since 2005.",
                    "Qəbələdəki öz bağlarımızdan premium fındıq inqrediyentləri, 2005-ci ildən bəri yetişdirilir, emal olunur və dünya üzrə qida istehsalçılarına təqdim edilir.",
                    "Премиальные ингредиенты из фундука из собственных садов в Габале, Азербайджан, выращиваем, перерабатываем и поставляем производителям продуктов питания по всему миру с 2005 года."),
    "footer_company": T("Company", "Şirkət", "Компания"),
    "footer_products": T("Products", "Məhsullar", "Продукция"),
    "footer_contact": T("Contact", "Əlaqə", "Контакты"),
    "address": T("Address", "Ünvan", "Адрес"),
    "phone": T("Phone", "Telefon", "Телефон"),
    "email": T("Email", "E-poçt", "Эл. почта"),
    "tagline": T("Gabala · Azerbaijan", "Qəbələ · Azərbaycan", "Габала · Азербайджан"),
    "since": T("Since", "Təsis", "Основана"),
    "gabala": T("Gabala", "Qəbələ", "Габала"),
    "azerbaijan": T("Azerbaijan", "Azərbaycan", "Азербайджан"),
    "lang_label": T("Language", "Dil", "Язык"),
}

# ---------------------------------------------------------------- home
HOME = {
    "title": T("Bionut | Premium Hazelnut Ingredients from Azerbaijan",
               "Bionut | Azərbaycandan Premium Fındıq İnqrediyentləri",
               "Bionut | премиальные ингредиенты из фундука из Азербайджана"),
    "meta": T("Bionut cultivates, processes and supplies premium hazelnut kernels, roasted, chopped and flour products from 500+ hectares of own orchards in Gabala, Azerbaijan. FSSC 22000 & ISO 22000 certified.",
              "Bionut Qəbələdəki 500+ hektar öz bağlarından premium fındıq ləpəsi, qovrulmuş, doğranmış fındıq və fındıq unu yetişdirir, emal edir və tədarük edir. FSSC 22000 və ISO 22000 sertifikatlı.",
              "Bionut выращивает, перерабатывает и поставляет ядра фундука, обжаренный, дроблёный фундук и муку из 500+ гектаров собственных садов в Габале, Азербайджан. Сертификаты FSSC 22000 и ISO 22000."),
    "eyebrow": T("Gabala · Azerbaijan · Since 2005", "Qəbələ · Azərbaycan · 2005-ci ildən", "Габала · Азербайджан · с 2005 года"),
    "h1": T("Premium Hazelnut Ingredients from Azerbaijan",
            "Azərbaycandan Premium Fındıq İnqrediyentləri",
            "Премиальные ингредиенты из фундука из Азербайджана"),
    "lead": T("From our own orchards in Gabala to global markets. We cultivate, process and supply premium hazelnut ingredients for international food manufacturers.",
              "Qəbələdəki öz bağlarımızdan qlobal bazarlara. Beynəlxalq qida istehsalçıları üçün premium fındıq inqrediyentlərini yetişdirir, emal edir və tədarük edirik.",
              "Из собственных садов в Габале, на мировые рынки. Мы выращиваем, перерабатываем и поставляем премиальные ингредиенты из фундука для международных производителей продуктов питания."),
    "cta1": T("Explore Our Products", "Məhsullarımızla tanış olun", "Наша продукция"),
    "cta2": T("Contact Our Sales Team", "Satış komandamızla əlaqə", "Связаться с отделом продаж"),
    "hero_caption": T("Own orchards at the foot of the Greater Caucasus, Gabala",
                      "Böyük Qafqazın ətəyində öz bağlarımız, Qəbələ",
                      "Собственные сады у подножия Большого Кавказа, Габала"),
    "slides": [
        ("hero-orchard", T("Origin", "Mənşə", "Происхождение"),
         T("500+ hectares of own orchards at the foot of the Greater Caucasus", "Böyük Qafqazın ətəyində 500+ hektar öz bağlarımız", "500+ гектаров собственных садов у подножия Большого Кавказа")),
        ("hero-branch", T("Harvest", "Məhsul", "Урожай"),
         T("Premium hazelnuts ripening in our Gabala orchards", "Qəbələ bağlarımızda yetişən premium fındıq", "Премиальный фундук созревает в наших садах Габалы")),
        ("hero-production", T("Production", "İstehsal", "Производство"),
         T("Modern processing facility with over 20 tons of daily capacity", "Gündəlik 20 tondan çox emal gücünə malik müasir müəssisə", "Современное производство мощностью более 20 тонн в сутки")),
        ("warehouse-pallets", T("Export", "İxrac", "Экспорт"),
         T("Processed, packed and shipped to food manufacturers worldwide", "Emal olunur, qablaşdırılır və dünya üzrə qida istehsalçılarına göndərilir", "Перерабатывается, упаковывается и отгружается производителям по всему миру")),
    ],
    "scroll": T("Scroll", "Aşağı", "Вниз"),
    "marquee": [
        T("Natural Hazelnut Kernels", "Təbii Fındıq Ləpəsi", "Натуральные ядра фундука"),
        T("FSSC 22000", "FSSC 22000", "FSSC 22000"),
        T("Blanched Kernels", "Ağardılmış Ləpə", "Бланшированные ядра"),
        T("ISO 22000:2018", "ISO 22000:2018", "ISO 22000:2018"),
        T("Roasted Kernels", "Qovrulmuş Ləpə", "Обжаренные ядра"),
        T("Organic / Bio", "Üzvi / Bio", "Органик / Bio"),
        T("Roasted & Chopped", "Qovrulmuş və Doğranmış", "Обжаренный дроблёный"),
        T("SEDEX Member", "SEDEX Üzvü", "Член SEDEX"),
        T("Hazelnut Flour", "Fındıq Unu", "Ореховая мука"),
        T("In-Shell Hazelnuts", "Qabıqlı Fındıq", "Фундук в скорлупе"),
        T("Made in Gabala, Azerbaijan", "Qəbələ, Azərbaycan istehsalı", "Произведено в Габале, Азербайджан"),
    ],
    "stats": [
        ("500", "+", T("Hectares of Own Orchards", "Hektar öz fındıq bağları", "Гектаров собственных садов")),
        ("7,000", "+", T("Tons Annual Production Volume", "Ton illik istehsal həcmi", "Тонн годового объёма производства")),
        ("20", "+", T("Tons Average Daily Processing Capacity", "Ton orta gündəlik emal gücü", "Тонн среднесуточной мощности переработки")),
        ("20", "+", T("Years of Export Experience (Since 2005)", "İl ixrac təcrübəsi (2005-ci ildən)", "Лет экспортного опыта (с 2005 года)")),
    ],
    "intro_eyebrow": T("Orchard to market", "Bağdan bazara", "От сада до рынка"),
    "intro_h": T("One company. Every step under our own control.",
                 "Bir şirkət. Hər mərhələ öz nəzarətimizdə.",
                 "Одна компания. Каждый этап, под нашим контролем."),
    "intro_p": T("Bionut grows hazelnuts on more than 500 hectares of its own orchards in Gabala, in the foothills of the Greater Caucasus. Harvest, processing, laboratory control and export packing all take place within one integrated operation, giving food manufacturers consistent quality, full traceability and a reliable partner for long-term supply.",
                 "Bionut fındığı Böyük Qafqazın ətəklərində, Qəbələdəki 500 hektardan çox öz bağlarında yetişdirir. Məhsul yığımı, emal, laboratoriya nəzarəti və ixrac qablaşdırması vahid inteqrasiya olunmuş istehsal daxilində həyata keçirilir, bu da qida istehsalçılarına sabit keyfiyyət, tam izlənilmə və uzunmüddətli tədarük üçün etibarlı tərəfdaş təmin edir.",
                 "Bionut выращивает фундук на более чем 500 гектарах собственных садов в Габале, в предгорьях Большого Кавказа. Сбор урожая, переработка, лабораторный контроль и экспортная упаковка выполняются в рамках единого интегрированного производства, это обеспечивает производителям стабильное качество, полную прослеживаемость и надёжного партнёра для долгосрочных поставок."),
    "intro_points": [
        T("Organic and conventional production", "Üzvi və ənənəvi istehsal", "Органическое и традиционное производство"),
        T("In-house laboratory and metal detection", "Daxili laboratoriya və metal detektor", "Собственная лаборатория и металлодетекция"),
        T("Bulk and retail packaging formats", "Toplu və pərakəndə qablaşdırma formatları", "Оптовая и розничная упаковка"),
    ],
    "intro_link": T("About Bionut", "Bionut haqqında", "О компании Bionut"),
    "products_eyebrow": T("Our products", "Məhsullarımız", "Наша продукция"),
    "products_h": T("Hazelnut ingredients for industrial food manufacturing",
                    "Sənaye qida istehsalı üçün fındıq inqrediyentləri",
                    "Ингредиенты из фундука для пищевой промышленности"),
    "products_p": T("Six product lines, each processed to precise moisture and size specifications and available in bulk and retail packaging.",
                    "Altı məhsul xətti, hər biri dəqiq nəmlik və ölçü spesifikasiyalarına uyğun emal olunur, toplu və pərakəndə qablaşdırmada təqdim edilir.",
                    "Шесть продуктовых линеек, каждая обрабатывается по точным спецификациям влажности и размера и поставляется в оптовой и розничной упаковке."),
    "process_eyebrow": T("Process & quality", "Proses və keyfiyyət", "Процесс и качество"),
    "process_h": T("From blossom to container in four controlled stages",
                   "Çiçəkdən konteynerə qədər dörd nəzarətli mərhələ",
                   "От цветения до контейнера: четыре контролируемых этапа"),
    "process_link": T("Our process in detail", "Prosesimiz ətraflı", "Подробнее о процессе"),
    "quality_h": T("A quality system built into every batch", "Hər partiyaya inteqrasiya olunmuş keyfiyyət sistemi", "Система качества в каждой партии"),
    "cert_eyebrow": T("Certifications", "Sertifikatlar", "Сертификаты"),
    "cert_h": T("Internationally recognised food safety standards",
                "Beynəlxalq səviyyədə tanınan qida təhlükəsizliyi standartları",
                "Международно признанные стандарты безопасности пищевых продуктов"),
    "cert_link": T("View certificates", "Sertifikatlara bax", "Смотреть сертификаты"),
    "markets_eyebrow": T("Global markets", "Qlobal bazarlar", "Мировые рынки"),
    "markets_h": T("Trusted by food manufacturers across three continents",
                   "Üç qitədə qida istehsalçılarının etibar etdiyi tərəfdaş",
                   "Нам доверяют производители продуктов питания на трёх континентах"),
    "markets_p": T("From Gabala, Bionut hazelnuts are shipped to confectionery, bakery and food processing customers in Europe, the Middle East, North America and Asia.",
                   "Bionut fındığı Qəbələdən Avropa, Yaxın Şərq, Şimali Amerika və Asiyadakı qənnadı, çörək-bulka və qida emalı müştərilərinə göndərilir.",
                   "Из Габалы фундук Bionut поставляется кондитерским, хлебопекарным и пищевым предприятиям в Европе, на Ближнем Востоке, в Северной Америке и Азии."),
    "markets_origin": T("Origin: Gabala, Azerbaijan", "Mənşə: Qəbələ, Azərbaycan", "Происхождение: Габала, Азербайджан"),
    "insights_eyebrow": T("Insights", "Bilgi Mərkəzi", "Аналитика"),
    "insights_h": T("Market and quality intelligence", "Bazar və keyfiyyət üzrə analitika", "Рыночная аналитика и качество"),
    "cta_h": T("Looking for a reliable hazelnut supplier?", "Etibarlı fındıq tədarükçüsü axtarırsınız?", "Ищете надёжного поставщика фундука?"),
    "cta_p": T("Tell us your product, specification and volume. Our sales team will reply with availability and a tailored offer.",
               "Məhsulu, spesifikasiyanı və həcmi bizə bildirin. Satış komandamız mövcudluq və fərdi təkliflə cavab verəcək.",
               "Сообщите нам продукт, спецификацию и объём. Наш отдел продаж ответит с информацией о наличии и индивидуальным предложением."),
}

MARKETS = [
    ("DE", "276", T("Germany", "Almaniya", "Германия")),
    ("IT", "380", T("Italy", "İtaliya", "Италия")),
    ("TR", "792", T("Türkiye", "Türkiyə", "Турция")),
    ("CA", "124", T("Canada", "Kanada", "Канада")),
    ("RU", "643", T("Russia", "Rusiya", "Россия")),
    ("EG", "818", T("Egypt", "Misir", "Египет")),
    ("IN", "356", T("India", "Hindistan", "Индия")),
]

# ---------------------------------------------------------------- process
STEPS = [
    {"img": "step-cultivation",
     "t": T("Cultivation & Harvest", "Yetişdirmə və Məhsul Yığımı", "Выращивание и сбор урожая"),
     "s": T("Own orchards, Gabala", "Öz bağlarımız, Qəbələ", "Собственные сады, Габала"),
     "p": T("Our 500+ hectares of orchards in Gabala are managed by agronomists with more than 20 years of hazelnut experience, following ecological production practices. Nuts are harvested at optimal maturity.",
            "Qəbələdəki 500+ hektar bağlarımız fındıqçılıqda 20 ildən artıq təcrübəsi olan aqronomlar tərəfindən ekoloji istehsal təcrübələrinə uyğun idarə olunur. Fındıq optimal yetişkənlik dövründə yığılır.",
            "Наши 500+ гектаров садов в Габале обслуживают агрономы с более чем 20-летним опытом, следуя экологическим принципам производства. Орехи собирают в период оптимальной зрелости.")},
    {"img": "step-processing",
     "t": T("Processing", "Emal", "Переработка"),
     "s": T("Modern processing facility", "Müasir emal müəssisəsi", "Современное производство"),
     "p": T("Cracking, sorting, calibration, blanching, roasting, chopping and milling are carried out in our modern facility, with a processing capacity of more than 20 tons per day.",
            "Qırma, çeşidləmə, kalibrləmə, ağardılma, qovurma, doğrama və üyütmə gündəlik 20 tondan çox emal gücünə malik müasir müəssisəmizdə həyata keçirilir.",
            "Колка, сортировка, калибровка, бланширование, обжарка, дробление и помол выполняются на нашем современном предприятии мощностью более 20 тонн в сутки.")},
    {"img": "step-quality",
     "t": T("Quality Control", "Keyfiyyət Nəzarəti", "Контроль качества"),
     "s": T("Laboratory & metal detection", "Laboratoriya və metal detektor", "Лаборатория и металлодетекция"),
     "p": T("Every lot is tested in our in-house laboratory for moisture and quality parameters, and finished products pass through metal detection before packing.",
            "Hər partiya daxili laboratoriyamızda nəmlik və keyfiyyət göstəriciləri üzrə yoxlanılır, hazır məhsul isə qablaşdırmadan əvvəl metal detektordan keçir.",
            "Каждая партия проверяется в нашей лаборатории на влажность и показатели качества, а готовая продукция проходит металлодетекцию перед упаковкой.")},
    {"img": "warehouse-pallets",
     "t": T("Packaging & Export", "Qablaşdırma və İxrac", "Упаковка и экспорт"),
     "s": T("Bulk & retail formats", "Toplu və pərakəndə formatlar", "Оптовые и розничные форматы"),
     "p": T("Products are packed in vacuum bags, paper bags, PP bags, big bags or retail packs, palletised and shipped as FCL or LCL loads to customers worldwide.",
            "Məhsullar vakuum, kağız, PP kisələrə, big bag-lara və ya pərakəndə qablara qablaşdırılır, paletlənir və FCL və ya LCL yükləri ilə dünya üzrə müştərilərə göndərilir.",
            "Продукция упаковывается в вакуумные, бумажные, полипропиленовые мешки, биг-бэги или розничную упаковку, паллетируется и отгружается партиями FCL или LCL клиентам по всему миру.")},
]

QUALITY = [
    ("lab", T("In-House Laboratory", "Daxili Laboratoriya", "Собственная лаборатория"),
     T("Moisture, size and quality parameters are tested on site for every production lot.",
       "Hər istehsal partiyası üçün nəmlik, ölçü və keyfiyyət göstəriciləri yerində yoxlanılır.",
       "Влажность, размер и показатели качества проверяются на месте для каждой партии.")),
    ("metal", T("Metal Detection", "Metal Detektor", "Металлодетекция"),
     T("Finished products pass through metal detection before packing.",
       "Hazır məhsul qablaşdırmadan əvvəl metal detektordan keçir.",
       "Готовая продукция проходит металлодетекцию перед упаковкой.")),
    ("raw", T("Raw Material Inspection", "Xammalın Yoxlanılması", "Входной контроль сырья"),
     T("Incoming nuts are inspected and graded before entering production.",
       "Daxil olan fındıq istehsala buraxılmazdan əvvəl yoxlanılır və çeşidlənir.",
       "Поступающие орехи проверяются и сортируются до запуска в производство.")),
    ("monitor", T("Production Monitoring", "İstehsalın Monitorinqi", "Мониторинг производства"),
     T("Critical process parameters are monitored and recorded at each stage.",
       "Kritik proses parametrləri hər mərhələdə izlənilir və qeydə alınır.",
       "Критические параметры процесса контролируются и фиксируются на каждом этапе.")),
    ("finished", T("Finished Product Inspection", "Hazır Məhsulun Yoxlanılması", "Контроль готовой продукции"),
     T("Each batch is checked against its specification before release.",
       "Hər partiya buraxılmazdan əvvəl spesifikasiyaya uyğunluq üzrə yoxlanılır.",
       "Каждая партия проверяется на соответствие спецификации перед отгрузкой.")),
    ("trace", T("Traceability", "İzlənilmə", "Прослеживаемость"),
     T("Every lot can be traced from orchard to shipment.",
       "Hər partiya bağdan göndərişə qədər izlənilə bilər.",
       "Каждую партию можно отследить от сада до отгрузки.")),
]

PROCESS_PAGE = {
    "title": T("Process & Quality", "Proses və Keyfiyyət", "Процесс и качество"),
    "meta": T("How Bionut grows, processes, tests and exports hazelnut ingredients: four controlled stages and a quality system with in-house laboratory, metal detection and full traceability.",
              "Bionut fındıq inqrediyentlərini necə yetişdirir, emal edir, yoxlayır və ixrac edir: dörd nəzarətli mərhələ və daxili laboratoriya, metal detektor və tam izlənilmə ilə keyfiyyət sistemi.",
              "Как Bionut выращивает, перерабатывает, проверяет и экспортирует фундук: четыре контролируемых этапа и система качества с собственной лабораторией, металлодетекцией и полной прослеживаемостью."),
    "eyebrow": T("Process & quality", "Proses və keyfiyyət", "Процесс и качество"),
    "h1": T("Integrated from orchard to shipment", "Bağdan göndərişə qədər inteqrasiya olunmuş", "Интеграция от сада до отгрузки"),
    "lead": T("Because we grow, process and pack our own hazelnuts, every stage is managed by our own team, with controls that protect quality, safety and consistency for our customers.",
              "Fındığımızı özümüz yetişdirdiyimiz, emal etdiyimiz və qablaşdırdığımız üçün hər mərhələ öz komandamız tərəfindən idarə olunur, müştərilərimiz üçün keyfiyyəti, təhlükəsizliyi və sabitliyi qoruyan nəzarətlərlə.",
              "Поскольку мы сами выращиваем, перерабатываем и упаковываем фундук, каждый этап находится под управлением нашей команды, с контролем, который гарантирует клиентам качество, безопасность и стабильность."),
    "stages_h": T("Four production stages", "Dörd istehsal mərhələsi", "Четыре этапа производства"),
    "quality_eyebrow": T("Quality system", "Keyfiyyət sistemi", "Система качества"),
    "quality_h": T("Six controls behind every shipment", "Hər göndərişin arxasında altı nəzarət", "Шесть видов контроля в каждой поставке"),
    "quality_p": T("Our food safety management system is certified to FSSC 22000 and ISO 22000:2018.",
                   "Qida təhlükəsizliyi idarəetmə sistemimiz FSSC 22000 və ISO 22000:2018 üzrə sertifikatlaşdırılıb.",
                   "Наша система менеджмента безопасности пищевой продукции сертифицирована по FSSC 22000 и ISO 22000:2018."),
}

# ---------------------------------------------------------------- products
PRODUCTS = [
    {
        "slug": "natural-hazelnut-kernels", "img": "p-natural", "gallery": ["g-natural-vacuum", "g-natural-carton2", "g-natural-carton"],
        "name": T("Natural Hazelnut Kernels", "Təbii Fındıq Ləpəsi", "Натуральные ядра фундука"),
        "short": T("Premium selected natural hazelnut kernels, carefully processed for food manufacturers.",
                   "Qida istehsalçıları üçün diqqətlə emal olunmuş, seçilmiş premium təbii fındıq ləpəsi.",
                   "Отборные натуральные ядра фундука премиум-класса, тщательно обработанные для производителей продуктов питания."),
        "long": T("Our natural kernels are cracked from hazelnuts grown in our own Gabala orchards, then sorted and calibrated to deliver uniform size and clean, sweet flavour. They are the ideal base for roasting, blanching and further processing in confectionery and food production.",
                  "Təbii ləpələrimiz Qəbələdəki öz bağlarımızda yetişdirilən fındıqdan qırılır, sonra vahid ölçü və təmiz, şirin dad təmin etmək üçün çeşidlənir və kalibrlənir. Qənnadı və qida istehsalında qovurma, ağardılma və sonrakı emal üçün ideal əsasdır.",
                  "Натуральные ядра получают из фундука, выращенного в наших садах в Габале, затем сортируют и калибруют для однородного размера и чистого сладкого вкуса. Идеальная основа для обжарки, бланширования и дальнейшей переработки в кондитерском и пищевом производстве."),
        "moisture": "Max. 6%", "size_kind": "calibers", "sizes": ["9–11 mm", "11–13 mm", "13–15 mm"],
        "packaging": T("25 kg vacuum bags · 25 kg paper bags · 40 kg PP bags · 1000 kg Big Bags",
                       "25 kq vakuum kisələr · 25 kq kağız kisələr · 40 kq PP kisələr · 1000 kq Big Bag",
                       "Вакуумные мешки 25 кг · бумажные мешки 25 кг · ПП-мешки 40 кг · биг-бэги 1000 кг"),
        "apps": [T("Chocolate & confectionery", "Şokolad və qənnadı", "Шоколад и кондитерские изделия"),
                 T("Roasting & blanching", "Qovurma və ağardılma", "Обжарка и бланширование"),
                 T("Spreads & pastes", "Kremlər və pastalar", "Пасты и спреды"),
                 T("Bakery", "Çörək-bulka məmulatları", "Хлебобулочные изделия")],
    },
    {
        "slug": "blanched-hazelnut-kernels", "img": "p-blanched", "gallery": ["g-blanched-vacuum"],
        "name": T("Blanched Hazelnut Kernels", "Ağardılmış Fındıq Ləpəsi", "Бланшированные ядра фундука"),
        "short": T("Carefully blanched hazelnut kernels with the skin removed, suitable for various food manufacturing applications.",
                   "Qabığı təmizlənmiş, diqqətlə ağardılmış fındıq ləpəsi, müxtəlif qida istehsalı sahələri üçün.",
                   "Тщательно бланшированные ядра фундука без кожицы для различных пищевых производств."),
        "long": T("Gentle heat treatment removes the inner skin, revealing a clean, ivory-coloured kernel with a mild, buttery taste. Blanched kernels give a smooth colour and texture in pralines, fillings, ice cream and premium bakery.",
                  "Yumşaq istilik emalı daxili qabığı təmizləyir və zərif, kərəyağı dadlı, fil sümüyü rəngli təmiz ləpə əldə edilir. Ağardılmış ləpə pralinlərdə, içliklərdə, dondurmada və premium çörək-bulka məmulatlarında hamar rəng və tekstura verir.",
                  "Мягкая термообработка удаляет внутреннюю кожицу, открывая чистое ядро цвета слоновой кости с мягким сливочным вкусом. Бланшированные ядра обеспечивают ровный цвет и текстуру в пралине, начинках, мороженом и премиальной выпечке."),
        "moisture": "Max. 4%", "size_kind": "calibers", "sizes": ["11–13 mm", "13–15 mm"],
        "packaging": T("200 g, 400 g retail packs · 20 kg, 25 kg vacuum bags",
                       "200 q, 400 q pərakəndə qablar · 20 kq, 25 kq vakuum kisələr",
                       "Розничная упаковка 200 г, 400 г · вакуумные мешки 20 кг, 25 кг"),
        "apps": [T("Pralines & fillings", "Pralinlər və içliklər", "Пралине и начинки"),
                 T("Ice cream & dairy", "Dondurma və süd məhsulları", "Мороженое и молочные продукты"),
                 T("Premium bakery", "Premium çörək-bulka", "Премиальная выпечка"),
                 T("Snack mixes", "Qəlyanaltı qarışıqları", "Снековые смеси")],
    },
    {
        "slug": "roasted-hazelnut-kernels", "img": "p-roasted", "gallery": ["p-blanched"],
        "name": T("Roasted Hazelnut Kernels", "Qovrulmuş Fındıq Ləpəsi", "Обжаренные ядра фундука"),
        "short": T("Carefully roasted hazelnut kernels with a rich flavour and aroma, suitable for confectionery and food manufacturing.",
                   "Zəngin dad və ətirli, diqqətlə qovrulmuş fındıq ləpəsi, qənnadı və qida istehsalı üçün.",
                   "Тщательно обжаренные ядра фундука с насыщенным вкусом и ароматом для кондитерского и пищевого производства."),
        "long": T("Roasted under controlled time and temperature to develop a deep golden colour, crunchy texture and the characteristic aroma that defines premium hazelnut products.",
                  "Dərin qızılı rəng, xırtıldayan tekstura və premium fındıq məhsullarını fərqləndirən xarakterik ətir əldə etmək üçün nəzarət olunan vaxt və temperaturda qovrulur.",
                  "Обжариваются при контролируемом времени и температуре, приобретая глубокий золотистый цвет, хрустящую текстуру и характерный аромат премиального фундука."),
        "moisture": "2–3%", "size_kind": "calibers", "sizes": ["9–11 mm", "11–13 mm", "13–15 mm"],
        "packaging": T("200 g, 400 g retail packs · 20 kg, 25 kg vacuum bags",
                       "200 q, 400 q pərakəndə qablar · 20 kq, 25 kq vakuum kisələr",
                       "Розничная упаковка 200 г, 400 г · вакуумные мешки 20 кг, 25 кг"),
        "apps": [T("Chocolate bars & pralines", "Şokolad batonları və pralinlər", "Шоколадные плитки и пралине"),
                 T("Hazelnut spreads", "Fındıq kremləri", "Ореховые пасты"),
                 T("Snacks & cereals", "Qəlyanaltılar və dənli məhsullar", "Снеки и хлопья"),
                 T("Ice cream", "Dondurma", "Мороженое")],
    },
    {
        "slug": "roasted-chopped-hazelnuts", "img": "p-chopped", "gallery": ["g-chopped-blanched"],
        "name": T("Roasted & Chopped Hazelnuts", "Qovrulmuş və Doğranmış Fındıq", "Обжаренный дроблёный фундук"),
        "short": T("Roasted hazelnuts processed into different particle sizes for industrial food applications.",
                   "Sənaye qida tətbiqləri üçün müxtəlif kalibrlərdə emal olunmuş qovrulmuş fındıq.",
                   "Обжаренный фундук, измельчённый до разных размеров частиц для промышленного применения."),
        "long": T("Roasted kernels are chopped and sieved into tightly controlled particle sizes, delivering consistent coverage and crunch as inclusions, toppings and coatings.",
                  "Qovrulmuş ləpələr doğranır və ciddi nəzarət olunan kalibrlərə ələnir, daxiletmə, üzlük və örtük kimi sabit örtmə və xırtıldama təmin edir.",
                  "Обжаренные ядра дробятся и просеиваются до строго контролируемых фракций, обеспечивая равномерное покрытие и хруст в качестве включений, посыпок и обсыпок."),
        "moisture": "2–3%", "size_kind": "sizes", "sizes": ["0–2 mm", "2–4 mm", "4–6 mm"],
        "packaging": T("200 g, 400 g retail packs · 20 kg, 25 kg vacuum bags",
                       "200 q, 400 q pərakəndə qablar · 20 kq, 25 kq vakuum kisələr",
                       "Розничная упаковка 200 г, 400 г · вакуумные мешки 20 кг, 25 кг"),
        "apps": [T("Chocolate inclusions", "Şokolad daxiletmələri", "Включения в шоколад"),
                 T("Ice cream toppings", "Dondurma üzlükləri", "Топпинги для мороженого"),
                 T("Bakery decoration", "Çörək-bulka bəzəyi", "Декор выпечки"),
                 T("Cereal & granola bars", "Dənli və qranola batonları", "Злаковые батончики и гранола")],
    },
    {
        "slug": "hazelnut-flour", "img": "p-flour", "gallery": ["p-chopped"],
        "name": T("Hazelnut Flour", "Fındıq Unu", "Ореховая мука из фундука"),
        "short": T("Finely processed hazelnut flour suitable for confectionery, bakery and other food manufacturing applications.",
                   "Qənnadı, çörək-bulka və digər qida istehsalı sahələri üçün incə üyüdülmüş fındıq unu.",
                   "Тонко измельчённая мука из фундука для кондитерских, хлебопекарных и других пищевых производств."),
        "long": T("Milled from selected kernels into a fine, free-flowing flour that adds rich hazelnut flavour, moisture and structure to pastries, fillings and gluten-free recipes.",
                  "Seçilmiş ləpələrdən üyüdülən incə, axıcı un, xəmir məmulatlarına, içliklərə və qlütensiz reseptlərə zəngin fındıq dadı, nəmlik və struktur verir.",
                  "Мелкая сыпучая мука из отборных ядер придаёт выпечке, начинкам и безглютеновым рецептам насыщенный ореховый вкус, влажность и структуру."),
        "moisture": "Max. 2.5%", "size_kind": "sizes", "sizes": ["0–2 mm", "0–3 mm"],
        "packaging": T("90 g, 200 g, 400 g retail packs · 20 kg, 22 kg vacuum bags",
                       "90 q, 200 q, 400 q pərakəndə qablar · 20 kq, 22 kq vakuum kisələr",
                       "Розничная упаковка 90 г, 200 г, 400 г · вакуумные мешки 20 кг, 22 кг"),
        "apps": [T("Pastry & macarons", "Xəmir məmulatları və makaronlar", "Выпечка и макарон"),
                 T("Gluten-free baking", "Qlütensiz çörəkçilik", "Безглютеновая выпечка"),
                 T("Fillings & creams", "İçliklər və kremlər", "Начинки и кремы"),
                 T("Confectionery", "Qənnadı məmulatları", "Кондитерские изделия")],
    },
    {
        "slug": "in-shell-hazelnuts", "img": "p-inshell", "gallery": ["hazel-branch", "orchard-tree"],
        "name": T("In-Shell Hazelnuts", "Qabıqlı Fındıq", "Фундук в скорлупе"),
        "short": T("Natural selected hazelnuts in their shells.",
                   "Qabığında təbii seçilmiş fındıq.",
                   "Натуральный отборный фундук в скорлупе."),
        "long": T("Harvested from our Gabala orchards, dried and selected for size and soundness. Supplied for wholesale, retail and further processing; calibers and packaging are agreed according to your requirements.",
                  "Qəbələ bağlarımızdan yığılır, qurudulur və ölçü və sağlamlıq baxımından seçilir. Topdan, pərakəndə satış və sonrakı emal üçün tədarük olunur; kalibr və qablaşdırma tələblərinizə uyğun razılaşdırılır.",
                  "Собран в наших садах в Габале, высушен и отобран по размеру и качеству. Поставляется для оптовой, розничной торговли и дальнейшей переработки; калибр и упаковка согласовываются по вашим требованиям."),
        "moisture": None, "size_kind": "calibers", "sizes": None,
        "packaging": None,
        "apps": [T("Wholesale & retail", "Topdan və pərakəndə satış", "Опт и розница"),
                 T("Further processing", "Sonrakı emal", "Дальнейшая переработка"),
                 T("Seasonal trade", "Mövsümi ticarət", "Сезонная торговля")],
    },
]

PRODUCTS_PAGE = {
    "title": T("Products", "Məhsullar", "Продукция"),
    "meta": T("Natural, blanched, roasted and chopped hazelnut kernels, hazelnut flour and in-shell hazelnuts from Bionut, Azerbaijan. Specifications, calibers and packaging.",
              "Bionut-dan təbii, ağardılmış, qovrulmuş və doğranmış fındıq ləpəsi, fındıq unu və qabıqlı fındıq. Spesifikasiyalar, kalibrlər və qablaşdırma.",
              "Натуральные, бланшированные, обжаренные и дроблёные ядра фундука, ореховая мука и фундук в скорлупе от Bionut, Азербайджан. Спецификации, калибры и упаковка."),
    "eyebrow": T("Our products", "Məhsullarımız", "Наша продукция"),
    "h1": T("Hazelnut ingredients, made to specification", "Spesifikasiyaya uyğun fındıq inqrediyentləri", "Ингредиенты из фундука по спецификации"),
    "lead": HOME["products_p"],
    "custom_h": T("Need a custom specification?", "Fərdi spesifikasiya lazımdır?", "Нужна индивидуальная спецификация?"),
    "custom_p": T("Caliber, roast level, particle size and packaging can be adapted to your production requirements. Talk to our sales team.",
                  "Kalibr, qovurma dərəcəsi, hissəcik ölçüsü və qablaşdırma istehsal tələblərinizə uyğunlaşdırıla bilər. Satış komandamızla əlaqə saxlayın.",
                  "Калибр, степень обжарки, размер частиц и упаковка могут быть адаптированы под ваши производственные требования. Свяжитесь с отделом продаж."),
}

# ---------------------------------------------------------------- certifications
CERTS = [
    {"code": "FSSC 22000", "logo": "fssc-22000", "mark": "FSSC\n22000",
     "name": T("FSSC 22000", "FSSC 22000", "FSSC 22000"),
     "desc": T("GFSI-recognised food safety system certification covering our processing and packaging operations.",
               "Emal və qablaşdırma əməliyyatlarımızı əhatə edən, GFSI tərəfindən tanınan qida təhlükəsizliyi sistemi sertifikatı.",
               "Признанная GFSI сертификация системы безопасности пищевой продукции, охватывающая переработку и упаковку."),
     "number": None, "issuer": None, "valid": None, "pdf": None},
    {"code": "ISO 22000:2018", "logo": "iso-22000-2018", "mark": "ISO\n22000",
     "name": T("ISO 22000:2018", "ISO 22000:2018", "ISO 22000:2018"),
     "desc": T("International standard for food safety management systems across the food chain.",
               "Qida zənciri boyunca qida təhlükəsizliyi idarəetmə sistemləri üçün beynəlxalq standart.",
               "Международный стандарт систем менеджмента безопасности пищевой продукции по всей цепочке."),
     "number": None, "issuer": None, "valid": None, "pdf": None},
    {"code": "Organic", "logo": "eu-organic", "mark": "BIO\nORGANIC",
     "name": T("Organic / Bio Certification", "Üzvi / Bio Sertifikatı", "Органик / Bio сертификация"),
     "desc": T("Certification of our organic hazelnut production, available alongside conventional supply.",
               "Ənənəvi tədarüklə yanaşı təqdim olunan üzvi fındıq istehsalımızın sertifikatı.",
               "Сертификация нашего органического производства фундука, доступного наряду с традиционным."),
     "number": None, "issuer": None, "valid": None, "pdf": None},
    {"code": "SEDEX", "logo": "sedex-member", "mark": "SEDEX\nMEMBER",
     "name": T("SEDEX: Membership / Social Audit", "SEDEX: Üzvlük / Sosial Audit", "SEDEX: членство / социальный аудит"),
     "desc": T("Member of SEDEX, the ethical trade platform for responsible sourcing, labour standards and social audits.",
               "Məsuliyyətli tədarük, əmək standartları və sosial auditlər üzrə etik ticarət platforması olan SEDEX-in üzvü.",
               "Участник SEDEX, платформы этичной торговли по ответственным закупкам, трудовым стандартам и социальным аудитам."),
     "number": None, "issuer": None, "valid": None, "pdf": None},
]

CERT_PAGE = {
    "title": T("Certifications", "Sertifikatlar", "Сертификаты"),
    "meta": T("Bionut certifications: FSSC 22000, ISO 22000:2018, Organic / Bio and SEDEX membership.",
              "Bionut sertifikatları: FSSC 22000, ISO 22000:2018, Üzvi / Bio və SEDEX üzvlüyü.",
              "Сертификаты Bionut: FSSC 22000, ISO 22000:2018, Органик / Bio и членство в SEDEX."),
    "eyebrow": T("Certifications", "Sertifikatlar", "Сертификаты"),
    "h1": T("Certified food safety, verified responsibility", "Sertifikatlı qida təhlükəsizliyi, təsdiqlənmiş məsuliyyət", "Сертифицированная безопасность, подтверждённая ответственность"),
    "lead": T("Our certifications give international buyers independent assurance of food safety, organic integrity and ethical business practices.",
              "Sertifikatlarımız beynəlxalq alıcılara qida təhlükəsizliyi, üzvi bütövlük və etik biznes təcrübələri barədə müstəqil təminat verir.",
              "Наши сертификаты дают международным покупателям независимые гарантии безопасности пищевой продукции, органической целостности и этичной деловой практики."),
    "number": T("Certificate No.", "Sertifikat №", "№ сертификата"),
    "issuer": T("Issued by", "Verən qurum", "Орган сертификации"),
    "valid": T("Valid until", "Qüvvədədir", "Действителен до"),
    "on_request": T("Available on request", "Sorğu əsasında", "По запросу"),
    "download": T("Download certificate (PDF)", "Sertifikatı yüklə (PDF)", "Скачать сертификат (PDF)"),
    "request": T("Request a copy", "Nüsxəsini istə", "Запросить копию"),
    "view_one": T("View certificate", "Sertifikata bax", "Смотреть сертификат"),
    "new_tab": T("opens in a new tab", "yeni tabda açılır", "откроется в новой вкладке"),
}

# ---------------------------------------------------------------- about
ABOUT = {
    "title": T("About Us", "Haqqımızda", "О компании"),
    "meta": T("Since 2005, Gilan Gabala Food Products Manufacturing OJSC (Bionut) has grown, processed and exported hazelnuts from its own orchards in Gabala, Azerbaijan.",
              "2005-ci ildən “Gilan Qəbələ Qida Məhsullarının İstehsalı” ASC (Bionut) Qəbələdəki öz bağlarından fındıq yetişdirir, emal edir və ixrac edir.",
              "С 2005 года ОАО «Гилан Габала» (Bionut) выращивает, перерабатывает и экспортирует фундук из собственных садов в Габале, Азербайджан."),
    "eyebrow": T("About Bionut", "Bionut haqqında", "О компании Bionut"),
    "h1": T("Two decades of Azerbaijani hazelnut expertise", "Azərbaycan fındığında iki onillik təcrübə", "Два десятилетия опыта в азербайджанском фундуке"),
    "lead": T("Founded in 2005 in Gabala, Gilan Gabala Food Products Manufacturing OJSC, trading as Bionut, has grown into one of Azerbaijan's leading hazelnut exporters.",
              "2005-ci ildə Qəbələdə təsis edilmiş “Gilan Qəbələ Qida Məhsullarının İstehsalı” ASC, Bionut brendi ilə, Azərbaycanın aparıcı fındıq ixracatçılarından birinə çevrilib.",
              "Основанное в 2005 году в Габале ОАО «Гилан Габала по производству пищевых продуктов», работающее под брендом Bionut, стало одним из ведущих экспортёров фундука Азербайджана."),
    "story_h": T("Our story", "Tariximiz", "Наша история"),
    "story": [
        T("Gabala lies in the foothills of the Greater Caucasus, where fertile soils, mountain air and reliable rainfall create some of the finest hazelnut-growing conditions in the region. It is here, in 2005, that Gilan Gabala Food Products Manufacturing OJSC began cultivating and exporting hazelnuts.",
          "Qəbələ Böyük Qafqazın ətəklərində yerləşir, burada münbit torpaq, dağ havası və sabit yağıntılar regionda fındıq yetişdirilməsi üçün ən yaxşı şəraiti yaradır. Məhz burada, 2005-ci ildə “Gilan Qəbələ Qida Məhsullarının İstehsalı” ASC fındıq yetişdirməyə və ixrac etməyə başladı.",
          "Габала расположена в предгорьях Большого Кавказа, где плодородные почвы, горный воздух и стабильные осадки создают одни из лучших условий для выращивания фундука в регионе. Именно здесь в 2005 году ОАО «Гилан Габала» начало выращивать и экспортировать фундук."),
        T("Today, all agronomic care across our 500+ hectares of orchards is carried out by specialists with more than 20 years of experience, in line with ecological production standards. We produce and export both organic and conventional hazelnuts.",
          "Bu gün 500+ hektar bağlarımızda bütün aqrotexniki qulluq ekoloji istehsal standartlarına uyğun olaraq 20 ildən artıq təcrübəyə malik mütəxəssislər tərəfindən həyata keçirilir. Biz həm üzvi, həm də ənənəvi fındıq istehsal və ixrac edirik.",
          "Сегодня весь агротехнический уход на наших 500+ гектарах садов осуществляют специалисты с более чем 20-летним опытом в соответствии с экологическими стандартами производства. Мы производим и экспортируем как органический, так и традиционный фундук."),
        T("Our processing plant handles more than 7,000 tons per season and over 20 tons per day, supplying confectionery, bakery and food manufacturers in Germany, Italy, Türkiye, Canada, Russia, Egypt and India.",
          "Emal zavodumuz mövsüm ərzində 7 000 tondan, gündə isə 20 tondan çox məhsul emal edir və Almaniya, İtaliya, Türkiyə, Kanada, Rusiya, Misir və Hindistandakı qənnadı, çörək-bulka və qida istehsalçılarını təchiz edir.",
          "Наш перерабатывающий завод обрабатывает более 7 000 тонн за сезон и свыше 20 тонн в сутки, снабжая кондитерские, хлебопекарные и пищевые предприятия в Германии, Италии, Турции, Канаде, России, Египте и Индии."),
    ],
    "values_h": T("What we stand for", "Dəyərlərimiz", "Наши ценности"),
    "values": [
        (T("Customer satisfaction", "Müştəri məmnuniyyəti", "Удовлетворённость клиентов"),
         T("Long-term partnerships built on responsiveness, transparency and reliable delivery.",
           "Operativlik, şəffaflıq və etibarlı tədarükə əsaslanan uzunmüddətli tərəfdaşlıq.",
           "Долгосрочное партнёрство на основе оперативности, прозрачности и надёжных поставок.")),
        (T("Guaranteed quality", "Zəmanətli keyfiyyət", "Гарантированное качество"),
         T("Certified food safety systems and laboratory control on every lot we ship.",
           "Göndərdiyimiz hər partiyada sertifikatlı qida təhlükəsizliyi sistemləri və laboratoriya nəzarəti.",
           "Сертифицированные системы безопасности и лабораторный контроль каждой партии.")),
        (T("Respect for nature", "Təbiətə hörmət", "Уважение к природе"),
         T("Ecological orchard management and organic production in the Gabala region.",
           "Qəbələ bölgəsində ekoloji bağ idarəçiliyi və üzvi istehsal.",
           "Экологичное ведение садов и органическое производство в Габалинском регионе.")),
    ],
    "team_eyebrow": T("Leadership", "Rəhbərlik", "Руководство"),
    "team_h": T("Talk directly to our team", "Komandamızla birbaşa əlaqə", "Свяжитесь с нашей командой напрямую"),
    "team": [
        {"name": T("Rahib Rahimov", "Rahib Rəhimov", "Рахиб Рагимов"), "initials": "RR",
         "role": T("Management", "Rəhbərlik", "Руководство"), "email": "rahib.rahimov@bionut.az"},
        {"name": T("Anar Ismayilov", "Anar İsmayılov", "Анар Исмайылов"), "initials": "AI",
         "role": T("Management", "Rəhbərlik", "Руководство"), "email": "anar.ismayilov@bionut.az"},
    ],
    "facts": [
        ("2005", T("Founded in Gabala", "Qəbələdə təsis edilib", "Основана в Габале")),
        ("500+", T("Hectares of own orchards", "Hektar öz bağları", "Гектаров собственных садов")),
        ("7", T("Export markets", "İxrac bazarı", "Экспортных рынков")),
        ("4", T("Certifications", "Sertifikat", "Сертификата")),
    ],
}

# ---------------------------------------------------------------- contact
CONTACT = {
    "title": T("Contact", "Əlaqə", "Контакты"),
    "meta": T("Contact Bionut's sales team for hazelnut kernels, roasted, chopped and flour products. Gabala, Azerbaijan. +994 50 290 20 70, info@bionut.az.",
              "Fındıq ləpəsi, qovrulmuş, doğranmış fındıq və fındıq unu üçün Bionut satış komandası ilə əlaqə. Qəbələ, Azərbaycan. +994 50 290 20 70, info@bionut.az.",
              "Свяжитесь с отделом продаж Bionut по ядрам фундука, обжаренному, дроблёному фундуку и муке. Габала, Азербайджан. +994 50 290 20 70, info@bionut.az."),
    "eyebrow": T("Contact", "Əlaqə", "Контакты"),
    "h1": T("Let's talk hazelnuts", "Gəlin fındıqdan danışaq", "Давайте обсудим фундук"),
    "lead": T("Send us your enquiry and our sales team will respond within one business day with availability, specifications and a tailored offer.",
              "Sorğunuzu göndərin, satış komandamız bir iş günü ərzində mövcudluq, spesifikasiyalar və fərdi təkliflə cavab verəcək.",
              "Отправьте запрос, и наш отдел продаж в течение одного рабочего дня ответит с информацией о наличии, спецификациях и индивидуальным предложением."),
    "form_h": T("Request a quote", "Qiymət təklifi istəyin", "Запрос коммерческого предложения"),
    "f_name": T("Full name", "Ad, soyad", "Имя и фамилия"),
    "f_company": T("Company", "Şirkət", "Компания"),
    "f_email": T("Business email", "İş e-poçtu", "Рабочий e-mail"),
    "f_phone": T("Phone", "Telefon", "Телефон"),
    "f_country": T("Country", "Ölkə", "Страна"),
    "f_product": T("Product of interest", "Maraqlandığınız məhsul", "Интересующий продукт"),
    "f_any": T("Several / not sure yet", "Bir neçə / hələ dəqiq deyil", "Несколько / пока не определились"),
    "f_volume": T("Estimated volume (MT)", "Təxmini həcm (MT)", "Ориентировочный объём (MT)"),
    "f_message": T("Message", "Mesaj", "Сообщение"),
    "f_message_ph": T("Specification, caliber, packaging, destination port, delivery timing…",
                      "Spesifikasiya, kalibr, qablaşdırma, təyinat limanı, çatdırılma vaxtı…",
                      "Спецификация, калибр, упаковка, порт назначения, сроки поставки…"),
    "f_submit": T("Send enquiry", "Sorğunu göndər", "Отправить запрос"),
    "f_note": T("Submitting opens your email client with the enquiry addressed to info@bionut.az.",
                "Göndər düyməsi sorğunu info@bionut.az ünvanına hazırlanmış şəkildə e-poçt proqramınızda açır.",
                "При отправке откроется ваша почтовая программа с запросом на info@bionut.az."),
    "f_required": T("Please fill in the required fields.", "Zəhmət olmasa, tələb olunan sahələri doldurun.", "Пожалуйста, заполните обязательные поля."),
    "f_subject": T("Quote request", "Qiymət sorğusu", "Запрос предложения"),
    "details_h": T("Contact details", "Əlaqə məlumatları", "Контактные данные"),
    "sales_h": T("Sales & management", "Satış və rəhbərlik", "Продажи и руководство"),
    "hours": T("Monday – Friday, 09:00 – 18:00 (GMT+4)", "Bazar ertəsi – Cümə, 09:00 – 18:00 (GMT+4)", "Понедельник – пятница, 09:00 – 18:00 (GMT+4)"),
    "map_title": T("Bionut location in Zaragan, Gabala", "Bionut-un Zarağan, Qəbələdəki yeri", "Расположение Bionut в Зарагане, Габала"),
}

# ---------------------------------------------------------------- insights (blog)
INSIGHTS_PAGE = {
    "title": T("Insights", "Bilgi Mərkəzi", "Аналитика"),
    "meta": T("Hazelnut market updates and food safety research, curated by Bionut.",
              "Bionut tərəfindən hazırlanmış fındıq bazarı yenilikləri və qida təhlükəsizliyi araşdırmaları.",
              "Обзоры рынка фундука и исследования в области безопасности пищевых продуктов от Bionut."),
    "eyebrow": T("Insights", "Bilgi Mərkəzi", "Аналитика"),
    "h1": T("Hazelnut market & quality insights", "Fındıq bazarı və keyfiyyət üzrə analitika", "Аналитика рынка фундука и качества"),
    "lead": T("Concise briefings on crop outlooks, trade data and food safety research relevant to hazelnut buyers.",
              "Fındıq alıcıları üçün məhsul proqnozları, ticarət məlumatları və qida təhlükəsizliyi araşdırmaları üzrə qısa icmallar.",
              "Краткие обзоры прогнозов урожая, торговой статистики и исследований безопасности для покупателей фундука."),
}

ARTICLES = [
    {
        "slug": "2026-hazelnut-crop-update-outlook",
        "img": "hazel-branch",
        "date": "2026-11-12", "date_label": T("12 November 2026", "12 noyabr 2026", "12 ноября 2026"),
        "read": 4,
        "tag": T("Market update", "Bazar icmalı", "Обзор рынка"),
        "title": T("2026 Hazelnut Crop Update & Outlook", "2026 Fındıq Məhsulu: Yenilik və Proqnoz", "Урожай фундука 2026: обзор и прогноз"),
        "excerpt": T("Türkiye's crop forecast, export performance and stock outlook, plus harvest reports from Italy, the USA and Chile, what the 2026/27 season looks like for buyers.",
                     "Türkiyənin məhsul proqnozu, ixrac göstəriciləri və ehtiyat proqnozu, həmçinin İtaliya, ABŞ və Çilidən məhsul hesabatları, alıcılar üçün 2026/27 mövsümü.",
                     "Прогноз урожая Турции, экспорт и запасы, а также отчёты из Италии, США и Чили, каким будет сезон 2026/27 для покупателей."),
        "sources": [("International Nut & Dried Fruit Council (INC), Hazelnut Crop Update & Outlook, 12 Nov 2026",
                     "https://inc.nutfruit.org/hazelnut-crop-update-outlook-2/")],
        "body": T(
            """<p>The International Nut &amp; Dried Fruit Council (INC) published its latest hazelnut crop update in November 2026, based on information gathered between mid-September and October. Here is a summary of the key figures and what they mean for buyers.</p>
<h2>Türkiye: a slightly smaller forecast</h2>
<p>The Black Sea Hazelnut Exporters' Association trimmed its 2026 crop estimate to <strong>803,770 MT (in-shell basis)</strong>, down from 805,246 MT in late July, after further orchard assessments of kernel size and yield. The kernel recovery ratio is estimated at 50%.</p>
<ul>
<li><strong>2025/26 exports:</strong> 197,085 MT kernel equivalent, 36% below 2024/25, worth US$2.51 billion.</li>
<li><strong>September 2026</strong> (first month of the new season): 18,929 MT exported, up 36% year on year, valued at US$192.1 million.</li>
<li><strong>TMO purchases:</strong> around 77,000 MT in-shell bought so far, with a further 100,000 MT scheduled for delivery.</li>
<li><strong>Ending stocks 2026/27:</strong> tentatively 270,000 MT, as exports have been moving more slowly than usual.</li>
</ul>
<h2>Italy, USA and Chile</h2>
<p><strong>Italy</strong> proved resilient despite an exceptionally long, record-hot summer, with a crop estimated above average. In the <strong>USA</strong>, the Oregon harvest started in September in excellent weather; the crop looks slightly larger than forecast, with normal sizing and excellent kernel quality. In <strong>Chile</strong>, winter and spring conditions were favourable, and new orchards entering production should lift the 2027 crop.</p>
<h2>What it means for buyers</h2>
<p>A comfortable stock position in Türkiye and solid crops in Italy and the USA point to a well-supplied 2026/27 season, with confectionery demand rebuilding after the high prices of 2025. For manufacturers, it is a good moment to diversify origins and secure consistent, traceable supply. Azerbaijani hazelnuts, grown in the Gabala region and processed under certified food safety systems, offer a reliable complement to traditional origins.</p>""",
            """<p>Beynəlxalq Qoz-fındıq və Quru Meyvə Şurası (INC) 2026-cı ilin noyabrında sentyabrın ortası – oktyabr aylarında toplanmış məlumatlar əsasında fındıq məhsulu üzrə son icmalını dərc edib. Əsas rəqəmlər və onların alıcılar üçün mənası aşağıda təqdim olunur.</p>
<h2>Türkiyə: bir qədər azaldılmış proqnoz</h2>
<p>Qara dəniz Fındıq İxracatçıları Assosiasiyası ləpə ölçüsü və məhsuldarlıq üzrə əlavə qiymətləndirmələrdən sonra 2026-cı il məhsul proqnozunu iyulun sonundakı 805 246 MT-dan <strong>803 770 MT-a (qabıqlı əsasda)</strong> endirib. Ləpə çıxımı 50% qiymətləndirilir.</p>
<ul>
<li><strong>2025/26 ixracı:</strong> 197 085 MT ləpə ekvivalenti, 2024/25-dən 36% az, dəyəri 2,51 milyard ABŞ dolları.</li>
<li><strong>Sentyabr 2026</strong> (yeni mövsümün ilk ayı): 18 929 MT ixrac, illik 36% artım, dəyəri 192,1 milyon ABŞ dolları.</li>
<li><strong>TMO alışları:</strong> indiyədək təxminən 77 000 MT qabıqlı fındıq alınıb, əlavə 100 000 MT-ın təhvili planlaşdırılır.</li>
<li><strong>2026/27 mövsüm sonu ehtiyatları:</strong> ixracın adi haldan yavaş getməsi səbəbindən ilkin olaraq 270 000 MT.</li>
</ul>
<h2>İtaliya, ABŞ və Çili</h2>
<p><strong>İtaliyada</strong> müstəsna dərəcədə uzun və rekord isti yaya baxmayaraq istehsal davamlı qalıb, məhsul ortadan yuxarı qiymətləndirilir. <strong>ABŞ-da</strong> Oreqonda yığım sentyabrda əla hava şəraitində başlayıb; məhsul proqnozdan bir qədər çox, ölçülər normal, ləpə keyfiyyəti isə əladır. <strong>Çilidə</strong> qış və yaz şəraiti əlverişli olub, istehsala daxil olan yeni bağlar 2027-ci il məhsulunu artırmalıdır.</p>
<h2>Alıcılar üçün nə deməkdir</h2>
<p>Türkiyədə rahat ehtiyat vəziyyəti, İtaliya və ABŞ-da sabit məhsul 2026/27 mövsümünün yaxşı təchiz olunacağını göstərir; qənnadı tələbatı isə 2025-ci ilin yüksək qiymətlərindən sonra bərpa olunur. İstehsalçılar üçün mənşə ölkələrini şaxələndirmək və sabit, izlənilə bilən tədarükü təmin etmək üçün əlverişli məqamdır. Qəbələ bölgəsində yetişdirilən və sertifikatlı qida təhlükəsizliyi sistemləri ilə emal olunan Azərbaycan fındığı ənənəvi mənşələrə etibarlı əlavədir.</p>""",
            """<p>Международный совет по орехам и сухофруктам (INC) в ноябре 2026 года опубликовал свежий обзор урожая фундука на основе данных, собранных с середины сентября по октябрь. Ниже приведены ключевые цифры и их значение для покупателей.</p>
<h2>Турция: немного сниженный прогноз</h2>
<p>Ассоциация экспортёров фундука Черноморского региона после дополнительной оценки размера ядра и урожайности снизила прогноз урожая 2026 года до <strong>803 770 MT (в скорлупе)</strong> против 805 246 MT в конце июля. Выход ядра оценивается в 50%.</p>
<ul>
<li><strong>Экспорт 2025/26:</strong> 197 085 MT в пересчёте на ядро, на 36% меньше, чем в 2024/25,, на сумму 2,51 млрд долларов США.</li>
<li><strong>Сентябрь 2026</strong> (первый месяц нового сезона): экспорт 18 929 MT, рост на 36% в годовом выражении, стоимость 192,1 млн долларов США.</li>
<li><strong>Закупки TMO:</strong> около 77 000 MT фундука в скорлупе, ещё 100 000 MT запланированы к поставке.</li>
<li><strong>Конечные запасы 2026/27:</strong> предварительно 270 000 MT, так как экспорт идёт медленнее обычного.</li>
</ul>
<h2>Италия, США и Чили</h2>
<p><strong>Италия</strong> сохранила устойчивость, несмотря на исключительно долгое и рекордно жаркое лето: урожай оценивается выше среднего. В <strong>США</strong> сбор в Орегоне начался в сентябре при отличной погоде; урожай немного выше прогноза, калибровка в норме, качество ядра отличное. В <strong>Чили</strong> зима и весна были благоприятными, а новые сады, вступающие в плодоношение, должны увеличить урожай 2027 года.</p>
<h2>Что это значит для покупателей</h2>
<p>Комфортные запасы в Турции и хорошие урожаи в Италии и США указывают на хорошо обеспеченный сезон 2026/27, а спрос со стороны кондитерской отрасли восстанавливается после высоких цен 2025 года. Для производителей это удачный момент диверсифицировать происхождение сырья и обеспечить стабильные, прослеживаемые поставки. Азербайджанский фундук из Габалинского региона, переработанный по сертифицированным системам безопасности,, надёжное дополнение к традиционным источникам.</p>"""),
    },
    {
        "slug": "post-harvest-management-aflatoxin",
        "img": "orchard-young",
        "date": "2026-01-10", "date_label": T("January 2026", "Yanvar 2026", "Январь 2026"),
        "read": 5,
        "tag": T("Food safety research", "Qida təhlükəsizliyi araşdırması", "Исследование безопасности"),
        "title": T("Post-harvest Management and Aflatoxin Contamination", "Məhsul Yığımından Sonrakı İdarəetmə və Aflatoksin Çirklənməsi", "Послеуборочная обработка и загрязнение афлатоксинами"),
        "excerpt": T("A three-year study of Azerbaijani hazelnuts, published in 2026, finds that drying, more than storage, determines aflatoxin risk. Key findings for buyers and producers.",
                     "2026-cı ildə dərc edilmiş, Azərbaycan fındığı üzrə üç illik araşdırma göstərir ki, aflatoksin riskini saxlamadan çox qurutma müəyyən edir. Alıcılar və istehsalçılar üçün əsas nəticələr.",
                     "Трёхлетнее исследование азербайджанского фундука, опубликованное в 2026 году, показывает, что риск афлатоксинов определяет прежде всего сушка, а не хранение. Главные выводы."),
        "sources": [
            ("Casu A., Chiusa G., Zagottis E., Genova G., Battilani P., Effect of Post-Harvest Management on Aspergillus flavus Growth and Aflatoxin Contamination of Stored Hazelnuts. Toxins 18(1):38, 2026 (CC BY)",
             "https://doi.org/10.3390/toxins18010038"),
            ("Frontiers in Plant Science, 2026, pre-harvest aflatoxin risk in hazelnut orchards",
             "https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2026.1791562/full"),
        ],
        "body": T(
            """<p>Aflatoxins, toxic compounds produced mainly by the mould <em>Aspergillus flavus</em>, are the most important food safety risk for tree nuts and are strictly regulated in the EU and other import markets. A study published in January 2026 in the journal <em>Toxins</em> examined how post-harvest handling affects this risk, using hazelnuts from <strong>Azerbaijan</strong> over three years.</p>
<h2>Key findings</h2>
<ul>
<li><strong>Drying is the decisive factor.</strong> Drying efficiency was the primary driver of fungal persistence and aflatoxin risk. Proper drying significantly reduced contamination regardless of storage conditions.</li>
<li><strong>Storage matters less when drying is right.</strong> With adequate drying, storage temperature and shell condition had only a minimal influence.</li>
<li><strong>Traditional sun-drying carries the highest risk.</strong> Drying on the ground or under variable weather was associated with elevated risk, while mechanical drying and well-controlled storage significantly reduced contamination.</li>
</ul>
<p>A companion study in <em>Frontiers in Plant Science</em> (2026) found low aflatoxin levels in orchards at harvest, but markedly higher contamination in late-harvested nuts, particularly those collected from the ground. The authors point to orchard microclimate and harvest timing as the main pre-harvest drivers and recommend Good Agricultural Practices, timely harvest and rapid post-harvest drying.</p>
<h2>What it means for buyers</h2>
<p>The research confirms that aflatoxin control starts long before a container is loaded. When qualifying a hazelnut supplier, buyers should ask how and how quickly nuts are dried after harvest, how storage is controlled, and how every lot is tested before shipment.</p>
<p>At Bionut, harvest, processing and packing take place within one integrated operation. Raw material is inspected on arrival, every lot is checked in our in-house laboratory, and full traceability links each shipment back to the orchard, all under an FSSC 22000 and ISO 22000:2018 certified food safety system.</p>""",
            """<p>Aflatoksinlər, əsasən <em>Aspergillus flavus</em> göbələyi tərəfindən əmələ gələn toksik birləşmələr, qoz-fındıq üçün ən mühüm qida təhlükəsizliyi riskidir və AB-də, eləcə də digər idxal bazarlarında ciddi şəkildə tənzimlənir. 2026-cı ilin yanvarında <em>Toxins</em> jurnalında dərc edilmiş araşdırma üç il ərzində <strong>Azərbaycan</strong> fındığı üzərində yığımdan sonrakı əməliyyatların bu riskə təsirini öyrənib.</p>
<h2>Əsas nəticələr</h2>
<ul>
<li><strong>Qurutma həlledici amildir.</strong> Göbələyin qalması və aflatoksin riskini əsasən qurutmanın səmərəliliyi müəyyən edir. Düzgün qurutma saxlama şəraitindən asılı olmayaraq çirklənməni əhəmiyyətli dərəcədə azaldıb.</li>
<li><strong>Qurutma düzgün olduqda saxlama daha az təsir edir.</strong> Kifayət qədər qurutma şəraitində saxlama temperaturu və qabığın vəziyyəti minimal təsir göstərib.</li>
<li><strong>Ənənəvi günəşdə qurutma ən yüksək risk daşıyır.</strong> Yerdə və ya dəyişkən hava şəraitində qurutma yüksək risklə əlaqələndirilib, mexaniki qurutma və yaxşı idarə olunan saxlama isə çirklənməni xeyli azaldıb.</li>
</ul>
<p><em>Frontiers in Plant Science</em> jurnalındakı müşayiətedici araşdırma (2026) yığım zamanı bağlarda aflatoksin səviyyəsinin aşağı olduğunu, gec yığılmış, xüsusilə yerdən toplanmış, fındıqda isə çirklənmənin xeyli yüksək olduğunu göstərib. Müəlliflər bağın mikroiqlimini və yığım vaxtını yığımdan əvvəlki əsas amillər kimi göstərir və Yaxşı Kənd Təsərrüfatı Təcrübələrini, vaxtında yığımı və sürətli qurutmanı tövsiyə edir.</p>
<h2>Alıcılar üçün nə deməkdir</h2>
<p>Araşdırma təsdiq edir ki, aflatoksin nəzarəti konteyner yüklənməzdən çox əvvəl başlayır. Fındıq tədarükçüsünü qiymətləndirərkən alıcılar fındığın yığımdan sonra necə və nə qədər tez qurudulduğunu, saxlamanın necə idarə olunduğunu və hər partiyanın göndərişdən əvvəl necə yoxlanıldığını soruşmalıdır.</p>
<p>Bionut-da yığım, emal və qablaşdırma vahid inteqrasiya olunmuş istehsal daxilində həyata keçirilir. Xammal daxil olarkən yoxlanılır, hər partiya daxili laboratoriyamızda yoxlanılır, tam izlənilmə isə hər göndərişi bağa qədər əlaqələndirir, hamısı FSSC 22000 və ISO 22000:2018 sertifikatlı qida təhlükəsizliyi sistemi çərçivəsində.</p>""",
            """<p>Афлатоксины, токсичные соединения, вырабатываемые главным образом плесневым грибом <em>Aspergillus flavus</em>, представляют важнейший риск безопасности для орехов; они строго регулируются в ЕС и на других импортных рынках. Исследование, опубликованное в январе 2026 года в журнале <em>Toxins</em>, в течение трёх лет изучало, как послеуборочная обработка влияет на этот риск, на примере фундука из <strong>Азербайджана</strong>.</p>
<h2>Главные выводы</h2>
<ul>
<li><strong>Сушка: решающий фактор.</strong> Эффективность сушки является основным фактором сохранения грибка и риска афлатоксинов. Правильная сушка значительно снижала загрязнение независимо от условий хранения.</li>
<li><strong>При правильной сушке хранение влияет меньше.</strong> При достаточной сушке температура хранения и состояние скорлупы оказывали минимальное влияние.</li>
<li><strong>Традиционная сушка на солнце наиболее рискованна.</strong> Сушка на земле или при переменчивой погоде связана с повышенным риском, а механическая сушка и контролируемое хранение значительно снижают загрязнение.</li>
</ul>
<p>Сопутствующее исследование в <em>Frontiers in Plant Science</em> (2026) показало низкий уровень афлатоксинов в садах на момент сбора, но заметно более высокое загрязнение у поздно собранных орехов, особенно поднятых с земли. Авторы называют главными доуборочными факторами микроклимат сада и сроки сбора и рекомендуют надлежащую сельскохозяйственную практику, своевременный сбор и быструю сушку.</p>
<h2>Что это значит для покупателей</h2>
<p>Исследование подтверждает: контроль афлатоксинов начинается задолго до загрузки контейнера. Оценивая поставщика фундука, покупателям стоит узнать, как и насколько быстро орехи сушат после сбора, как контролируется хранение и как проверяется каждая партия перед отгрузкой.</p>
<p>В Bionut сбор, переработка и упаковка выполняются в рамках единого интегрированного производства. Сырьё проверяется при поступлении, каждая партия, в нашей собственной лаборатории, а полная прослеживаемость связывает каждую отгрузку с садом, всё в рамках системы безопасности, сертифицированной по FSSC 22000 и ISO 22000:2018.</p>"""),
    },
]
