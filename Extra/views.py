from utils.utils import even_split, add_tax, add_discount

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from json import loads, dumps

'''
Guidelines: https://gist.github.com/Muzammil-Bilwani/5f2c7adadf01a4134a17b7d7240de754

Note: Some operations are performed on evenly distributed amount as it say in guideline!
'''

{"noOfPeople": 4, "total": 320}
# Split Evenly
@csrf_exempt
def split_evenly(request):
    try:
        if request.method == "POST":
            data = loads(request.body)
            no_of_people = data.get("noOfPeople", 0)
            if (not no_of_people):
                return JsonResponse({"ERROR": "noOfPeople should be number with base 10 and greater than 0!"})
            
            total = data.get("total", 0)
            if not total:
                return JsonResponse({"ERROR": "Total should be a number with base 10 and greater than 0!"})

            # Enforcly Typecasting noOfPeople to int, truncate decimal values and real division
            evenly_splited = even_split(total, int(no_of_people))

            return JsonResponse({"evenly_splited": evenly_splited})
        
    except:
        return JsonResponse({500: "Server may has several issues."})


# People may be any id or name, simply iterable
{"peoples": [{"name": "Saad", "money": 1000},{"name": "Mohib", "money": 2000},{"name": "Saif", "money": 3000}], "total": 6000}
# Split Evenly
'''
If total is less than total of all peoples money then result may be weird?
'''
@csrf_exempt
def split_unevenly(request):
    try:
        if request.method == "POST":
            data = loads(request.body)
            print(data)
            peoples = data.get("peoples", 0)
            if (not peoples):
                return JsonResponse({"ERROR": 'people should be a List/Array, like: [{"peoples": [{"name": "Saad", "money": 1000}]}'})
            
            total = data.get("total", 0)
            if not total:
                return JsonResponse({"ERROR": "Total should be a number with base 10 and greater than 0!"})

            # Typecasting noOfPeople to int, truncate decimal values and real division
            evenly_splited = even_split(total, len(peoples))
            unevenly_splited = dict()

            for person in peoples:
                print(person)
                unevenly_splited[person["name"]] = evenly_splited - person["money"]

            return JsonResponse({"unevenly_splited": unevenly_splited})

    except Exception as e:
        print(e)
        return JsonResponse({500: "Server may has several issues.", "error": str(e)})



{"noOfPeople": 4, "total": 400, "tax_rate": 18, "tip": 80}
# Tip and Tax
'''
If total is less than total of all peoples money then result may be weird?
'''
@csrf_exempt
def add_tip_tax_and_evenly_split(request):
    try:
        if request.method == "POST":
            data = loads(request.body)

            no_of_people = data.get("noOfPeople", 0)
            if (not no_of_people):
                return JsonResponse({"ERROR": "noOfPeople should be number with base 10 and greater than 0!"})
            
            total = data.get("total", 0)
            if not total:
                return JsonResponse({"ERROR": "Total should be a number with base 10 and greater than 0!"})

            # Extracting tax rate and tip, if not then 0 will considered
            tax_rate = data.get("tax_rate", 0)
            tip = data.get("tip", 0)

            # Adding tax and tip, when 0 then total will not effected
            total = add_tax(total, tax_rate) + tip

            # Enforcly Typecasting noOfPeople to int, truncate decimal values and real division
            evenly_splited = even_split(total, int(no_of_people))

            return JsonResponse({"evenly_splited": evenly_splited})

    except:
        return JsonResponse({500: "Server may has several issues."})




{"noOfPeople": 4, "total": 400, "discount_rate": 50}
# Tip and Tax
'''
If total is less than total of all peoples money then result may be weird?
'''
@csrf_exempt
def add_discount_and_evenly_split(request):
    try:
        if request.method == "POST":
            data = loads(request.body)
            
            no_of_people = data.get("noOfPeople", 0)
            if (not no_of_people):
                return JsonResponse({"ERROR": "noOfPeople should be number with base 10 and greater than 0!"})
            
            total = data.get("total", 0)
            if not total:
                return JsonResponse({"ERROR": "Total should be a number with base 10 and greater than 0!"})

            # Extracting tax rate and tip, if not then 0 will considered
            discount_rate = data.get("discount_rate", 0)

            # Adding tax and tip, when 0 then total will not effected
            total = add_discount(total, discount_rate)

            # Enforcly Typecasting noOfPeople to int, truncate decimal values and real division
            evenly_splited = even_split(total, int(no_of_people))

            return JsonResponse({"evenly_splited": evenly_splited})

    except:
        return JsonResponse({500: "Server may has several issues."})



