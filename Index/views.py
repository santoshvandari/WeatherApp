from django.shortcuts import render
import requests,datetime

# Create your views here.
def home(request):
    city=""
    if request.method=='POST':
        city = request.POST.get("city").strip()
    if city=="":
        city="Kathmandu"
    api_url = f'https://api.api-ninjas.com/v1/weather?city={city}'
    try: 
            response = requests.get(api_url, headers={'X-Api-Key': 'U3b+x3/lun8o6+Mm0qYWQw==H7yIc2DshurjNdq7'})
            if response.status_code == requests.codes.ok:
                response=response.json()
                response['city']=city
                response['sunrise']= datetime.datetime.fromtimestamp(response['sunrise']).strftime('%H:%M:%S')
                response['sunset']=datetime.datetime.fromtimestamp(response['sunset']).strftime('%H:%M:%S')
                # print(response + {"city":city})
                return render(request,"index.html",response)
            else:
                return render(request,"index.html",{'code':response.status_code,'city':city})
    except:
            return render(request,"index.html",{"error":True,'city':city})   
