from owlready2 import *
import owlready2
from config import config

Subway_onto = get_ontology("http://test.org/subway.owl")
Subway_onto

with Subway_onto:
    class Subway(Thing):
        pass
    class Menu(Subway):
        #equivalent_to = [WaterSource & Not(ManMadeWaterSource)]
        pass
'''
Olives, Cucumbers, Peppers, Lettuce,
Pickle, Onions, Tomatoes, jalapeno,
'''
with Subway_onto :
    class Sub_topping(Menu):
        label = 'sub topping'
        pass
    class Olives(Sub_topping):
        label = 'olives'
        pass   
    class Cucumbers(Sub_topping):
        label = 'cucumbers'
        pass   
    class Sweet_Peppers(Sub_topping):
        label = 'sweet peppers'
        pass   
    class Lettuce(Sub_topping):
        label = 'lettuce'
        pass   
    class Pickle(Sub_topping):
        label = 'pickle'
        pass   
    class Tomatoes(Sub_topping):
        label = 'tomatoes'
        pass   
    class jalapeno(Sub_topping):
        label = 'jalapeno'
        pass   
    class Onions(Sub_topping):
        label = 'onions'
        pass       
    #서브 식재료 하위 클래스 만들기
Sub_topping_dict={'Olives':Olives,
                'Cucumbers':Cucumbers,
                'Sweet_Peppers':Sweet_Peppers,
                 'Lettuce':Lettuce,
                 'Pickle':Pickle,
                 'Tomatoes':Tomatoes,
                 'jalapeno':jalapeno,
                 'Onions':Onions}
sub_topping_list = list(Sub_topping_dict.keys())

''
with Subway_onto :
    class Main_topping(Menu):
        label = 'main topping'
        pass
    class Egg_mayo(Main_topping):
        label = 'egg mayo'
        pass   
    class Ham(Main_topping):
        label = 'ham'
        pass   
    class Tuna(Main_topping):
        label = 'tuna'
        pass   
    class Meatball(Main_topping):
        label = 'meatball'
        pass   
    class Bacon(Main_topping):
        label = 'bacon'
        pass   
    class Salami(Main_topping):
        label = 'salami'
        pass   
    class Rotisserie_chicken(Main_topping):
        label = 'rotisserie chicken'
        pass   
    class Roasted_chicken(Main_topping):
        label = 'roasted chicken'
        pass
    class Chicken_teriyaki(Main_topping):
        label = 'chicken teriyaki'
        pass
    class Pepperoni(Main_topping):
        label = 'pepperoni'
        pass
    class Roasted_beef(Main_topping):
        label = 'roasted beef'
        pass 
    class Chicken_strip(Main_topping):
        label = 'chicken strip'
        pass 
    class Pulled_Pork(Main_topping):
        label = 'pulled pork'
        pass 
    class Steak(Main_topping):
        label = 'steak'
        pass 
    class Omelet(Main_topping):
        label = 'omelet'
        pass 
    class Turkey(Main_topping):
        label = 'turkey'
        pass
    class Avocado(Main_topping):
        label = 'avocado'
        pass 
    #메인 식재료 하위 클래스 만들기
Main_topping_dict={'Egg_mayo':Egg_mayo,
                'Ham':Ham,
                'Tuna':Tuna,
                 'Meatball':Meatball,
                 'Bacon':Bacon,
                 'Salami':Salami,
                 'Rotisserie_chicken':Rotisserie_chicken,
                 'Roasted_chicken':Roasted_chicken,
                 'Chicken_teriyaki':Chicken_teriyaki,
                 'Pepperoni':Pepperoni,
                 'Roasted_beef':Roasted_beef,
                 'Chicken_strip':Chicken_strip,
                 'Pulled_Pork':Pulled_Pork,
                 'Steak':Steak,
                 'Omelet':Omelet,
                 'Turkey':Turkey,
                 'Avocado':Avocado}

'''
American
Shredded
Mozzarella
'''
with Subway_onto :
    class Cheese(Menu):
        label = 'cheese'
        pass
    class American(Cheese):
        label = 'american'
        pass 
    class Shredded(Cheese):
        label = 'shredded'
        pass 
    class Mozzarella(Cheese):
        label = 'mozzarella'
        pass 
    #치즈 하위 클래스 만들기
Cheese_dict={'American':American,
            'Shredded':Shredded,
            'Mozzarella':Mozzarella}

with Subway_onto :
    class Bread(Menu):
        label = 'bread'
        pass
    class Honey_Oat(Bread):
        label = 'honey oat'
        pass 
    class Hearty_Italian(Bread):
        label = 'hearty italian'
        pass 
    class Wheat(Bread):
        label = 'wheat'
        pass 
    class Parmesan_Oregano(Bread):
        label = 'parmesan oregano'
        pass 
    class White(Bread):
        label = 'white'
        pass 
    class Flat_Bread(Bread):
        label = 'flat bread'
        pass 
    #빵 하위 클래스 만들기
