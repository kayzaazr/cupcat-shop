from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
        
     # Test untuk menguji apakah model Item telah berhasil dibuat
    def test_item_model_fields(self):
        # Membuat objek Item untuk memeriksa atribut-atributnya
        item = Item.objects.create (
            name='Contoh Item',
            amount= 26,
            description='Deskripsi Item',
            sweetness = 10,
            price = 12000,
        )

        # Memeriksa apakah nilai atribut sesuai
        self.assertEqual(item.name, 'Contoh Item')
        self.assertEqual(item.amount, 26)
        self.assertEqual(item.description, 'Deskripsi item')