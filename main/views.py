from django.shortcuts import render

# Create your views here.
def show_main(request):
    cupcakes = [
        {
        'name': 'Red Velvet Bliss',
        'price' : 25000,
        'amount' : 8,
        'description' : 'Cupcake berwarna merah dengan rasa khas cokelat dan kelembutan yang sempurna, dilapis dengan cream cheese frosting yang lembut.',
        'sweetness' : 7
        }
        
        ,{
        'name': 'Chocolate Fudge Delight',
        'price' : 30000,
        'amount' : 3,
        'description' : 'Cupcake cokelat intens dengan tekstur lembut dan kaya, dihiasi dengan ganache cokelat yang lezat.',
        'sweetness' : 9      
        }
        
        ,{
        'name': 'Vanilla Bean Dream',
        'price' : 28000,
        'amount' : 7,
        'description' : 'Cupcake vanila yang lembut dengan biji vanila asli, diberi hiasan buttercream vanilla yang lembut dan manis.',
        'sweetness' : 7 
        }
        
        ,{
        'name': 'Lemon Sunshine Cupcake',
        'price' : 23000,
        'amount' : 5,
        'description' : 'Cupcake beraroma jeruk lemon yang menyegarkan, dengan lapisan lemon curd di tengahnya dan frosting lemon yang cerah',
        'sweetness' : 6
        }
        
        ,{
        'name': 'Strawberry Swirl Sensation',
        'price' : 35000,
        'amount' : 10,
        'description' : 'Cupcake berisi selai strawberry dengan swirl merah muda yang cantik, ditutupi dengan whipped cream dan potongan buah strawberry segar.',
        'sweetness' : 7
        }
        
        ,{
        'name': 'Pumpkin Spice Pleasure',
        'price' : 40000,
        'amount' : 9,
        'description' : 'Cupcake labu dengan rempah-rempah musim gugur yang khas, dilapisi dengan cream cheese frosting',
        'sweetness' : 5
        }
        ]
    
    context = {
        'cupcakes' : cupcakes,
    }
    

    return render(request, "main.html", context)