from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

#-------------------------------------------------------------------------------------------#
#-----------------------API CITAS METHODS GET POST PUT DELETE-------------------------------#
#-------------------------------------------------------------------------------------------#

class QuotesView(View): 
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
#-----METHOD GET------#
    def get(self, request, id=0):
        if (id>0):
            quotes=list(Quotes.objects.filter(Id_quotes=id).values())
            if len(quotes) > 0:
                quote=quotes[0]
                datos = {'message': 'Sucess', 'quote':quote}
            else:
                datos = {'message': "Quotes not found..."}
            return JsonResponse(datos)
        else:
            quotes=list(Quotes.objects.values())
            if len(quotes)>0:
                datos={'message':"success", 'quotes':quotes}
            else:
                datos={'message':"quotes not found..."}
            return JsonResponse(datos)
        
#-----METHOD POST------#
    def post (self, request):
        jd=json.loads(request.body)
        # print(jd)
        Quotes.objects.create(Id_quotes=jd['Id_quotes'],
                              Tattoo_artist_id=jd['Tattoo_artist_id'],
                              User_id=jd['User_id'],
                              Date=jd['Date'],
                              Time=jd['Time'],
                              Img=jd['Img'],
                              Description=jd['Description'])
        datos={'message':"success"}
        return JsonResponse(datos)
    
#-----METHOD PUT------#
    def put(self, request, id):
        jd=json.loads(request.body)
        quotes=list(Quotes.objects.filter(Id_quotes=id).values())
        if len(quotes) > 0:
            quote=Quotes.objects.get(Id_quotes=id)
            quote.Id_quotes=jd['Id_quotes']
            quote.Tattoo_artist_id=jd['Tattoo_artist_id']
            quote.User_id=jd['User_id']
            quote.Date=jd['Date']
            quote.Time=jd['Time']
            quote.Img=jd['Img']
            quote.Description=jd['Description']
            quote.save()
            datos={'message':"success"}
        else:
            datos={'message':"quote removed successfully..."}
        return JsonResponse(datos)
    
#-----METHOD DELETE------#
    def delete(self, request, id):
        quotes=list(Quotes.objects.filter(Id_quotes=id).values())
        if len(quotes) > 0:
            Quotes.objects.filter(Id_quotes=id).delete()
            datos={'message':"success"}
        else:
            datos={'message':"quotes not found..."}
        return JsonResponse(datos)
