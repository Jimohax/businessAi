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

conversation2 = "John: Hi, how are you? \nJane: I'm good, thanks for asking. How about you? \nJohn: I'm doing well, thanks. Did you get the report I sent you?"


conversation3 = """
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


def extract_customer_sentences(chat):
    pattern = re.compile(r'-- VISITOR: ([\s\S]*?)\n\n')
    matches = re.findall(pattern, chat)
    sentences = []
    for match in matches:
        sent_tokenize_list = nltk.sent_tokenize(match)
        for sentence in sent_tokenize_list:
            if sentence.strip():
                sentences.append(sentence.strip())
    return sentences


print(extract_customer_sentences(conversation1))