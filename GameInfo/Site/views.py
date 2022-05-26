from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
import requests
import googletrans
from googletrans import Translator
from firstapp.models import GeeksModel

# Create your views here.
def GameInfo(request):
    response = requests.get('http://127.0.0.1:8000/geeks/?format=json')
    list=()
    i=0
    while i<len(response.json()):
        id=response.json()[i]['title']
        name=response.json()[i]['description']
        list=list+(f"<option value='{id}'>{name}</option>",)
        i+=1
    data={"List":list[:]}
    return render(request, "GameInfo.html",data)
    '''response = requests.get('http://api.steampowered.com/ISteamApps/GetAppList/v2')
    list=()
    i=0
    while i<100:
        id=response.json()['applist']['apps'][i]['appid']
        name=response.json()['applist']['apps'][i]['name']
        list=list+(f"<option value='{id}'>{name}</option>",)
        i+=1
    data={"List":list[:]}
    return render(request, "GameInfo.html", context=data)'''
    
def index(request):
    if request.method == "Get":
        id = request.Get.get("Id",0)
        id=1971850
        response = requests.get(f'https://store.steampowered.com/api/appdetails/?appids={id}')
        userform = UserForm()
        name=response.json()[id]['data']['name']

        developers=""
        number=0
        while number<len(response.json()[id]["data"]["developers"]):
            developers=developers+response.json()[id]["data"]["developers"][number]+", "
            number+=1
        developers=developers[:-2]
        publishers=""
        number=0
        while number<len(response.json()[id]["data"]["developers"]):
            publishers=publishers+response.json()[id]["data"]["publishers"][number]+", "
            number+=1
        publishers=publishers[:-2]
        categories=" "
        number=0
        while number<len(response.json()[id]["data"]["categories"]):
            categories=categories+response.json()[id]["data"]["categories"][number]["description"]+", "
            number+=1
        categories=categories[:-2]
        genres=" "
        number=0
        while number<len(response.json()[id]["data"]["genres"]):
            genres=genres+response.json()[id]["data"]["genres"][number]["description"]+", "
            number+=1
        genres=genres[:-2]
        release_date=response.json()[id]["data"]["release_date"]["date"]
        
        platforms=response.json()[id]["data"]["platforms"]
        score=""
        try: score=response.json()[id]["data"]["metacritic"]["score"]
        except KeyError:score="Нет данных"

        platforms=response.json()[id]["data"]["platforms"]['windows']
        if response.json()[id]["data"]["platforms"]['windows']==" True":
            platforms=platforms+"windows "
        if response.json()[id]["data"]["platforms"]['mac']==" True":
            platforms=platforms+"mac "
        if response.json()[id]["data"]["platforms"]['linux']=="True":
            platforms=platforms+"linux "
        
        img=response.json()[id]["data"]["header_image"]
        video=response.json()[id]["data"]["movies"][0]["mp4"]["480"]
        if(len(response.json()[id]["data"]["movies"])>1):
            video1=response.json()[id]["data"]["movies"][1]["mp4"]["480"]
        else:
            video1=response.json()[id]["data"]["movies"][0]["mp4"]["480"]
        
        info=response.json()[id]["data"]["detailed_description"]
        #translator = Translator()
        #info=googletrans.LANGUAGES
        #info = (translator.translate("Info", src='en', dest='ru')).text
        data = {"id": id,"form": userform,"name":name,"developers":developers,"publishers":publishers,
        "genres":genres,"categories":categories,"score":score,"platforms":platforms,"release_date":release_date,
        "video":video,"video1":video1,"img":img,"info":info,
        }
        return render(request, "index.html", context=data)

    if request.method == "POST":
        id = request.POST.get("Id")
        response = requests.get(f'https://store.steampowered.com/api/appdetails/?appids={id}')
        userform = UserForm()
        try:name=response.json()[id]['data']['name']
        except KeyError :  
                response = requests.get('http://127.0.0.1:8000/geeks/?format=json')
                list=()
                i=0
                while i<len(response.json()):
                    id=response.json()[i]['title']
                    name=response.json()[i]['description']
                    list=list+(f"<option value='{id}'>{name}</option>",)
                    i+=1
                text="Данного Api нет выберете один из предложенных"
                data={"List":list[:],'text':text}
                return render(request, "GameInfo.html",data)
        developers=""
        number=0
        values_for_update={"description":name}
        GeeksModel.objects.update_or_create(title=id,defaults = values_for_update)
        while number<len(response.json()[id]["data"]["developers"]):
            developers=developers+response.json()[id]["data"]["developers"][number]+", "
            number+=1
        developers=developers[:-2]
        publishers=""
        number=0
        while number<len(response.json()[id]["data"]["publishers"]):
            publishers=publishers+response.json()[id]["data"]["publishers"][number]+", "
            number+=1
        publishers=publishers[:-2]
        categories=" "
        number=0
        while number<len(response.json()[id]["data"]["categories"]):
            categories=categories+response.json()[id]["data"]["categories"][number]["description"]+", "
            number+=1
        categories=categories[:-2]
        genres=" "
        number=0
        while number<len(response.json()[id]["data"]["genres"]):
            genres=genres+response.json()[id]["data"]["genres"][number]["description"]+", "
            number+=1
        genres=genres[:-2]

        try: release_date=response.json()[id]["data"]["release_date"]["date"]
        except KeyError:release_date="Нет данных"
        
        platforms=response.json()[id]["data"]["platforms"]
        
        try: score=response.json()[id]["data"]["metacritic"]["score"]
        except KeyError:score="Нет данных"

        platforms=response.json()[id]["data"]["platforms"]['windows']
        if response.json()[id]["data"]["platforms"]['windows']==" True":
            platforms=platforms+"windows "
        if response.json()[id]["data"]["platforms"]['mac']==" True":
            platforms=platforms+"mac "
        if response.json()[id]["data"]["platforms"]['linux']=="True":
            platforms=platforms+"linux "
        
        img=response.json()[id]["data"]["header_image"]
        video=response.json()[id]["data"]["movies"][0]["mp4"]["480"]
        if(len(response.json()[id]["data"]["movies"])>1):
            video1=response.json()[id]["data"]["movies"][1]["mp4"]["480"]
        else:
            video1=response.json()[id]["data"]["movies"][0]["mp4"]["480"]
        
        info=response.json()[id]["data"]["detailed_description"]
        #translator = Translator()
        #info=googletrans.LANGUAGES
        #info = (translator.translate("Info", src='en', dest='ru')).text
        data = {"id": id,"form": userform,"name":name,"developers":developers,"publishers":publishers,
        "genres":genres,"categories":categories,"score":score,"platforms":platforms,"release_date":release_date,
        "video":video,"video1":video1,"img":img,"info":info,
        }
        return render(request, "index.html", context=data)
    else:
        userform = UserForm()
        name="Нет данных"
        developers="Нет данных"
        publishers="Нет данных"
        categories="Нет данных"
        genres="Нет данных"
        release_date="Нет данных"
        
        platforms="Нет данных"
        
        score="Нет данных"

        platforms="Нет данных"
        
        img=""
        video=""
        video1=""
        
        info="Нет данных"

        data = {"form": userform,"name":name,"developers":developers,"publishers":publishers,
        "genres":genres,"categories":categories,"score":score,"platforms":platforms,"release_date":release_date,
        "video":video,"video1":video1,"img":img,"info":info,
        }
        data = {"form": userform}
        return render(request, "index.html", context=data)
        