Bread_dict={'Honey_Oat':Honey_Oat, 
            'Hearty_Italian':Hearty_Italian, 
            'Wheat':Wheat, 
            'Parmesan_Oregano':Parmesan_Oregano, 
            'White':White,
            'Flat_Bread':Flat_Bread}

with Subway_onto :
    class Sauce(Menu):
        label = 'sauce'
        pass
    class Ranch(Sauce):
        label = 'ranch'
        pass   
    class Sweet_Onion(Sauce):
        label = 'sweet onion'
        pass   
    class Honey_Mustard(Sauce):
        label = 'honey mustard'
        pass   
    class Sweet_Chilli(Sauce):
        label = 'sweet chilli'
        pass   
    class Hot_Chilli(Sauce):
        label = 'hot chilli'
        pass   
    class Southwest_Chipotle(Sauce):
        label = 'southwest chipotle'
        pass   
    class Yellow_Mustard(Sauce):
        label = 'yellow mustard'
        pass   
    class Horseradish(Sauce):
        label = 'horseradish'
        pass   
    class Olive_Oil(Sauce):
        label = 'olive oil'
        pass   
    class Red_Wine_Vinaigrette(Sauce):
        label = 'red wine vinaigrette'
        pass   
    class Salt(Sauce):
        label = 'salt'
        pass   
    class Black_Pepper(Sauce):
        label = 'black pepper'
        pass   
    class Thousand_Island(Sauce):
        label = 'thousand island'
        pass   
    class Smoke_BBQ(Sauce):
        label = 'smoke bbq'
        pass
    class Mayonnaise(Sauce):
        label = 'mayonnaise'
        pass  
    class Italian_Dressing(Sauce):
        label = 'italian dressing'
        pass  
    #소스 하위 클래스 만들기
Sauce_dict={'Ranch':Ranch,
            'Mayonnaise':Mayonnaise,
            'Italian_Dressing':Italian_Dressing,
            'Sweet_Onion':Sweet_Onion, 
            'Honey_Mustard':Honey_Mustard, 
            'Sweet_Chilli':Sweet_Chilli, 
            'Hot_Chilli':Hot_Chilli,
            'Southwest_Chipotle':Southwest_Chipotle,
            'Horseradish':Horseradish,
            'Yellow_Mustard':Yellow_Mustard,
            'Olive_Oil':Olive_Oil,
            'Red_Wine_Vinaigrette':Red_Wine_Vinaigrette,
            'Salt':Salt,
            'Black_Pepper':Black_Pepper,
            'Thousand_Island':Thousand_Island,
            'Smoke_BBQ':Smoke_BBQ,
           }


class Sandwich(Menu):
    label = 'sandwich'
    pass
class Classic(Sandwich):
    label = 'classic'
    pass    
class Egg_Mayo_sandwich(Classic):
    label = 'egg mayo sandwich'
    pass
    #추천 소스 : Honey_Mustard, Sweet_Chilli
class Ham_sandwich(Classic):
    label = 'ham sandwich'
    pass   
    #추천 소스 : Ranch, Thousand_Island
class Tuna_sandwich(Classic):
    label = 'tuna sandwich'
    pass
    #추천 소스 : Honey_Mustard, Smoke_BBQ
class Meatball_sandwich(Classic):
    label = 'meatball sandwich'
    pass   
    #추천 소스 : Ranch, Hot_Chilli
class BLT_sandwich(Classic):
    label = 'blt sandwich'
    pass   
    #추천 소스 : Mayonnaise, Sweet_Chilli
class Italian_BMT_sandwich(Classic):
    label = 'italian bmt sandwich'
    pass   
    #추천 소스 : Mayonnaise, Southwest, Southwest_Chipotle
#------------------------------------------------------------------------------------------------------       
# ㅅㅜ저ㅇ 필요
class Fresh_and_Light(Sandwich):
    label = 'fresh and light'
    pass    
class Veggie_Delite_sandwich(Fresh_and_Light):
    label = 'veggie delite sandwich'
    pass
    #추천 소스 : Red_Wine_Vinaigrette, Olive_Oil, Southwest_Chipotle
class Turkey_sandwich(Fresh_and_Light):
    label = 'turkey sandwich'
    pass
    #추천 소스 : Honey Mustard, Southwest_Chipotle, Ranch
class Subway_Club_sandwich(Fresh_and_Light):
    label = 'subway club sandwich'
    pass
    #추천 소스 : Honey Mustard, Smoke_BBQ, Ranch
