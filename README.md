# start
```py
# Create the directory for the project
mkdir back_end_python
cd back_end_python

# Create venv 
py -m venv myvenv
myvenv\Scripts\activate
# on Mac use `source myvenv/bin/activate

# Install Django and REST framework into myvenv
pip install django
pip install djangorestframework

# set up new project
django-admin startproject django_project .
cd django_project
django-admin startapp django_api


pip install django-cors-headers
```

# Database Mysql
```py
# install mysqlclient
pip install mysqlclient
```
# coding
## setting.py
```py
INSTALLED_APPS = [
    'corsheaders',
    'django_api',
    'rest_framework',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',#Access-Control-Allow-Origin
]
```
# tips
```python
# server will postpone response about 5 seconds after got the request from front-end.
py manage.py runserver
# will resolve the the delay response
py manage.py runserver --noreload
# Allow: GET,POST,HEAD, OPTIONS, Not allowed PUT,PATCH, DELETE  
class CategoriesViewSet(viewsets.ModelViewSet):
# generics.RetrieveUpdateDestroyAPIView will  allowed PUT,PATCH, DELETE 
class CategoriesViewSet(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):    
```
## install Django filter
### tutorial: https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html
```
 pip install django-filter
```
## category create
![](./screenshoot/categoryCreate.png)
![](./screenshoot/categorydb.png)
![](./screenshoot/categories.png)

## API (Categories)
```
# (get: get categories, post: create category): 
http://127.0.0.1:8000/api/categories/ 
# (put,patch: update category ,delete: remove category): 
http://127.0.0.1:8000/api/categories/_id/
# filter(get: get by parentId) : 
http://127.0.0.1:8000/api/categories/?parentId=2

```
## API (products)
```
# (get: get products, post: crete product)
http://127.0.0.1:8000/api/products/ 
# (put,patch: update product, delete: remove product)
http://127.0.0.1:8000/api/products/_id/ 
```
## API (roles)
```
# (get: get roles, post: crete role)
http://127.0.0.1:8000/api/roles/ 
# (put,patch: update role, delete: remove role)
http://127.0.0.1:8000/api/products/_id/ 
## save picture to and get picture form back-end & save array to Mysql
![](./screenshoot/getPicture.png)


