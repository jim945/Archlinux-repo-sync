#!/usr/bin/env python3
# ArchLinux repositories mirrored with an exception.
# ver. 2.0
# jim945@mail.ru

import os
import subprocess


# Файл исключений
p_ex = '/tmp/pac.exclude'

while True:                            # Генерация исключений
    if  os.path.exists (p_ex):
      i = input ('Обновить файл исключений? (y/N) ')
    else :
      i = 'y'
    if i in {'','n','N','н','Н'}:
      break
    elif i in {'y','Y','д','Д'}:
      # Дополнительные исключения
      dop_ex = [
      'os/ppc',
      'iso',
      '*.sig',
      '*.old',
      '*sauerbraten-*',
      '*nexuiz-*',
      '*tremulous-*',
      '*alienarena-*',
      '*flightgear-*',
      '*frogatto-*',
      '*vdrift-*',
      '*warsow-*',
      ]

      pac_ex = open (p_ex, 'w')            # Открытие файла
      for d in dop_ex:                     # Добавление дополнительных исключений (dop_ex)
          pac_ex.write (d + '\n')

      # Исключаемые языки
      lang = [                             # Список исключаемых языков
      'af','ar','ak','am','as','ast',
      'be','bg','bn-bd','bn-in','bn','bo','br','brx','bs',
      'ca','ca@valencia','csb','cs','cy',
      'da','de','dgo','dz',
      'el','en_gb','en-gb','en-GB','en-us','en-US','en-za','en-ZA','es','eo','et','eu',#'en',#'english',
      'fa','fi','ff','fo','fr','fy','fy-nl',
      'ga','gl','gu','gu-in','gd',
      'he','hi','hi-in','hr','hu','hy-am',
      'ia','id','is','it',
      'ja',
      'ka','kk','km','kn','ko','kok','ks','ku','lg',
      'la','lij','lo','lt','lv',
      'mai','mg','mi','mk','ml','mn','mni','mr','ms','my',
      'nb','ne','nds','nl','nn','nr','nso','ny',
      'oc','om','or',
      'pa','pl','pt','pt_br',
      'rm','ro','rw',#'ru',
      'sa-IN','sat','sd','sh','sk','sl','sr','sv','si','son','sq','ss','sw','sw-TZ','st', # conflict mt-st
      'ta','ta-lk','te','tet','tg','th','tl','tn','tr','ts',
      'ug','uk','us','uz',
      've','vi',
      'wa',
      'xh',
      'zh_cn','zh-cn','zh_tw','zh-tw','zh-CN','zh-TW','zu',
      'yi',
      ]

      #lang2 = [ ]
      #for l in lang2 :                        # Сравнение списков языков lang и lang2
          #if l in lang:                       # Выводит языки отсутствующие в lang
              #None
          #else :
              #print ('\'', l, '\',', sep='')

      pacs = [                                # Целое (или *часть) название программы,
      '*i18n',                                # языковые пакеты которого не требуются.
      '*l10n',
      'libreoffice-still',
      'libreoffice-fresh',
      #'libreoffice \s 1',                     # Число после ' \s ' указывает для какой архитектуры (arch {}) добавить исключение
      #'libreoffice \s 2',
      'festival',
      'aspell',
      'gimp-help',
      'hunspell',
      'hyphen',
      'mythes',
      'vim-spell',
      'man-pages',
      ]
                              # Компоновка архитектуры, названия и языка и добавление в список
      global perf
      for p in pacs:
        i = '4'
        if ' \s ' in p:
          i = str.split(p, ' \s ')[1]
          p = str.split(p, ' \s ')[0]
        for l in lang:
          pac_ex.write ('*' + p + '-' + l + '-*.pkg.tar.zst*' + '\n')
      pac_ex.close ()
      break
    else:
      continue