# People may be any id or name, simply iterable
{"peoples": [{"name": "Saad", "money": 1000},{"name": "Mohib", "money": 2000},{"name": "Saif", "money": 3000},], "total": 6000}
# Split Evenly
'''
If total is less than total of all peoples money then result may be weird?


Now we have list of list of dict where list of dict is same as simple uneven split, just we break it into shared items and make then separate so they treate as seperate
{shared_items: {
"item1": {"peoples": [{"name": "Saad", "money": 1000},{"name": "Mohib", "money": 2000}], "total":3000},
"item2": {"peoples": [{"name": "Saad", "money": 1000},{"name": "Mohib", "money": 2000}], "total":3000},
"item3": {"peoples": [{"name": "Saad", "money": 1000},{"name": "Mohib", "money": 2000}], "total":3000},
}
Items name in dict allows for dublication
{shared_items: {
{"item": "Biryani", "peoples": [{"name": "Saad", "money": 1000},{"name": "Mohib", "money": 2000}], "total":3000},
{"item": "Biryani", "peoples": [{"name": "Saad", "money": 1000},{"name": "Mohib", "money": 2000}], "total":3000},
{"item": "Biryani", "peoples": [{"name": "Saad", "money": 1000},{"name": "Mohib", "money": 2000}], "total":3000},
}

'''
@csrf_exempt
def shared_items_and_unevenly_split(request):
    try:
        if request.method == "POST":
            data = loads(request.body)
            # print(data)
            shared_items = data.get("shared_items", 0)
            if (not shared_items):
                return JsonResponse({"ERROR": 'people should be a List/Array, like: [{"peoples": [{"name": "Saad", "money": 1000}]}'})
            
            response = {"shared_items": list(), "wrong_items": list()}

            for shared_item in shared_items:
                item_is_wrong = False

                print(shared_item.keys())
                total = shared_item.get("total", 0)
                print(total)
                if not total:
                    total = "Total is not exists!"
                    item_is_wrong = True
                
                peoples = shared_item.get("peoples", 0)
                if not peoples:
                    peoples = "Peoples are not exists!"
                    item_is_wrong = True


                # Checking that both requirement are fulfilled?
                if item_is_wrong:
                    # Adding wrong shared items and also their errors
                    response["wrong_items"].append({"item": shared_item, "errors": (total, peoples)})
                    continue
                
                item = shared_item.get("item", None)
                if not item:
                    item = "N/A"

                evenly_splited = even_split(total, len(peoples))
                
                item_result = {item: list(), "total": total}

                for person in peoples:
                    money = evenly_splited - person["money"]
                    item_result[item].append({"name": person["name"], "money": money})

                response["shared_items"].append(item_result)

            return JsonResponse(response)

    except:
        return JsonResponse({500: "Server may has several issues."})




{
  "shared_items": [
    {
      "results": [
        {
          "name": "Saad",
          "money": 500.0
        },
        {
          "name": "Mohib",
          "money": -500.0
        }
      ],
      "total": 3000
    },
    {
      "results": [
        {
          "name": "Saad",
          "money": 500.0
        },
        {
          "name": "Mohib",
          "money": -500.0
        }
      ],
      "total": 3000
    }
  ],
  "wrong_items": [
    {
      "item": {
        "peoples": [
          {
            "name": "Saad",
            "money": 1000
          },
          {
            "name": "Mohib",
            "money": 2000
          }
        ]
      },
      "errors": [
        "Total is not exists!",
        [
          {
            "name": "Saad",
            "money": 1000
          },
          {
            "name": "Mohib",
            "money": 2000
          }
        ]
      ]
    }
  ]
}