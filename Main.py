import requests  

# M - wind speed m/s 
# T - no colors
# q - quiet version
# n - only day and night
reqSheremetyevo = requests.get(url = "https://wttr.in/~Sheremetyevo?lang=ru&M&T&q&n")
reqLondon = requests.get(url = "https://wttr.in/London?lang=ru&M&T&q&n")
reqCherepovec = requests.get(url = "https://wttr.in/Cherepovec?lang=ru&M&T&q&n")
print(reqSheremetyevo.text)
print(reqLondon.text)
print(reqCherepovec.text)