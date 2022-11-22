from django.http import JsonResponse,  HttpResponse


def Convertion_ratio(request, *args, **kwargs):
    return JsonResponse({
	'months':['jan','feb','mar','apr','may','june'],
	'values':[1.2,1.4,1.56,3.2,4.5,6.7],
})
    
    
def Harvest_Trend(request, *args, **kwargs):
    return JsonResponse({
	'months':['jan','feb','mar','apr','may','june'],
	'values':[1.2,1.4,1.56,3.2,4.5,6.7],
})
    

def Cycle_Graphs(request, *args, **kwargs):
    return JsonResponse({
	'months':['jan','feb','mar','apr','may','june'],
	'values':[1.2,1.4,1.56,3.2,4.5,6.7],
})        