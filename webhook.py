#Sends Tiktok Username Data via Discord webhook
import httpx, time
def webhook(good, bad, r, amt, webhook, t, tt):
	body = {
		"username":"Tiktok Username Checker - Made by Windex <3",
		"avatar_url":"https://scontent-ort2-2.xx.fbcdn.net/v/t1.6435-9/38200127_936914206478902_8945096849434345472_n.png?_nc_cat=1&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=4U_OfaoEhQgAX-LRWM9&_nc_ht=scontent-ort2-2.xx&oh=ef628743de71d700777cdb3815cbfef0&oe=619D5203",
		"embeds": [
		{
			"author":{
			"name":"Tiktok Username Checker",
			"url":"https://windex.com"
			},
		"color":16582407,
		"fields":[
		{
		"name":":exclamation: *Results* :exclamation: ",
		"value":f"***Total Usernames Checked: {amt}***",
		"inline":False
		},
		{
		"name":"Good Usernames",
		"value":good,
		"inline":True
		},
		{
		"name":"Bad Usernames",
		"value":bad,
		"inline":True
		},
		{
		"name":"Ratelimited",
		"value":r,
		"inline":True
		}],
		"footer":{
			"text":f"Tiktok Username Checker Took {round(tt - t)} Second(s) to complete."
		}
	}]
	}
	httpx.post(webhook, json=body)
