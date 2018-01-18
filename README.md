## 博客
-------

### 演示:
- [http://www.billionhouse.com/blog](http://www.billionhouse.com/blog)

### 技术

- Django 2.0.1
- Python 3.6
- MySQL

### 环境依赖

diff-match-patch==20121119
Django==2.0.1
django-disqus==0.5
django-import-export==0.7.0
django-nocaptcha-recaptcha==0.0.20
django-suit==0.2.25
django-wysiwyg-redactor==0.5.1
et-xmlfile==1.0.1
freeze==1.0.10
jdcal==1.3
mock==2.0.0
odfpy==1.3.6
openpyxl==2.4.9
pbr==1.10.0
Pillow==5.0.0
PyMySQL==0.8.0
pytz==2016.6.1
PyYAML==3.12
six==1.10.0
tablib==0.12.1
unicodecsv==0.14.1
xlrd==1.1.0
xlwt==1.3.0

### 安装

**1. 创建虚拟环境.**

```
$ virtualenv --python=/usr/bin/python3 yourenv
$ source bin/activate
```

**2. 克隆项目t**

```
$ git clone https://github.com/Aibd/blogproject.git
```

**3. 安装所有依赖包**

```
$ pip install -r requirements.txt
```

**4. 数据库 迁移**

```
$ ./manage.py makemigrations
$ ./manage.py migrate
```

**5. 运行服务**

```
$ ./manage.py runserver
```
-------

### 截图:

#### 主页

![Homepage](__screenshot/home.png  "Homepage")

#### 详细博文

![Detail Post](__screenshot/detail.png  "Detail Post")

#### 后台管理 _(用 django suit)_

![Admin Dashboard](__screenshot/admin.png  "Admin Dashboard")