class Roasted_Beef_sandwich(Fresh_and_Light):
    label = 'roasted beef sandwich'
    pass 
    #추천 소스 : Salt, Black_Pepper, Red_Wine_Vinaigrette, Olive_Oil
class Rotisserie_Chicken_sandwich(Fresh_and_Light):
    label = 'rotisserie chicken sandwich'
    pass
    #추천 소스 : Horseradish, Sweet_Onion
class Roasted_Chicken_sandwich(Fresh_and_Light):
    label = 'roasted chicken sandwich'
    pass
    #추천 소스 : Salt, Black_Pepper, Honey_Mustard
#------------------------------------------------------------------------------------------------------      
class Premium(Sandwich):
    label = 'premium'
    pass
class Chicken_Teriyaki_sandwich(Premium):
    label = 'chicken teriyaki sandwich'
    pass
    #추천 소스 : Ranch, Sweet_Onion, Smoke_BBQ 
class Turkey_Bacon_sandwich(Premium):
    label = 'turkey bacon sandwich'
    pass   
    #추천 소스 : Sweet_Onion, Southwest_Chipotle 
class Spicy_Italian_sandwich(Premium):
    label = 'spicy italian sandwich'
    pass     
    #추천 소스 : Ranch, Mayonnaise, Hot_Chilli
class Chicken_Bacon_Ranch_sandwich(Premium):
    label = 'chicken bacon ranch sandwich'
    pass 
    #추천 소스 : Black_Pepper, Horseradish, Ranch
class Subway_Melt_sandwich(Premium):
    label = 'subway melt sandwich'
    pass    
    #추천 소스 : Honey Mustard, Sweet_Chilli
class Pulled_Pork_sandwich(Premium):
    label = 'pulled pork sandwich'
    pass   
    #추천 소스 : Ranch, Sweet_Onion, Smoke_BBQ  
class Steak_And_Cheese_sandwich(Premium):
    label = 'steak and cheese sandwich'
    pass
    #추천 소스 : Smoke_BBQ, Yellow_Mustard
class Turkey_Bacon_Avocado_sandwich(Premium):
    label = 'turkey bacon avocado sandwich'
    pass   
    #추천 소스 : Salt, Black_Pepper, Olive_Oil

Sandwich_dict = {
                'Egg_Mayo_sandwich':Egg_Mayo_sandwich,
                'Ham_sandwich':Ham_sandwich,
                'Tuna_sandwich':Tuna_sandwich,
                'Meatball_sandwich':Meatball_sandwich,
                'BLT_sandwich':BLT_sandwich,
                'Italian_BMT_sandwich':Italian_BMT_sandwich,
                'Veggie_Delite_sandwich':Veggie_Delite_sandwich,
                'Turkey_sandwich':Turkey_sandwich,
                'Subway_Club_sandwich':Subway_Club_sandwich,
                'Roasted_Beef_sandwich':Roasted_Beef_sandwich,
                'Rotisserie_Chicken_sandwich':Rotisserie_Chicken_sandwich,
                'Roasted_Chicken_sandwich':Roasted_Chicken_sandwich,
                'Chicken_Teriyaki_sandwich':Chicken_Teriyaki_sandwich,
                'Turkey_Bacon_sandwich':Turkey_Bacon_sandwich,
                'Spicy_Italian_sandwich':Spicy_Italian_sandwich,
                'Chicken_Bacon_Ranch_sandwich':Chicken_Bacon_Ranch_sandwich,
                'Subway_Melt_sandwich':Subway_Melt_sandwich,
                'Pulled_Pork_sandwich':Pulled_Pork_sandwich,
                'Steak_And_Cheese_sandwich':Steak_And_Cheese_sandwich,
                'Turkey_Bacon_Avocado_sandwich':Turkey_Bacon_Avocado_sandwich
                                    }

############calorie Property
with Subway_onto:
    class has_for_bread_calorie(DataProperty, FunctionalProperty): 
        domain = [Bread]
        range = [float]
    class has_for_sauce_calorie(DataProperty, FunctionalProperty): 
        domain = [Sauce]
        range = [float]
    class has_for_sandwich_calorie(DataProperty, FunctionalProperty): 
        domain = [Sandwich]
        range = [float]
    class has_for_cheese_calorie(DataProperty, FunctionalProperty): 
        domain = [Cheese]
        range = [float]
    class has_for_extra_topping_calorie(DataProperty, FunctionalProperty): 
        domain = [Main_topping]
        range = [float]
    class has_for_sub_topping_calorie(DataProperty, FunctionalProperty): 
        domain = [Sub_topping]
        range = [float]
        
