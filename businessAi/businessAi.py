import datefinder
import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# nltk.download('punkt')

conversation1 = """"Chat started on Thursday, February 11, 2021 4:19:40 AM

(4:19:40 AM) *** Tammy Omilgoetok has joined the chat ***
(4:19:40 AM) *** Skills identified: bot_escalation. ***
(4:19:40 AM) Tammy Omilgoetok: https://.zendesk.com/agent/tickets/3769628
Bot: Hi Tammy! I'm ·Zee·, your personal eyewear assistant. I can help you with the following:

Bot: 
[Button] Check Order Status | Follow-Up Care and Support | Choose the Right Frame

Bot: You can also visit your ·dashboard· for account/order information.

Bot: Need help with something else? Ask away. If I can't help, I'll get you over to a live agent.

-- VISITOR: How can I cancel or change my order? I have the left and right prescriptions on the wrong side for my order

Bot: Let me get you a live agent to assist with your order inquiry.

Bot: Hold tight! Someone will be right with you. It can take a few minutes.----------------------------------- 
(NOTE:  Modify order. )
(4:19:45 AM) *** Chat assigned based on skills identified. ***
(4:19:45 AM) *** Arya H -  has joined the chat ***
(4:19:49 AM) Arya H - : Hi, Tammy Omilgoetok! Thank you for reaching out to  Customer Service.
(4:19:52 AM) Arya H - : Let me check on that, one moment please!
(4:20:04 AM) Tammy Omilgoetok: thank you
(4:20:15 AM) Arya H - : May I have your order number please?
(4:21:10 AM) Tammy Omilgoetok: https://default-console.rul.ai/v1/resource/9b41b0647c26497bb305449289b78d2c/file/19b82049754d4e18b5b454871d9f0720?token=41f7efb8463e5c7b8b8205d309ea43b776dbb214b6ec66365b417c091b22df12
(4:22:54 AM) Arya - : Found order o3641495003
(4:23:06 AM) Arya H - : I have updated prescription and emailed you an order copy indicating the change. Would you please check it to see if it is correct now? Please note this change can only be found in our database and the order copy we sent. It will not be reflected in your online account.
(4:25:05 AM) Tammy Omilgoetok: Yes! Thank you ☺️
(4:26:37 AM) Arya H - : My pleasure!
(4:31:18 AM) *** Tammy Omilgoetok has left ***"""

conversation2 = "John: Hi, how are you? \nJane: I'm good, thanks for asking. How about you? \nJohn: I'm doing well, thanks. Did you get the report I sent you?"


conversation3 = [
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
]

def extract_sentences(conversation, word):
    relevant_sentences = []
    sentences = sent_tokenize(conversation)
    for sentence in sentences:
        re.findall(word, sentence)
        return sentence

        # if re.search(word, sentence):
        #     return sentence
        # else:
        #     return None

            # relevant_sentences.append(sentence)
    # return relevant_sentences


pattern = r'^[A-Z][a-z]+(\s[A-Z][a-z]+)*:'
pattern2 = r'(?:[^\n:]+:)?\s*(.*?)(?=(?:(?:\n(?:Bot|Agent):)|\Z))'
pattern3 = r'\d{1,2}:\d{2}:\d{2} AM\) Tammy Omilgoetok: .*'


def extract_client_sentences(conversation):
    pattern2 = r'(?:[^\n:]+:)?\s*(.*?)(?=(?:(?:\n(?:Bot|Agent):)|\Z))'
    speaker_pattern = re.compile(pattern2)
    client_sentences = []
    sentences = extract_sentences(conversation, pattern2)
    for sentence in sentences:
        return sentence
        # if re.match(speaker_pattern, sentence):
        # client_sentences.append(sentence)
    # return client_sentences


# print(extract_client_sentences(conversation1))
print(extract_sentences(conversation1, pattern3))

