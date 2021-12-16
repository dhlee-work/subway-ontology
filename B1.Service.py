from owlready2 import *
import owlready2
from config import config
import time
#
Subway_onto = get_ontology('./subway_ontology.rdf')
Subway_onto.load() 

#
def return_subclass_label(val):
    _q = f'SELECT ?y ' + '{ '+f'?x rdfs:label "{val}"'+' . ?y rdfs:subClassOf ?x}'
    r = list(default_world.sparql(_q))
    return [_cate[0].label[0] for _cate in r]
def return_subclass(val):
    _q = f'SELECT ?y ' + '{ '+f'?x rdfs:label "{val}"'+' . ?y rdfs:subClassOf* ?x}'
    r = list(default_world.sparql(_q))
    return r
def return_class(val):
    _q = f'SELECT ?x ' + '{ '+f'?x rdfs:label "{val}"'+' . }'
    r = list(default_world.sparql(_q))
    return r[0]

with Subway_onto:
    Total_cost_is = Imp()
    Total_cost_is.set_as_rule('''
    Menu(?x), 
    sandwich_cost(?x, ?c), 
    extra_topping_cost(?x, ?c1), 
    add(?result, ?c, ?c1) 
    -> total_cost(?x, ?result)
    ''')
with Subway_onto:
    Total_cal_is = Imp()
    Total_cal_is.set_as_rule('''
    Menu(?x), 
    sub_topping_cal(?x, ?c),
    bread_cal(?x, ?c1), 
    sauce_cal(?x, ?c2), 
    cheese_cal(?x, ?c3),
    extra_topping_cal(?x, ?c4),
    add(?d, ?c, ?c1),
    add(?e, ?d, ?c2),
    add(?f, ?e, ?c3),
    add(?result, ?f, ?c4)
    -> total_cal(?x, ?result)
    ''')
    
def choose_sanwich():
    print('안녕하세요? 무엇을 주문하시겠습니까? : sandwich')
    print('\n')
    _val = input() #'sandwich
    
    _tmp = return_subclass_label(_val)
    print('')
    print('--------------------------------------')
    print('어떤 종류의 대분류 샌드위치를 드시겠습니까?')
    print(' \n'.join(_tmp))
    print('\n')    
    _val = input() #input()
    _tmp = return_subclass_label(_val)
    print('--------------------------------------')
    print('어떤 종류의 소분류 샌드위치를 드시겠습니까?')
    print(' \n'.join(_tmp))
    print('\n')
    _val = input() #input()
    selected_sandwich = return_class(_val)[0]
    print('--------------------------------------')
    print(f'고객님께서 선택한 샌드위치는 {selected_sandwich.label[0]} 입니다')  
    return selected_sandwich

