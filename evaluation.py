from openai.src.generatemessage import generate_dialogue
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def evaluate_string(message):
    vader = SentimentIntensityAnalyzer()
    results = [vader.polarity_scores(message)]
    return results

    
#Purpose of the function is to generate and evaluate the possible response options given a message
def evaluate_dialogue(message):
    
    #OpenAI generation of the messages
    dialogue_options = generate_dialogue(raw_text=message)
    
    #Initialize the sentiment algorithm and then use the algorithm on each of the dialogue options
    vader = SentimentIntensityAnalyzer()
    results = [vader.polarity_scores(dialogue_option) for dialogue_option in dialogue_options]

    #Logistics stuff, just matches the evaluation score determined with 
    #the sentiment algorithm to the correct message in one dictionary
    possible_messages = {}
    index = 0
    for i in results:
        possible_messages.update({dialogue_options[index] : i['compound']}) 
        index = index + 1
    sorted_messages = sorted(possible_messages.items(), key=lambda x: x[1])
    return sorted_messages

def decide_dialogue(target_score, messages):
    closest_match_message = ""
    closest_match_score =  10 #junk value, doesn't matter at all
    for message, message_score in messages:
        score_difference = abs(target_score - message_score)
        if(score_difference < closest_match_score):
            closest_match_score = score_difference
            closest_match_message = message
    return closest_match_message


#running this file by itself will generate a sample of the evaulation message dictionary 
#when given the message of 'Hey how was your day?'
#IMPORTANT: Please escape your double quotes! Otherwise the OpenAI will generate passages that are narrated
#rather than conversational.
if __name__ == '__main__':
    messages = evaluate_dialogue('"Hey how was your day?"')
    print(messages)
    print(decide_dialogue(.2, messages))