#დაწერეთ პროგრამა სადაც მომხმარებელს შეეძლება შემოიყვანოსტ წილადი, მაგალითად 1/4 ანდ 2/7 და ა.შ.
#შემოტანილი მონაცემებიდან წილადი გადაიყვანეთ პროცენტებში, მაგალითად თუ შემოვიდა 1/4 ეს არის 25%, რადგან 1 / 4 * 100 = 25
#იმ შემთხვევაში თუ მიღებული შედეგი 1-ზე ნაკლებია ან ტოლია მაშინ გამოპრინტეთ E,
#იმ შემთხვევაში თუ შედეგი 99 ტოლია ან მეტია გამოპრინტეთ F, სხვა შემთხვევაში შედეგის რიცხვითი მნიშვნელობა % ნიშანთან ერთად. 


while True:
    a =(input("what number would you like to enter? only decimals pls: "))
   
    try:
        answer = a.split("/")
        if answer[1] == '0':
            continue
        result = (int(answer[0]) / int(answer[1]) * 100)
        if result <= 1:
            print('E')
        elif result >= 99:
            print('F')
        else:
            print(final)
        
    
    except:
        continue
    final = (f'your % is {result:.2f}')
    if result <= 1:
        print('E')
    elif result >= 99:
        print('F')
    else:
        print(final)
        break
 





# დაწერეთ პროგრამა რომლის მეშვეობითაც მომხმარებელს ეხნება შესაძლებლობა ჩაწეროს კერძის დასახელება იმდენჯერ რამდენჯერაც მოისურვებს, 
# ყოველ ჩაწერაზე თქვენ უნდა გამოიტანოთ ჯამური ღირებულება ამ კერძების.
# პროგრამის მუშაობა უნდა შეწყდეს მხოლოდ მაშინ თუ მომხმარებელი გამოიყენებს EOFError.


# food_dict = {
#     "Baja Taco": 4.25,
#     "Burrito": 7.50,
#     "Bowl": 8.50,
#     "Nachos": 11.00,
#     "Quesadilla": 8.50,
#     "Super Burrito": 8.50,
#     "Super Quesadilla": 9.50,
#     "Taco": 3.00,
#     "Tortilla Salad": 8.00
# }
# total = 0
# while True:
#     try:
#         answer  = input("what food would you like? ")
#         item = answer.title()
#         if item in food_dict:
#             total += food_dict[item]
#             print(total)
#             continue
       
#         else:
#             item not in food_dict
#             continue

#     except EOFError:
#         break




# დაწერეთ პროგრამა სადაც მომხმარებელს ექნება საშუალება შეიყვანოს თითოეულ ხაზზე სასურსათო სია 
# მას შემდეგ რაც ამუშავდება EOFError მაშინ თქვენ უნდა გამოიტანოთ უნიკალური დასახელებული სურსათის დასახელებები მათი რაოდენობის მიხედვით,
# გაითვალისწინეთ რომ გამოტანილი სია უნდა იყოს მაღალი რეგისტრის ასოებით, სორტირებული ალფავიტის მიხედვით და წინ უნდა ეწეროს რაოდენობა 
# თუ რამდენჯერ აკრიფა კონკრეტული სურსათის დასახელება




# grocery = {}

# while True:
#     try:
#         item = input("what are you going to buy? ").upper().strip()
#         if not item: 
#             continue

#         if item in grocery:
#             grocery[item] += 1
#         elif item.isalpha():
#             grocery[item] = 1 
        
#         #sorted_grocery = dict(sorted(grocery.items()))
        

#     except EOFError:
        
#         sorted_grocery = dict(sorted(grocery.items()))
#         for name, count in sorted_grocery.items():
#             print(f"{count} {name}")


#         break
    
#     # else:

    #     sorted_grocery = dict(sorted(grocery.items()))