def topping(selected_sandwich):
    queue_sandwich = Subway_onto.Sandwich()
    queue_sandwich.sandwich_cost = selected_sandwich.cost_is
    print('주문하신 샌드위치의 기본 토핑은 아래와 같습니다 \n')
    # 메인토핑 추가
    for step3_val in selected_sandwich.has_for_main_topping:
        print(step3_val)
        #step3_val = selected_sandwich.has_for_main_topping[0].label[0]
        queue_sandwich.has_for_main_topping.append(step3_val())

    queue_sandwich.extra_topping_cal = 0
    for ii in queue_sandwich.has_for_main_topping:
        queue_sandwich.extra_topping_cal += ii.is_instance_of[0].has_for_extra_topping_calorie
    
    # 서브토핑 추가
    return_subclass_label('sub topping')
    for i in return_subclass_label('sub topping'):
        queue_sandwich.has_for_sub_topping.append(return_class(i)[0]())
    print('Main Topping :')
    print(queue_sandwich.has_for_main_topping)
    print('')
    print('Sub(Vege) Topping :')
    print(queue_sandwich.has_for_sub_topping)
    print('\n')
    print('------------------------------')
    print('1. 어떤 종류의 빵을 드시겠습니까?')
    step1_val = selected_sandwich.has_for_bread[0].label[0]
    _tmp = return_subclass_label(step1_val)    
    print(' \n'.join(_tmp))
    print('\n')    
    _val = input() #input()
    queue_sandwich.has_for_bread = [return_class(_val)[0]()]
    queue_sandwich.bread_cal = queue_sandwich.has_for_bread[0].is_instance_of[0].has_for_bread_calorie
    print(f'input : {queue_sandwich.has_for_bread}')
    
    print('------------------------------')
    print('2. 어떤 종류의 치즈를 드시겠습니까?')
    step2_val = selected_sandwich.has_for_cheese_topping[0].label[0]
    _tmp = return_subclass_label(step2_val)  
    print(' \n'.join(_tmp))
    print('\n')    
    _val = input() #input()
    queue_sandwich.has_for_cheese_topping = [return_class(_val)[0]()]
    queue_sandwich.cheese_cal = queue_sandwich.has_for_cheese_topping[0].is_instance_of[0].has_for_cheese_calorie
    print(f'input : {queue_sandwich.has_for_cheese_topping}')

    print('------------------------------')
    print('3. 토핑을 추가하겠겠습니까? : yes/no')
    _tmp = return_subclass_label('main topping')  
    print(' \n'.join(_tmp))
    print('\n')    
    _val = input() #input()
    if _val =='yes':
        print('어떤 종류의 토핑을 추가하겠겠습니까? : yes/no')
        print('\n')
        _val = input() #input()
        queue_sandwich.has_for_main_topping.append(return_class(_val)[0]())
        queue_sandwich.extra_topping_cost = return_class(_val)[0].extra_cost_is
        
        
        queue_sandwich.extra_topping_cal += queue_sandwich.has_for_main_topping[-1].is_instance_of[0].has_for_extra_topping_calorie
        print(f'input : {queue_sandwich.has_for_main_topping}')
    if _val =='no':
        print(f'input : {queue_sandwich.has_for_main_topping}')
        queue_sandwich.extra_topping_cal += 0
        queue_sandwich.extra_topping_cost = 0        
        
    print('------------------------------')
    print('4. 안드시는 채소가 있나요? : yes/no')
    for idx, j in enumerate(queue_sandwich.has_for_sub_topping):
        print(f'{idx} : {j}')
    print('\n')
    _val = str(input()) 
    if _val == 'no':
        pass
    else:
        complete='yes'
        while complete == 'yes':
            complete = _val
            print('몇 번째 채소를 빼겠습니까?')
            for idx, j in enumerate(queue_sandwich.has_for_sub_topping):
                print(f'{idx} : {j}')
            print('\n')
            _val = int(input())        
            queue_sandwich.has_for_sub_topping.pop(_val)
            print('더 채소를 빼시겠어요? : yes/no')
            print('\n')
            _val = input()
            complete = _val
    queue_sandwich.sub_topping_cal = 5*len(queue_sandwich.has_for_sub_topping)
    print(f'input : {queue_sandwich.has_for_sub_topping}')
    
    print('------------------------------')
    print('5. 어떤 소스를 뿌릴까요?')
    step5_val = selected_sandwich.has_for_sauce[0].label[0]
    _tmp = return_subclass_label(step5_val)  
    print(' \n'.join(_tmp))
    print('\n')    
    _val = input() #input()
    queue_sandwich.has_for_sauce = [return_class(_val)[0]]
    queue_sandwich.sauce_cal = queue_sandwich.has_for_sauce[0].has_for_sauce_calorie
    print(f'input : {queue_sandwich.has_for_sauce}')
    
    print('------------------------------')    
    print('샌드위치가 완성되었습니다.')
    for prop in list(queue_sandwich.get_properties()):
        print(f'{prop} : {prop[queue_sandwich]}\n')
    return queue_sandwich


print('Step1: choose sandwich')
selected_sandwich = choose_sanwich()

print('Step2: topping sandwich')
queue_sandwich = topping(selected_sandwich)
time.sleep(20)

print('Step3: reasoning')
sync_reasoner_pellet(infer_property_values = True,
                     infer_data_property_values = True)
time.sleep(20)
total_cost = queue_sandwich.total_cost
calorie = queue_sandwich.total_cal
print(f'고객님이 주문하신 샌드위치 칼로리는 : {calorie} Calorie, 가격은 : {total_cost}원 입니다')
