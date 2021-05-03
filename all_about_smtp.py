import smtplib  

sender_mail = 'maryannrankapolerm@gmail.com'    
receivers_mail = 'maryannrankapolerm@gmail.com'      
message = """
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is a link to my github python repository <a href="https://github.com/mareloper/Python">link</a> you wanted.
    </p>
  </body>
</html>
""" 
try:    
   smtpObj = smtplib.SMTP("gmail.com")    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email")   