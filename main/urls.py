from django.urls import path
from main.views import create_product_flutter, show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, increase_amount, decrease_amount, delete_product
from main.views import edit_product
from main.views import delete_product, get_product_json, add_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),

    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),

    path('increase-amount/<int:id>', increase_amount, name='increase_amount'),
    path('decrease-amount/<int:id>', decrease_amount, name='decrease_amount'),
    path('delete-product/<int:id>', delete_product, name='delete_product'),

    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete/<int:id>', delete_product, name='delete_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]