############Cost Property        
with Subway_onto:
    class cost_is(DataProperty, FunctionalProperty): 
        domain = [Sandwich]
        range = [float]
    class extra_cost_is(DataProperty, FunctionalProperty): 
        domain = [Main_topping]
        range = [float]
        
######### calorie
for key in Bread_dict:
    Bread_dict[key].has_for_bread_calorie = config.bread_cal[key]
for key in Sauce_dict:
    Sauce_dict[key].has_for_sauce_calorie = config.sauce_cal[key]
for key in Sandwich_dict:
    Sandwich_dict[key].has_for_sandwich_calorie = config.sandwich_cal[key]
for key in Cheese_dict:
    Cheese_dict[key].has_for_cheese_calorie = config.cheese_cal[key] 
for key in Sub_topping_dict:
    Sub_topping_dict[key].has_for_sub_topping_calorie = config.sub_topping_cal[key] 
for key in Main_topping_dict:
    Main_topping_dict[key].has_for_extra_topping_calorie = config.Main_topping_cal[key] 
######### Cost - Sandwich 
for key in Sandwich_dict:
    Sandwich_dict[key].cost_is = config.Sandwich_cost[key]
for key in Main_topping_dict:
    Main_topping_dict[key].extra_cost_is = config.Extra_topping_cost[key]

######### Sandwich Property
with Subway_onto:
    class has_for_bread(Bread >> Sandwich):
        pass
    class has_for_cheese_topping(Cheese >> Sandwich):
        pass
    class has_for_main_topping(Main_topping >> Sandwich):
        pass
    class has_for_sub_topping(Sub_topping >> Sandwich):
        pass
    class has_for_sauce(Sauce >> Sandwich):
        pass
    
with Subway_onto:
    class sandwich_cost(Subway >> float, FunctionalProperty): pass
    class extra_topping_cost(Subway >> float, FunctionalProperty): pass
    class total_cost(Subway >> float, FunctionalProperty): pass
    class sub_topping_cal(Subway >> float, FunctionalProperty): pass
    class bread_cal(Subway >> float, FunctionalProperty): pass
    class sauce_cal(Subway >> float, FunctionalProperty): pass
    class cheese_cal(Subway >> float, FunctionalProperty): pass
    class extra_topping_cal(Subway >> float, FunctionalProperty): pass
    class total_cal(Subway >> float, FunctionalProperty): pass
    

Egg_Mayo_sandwich.equivalent_to = [Sandwich &
                                   has_for_bread.some(Bread) & \
                                   has_for_main_topping.some(Egg_mayo) & \
                                   has_for_cheese_topping.some(Cheese)& \
                                   has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Ham_sandwich.equivalent_to = [Sandwich &
                              has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Ham) & \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Tuna_sandwich.equivalent_to = [Sandwich &
                               has_for_bread.some(Bread) & \
                               has_for_main_topping.some(Tuna) & \
                               has_for_cheese_topping.some(Cheese)& \
                               has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Meatball_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Meatball) & \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
BLT_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Bacon) & \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Italian_BMT_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Pepperoni)& \
                              has_for_main_topping.some(Salami)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Veggie_Delite_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Turkey_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Turkey)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Subway_Club_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Turkey)& \
                              has_for_main_topping.some(Ham)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Roasted_Beef_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Roasted_beef)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Rotisserie_Chicken_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Rotisserie_chicken)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Roasted_Chicken_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Roasted_chicken)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Chicken_Teriyaki_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Chicken_teriyaki)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Turkey_Bacon_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Turkey)& \
                              has_for_main_topping.some(Bacon)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Spicy_Italian_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Pepperoni)& \
                              has_for_main_topping.some(Salami)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Chicken_Bacon_Ranch_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Chicken_strip)& \
                              has_for_main_topping.some(Bacon)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Subway_Melt_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Turkey)& \
                              has_for_main_topping.some(Ham)& \
                              has_for_main_topping.some(Bacon)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Pulled_Pork_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Pulled_Pork)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
Steak_And_Cheese_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Steak)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]
#Turkey_Bacon_Avocado_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
#                              has_for_main_topping.some(Turkey&Avocado&Bacon)& \
#                              has_for_cheese_topping.some(Cheese)& \
#                              has_for_sub_topping.some(Sub_topping) &\
#                                   has_for_sauce.some(Sauce)]
Turkey_Bacon_Avocado_sandwich.equivalent_to = [has_for_bread.some(Bread) & \
                              has_for_main_topping.some(Turkey)& \
                              has_for_main_topping.some(Avocado)& \
                              has_for_main_topping.some(Bacon)& \
                              has_for_cheese_topping.some(Cheese)& \
                              has_for_sub_topping.some(Sub_topping) &\
                                   has_for_sauce.some(Sauce)]

Subway_onto.save(file='./subway_ontology.rdf', format='rdfxml')