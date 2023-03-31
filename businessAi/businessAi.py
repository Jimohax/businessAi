import datefinder
import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# nltk.download('punkt')

conversation1 = """
Chat started on Tuesday, December 15, 2020 7:52:31 PM

(7:52:31 PM) *** Ellen Shandalove has joined the chat ***
(7:52:31 PM) *** Skills identified: bot_escalation. ***
(7:52:31 PM) Ellen Shandalove: https://.zendesk.com/agent/tickets/3287999

Bot: Hi Ellen! I'm ·Zee·, your personal eyewear assistant. I can help you with the following:

Bot: 
[Button] Check Order Status | Follow-Up Care and Support | Choose the Right Frame

Bot: You can also visit your ·dashboard· for account/order information.

Bot: Need help with something else? Ask away. If I can't help, I'll get you over to a live agent.

-- VISITOR: Check Order Status

Bot: Great, I'll look up your order status.

Bot: · · · · · · · · · · · ·Ordered December 3·Ready and En-route to Shipping Center·Order On the Way·Expected Delivery December 17-24·

Bot: Can I help you with anything else today?
[Button] No | Yes

-- VISITOR: Yes

Bot: Ok. I can help with the following:

Bot: 
[Button] Check Order Status | Follow-Up Care and Support | Choose the Right Frame

-- VISITOR: When will my order be shipped?

Bot: Delivery timelines are expected to be impacted by increased demand during the holiday season. We are currently experiencing some delays with our estimated shipping timeframes. Refer to your selected shipping option for a guideline or My Account Dashboard for order status. If you selected the Standard shipping, then you can expect the turnaround at 14 – 21 days from the date of order. We continue to strive to deliver your glasses within or earlier than the estimated windows even when something unexpected occurs!

-- VISITOR: Do you have any more specific information about when I will receive this order?

Bot: I'm still learning. Try your question a different way?

-- VISITOR: When will I recieve this order?

Bot: I'm sorry I'm having trouble with this. Would you like me to connect you with an agent?
[Button] Yes, continue to live agent

-- VISITOR: Yes, continue to live agent

Bot: Hold tight! Someone will be right with you. It can take a few minutes.

----------------------------------- 
(NOTE:  Zee confused by "When will I recieve this order?")

------------------------------------ Transcript with Agent

Robin A - : Hi Ellen! You've reached  customer service my name is Robin. Let me verify the status of your order.

-- Visitor: Okay

Robin A - : Upon checking the order, it shows that your package was already shipped out from the lab since last week, please allow more time for your package to arrive in our warehouse and you will receive an email with the tracking number.

Robin A - : Your order is on track and since you placed your order Dec 2, you can start expecting the package to arrive from Dec 16 to 23, although sometimes the package can be delivered earlier than that.

-- Visitor: Great amd thanks for checking the status of ,my order

-- Visitor: Is the order being shipped in the US mail or UPS or Fedex?

Robin A - : You are welcome. 
Will there be anything else aside from this?

Robin A - : It will be shipped through USPS

-- Visitor: Thanks

-- Visitor: Goodbye

Robin A - : Thank you for giving us the opportunity to help and assist you. Thank you for choosing ! Stay safe and have a good one!

Robin A - : Happy Holidays!

------------------------------------
(7:52:31 PM) Ellen Shandalove: Happy holidays to you also.
(7:53:54 PM) *** Chat assigned based on skills identified. ***
(7:53:54 PM) *** Leah Z -  has joined the chat ***
(7:53:58 PM) Leah Z - : Hi, Ellen Shandalove! Thank you for reaching out to  Customer Service.
(7:54:04 PM) Leah Z - : May I know if there is anything else that I can help? :)
(7:55:51 PM) *** Ellen Shandalove has left ***
"""



