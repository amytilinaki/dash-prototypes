import settings2

_cache = None

def data():

    global _cache

    if _cache is None:

        print(f"Cache is empty. Loading {settings2.data_path}")
        
        _cache=settings2.data_path
    
       
    else:
        
        print(f"Dataframe cache already loaded. Returning cached values")

    return _cache
