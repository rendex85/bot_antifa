# Не хочу эти штуки в базу писать, пусть тут лежат
import os

naz_list = os.getenv("NAZ").split(",")

gacha_list = os.getenv("GACHA").split(",")
cerf_list = os.getenv("CERF").split(",")

gatari_alb_lsit = os.getenv("GATARI").split(",")
photo_garik_list = os.getenv("PHOTO_GARIK").split(",")
account_garik_list = os.getenv("ACCOUNT_GARIK").split(",")

answ = ['Я думаю, что ', 'С уверенностью могу сказать, что ', 'Мне кажется, ',
        'С помощью фактов и логики я доказал, что ',
        'Я провел мысленный экперимент и выяснил, что ', 'Здравый смысл говорит мне о том, что ',
        'Как показывает практика, ',
        'Используя диалектическую логику, я пришел к выводу, что ', 'Как по мне, то ',
        'Благодаря чувственному опыту я определил, что ', 'Думается мне, что ',
        'Проведя некие изыскания, я высяснил, что ',
        'Чуйка мне нашептала о том, что ',
        'Прикинув раз на раз, я определился с тем, что ', 'Мои интеллектуальные потуги привели меня к тому, что ',
        'Уверяю вас в том, что ', 'Долго размышляя, я пришел к идеи, что ']