conversation2 = """ 
Chat started on Monday, December 21, 2020 8:19:22 PM

(8:19:22 PM) *** Fernando Gonzalez has joined the chat ***
(8:19:22 PM) *** Skills identified: bot_escalation. ***
(8:19:22 PM) Fernando Gonzalez: https://.zendesk.com/agent/tickets/3340059

Bot: Hi Fernando! I'm ·Zee·, your personal eyewear assistant. I can help you with the following:

Bot: 
[Button] Check Order Status | Follow-Up Care and Support | Choose the Right Frame

Bot: You can also visit your ·dashboard· for account/order information.

Bot: Need help with something else? Ask away. If I can't help, I'll get you over to a live agent.

-- VISITOR: Live agent

Bot: Absolutely. One of my colleagues would be happy to help you.

Bot: Hold tight! Someone will be right with you. It can take a few minutes.

----------------------------------- 
(NOTE:  User asked for a human.)
(8:19:47 PM) *** Chat assigned based on skills identified. ***
(8:19:47 PM) *** Julie B -  has joined the chat ***
(8:19:52 PM) Julie B - : Hi, Fernando Gonzalez! Thank you for reaching out to  Customer Service.
(8:19:55 PM) Julie B - : How can I assist you today?
(8:20:51 PM) Fernando Gonzalez: Hi, on Friday Tatiana in customer service, told me to contact there again today if my order still was not delivered
(8:20:55 PM) Fernando Gonzalez: o3452965093
(8:21:11 PM) Julie B - : I understand the issue and I will do my best to assist you.
(8:21:14 PM) Julie B - : Let me check on that.  One moment.
(8:23:18 PM) Fernando Gonzalez: Ok
(8:26:15 PM) Julie B - : I am sorry for the inconvenienced that we have caused you. The tracking information is not yet updated due to some process delays with our US courier. Your glasses are already in transit to your address .Please allow us few more days to complete the delivery. For this, we will refund the amount that you paid for the shipping to your original mode of payment.
(8:26:41 PM) Fernando Gonzalez: OK, thanks
(8:26:51 PM) Julie B - : Is there something else I can do for you today?
(8:27:21 PM) Fernando Gonzalez: No thank you
(8:27:30 PM) Julie B - : Please feel free to contact us again if you need further assistance.  Thank you for contacting  and have a great day!
(8:27:33 PM) *** Julie B -  has left ***
(8:27:37 PM) *** Fernando Gonzalez has left ***
"""



conversation3 = """ 
Chat started on Thursday, February 11, 2021 8:28:38 AM

(8:28:38 AM) *** Nathan Gomez has joined the chat ***
(8:28:38 AM) *** Skills identified: bot_escalation. ***
(8:28:38 AM) Nathan Gomez: https://.zendesk.com/agent/tickets/3770032
Bot: Hi Nathan! I'm ·Zee·, your personal eyewear assistant. I can help you with the following:

Bot: 
[Button] Check Order Status | Follow-Up Care and Support | Choose the Right Frame

Bot: You can also visit your ·dashboard· for account/order information.

Bot: Need help with something else? Ask away. If I can't help, I'll get you over to a live agent.

-- VISITOR: Check Order Status

Bot: Great, I'll look up your order status.

Bot: · · · · · · · · · · · ·Ordered February 3·Ready and En-route to Shipping Center·Order On the Way·Delivered February 10·

Bot: 
[Button] Show tracking number

-- VISITOR: Check Order Status

Bot: 
[Button] Show tracking number

-- VISITOR: Never got package

Bot: Can you confirm which of these you mean?
[Button] I never got the package | I never received my package | none of those

-- VISITOR: I never received my package

Bot: Got it.

Bot: Sorry to hear that. Let's start by looking up your order.
[Button] 

Bot: If the website indicates your order has been delivered but you have not received it, please try the following:
[Button] 

Bot: ·Check with other household members and neighbors.·Check with your local post office or carrier.·
[Button] 

Bot: If after asking around, you can't find your package, please come back and ask to speak to an agent.
[Button] 

Bot: Let's go to order status now.

Bot: 
[Button] Show tracking number

-- VISITOR: Speak to an agent

Bot: Absolutely. One of my colleagues would be happy to help you.
[Button] 

Bot: Hold tight! Someone will be right with you. It can take a few minutes.----------------------------------- 
(NOTE:  User asked for a human. )
(8:29:13 AM) *** Chat assigned based on skills identified. ***
(8:29:13 AM) *** John D -  has joined the chat ***
(8:29:22 AM) John D - : Hi, Nathan Gomez! Thank you for reaching out to  Customer Service.
(8:29:27 AM) John D - : I'm sorry to know you haven't received your glasses, I’ll be happy to check that for you.
(8:29:48 AM) Nathan Gomez: Thank you
(8:31:30 AM) Nathan Gomez: Hello?
(8:31:50 AM) John D - : I found the order o3623809105.
(8:31:56 AM) John D - : Please bear with me.
(8:32:08 AM) Nathan Gomez: Ok.
(8:34:51 AM) Nathan Gomez: Connection keeps getting lost.
(8:35:12 AM) Nathan Gomez: My order was stated as delivered but I never got my package.
(8:35:17 AM) John D - : Thank you for waiting.
(8:35:34 AM) John D - : Yes, upon checking it was delivered Jan. 10.
(8:35:40 AM) John D - : May I know your shipping address?
(8:35:58 AM) Nathan Gomez: 3012 N Ventura Rd
(8:36:38 AM) John D - : Yes, that's correct.
(8:37:03 AM) John D - : I'm going to request now to our team to start the investigation for your glasses.
(8:37:18 AM) John D - : We will update you via email within 24-48 hrs.
(8:37:21 AM) Nathan Gomez: Yes, although I never got my package with my 2 glasses that were ordered.
(8:37:56 AM) John D - : We do apologize for the inconvenience.
(8:38:19 AM) Nathan Gomez: How will this be resolved?
(8:38:31 AM) Nathan Gomez: Will I get a refund for the poor handling of my order?
(8:40:00 AM) John D - : We coordinate 1st to USPS once the glasses is lost, we will remake the glasses without cost and send to you as soon as possible.
(8:41:14 AM) Nathan Gomez: I’d rather take my chances with eyebuydirect.com
(8:41:45 AM) Nathan Gomez: Rather than having it remade, I’d want to spend my refunded money with them.
(8:44:03 AM) John D - : I understand. We can request that after the investigation.
(8:45:17 AM) John D - : Is there something else I can do for you today?
(8:48:27 AM) John D - : Hello, We have not heard from you in the last few minutes, in order to assist other customers, I am going to close this chat.  Please don't hesitate to contact us again, if you have any further questions.  Thank you for contacting  , Have a great day!
(8:48:28 AM) *** John D -  has left ***
(8:49:09 AM) *** Nathan Gomez has left ***
"""

