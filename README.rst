Simple template for Telegram bot. Mostly for personal use.


```
Current issue can be checked: http://t.me/PyrogramTemplateBot #if my server is fine 😄
Not sure, that everything is well structured and easy to get, but it works for me.

Used libs:

Pyrogram    https://github.com/pyrogram/pyrogram            # as main
Plate       https://github.com/delivrance/plate             # for language switch
Pyromod     https://github.com/usernein/pyromod             # for dialogue mastering
Sqlitedict  https://github.com/RaRe-Technologies/sqlitedict # for sqlite managing

and others, of course, including dependencies, so my gratefulness to all authors,
developers, for their will to make the world a better place to live.
```



1. What can this bot do.

- adds new user to sqlite key-value database;
- checks user in database for certain attributes, like language;
- interviews user for personal data, for registration or contract;
- sends all data collected to google sheets;
- contains admin panel for mailing, restarting, etc.

2. Bot folders and files.

/entities  - classes are kept, User and Interview;
/locales   - .jsons with bot answer texts;
/maillogs  - logs after messaging bot subscribers;
/maindata  - config, session files, database
/plugins   - handlers, according to pyrogram's smart plugins;
/utils     - workers for database, validation, google sheets, etc.;
activator.py - session maker, can be removed after session is creates;
main.py      - main start file.

All imports are made to main.py, and imported to plugins with `from main impot *`, it
may not be a good decision, but works fine for me.

3. How to run in on your computer or else. # thats what i do, actually

1. Clone repository.
2. `git remote remove origin`.
3. Install requirements.
4. If needed, create google  - service account with drive and sheet apis;
                             - sheet, with access permition;
                             - credentials, rename, place to maindata.
5. Fill /maindata/config.py, so <PASTE_YOUR_DATA_HERE> is replaced.
6. Fill api_id, api_hash according to pyrogram docs in activator.py, run it.
7. Run main.py

From now session file in /maindata/ is created, and activator.py can be removed.
After running main.py (with venv enabled, of course) app will create main.db - database
file. main.csv file - is last one, that was sent to admin by bot, is overwritten
all the time. Log file with project name will appear in main project folder.

4. About admin panel.

To get access to admin panel - admin id is to be specified in admins list, so it can not
be checked in http://t.me/PyrogramTemplateBot.

Simply run `/admin` to get menu and `/commands` to get commands list.
Commands `/kill`, `/restart`, `/reboot` are tested in UBUNTU 18.04 only.



Notes.

I use key-value database, so sqlitedict can  be changed to redis by changing
database.py to some redis worker with minor work done.

For @usernain.

Cezar, implementation you were interested at - plugins/form. In works with class Interview,
so any other question or data request is simply defined as class attribute, without
messing up with code. Your new listener is in line 92. Code is not final, i keep
playing with it.

Best regards to all you people, thanks for any useful hint, advice and healthy criticism.
