# import pandas as pd
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .models import Sale


def user_logout(request):
    logout(request)
    return redirect('/')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home/')
            else:
                return HttpResponse('Invalid Login Credentials')
        else:
            return HttpResponse('Invalid Form Data')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def home(request):
    # total monthly sales
    monthly_total_sales = get_monthly_sales()
    months = get_month_lables()

    # total sales by product category
    categories = get_category_labels()
    sales_by_categories = get_sales_by_categories()

    # customer type chart
    customer_types = get_customer_types()
    customer_labels = ['Normal', 'Member']

    # customer gender  chart
    customers_by_gender = get_customers_by_gender()
    customer_gender_labels = ['Male', 'Female']

    # payment method chart
    payment_methods = get_payment_methods()
    payment_method_labels = ['eWallet', 'Cash', 'Credit Card']

    template = 'salesapp/home.html'
    context = {
        'months': months,
        'monthly_total_sales': monthly_total_sales,
        'categories': categories,
        'sales_by_categories': sales_by_categories,
        'customer_types': customer_types,
        'customer_labels': customer_labels,
        'customers_by_gender': customers_by_gender,
        'customer_gender_labels': customer_gender_labels,
        'payment_methods': payment_methods,
        'payment_method_labels': payment_method_labels
    }
    return render(request, template, context)


def get_customers_by_gender():
    male_customers = len(Sale.objects.filter(gender='Male'))
    female_customers = len(Sale.objects.filter(gender='Female'))
    return [male_customers, female_customers]


def get_customer_types():
    normal_customers = len(Sale.objects.filter(customer_type='Normal'))
    member_customers = len(Sale.objects.filter(customer_type='Member'))
    return [normal_customers, member_customers]


def get_ratings():
    sales = Sale.objects.all()
    ratings = []
    for sale in sales:
        ratings.append(sale.rating)
    return ratings


def get_payment_methods():
    ewallet_payments = len(Sale.objects.filter(
        payment_method__contains="Ewallet"))
    cash_payments = len(Sale.objects.filter(
        payment_method__contains="Cash"))
    credit_payments = len(Sale.objects.filter(
        payment_method__contains="Credit"))
    return [ewallet_payments, cash_payments, credit_payments]


def get_sales_by_categories():
    hb_sales = len(Sale.objects.filter(product_line__contains="Health"))
    ea_sales = len(Sale.objects.filter(product_line__contains="Electronic"))
    hl_sales = len(Sale.objects.filter(product_line__contains="Home"))
    st_sales = len(Sale.objects.filter(product_line__contains="Sports"))
    fb_sales = len(Sale.objects.filter(product_line__contains="Food"))
    fa_sales = len(Sale.objects.filter(product_line__contains="Fashion"))

    sales_by_categories = [hb_sales, ea_sales,
                           hl_sales, st_sales, fb_sales, fa_sales]

    return sales_by_categories


def get_category_labels():
    categories = ['Health & Beauty', 'Electronic Accessories', 'Home & Lifestyle',
                  'Sports & Travel', 'Food & Beverage', 'Fashion Accessories']
    return categories


def get_monthly_sales():
    jan_sales = len(Sale.objects.filter(date__month=1))
    feb_sales = len(Sale.objects.filter(date__month=2))
    mar_sales = len(Sale.objects.filter(date__month=3))
    apr_sales = len(Sale.objects.filter(date__month=4))
    may_sales = len(Sale.objects.filter(date__month=5))
    jun_sales = len(Sale.objects.filter(date__month=6))
    jul_sales = len(Sale.objects.filter(date__month=7))
    aug_sales = len(Sale.objects.filter(date__month=8))
    sep_sales = len(Sale.objects.filter(date__month=9))
    oct_sales = len(Sale.objects.filter(date__month=10))
    nov_sales = len(Sale.objects.filter(date__month=11))
    dec_sales = len(Sale.objects.filter(date__month=12))

    monthly_total_sales = [jan_sales, feb_sales, mar_sales, apr_sales, may_sales,
                           jun_sales, jul_sales, aug_sales, sep_sales, oct_sales, nov_sales, dec_sales]
    return monthly_total_sales


def get_month_lables():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months


@login_required
def health_beauty(request):
    template = 'salesapp/health_beauty.html'
    context = get_context('Health')
    return render(request, template, context)


@login_required
def home_lifestyle(request):
    template = 'salesapp/home_lifestyle.html'
    context = get_context('Home')
    return render(request, template, context)


