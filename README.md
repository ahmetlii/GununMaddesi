[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Günün maddesi

Eğer günün maddesi oluşturulmamış ise geçmiş günlerden rastgele bir GM sayfası seçip onun içeriği ile sayfayı oluşturur.

## Kurulum

* ```.pass``` dosyası içerisine kullanıcı adı ve şifresi kaydedilir
* ```deneme.py``` içerisinde ```username``` güncellenerek çalıştırılır. [Deneme sayfası](https://tr.wikipedia.org/wiki/Vikipedi:Deneme_tahtas%C4%B1) üzerinde test yapılır
* ```GununMaddesi.py``` içerisinde ```username``` güncellenerek çalıştırılır. Program test edilir
* Programı her gece otomatik çalıştırmak için [ToolsForge](https://wikitech.wikimedia.org/) üzerine aşağıdaki [cron](https://en.wikipedia.org/wiki/Cron) komutu düzenlenerek kaydedilir.
  
```text
35 23 * * *   /usr/bin/jsub    -N Vikipedi-GununMaddesi        -once -quiet python /data/project/mavrikant/GununMaddesi/GununMaddesi.py
```

## Uyarılar

Login methodu artık deprecated olduğu için uyarı vermekte. Şimdilik çalışsa da gelecekte değiştirilmeli.

```json
"warnings": {
    "login": {
        "*": "Main-account login via \"action=login\" is deprecated and may stop working without warning. To continue login with \"action=login\", see [[Special:BotPasswords]]. To safely continue using main-account login, see \"action=clientlogin\"."
    },
    "main": {
        "*": "Subscribe to the mediawiki-api-announce mailing list at <https://lists.wikimedia.org/mailman/listinfo/mediawiki-api-announce> for notice of API deprecations and breaking changes. Use [[Special:ApiFeatureUsage]] to see usage of deprecated features by your application."
    }
}
```

## Geliştiriciler

* [Mavrikant](https://tr.wikipedia.org/wiki/Kullan%C4%B1c%C4%B1:Mavrikant) (11 Ekim 2015)

## License

* This project is licensed under the terms of the  [MIT License](https://choosealicense.com/licenses/mit/)
* Copyright © 2015 M. Serdar Karaman
