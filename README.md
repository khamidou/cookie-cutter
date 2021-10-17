# Cookie – a django template to build things quickly.

Django is a really well thought out framework but every time I set up a project with it I end up spending
45 mins changing the project layout and the default to have reasonable values. This templates does this so I can skip doing that.

## What's the difference with a regular django install

1. Config (including `settings.py` is in `config/`°
2. App code is in `web/`
3. App is setup to use whitenoise, gunicorn and django-environ out of the box.

Happy hacking!
