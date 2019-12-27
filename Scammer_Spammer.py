#Import Libraries
import names, requests, random, string, os, urllib3

#Add proxies here. Need both HTTP and HTTPS.
proxies = {
    'http': 'http://49.51.68.122:1080',
    'https': 'http://49.51.68.122:1080',
}

#Create the session and set the proxies.
s = requests.Session()
#Uncomment below if you need to use proxies.
#s.proxies = proxies

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

#Replace with Scammer URL (Usually ends in .PHP but doesn't have to)
url = 'REPLACE WITH URL'

print('Started')

while True:
    #Generate random first/last name
    first = names.get_first_name().lower()
    last = names.get_last_name().lower()

    #Generate 3 random numbers
    rando = ''.join(random.choice(string.digits))
    rando2 = ''.join(random.choice(string.digits))
    rando3 = ''.join(random.choice(string.digits))

    #Chooses email format
    emailformat = random.choice([1,2,3,4,5,6,7,8,9,10,11])
    if emailformat == 1:        
        name = first + last + rando + rando2 + rando3
    if emailformat == 2:
        name = first + '_' + last + rando + rando2 + rando3
    if emailformat == 3:
        name = first + '-' + last + rando + rando2
    if emailformat == 4:
        name = last + first + rando + rando2 + rando3
    if emailformat == 5:
        name = first + rando + rando2 + last
    if emailformat == 6:
        name = last + rando + rando2 + rando3 + first
    if emailformat == 7:
        name = last + '-' + first + '-' + rando + rando2 + rando3 
    if emailformat == 8:
        name = first + last
    if emailformat == 9:
        name = last + first
    if emailformat == 10:
        name = first + rando + rando2 + rando3
    if emailformat == 11:
        name = first + '_' + last


    #Chooses email provider
    pickprov = random.choice([1,1,2,3,4,5,6,7,8,9])
    if pickprov == 1:
        username = name.lower() + '@yahoo.com'
    if pickprov == 2:
        username = name.lower() + '@gmail.com'
    if pickprov == 3:
        username = name.lower() + '@gmx.com'
    if pickprov == 4:
        username = name.lower() + '@icloud.com'
    if pickprov == 5:
        username = name.lower() + '@mail.com'
    if pickprov == 6:
        username = name.lower() + '@gmx.us'
    if pickprov == 7:
        username = name.lower() + '@outlook.com'
    if pickprov == 8:
        username = name.lower() + '@aol.com'
    if pickprov == 9:
        username = name.lower() + '@comcast.net'

    #Chooses randomly generated password between 8-16 characters long
    password = ''.join(random.choice(chars) for i in range(random.choice([8,8,8,9,10,11,12,13,14,15,16,17,18,19,20])))


    #Disables HTTPS warning
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    #Make post request
    #Replace parameters as needed.
    s.post(url, allow_redirects=False, verify=False, data={
		'login_email': username,
		'login_password': password,
	})

    #prints output
    print()
    print("Sending username: " + username + " and Password: " + password )
    print("To: " + url)