conversation4 = "John: Hi, how are you? \nJane: I'm good, thanks for asking. How about you? \nJohn: I'm doing well, thanks. Did you get the report I sent you?"


conversation5 = """
    "Alice: Hello, how are you?",
    "Bob: I'm good, thanks for asking.",
    "Alice: That's great to hear.",
    "Charlie: Hey guys, what's up?",
    "Alice: Not much, we're just chatting.",
    "Bob: Yeah, just catching up.",
    "Charlie: Cool, mind if I join in?",
    "Alice: Of course not, the more the merrier!",
    "Charlie: Thanks, you guys are the best.",
    "Bob: So, how's your new job going, Alice?",
    "Alice: It's going well, thanks for asking.",
    "Bob: That's great to hear.",
    "Charlie: Yeah, congrats on the new job!",
    "Alice: Thanks, I'm really enjoying it so far.",
"""




# def get_sentences(text):
#     # Tokenize the text into sentences using the NLTK library
#     sentences = sent_tokenize(text)
    
#     return sentences


# print(get_sentences(conversation1))



def sentence_finder(text,word):
    ## You will use this in client_only functions 
    sentences = sent_tokenize(text)
    conversation = []

    ## Hint : find sentences containing a pattern
    for sentence in sentences:
        if ':' in sentence:
            conversation.append(sentence)
    return conversation
    
    # return None

def client_only(text): 
    
    ##write script to return client data only
    ## use pattern matching with regex
    #pattern = (customer) 
    ## sentence_finder can help to get the conversations
    # word = word_tokenize(text)
    word_list =  [] ## Example of A pattern string 'joining'
    client_only_conv = ''
    return client_only_conv


def sentence_finder(text, word):
   
    sentences = sent_tokenize(text)
    # word_pattern = re.compile(r'\b{}\b'.format(word), flags=re.IGNORECASE)
    return matched_sentences

def client_only(text): 
   
    word_list =  ['visitor', 'customer', 'client'] # Example of pattern strings
    pattern = '|'.join(word_list)
    client_sentences = sentence_finder(text, word)
    client_only_conv = ' '.join(client_sentences)
    return client_only_conv


# print(client_only(conversation1))
sentence_finder(conversation2, "Nathan Gomez")
# word_list = [visitor, Jana, ]


#  word = pattern( first occurence of'joined' ":")  (jana)
# word_list.append(word) =

