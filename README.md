# Webmon

Simple web service status code monitoring script with telegram notifications

## Usage
```
python webmon.py --token <telegram bot token> --user_id <notification user id(yours e.g.)> --endpoint https://monitor_target --goal <desired http status code(default 200)>
```