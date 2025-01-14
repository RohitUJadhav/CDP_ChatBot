from flask import Flask, request, jsonify, send_from_directory
import requests
from bs4 import BeautifulSoup 
from flask_cors import CORS  # Import CORS
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS

app = Flask(__name__, static_url_path='')
CORS(app)  # Enable CORS for all routes

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
    elif "zeotap" in question.lower() and " integrate my data" in question.lower():
        return get_zeotap_info("integrate my data")
    else:
        return "I'm sorry, I don't have information on that topic."

def get_segment_info(task):
    if task == "set up a new source":
        return (
            "1. Log in to Segment\n" 
            "   - Visit Segment's dashboard.\n"
            "   - Log in with your credentials.\n\n"
            "2. Navigate to Your Workspace\n"
            "   - Once logged in, select the workspace where you want to add the new source.\n\n"
            "3. Add a New Source\n"
            "   - In the workspace, go to the **Sources** tab.\n"
            "   - Click on **Add Source**.\n\n"
            "4. Choose the Source Type\n"
            "   - Segment offers various source types, including:\n"
            "     - Web: Websites (e.g., using Analytics.js for JavaScript).\n"
            "     - Mobile: iOS or Android apps.\n"
            "     - Server-side: Node.js, Python, Ruby, etc.\n"
            "     - Cloud Sources: Salesforce, Google Analytics, etc.\n"
            "   - Select the appropriate source type for your use case.\n\n"
            "5. Configure the Source\n"
            "   - Name Your Source: Enter a descriptive name for easy identification.\n"
            "   - Set the Data Source Type: For instance, if it's a website, you might choose JavaScript as the method.\n"
            "   - Connect to a Destination: Choose where the data will be sent (e.g., a data warehouse, analytics platform, or CRM).\n\n"
            "6. Get Your Write Key\n"
            "   - After setting up the source, Segment will provide a Write Key. This key is used to send data from the source to Segment.\n"
            "   - Copy this key; you’ll need it for integration.\n\n"
            "7. Integrate the Source\n"
            "   - Depending on the source type, follow the integration instructions:\n"
            "     - For Web: Add the Segment snippet to your website's `<head>` section.\n"
            "     - For Mobile: Install the appropriate Segment SDK in your app.\n"
            "     - For Server-side: Use the Segment library for your chosen programming language.\n\n"
            "8. Test the Integration\n"
            "   - After setting up, test the source by sending some events.\n"
            "   - Use the Segment debugger to ensure data is correctly captured and sent to destinations.\n\n"
            "9. Monitor and Optimize\n"
            "   - Regularly check the source’s performance.\n"
            "   - Make adjustments to your tracking plan if necessary.\n\n"
        )
    else:
        return f"Instructions for {task} in Segment."

def get_mparticle_info(task):
    url = "https://docs.mparticle.com/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text()
        return f"Instructions for {task} in mParticle: {content[:500]}"
    else:
        return f"Failed to fetch data from mParticle. Status code: {response.status_code}"

def get_mparticle_info(task):
    if task == "create a user profile":
        return (
            "1. Log in to mParticle\n"
            "   - Visit the mParticle dashboard.\n"
            "   - Log in with your credentials.\n\n"
            "2. Navigate to the Audience Section\n"
            "   - Go to the **Audience** section in the dashboard.\n"
            "   - This is where user profiles and segments can be managed.\n\n"
            "3. Define Identity Information\n"
            "   - Ensure your platform is configured to send identity information.\n"
            "   - Common identifiers include email, customer ID, or device ID.\n\n"
            "4. Integrate the mParticle SDK\n"
            "   - Install and configure the appropriate mParticle SDK for your platform:\n"
            "     - Web: Use JavaScript SDK.\n"
            "     - Mobile: Use iOS or Android SDK.\n"
            "     - Server: Use the relevant server-side SDK (Node.js, Python, etc.).\n"
            "   - Include user identifiers in the tracking payloads.\n\n"
            "5. Send User Data\n"
            "   - Send user information via `mParticle.Identity().modify()` or other identity methods.\n"
            "   - Example for JavaScript:\n"
            "     ```javascript\n"
            "     mParticle.Identity.modify({\n"
            "         userIdentities: {\n"
            "             email: 'user@example.com',\n"
            "             customerId: '12345'\n"
            "         }\n"
            "     });\n"
            "     ```\n\n"
            "6. Create a User Profile in the Audience Builder\n"
            "   - Use the Audience Builder to create segments based on user attributes and behaviors.\n"
            "   - Define filters (e.g., users with a specific email domain or those who completed an event).\n\n"
            "7. Test and Monitor\n"
            "   - Use the mParticle Live Stream or Debugger to confirm user data is being sent and processed correctly.\n"
            "   - Verify that user profiles are updated as expected.\n\n"
            "8. Integrate with Destinations\n"
            "   - Set up integrations with downstream tools (e.g., CRMs, analytics platforms).\n"
            "   - Map user attributes and events to the destination schema.\n\n"
        )
    else:
        return f"Instructions for {task} in mParticle."



