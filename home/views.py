from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import os
import psycopg2
from .models import Product, Product_Label
import datetime

SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL')

def index(request):
  context = {
    'segment': 'index'
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/tables.html", context)

# @login_required(login_url='/accounts/login/')
# def bc_button(request):
#   context = {
#     'parent': 'basic_components',
#     'segment': 'button'
#   }
#   return render(request, "pages/components/bc_button.html", context)

# @login_required(login_url='/accounts/login/')
# def bc_badges(request):
#   context = {
#     'parent': 'basic_components',
#     'segment': 'badges'
#   }
#   return render(request, "pages/components/bc_badges.html", context)

# @login_required(login_url='/accounts/login/')
# def bc_breadcrumb_pagination(request):
#   context = {
#     'parent': 'basic_components',
#     'segment': 'breadcrumbs_&_pagination'
#   }
#   return render(request, "pages/components/bc_breadcrumb-pagination.html", context)

# @login_required(login_url='/accounts/login/')
# def bc_collapse(request):
#   context = {
#     'parent': 'basic_components',
#     'segment': 'collapse'
#   }
#   return render(request, "pages/components/bc_collapse.html", context)

# @login_required(login_url='/accounts/login/')
# def bc_tabs(request):
#   context = {
#     'parent': 'basic_components',
#     'segment': 'navs_&_tabs'
#   }
#   return render(request, "pages/components/bc_tabs.html", context)

# @login_required(login_url='/accounts/login/')
# def bc_typography(request):
#   context = {
#     'parent': 'basic_components',
#     'segment': 'typography'
#   }
#   return render(request, "pages/components/bc_typography.html", context)

# @login_required(login_url='/accounts/login/')
# def icon_feather(request):
#   context = {
#     'parent': 'basic_components',
#     'segment': 'feather_icon'
#   }
#   return render(request, "pages/components/icon-feather.html", context)

# # Forms and Tables
# @login_required(login_url='/accounts/login/')
# def form_elements(request):
#   context = {
#     'parent': 'form_components',
#     'segment': 'form_elements'
#   }
#   return render(request, 'pages/form_elements.html', context)

# @login_required(login_url='/accounts/login/')
# def basic_tables(request):
#   context = {
#     'parent': 'tables',
#     'segment': 'basic_tables'
#   }
#   return render(request, 'pages/tbl_bootstrap.html', context)

# # Chart and Maps
# @login_required(login_url='/accounts/login/')
# def morris_chart(request):
#   context = {
#     'parent': 'chart',
#     'segment': 'morris_chart'
#   }
#   return render(request, 'pages/chart-morris.html', context)

# @login_required(login_url='/accounts/login/')
# def google_maps(request):
#   context = {
#     'parent': 'maps',
#     'segment': 'google_maps'
#   }
#   return render(request, 'pages/map-google.html', context)

# Authentication
class UserRegistrationView(CreateView):
  template_name = 'accounts/auth-signup.html'
  form_class = RegistrationForm
  success_url = '/accounts/login/'

class UserLoginView(LoginView):
  template_name = 'accounts/auth-signin.html'
  form_class = LoginForm

class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/auth-reset-password.html'
  form_class = UserPasswordResetForm

class UserPasswrodResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/auth-password-reset-confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/auth-change-password.html'
  form_class = UserPasswordChangeForm

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')

@login_required(login_url='/accounts/login/')
def profile(request):
  context = {
    'segment': 'profile',
  }
  return render(request, 'pages/profile.html', context)

@login_required(login_url='/accounts/login/')
def sample_page(request):
  context = {
    'segment': 'sample_page',
  }
  return render(request, 'pages/sample-page.html', context)

#@login_required(login_url='/accounts/login/')
def prediction(request):
    DB_HOST =  os.environ.get('DB_HOST')
    DB_USERNAME =  os.environ.get('DB_USERNAME')
    DB_PORT =  os.environ.get('DB_PORT')
    DB_PASSWORD =  os.environ.get('DB_PASSWORD')
    DB_NAME = os.environ.get('DB_NAME')
    conn = psycopg2.connect(
    database=DB_NAME,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
    )
    cursor = conn.cursor()
    cursor.execute(
    f"""SELECT DISTINCT ON ("label") "label"
    FROM products;""")
    bdd_data = list(cursor.fetchall())
    cursor.close()
    Product_Label.clear_content()
    Product_Label.objects.bulk_create([Product_Label(label=data[0]) for data in bdd_data])
    context = {
        'segment': 'prediction',
    }
    return render(request, 'pages/prediction.html', context)

@csrf_exempt
def update_data(request):
    DB_HOST =  os.environ.get('DB_HOST')
    DB_USERNAME =  os.environ.get('DB_USERNAME')
    DB_PORT =  os.environ.get('DB_PORT')
    DB_PASSWORD =  os.environ.get('DB_PASSWORD')
    DB_NAME = os.environ.get('DB_NAME')
    conn = psycopg2.connect(
    database=DB_NAME,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
    )
    cursor = conn.cursor()
    magasin_id=1
    date = request.POST.get('date')
    Product.clear_content()
    cursor.execute(
    f"""SELECT DISTINCT ON (sp."UPC", sp."date")
    sp."UPC", sp."date", s."Product_name", total_yhat
    FROM (
    SELECT "UPC", "date", SUM("yhat") AS total_yhat
    FROM sells_pred
    WHERE "magasin" = {magasin_id} AND "am_pm" != 'oow' AND "date" = '{date}'
    GROUP BY "UPC", "date"
    ) AS sp
    JOIN sells AS s ON sp."UPC" = s."UPC"
    ORDER BY sp."UPC", sp."date"; """)
    bdd_data = list(cursor.fetchall())
    cursor.close()
    if len(bdd_data) == 0:
      print("No data")
    else:
      Product.objects.bulk_create(
                [Product(upc=data[0], name=data[2], date=data[1], quantite=data[3]) for data in bdd_data]
            )
      print("Data added")
    return JsonResponse({'message': 'Données ajoutées avec succès'})

@csrf_exempt
def get_products_by_label(request):
    label = request.GET.get('letter', None)
    if label is not None:
        products = Product_Label.objects.filter(label__istartswith=label)
        products_data = [product.label for product in products]
        return JsonResponse(products_data, safe=False)
    return JsonResponse([], safe=False)