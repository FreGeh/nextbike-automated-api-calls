# Idea
Creating a terminal based program, that enables you to book bicycles via the API. This would enable you to easier reserve bicycles for the time you need them instead of always actively looking on your phone and manually refreshing to see if any bicycles popped up.

# Attempt 1: Using public ressources
Since someone already reverse engineered the API years ago (https://github.com/cybre-finn/nextbike-api-reverse-engineering), I tried using the gained knowledge and requesting the API key from https://webview.nextbike.net/getAPIKey.json, which resulted me in an API key that actually worked for the API calls I was trying back then. So I got working on this python app and automated the proccess of requesting the current public API and logging in to get the loginkey. But then I found out most API calls are not permitted with this public API key, and that I would have to find that key somehow.

# Attempt 2: Reverse Engineering the App and looking through the code
The only thing to be found were the different API calls, which were already known from https://api.nextbike.net/api/documentation. And the default API keys mentioned, don't have the permission to do most API calls.

# Attempt 3: Catching the HTTPS traffic and understanding how to get the right API key
Using Genymotion to simulate the phone with the app and different toolkits, like mitmproxy or BurpSuite together with Frida to bypass SSL pinning. But even then only the API calls I could catch were the ones I was already able to do with the public API key. The Nextbike API doesn't trust the certificate used for mitmproxy or BurpSuite so it wouldn't send any traffic. Which lead to the app not working properly either.

# To Do:
Maybe its possible to modify the application in a way it accepts the Certificate so you can read the traffic properly or there is more to find in reverse engineering the app.
Since I'm a total beginner on this matter, this is all I can do, but I would be interested in more possibilities. Let me know if you have any ideas.