from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question')
    answer = process_question(user_question)
    response = {"answer": answer}
    return jsonify(response)

def process_question(question):
    if "segment" in question.lower() and "source" in question.lower():
        return get_segment_info("set up a new source")
    elif "mparticle" in question.lower() and "user profile" in question.lower():
        return get_mparticle_info("create a user profile")
    elif "lytics" in question.lower() and "audience segment" in question.lower():
        return get_lytics_info("build an audience segment")
    elif "zeotap" in question.lower() and "integrate data" in question.lower():
        return get_zeotap_info("integrate data")
    else:
        return "I'm sorry, I don't have information on that topic."

def get_segment_info(task): 
    if task == "set up a new source": 
        # Specific answer based on your request 
         return ( 
        #   "Segment Documentation\n\n" 
        #  "Learn how to use Segment to collect, responsibly manage, and integrate your customer data with hundreds of tools.\n\n"
        #  "Getting started with Segment\n\n" 
        # "Learn about Segment, plan and work through a basic implementation, and explore features and extensions.\n\n"
        #  "How can Segment help you?\n\n"
        #  "1. **Simplify data collection**\n"
        #  " - Integrate the tools you need for analytics, growth, marketing, and more.\n\n" 
        # "2. **Protect data integrity**\n" 
        # " - Prevent data quality issues with a tracking schema and enforcement with Protocols.\n\n" "3. **Personalize experiences**\n" 
        # " - Build audiences and journeys from real-time customer data to personalize experiences on every channel.\n\n" 
        # "4. **Respect users' privacy**\n" " - Keep customer data private with Segment's data discovery and policy enforcement tools."
        )
        else: return f"Instructions for {task} in Segment."

def get_mparticle_info(task):
    url = "https://docs.mparticle.com/"
    response = request.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()
    return f"Instructions for {task} in mParticle: {content[:500]}"

def get_lytics_info(task):
    url = "https://docs.lytics.com/"
    response = request.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()
    return f"Instructions for {task} in Lytics: {content[:500]}"

def get_zeotap_info(task):
    url = "https://docs.zeotap.com/home/en-us/"
    response = request.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()
    return f"Instructions for {task} in Zeotap: {content[:500]}"

if __name__ == '__main__':
    app.run(debug=True)




