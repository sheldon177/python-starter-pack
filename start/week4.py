#დაწერეთ პროგრამა სადაც მომხმარებელი შემოიტანს ტექსტს "camelCase" 
# პრინციპით, თქვენმა პროგრამამ იგივე ტექსტი უნდა დააბრუნოს "snake_case" პრინციპით.


# camelCase =input("give me 2 words ")


# for i in camelCase:
#     a = camelCase.isupper
#     if a:
#         print("lowwer pls")
#     else:
#         print("good")
    
#  #for c in s:
#   #  print(c, end="")





# camel = input("give me a 2 word ")
# snake = ""
# for i in camel:
#     if i.isupper():
#         snake += "_" + i.lower()
#     else:
#         snake += i

# print(snake)




#წარმოიდგინეთ აპარატის რომელიც ყიდის კოკაკოლას, კოკაკოლის ბოთლი ღირს 50 ცენტი,
#აპარატს შეუძლია მიიღოს მხოლოდ 25,10,5 ცენტიანი მონეტები.

#დაწერეთ პროგრამა სადაც იმიტაცია იქნება იმ პროცესის როცა აპარატში ვათავსებთ სხვადასხვა ტიპის მონეტებს და გვსურს რომ ვიყიდოთ კოკაკოლა.
#გაითვალისწინეთ რომ თუ 50 ცენტს გასცდა პროგრამამ დასრულებისას უნდა დააბრუნოს ის ხურდის რაოდენობა რაც ზედმეტად გადახდა მოხდა

##ასევე გაითვალისწინეთ რომ თუ მომხმარებელმა მიუთითა არარსებული მონეტა თავიდან უნდა მოხდეს კითვის დასმა


#kokakola girs 50 centi
#aparats sheudzlia marto 25,10,5 centis migeba
#iqamde unda davusvat ktixva momxmarebels sanam ar gadaixdis 50 cents  
#
# def main():
#     coke = 50
#     total = 0
#     numbers = [5, 10, 25]
#     while total < coke:
#         bill = int(input("how much are you paying? "))
#         if bill not in numbers:
#             print("try again")
#             continue
#         total += bill
#         if total < coke:
#             print(f"you still left {coke - total} to pay")
#             continue
#         if total == coke:
#             print(f"thanks you already payed {total} cent$")
#             break
#         else:
#             print(f"you pay over the price take a change {total - coke}")
#             break
        

# if __name__ == "__main__":
#    main()


########################################################################################################################################################


##დაწერეთ პროგრამა სადაც მომხმარებელი შემოიყვანს ტექსტს, პროგრამამ უნდა დააბრუნოს იგივე ტექსტი ოღონდ ხმოვნების გარეშე. 
#გაითვალისწინეთ რომ მომხმარებელმა შეიძლება შემოიყვანოს როგორც დაბალი ასევე მაღალი რეგისტრის ასოები.



# word = input("what word would you like to remove xmovnebi?")
# answer = ""
# letters = ("a","e","i","o","u")
# letter = ("A","E","I","O","U")
# for i in word:
#     if i not in letters and i not in letter:
#         answer +=i
# print(answer)





# დაწერეთ პროგრამა სადაც მომხარებელი შემოიყვანს ტექსტს. თქვენმა პროგრამამ უნდა შეამოწმოს ეს ტექსტი და 
# თუ აკმაყოფილებს ყველა მოთხოვნებს მაშინ გამოპრინტეთ "Valid" სხვა შემთხვევაში "Invalid".

# მოთხოვნები რომლელსაც მომხარებლის ტექსტი უნდა აკმაყოფილებდეს:

# 1 ტექსტის სიგრძე უნდა იყოს მინიმუმ 2 მაქსიმუმ 6 სიმბოლო
# 2 ტექსტის პირველი 2 სიმბოლო აუცილებლად უნდა იყოს ასობგერა
# 3 ტექსტი არ უნდა შეიცავდეს არცერთ პუნქტუაციის ნიშანს
# 4 თუ ტექსტში არის ციფრები პირველი ციფრი არ უნდა იყოს "0"
# 5 თუ ტექსტში არის ციფრები ციფრის მერე არ უნდა იყოს ასობგერა

# მოთხოვნები რომლელსაც მომხარებლის ტექსტი უნდა აკმაყოფილებდეს:
# 1 ტექსტის სიგრძე უნდა იყოს მინიმუმ 2 მაქსიმუმ 6 სიმბოლო
# 2 ტექსტის პირველი 2 სიმბოლო აუცილებლად უნდა იყოს ასობგერა
# 3 ტექსტი არ უნდა შეიცავდეს არცერთ პუნქტუაციის ნიშანს
# 4 თუ ტექსტში არის ციფრები პირველი ციფრი არ უნდა იყოს "0"
# 5 თუ ტექსტში არის ციფრები ციფრის მერე არ უნდა იყოს ასობგერა


# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
#     return (first_quest(s) and
#             second_quests(s) and
#             third_quest(s) and
#             fourth_quest(s) and
#             fifth_quest(s))


# def first_quest(s):
#     if len(s)<2 or len(s)>6:
#         return False
#     else:
#         return True
    

# def second_quests(s):
#     return s[:2].isalpha() 

# def third_quest(s):
#     return s.isalnum()

# def fourth_quest(s):
#     for i in s:
#         if i.isdigit():
#             if i == '0':
#                 return False
#             else:
#                 return True
#     return True

# def fifth_quest(s):
#     found_digit = False
#     for i in s:
#         if i.isdigit():
#             found_digit = True
#         elif i.isalpha() and found_digit:
#             return False
#     return True

# main()




x = input("what??:")
a = x.title
print(a)

