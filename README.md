# 100-Days-Python
Angela Yu's 100 day python course. These are files that contain my personal assignment challenges and work assigned by her.

Day28: 5th February 2026. I've finally gotten curious and realsied what the .readme file is actually for: providing information about my project, how to install it and how you can contribute to my project.
I wouldn't say it's a single project. I mean It's many projects... For now atleast. Eventually Ill start building professional python projects that will require their own github repo's but untill then,
I'm having fun scratching my head trying to understand Angela's scope logic. She's glazing over concepts like its familiar like the back of her hand. Anyways I'm yappng too hard but this is for the sake of my mental sanity. 
I don't know where exactly I'm headed but Im having fun getting there. 

Day47: I need to commit to docummenting my journey better. My python Journey will only be clarified by my commits, contributions and this readme file that documents my thoughts and what I've learned since the certificate of completion that I'll
obtian will be in Carl's name which is allright. Hopefully it can help him out. Today we just made a pretty simple project. I'll just descibe it real quick. Its an Amazon price tracker. Basically takes the URL page of a product that I want to buy,
it scrapes the page for the product price and name(BS4). If the price threshold is not exceeded it sends me an alert Email(SMTPlib). I learned to use the MIME email format in order to send emails that accept ascii characters because mime multipart and
MIMEText allow me to formatt the email properly and use the send_message() method from the SMTP connection which accepts the MIME message object. It was successful(SOmehow the Amazon live site didn't send me a re-capacha which is great.) This application is
not really practicle because theres no file to store URLs for products I wanna buy, and similarly I haven't automated the process with github actions for it to be continuous. Otherwise I'm proud of it.