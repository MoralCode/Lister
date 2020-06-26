# Lister
Lister is a simple list management tool to manage subscribe and unsubscribes from your mailing list so you can focus on sending emails.


As it stands Lister is not in a usable state and many more things still need to be implemented:

- [ ] adding new subscriptions to the database and sending a confirmation email
- [ ] handling email subscription confirmations
- [ ] periodically prune the database to remove unconfirmed subscriptions
- [ ] implement an interface so that multiple email-sending services can be set up (i.e. amazon SES, mailchimp, local email server, etc)
- [ ] provide the user with a way to configure new lists and generate HTML for the subscription forms (either iFrame or regular HTML forms)
- [ ] add settings to allow the user to configure security settings (such as a list of approved domains for receiveing HTML form data from) the `From` address, message headers, etc.
- [ ] add a way for the user to send emails (adding the appropriate headers and unsubscribe links to comply with laws on email spam). might be interesting to create a forwarding addresss so the user can just send an email to that address and the content will be wrapped in the appropriate headers .etc and re-sent to all the list members while appearing "from" whichever email is configured and set up
- [ ] add a way for ths user to set up, configure, and test a domain name configuration so that custom domains can be used




## Environment variables 


## LISTER_TABLE_PREFIX
defines a prefix to prepend to the tables in the database

default value: "lister_"
