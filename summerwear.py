grad=int(input())
time=input()
Outfit=None
shoes=None

if time=="Morning":
    if grad>=10 and grad<=18:
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'

    elif grad<18 and grad>=24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

    elif grad>=25:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
        
elif time=="Afternoon":
    if grad>=10 and grad<=18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

    elif grad<18 and grad>=24:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    elif grad>=25:
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
elif time=="Evening":
    if grad>=10 and grad<=18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

    elif grad<18 and grad>=24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

    elif grad>=25:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
        
print(f"It's {grad} degrees, get your {Outfit} and {Shoes}.")

