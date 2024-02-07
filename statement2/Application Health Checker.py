import requests

def check_application_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "up"
        else:
            return "down"
    except requests.RequestException as e:
        print(f"Error connecting to {url}: {e}")
        return "down"


if __name__ == "__main__":
    url = "http://google.com"  
    status = check_application_status(url)
    print(f"Application status: {status}")


#import requests
#import csv

#def check_uptime(url):
    #try:
        #response = requests.get(url)
        #if response.status_code == 200:
            #return "UP"
        #else:
           # return "DOWN"
    #except requests.ConnectionError:
        #return "DOWN"

#def main():
    #csv_file = "B:/dload/urls.csv" 
    #with open(csv_file, 'r') as file:
      #  reader = csv.reader(file)
      #  for row in reader:
        #    url = row[0]
        #    status = check_uptime(url)
         #   print(f"URL: {url}, Status: {status}")

#if __name__ == "__main__":
   #main()
