from django.core.paginator import Paginator



def get_filter_params(params,filterParams={},popList=[]):
    for p in params:
        par=params[p]
        if ',' in par:
            par=par.split(",")
        filterParams[p] =par
    filterParams.pop('1',1)
    filterParams.pop('limit',1)
    filterParams.pop('page',1)
    for p in popList:
        filterParams.pop(p,None)
    return filterParams


def pagination_util(limit,modelObj,params):
    paginator = Paginator(modelObj, limit)
    pageNo=params.get('page',1)
    try:
        pageObj = paginator.page(pageNo)
    except:
        pageObj=[]
    retData = {}
    retData['data'] = pageObj
    retData['total'] = paginator.count
    retData['num_of_pages'] = paginator.num_pages
    retData['page'] = pageNo
    return retData

def pagination_util_for_raw_query(limit,modelObj,params):
    paginator = Paginator(modelObj, limit)
    paginator.count = len(list(modelObj))
    pageNo=params.get('page',1)
    try:
        pageObj = paginator.page(pageNo)
    except:
        pageObj=[]
    retData = {}
    retData['data'] = pageObj
    retData['total'] = paginator.count
    retData['num_of_pages'] = paginator.num_pages
    retData['page'] = pageNo
    return retData