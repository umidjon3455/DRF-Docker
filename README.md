# DRF Docker

Django REST Framework loyihasi.

## Talablar

- Python 3.12+
- pip

## O'rnatish

```bash
git clone https://github.com/umidjon3455/DRF-Docker.git
cd DRF-Docker
python -m venv .venv
```

Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Kutubxonalarni o'rnating:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Muhit o'zgaruvchilari

Ishga tushirishdan oldin quyidagi muhit o'zgaruvchilarini belgilang:

- `DJANGO_SECRET_KEY` — maxfiy, tasodifiy Django kaliti.
- `DJANGO_DEBUG` — lokal ishlab chiqishda `True`, production'da `False`.
- `DJANGO_ALLOWED_HOSTS` — vergul bilan ajratilgan hostlar, masalan `example.com,www.example.com`.

Production'da haqiqiy maxfiy kalitni kodga yoki Git'ga joylamang. Avvalgi commitlarda maxfiy kalit oshkor bo'lgan bo'lsa, uni almashtiring.

## Migratsiya va server

```bash
python manage.py migrate
python manage.py runserver
```

API server: http://127.0.0.1:8000/

## Texnologiyalar

- Django
- Django REST Framework
- drf-yasg (Swagger/OpenAPI)
