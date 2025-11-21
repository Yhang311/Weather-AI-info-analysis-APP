import requests

# call API function
def get_info(city):

    url = f'https://wttr.in/{city}?format="%l:+%C+%t+%T"'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    # call the api with some info
    r = requests.get(url, headers=headers, timeout=10)

    # determine whether there is an error in api access
    if r.ok != True:
         return f'Api error!'

    # GET info in text. and delete extra space(data cleanning)
    # split data with " " to use
    info = r.text.strip()
    info_spl = info.split(' ')

    if info_spl:
        # return weather_info
        return info_spl
    else:
        # api acecess successful. But no info
        return f"CANNOT GET {city} IN INFORMATION, PLZ TRY ONE MORE TIME"
            
