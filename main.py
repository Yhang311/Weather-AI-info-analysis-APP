from get_info import get_info
from AI_info import ai_info

# input city name and call API
city = input('Please input A city or a place: ')
data = get_info(city)

print(f"\nCurrent time:{data[3]} {city.upper()} Information:\nWeather condition: {data[1]}\nTemperature (Actual): {data[2]}\n")

test1 = input(f"Do you need today's {city.upper()} weather AI suggestion? (yes/no) ")
if test1 == 'yes':
    # AI suggestion
    print('AI assistant: '+ ai_info(f'Now {city} Temperature is {data[2]},and Weather condition is {data[1]},Can you give me some suggestion?'))
    
    # AI prompt words
    weather_context = (
            f"City: {city}, Weather: {data[1]}, Temperature: {data[2]}, "
            f"Local time: {data[3]}"
        )
        
    print('\nYou can ask any question about the weather in this place....\ninput "exit" to exit')

    # AI and user Q&A
    while True:
        test2 = input('User:')
        if test2 == 'exit': break
        print('AI assistant: ' + ai_info(f'this place weather is{weather_context}'+test2))
       
else:
    print("Thank you for using")

