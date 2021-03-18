string1 = ("You are about to preform")
string2 = ("request on")
string3 = ("- Would you like to procede? (y | n)")

# Main
userIn1 = input("Input target URL: ")
target = requests.get(userIn1)
userIn2 = input("GET | POST | PUT | DELETE | HEAD | PATCH | OPTIONS\nEnter desired function from the above list: ")
print(string1, userIn2, string2, userIn1, string3)
check = input("")

if check == "y":
   if userIn2 == "GET":
       print(requests.get(target))
   elif userIn2 == "POST":
       print(request.post(target))
   elif userIn2 == "PUT":
       print(requests.put(target))
   elif userIn2 == "DELETE":
       print(request.delete(target))
   elif userIn2 == "HEAD":
       print(request.head(target))
   elif userIn2 == "PATCH":
       print(request.patch(target))
   elif userIn2 == "OPTIONS":
       print(request.options(target))
   else:
       print("Invalid")
else:
    print("Please come again!")