def get_lytics_info(task):
    if task == "build an audience segment":
        return (
            "1. Log in to Lytics\n"
            "   - Visit the Lytics dashboard.\n"
            "   - Log in with your credentials.\n\n"
            "2. Navigate to the Audience Section\n"
            "   - In the dashboard, go to the **Audiences** tab.\n"
            "   - This is where you can create and manage audience segments.\n\n"
            "3. Start a New Segment\n"
            "   - Click on Create New Segment** or a similar button.\n"
            "   - Enter a name for your audience segment for easy identification.\n\n"
            "4. Define Rules for the Segment\n"
            "   - Use the Lytics rule builder to set conditions based on user attributes and behaviors:\n"
            "     - Demographics:Age, gender, location.\n"
            "     - Behavioral Data: Page views, purchases, email clicks.\n"
            "     - Engagement Scores: Lytics engagement scores (e.g., active, dormant).\n"
            "   - Combine rules with AND/OR operators for complex logic.\n\n"
            "5. Preview the Audience\n"
            "   - Use the preview feature to see how many users match your criteria.\n"
            "   - Adjust the rules if the segment size is too large or small.\n\n"
            "6. Activate the Segment\n"
            "   - Once satisfied, save and activate the audience segment.\n"
            "   - Set up real-time syncing with downstream tools if required.\n\n"
            "7. Monitor and Optimize\n"
            "   - Regularly review segment performance using Lytics analytics tools.\n"
           "   - Refine rules to improve relevance and engagement.\n\n"
        )
           
    else:
        return f"Instructions for {task} in Lytics."



def get_zeotap_info(task):
    if task == "integrate my data":
        return (
            "1. Log in to Zeotap\n"
            "   - Visit the Zeotap dashboard.\n"
            "   - Log in using your credentials.\n\n"
            "2. Navigate to the Integration Section\n"
            "   - On the dashboard, locate and select the **Data Integration** tab.\n"
            "   - This section allows you to manage your data sources and integrations.\n\n"
            "3. Select Data Type\n"
            "   - Choose the type of data you wish to integrate:\n"
            "     - Customer Data: Demographic or behavioral data.\n"
            "     - Event Data: Transactional or interaction data.\n"
            "     - Third-Party Data: Partner-supplied datasets.\n\n"
            "4. Upload Your Data\n"
            "   - Use the data upload tool to import your dataset.\n"
            "   - Supported formats may include CSV, JSON, or API-based uploads.\n"
            "   - Ensure your data complies with Zeotap's formatting and privacy requirements.\n\n"
            "5. Map Your Data\n"
            "   - Use Zeotap's mapping tools to align your fields with the platform's schema:\n"
            "     - Match attributes like customer ID, email, or phone number.\n"
            "     - Validate field mapping for accuracy.\n\n"
            "6. Configure Destinations\n"
            "   - Select the platforms or tools where the integrated data should flow:\n"
            "     - CRM Systems: Salesforce, HubSpot, etc.\n"
            "     - Analytics Tools: Google Analytics, Tableau, etc.\n"
            "     - Advertising Platforms: Facebook Ads, Google Ads, etc.\n\n"
            "7. Test the Integration\n"
            "   - Conduct a test run to verify the data flow.\n"
            "   - Check logs or reports for errors or inconsistencies.\n\n"
            "8. Activate and Monitor\n"
            "   - Activate the integration once testing is successful.\n"
            "   - Use Zeotap's monitoring tools to track data performance and troubleshoot as needed.\n\n"
        )
    else:
        return f"Instructions for {task} in Zeotap."



if __name__ == '__main__':
    app.run(debug=True)
