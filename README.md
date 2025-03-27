# BlogSite

Merhaba! Bu proje, Django ve Tailwind CSS kullanılarak geliştirilmiş basit bir blog uygulamasıdır. Kullanıcılar kayıt olabilir, giriş yapabilir, post oluşturabilir, düzenleyebilir ve kendi profil sayfasından yalnızca kendi gönderilerini görebilirler.

## Özellikler

- Kullanıcı kayıt ve giriş sistemi  
- Yeni post oluşturma, düzenleme ve silme  
- Sadece kullanıcıya ait postların listelendiği profil sayfası  
- Tailwind CSS ile pastel tonlarda şık ve sade tasarım




## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

### 1. Reposu klonlayın:

```bash
git clone https://github.com/nslzsn/blogsite.git
cd blogsite
```

### 2. Sanal ortam oluşturun (isteğe bağlı ama önerilir):

```bash
python -m venv env
source env/bin/activate  # Windows için: env\Scripts\activate
```

### 3. Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

Eğer `requirements.txt` yoksa, aşağıdaki temel paketleri yükleyebilirsiniz:

```bash
pip install django
pip install django-tailwind
```

### 4. Tailwind kurulumu (ilk kez çalıştırırken):

```bash
python manage.py tailwind init
```

`settings.py` dosyanızda gerekli Tailwind ayarlarının yapıldığından emin olun.

### 5. Veritabanını oluşturun:

```bash
python manage.py migrate
```

### 6. Admin hesabı oluşturun (isteğe bağlı):

```bash
python manage.py createsuperuser
```

### 7. Uygulamayı başlatın:

```bash
python manage.py runserver
```

Tarayıcınızdan [http://127.0.0.1:8000](http://127.0.0.1:8000) adresine giderek uygulamayı görebilirsiniz.

---

## Katkı Sağlama

Katkıda bulunmak isterseniz pull request göndermekten çekinmeyin!

---

## Lisans

MIT License
