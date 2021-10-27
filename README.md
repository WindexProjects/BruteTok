# BruteTok
Tiktok Username Checker, Uses Asyncio + Httpx Async(hronous) Client to make Faster Requests. 

Features:
 + Fast
 + Asynchronous
 + Accurate
 + Sends to Discord Webhook with Results
 + Username Generator Included, Generates 4 Letter, 5 Letter, 6 Letter, and Custom Length Usernames.
 
 
 ![image](https://user-images.githubusercontent.com/60302058/138989919-26630b2e-85d0-45e8-8b28-0283293a9ef8.png)


(**Take note to the "10000" Usernames checked & The Amount of Ratelimits which Occured**)
 
Disadvantages:
  - Only Works with python 3.10 >
  - Only Supports Windows 10 (as of now).
  - Ratelimiting commonly occurs after more than 1000 usernames
  - No Proxy Support to Avoid Possible Spam and/or Denial of Service(s)
 


***__I am not liable for any Damages Caused or Ratelimits Given by Tiktok, Same for IP Bans / Blacklists.__***

*Common Checking Times For Common Username Amounts (Going of Greatest Time using **Wifi***:
+ 10000 Usernames: About 5 Minutes
+ 1000 Usernames: About 11 Seconds
+ 100 Usernames: About 4 Seconds

***Times may Vary depending on Internet Connection Strength + Computer Hardware.***


TODO:
 + Clean Code (?)


*More Screenshots*:

![image](https://user-images.githubusercontent.com/60302058/139157943-bb2a9b03-369c-4fe3-b150-aad0abe6b646.png))
![image](https://user-images.githubusercontent.com/60302058/139158099-32a4454b-67bf-49b3-92ae-4c09fe8d1131.png)
![image](https://user-images.githubusercontent.com/60302058/139158138-47d837b6-6de7-484f-aa06-9753e7a05cf4.png)


*FAQ*:
 + Q: *"Why does it say a name is available but I can't use the username?"*
 + A: If a username was used but the user got banned, tiktok doesn't allow usage of that username, EG: If the name "hsta" was banned, I could not use "hsta".
 **This is also why when a name is available it's printed saying "Available / Banned", since it could be available or well, banned.**
 
 + Q: *"Why does it say I have multiple Ratelimits?"*
 + A: Tiktok *(and many other websites)* will implement a ratelimit, to avoid spam, Denial of Service, and so on, so that the site remains functional
 
 + Q: *"How is this more accurate?"*
 + A: Using Python 3.10 and Status Codes, the Checker provides more accurate results, rather just assuming any other status code than 200 means the username being checked is available.
 
 + Q: *"Why does it say unavailable after checking a ton of usernames?"*
 + A: The smaller the username length, the less likely you're to get available usernames, as the chances of getting a username is shortened greatly
  *Higher Length Usernames = Higher Chances of getting an available Username*
 
 
 



