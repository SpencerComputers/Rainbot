# Self Hosting Tutorial
Many people will want to self host their own version of our code because they want to theme it to their own standards by applying a custom profile picture and name to the bot, or want to make changes to our code, this will teach you how to do this.

#### Step 1: Clone this repository
Clone this repository onto your computer by either using **GitHub Desktop, downloading with HTTPS or directly downloading from this page.**

<img src="/img/step1.png" alt="First Step" width="300"/>

#### Step 2: Create An Application
To make the code become a bot user and interact with the API, we need to create an application. To do this, navigate to [Discord's Developer Portal](https://discord.com/developers) and create a new application

<img src="/img/step2(01).png" alt="Second Step - Part 1"/>

Name your application whatever you want, for the purpose of this tutorial, I will name mine **Test Bot**. Once you have done this, go ahead and press **Create**

<img src="/img/step2(02).png" alt="Second Step - Part 2"/>

Once you have done this, go to the **Bot** tab, from here, press the **Add Bot** button

<img src="/img/step2(03).png" alt="Second Step - Part 3"/>

and confirm the action by pressing **Yes, do it!**.

<img src="/img/step2(04).png" alt="Second Step - Part 4"/>

You have now created a bot, you can change the name and profile picture of this bot at anytime by coming back to this page.

#### Step 3: Get token of bot
A token is the equivalent of a password, do not give this token to anybody else. We use this token so we can get the code to login to the bot, this means that anybody you share this token with can also login to your bot. To copy your token, press the copy button

<img src="/img/step3.png" alt="Third step"/>

The token of the bot is now copied to your clipboard.

#### Step 4: 
At this point in time, we have a `config.json`, however, it is not used. So instead, open up `main.py` and scroll to the very bottom, the very bottom line should be
```
client.run('TOKEN')
```
Replace `TOKEN` with your actual token, for example, I would replace TOKEN with `NzQzMzg2OTQxNTUwMTAwNTEy.XzT7Cg.Cpsg3zOR3frBRCuFj-3YBgE9gEE` (not a real token).

Once this is complete, you can now run main.py and your bot will appear online.

#### Step 5:
Now we need to get the bot into your server, as we cannot use it yet. To do this, go back over to the **Discord Developer Portal** and click on your application (if not already opened), then, click the **OAuth2** category.

<img src="/img/step5(1).png" alt="Fifth Step - Part 1"/>

Now tick the bot box under the Scopes category, and scroll down.

<img src="/img/step5(2).png" alt="Fifth Step - Part 2"/>

Tick the Administrator box and then copy the link that appears above and paste it into a new tab.

<img src="/img/step5(3).png" alt="Fifth Step - Part 3"/>

Now you can invite your bot to the server like you would any other bot.
