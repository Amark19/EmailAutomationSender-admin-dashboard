# EmailAutomationSender-admin-dashboard
<h3>Description</h3>
<p>So,I have used django admin as an dashboard.So ,all you have to do is just login with credentials that you have set,then you will be redirected to django admin page where
you can add user data.User data has username,email,city(mumbai,chennai,delhi,banglore,kolkata) attributes.And after saving this data one email along with temperature of
that particular city will be send on your entered emailid.If this email sent succesfully then only this data will be save in emailSucessfullySent Table.</p>
<hr>
<h3>How do I create this?</h3>
<br>
<p>So,to create this I have write my most of code in models.py.Whenever new user will be created then clean function will be called which is inside class Adduserdata.Then I have
created sentemail function where I have used <a href="https://docs.python.org/3/library/smtplib.html">SMTPLIB</a> library to send email to that particular emailid.
And to calculate the temperature I put get request to <a href ="https://openweathermap.org/api">openweather API</a> .
  </p>
<br>

