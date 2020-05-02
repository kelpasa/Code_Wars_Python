'''
Complete the method so that it does the following:
Removes any duplicate query string parameters from the url (the first occurence should be kept)
Removes any query string parameters specified within the 2nd argument (optional array)'''

def strip_url_params(url, params_to_strip=None):
    if params_to_strip == None:
        res =  url.split('&a')
        return res[0]
    else:
        if len(params_to_strip)> 1:
            sorted(params_to_strip)
            res = url.split(f'?{params_to_strip[0]}')
            return res[0]
        else:
            res = url.split(f'&{params_to_strip[0]}')
            return res[0]