@login_required
def sports_travel(request):
    template = 'salesapp/sports_travel.html'
    context = get_context('Sports')
    return render(request, template, context)


@login_required
def electronic_accessories(request):
    template = 'salesapp/electronic_acc.html'
    context = get_context('Electronic')
    return render(request, template, context)


@login_required
def fashion_accessories(request):
    template = 'salesapp/fashion_acc.html'
    context = get_context('Fashion')
    return render(request, template, context)


@login_required
def food_beverages(request):
    template = 'salesapp/food_beverage.html'
    context = get_context('Food')
    return render(request, template, context)


def get_context(product_category):
    monthly_total_sales = get_monthly_sales_by_category(product_category)
    months = get_month_lables()

    customers_by_gender = get_customers_by_gender_category(product_category)
    customer_gender_labels = ['Male', 'Female']

    branch_sales = get_branch_sales_category(product_category)
    branch_labels = ['Branch A', 'Branch B', 'Branch C']

    context = {

        'months': months,
        'monthly_total_sales': monthly_total_sales,
        'customers_by_gender': customers_by_gender,
        'customer_gender_labels': customer_gender_labels,
        'branch_sales': branch_sales,
        'branch_labels': branch_labels,
    }
    return context


def get_branch_sales_category(product_category):
    branch_a_sales = len(Sale.objects.filter(
        branch='A', product_line__contains=product_category))
    branch_b_sales = len(Sale.objects.filter(
        branch='B', product_line__contains=product_category))
    branch_c_sales = len(Sale.objects.filter(
        branch='C', product_line__contains=product_category))
    branch_sales = [branch_a_sales, branch_b_sales, branch_c_sales]
    return branch_sales


def get_customers_by_gender_category(product_category):
    male_customers = len(Sale.objects.filter(
        gender='Male', product_line__contains=product_category))
    female_customers = len(Sale.objects.filter(
        gender='Female', product_line__contains=product_category))
    customers_by_gender = [male_customers, female_customers]
    return customers_by_gender


def get_monthly_sales_by_category(product_category):
    jan_sales = len(Sale.objects.filter(
        product_line__contains=product_category, date__month=1))
    feb_sales = len(Sale.objects.filter(
        product_line__contains=product_category, date__month=2))
    mar_sales = len(Sale.objects.filter(
        product_line__contains=product_category, date__month=3))
    apr_sales = len(Sale.objects.filter(
        product_line__contains=product_category, date__month=4))
    may_sales = len(Sale.objects.filter(
        product_line__contains=product_category, date__month=5))
    jun_sales = len(Sale.objects.filter(
        product_line__contains=product_category, date__month=6))
    jul_sales = len(Sale.objects.filter(
        product_line__contains=product_category, date__month=7))
    aug_sales = len(Sale.objects.filter(
        product_line__contains=product_category, date__month=8))
    sep_sales = len(Sale.objects.filter(
        product_line__contains=product_category, date__month=9))
    oct_sales = len(Sale.objects.filter(
        product_line__contains=product_category, date__month=10))
    nov_sales = len(Sale.objects.filter(
        product_line__contains=product_category, date__month=11))
    dec_sales = len(Sale.objects.filter(
        product_line__contains=product_category, date__month=12))

    monthly_total_sales = [jan_sales, feb_sales, mar_sales, apr_sales, may_sales,
                           jun_sales, jul_sales, aug_sales, sep_sales, oct_sales, nov_sales, dec_sales]

    return monthly_total_sales


# def load_data(request):
#     df = pd.read_csv(
#         'C:\\Users\\nsush\\Desktop\\sales_data.csv', sep=',')
#     sales = []

#     for i in range(len(df)):
#         sales.append(
#             Sale(
#                 invoice_id=df.iloc[i, 0],
#                 branch=df.iloc[i, 1],
#                 city=df.iloc[i, 2],
#                 customer_type=df.iloc[i, 3],
#                 gender=df.iloc[i, 4],
#                 product_line=df.iloc[i, 5],
#                 unit_price=df.iloc[i, 6],
#                 quantity=df.iloc[i, 7],
#                 tax=df.iloc[i, 8],
#                 total=df.iloc[i, 9],
#                 date=df.iloc[i, 10],
#                 payment_method=df.iloc[i, 11],
#                 cogs=df.iloc[i, 12],
#                 gross_income=df.iloc[i, 13],
#                 rating=df.iloc[i, 14]

#             )
#         )
#     Sale.objects.bulk_create(sales)
#     return HttpResponse('data loaded.')
