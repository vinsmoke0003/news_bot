<h1 align="center">📰 WhatsApp News Bot</h1>

<p align="center"><strong>Created by Seenu</strong><br>
B.Tech Computer Science Engineering Student<br>
<strong>Amity University</strong>
</p>

<hr>

<h2>🙋‍♂️ About Me</h2>

<p>Hi, I’m <strong>Seenu</strong>, a Computer Science Engineering student at <strong>Amity University</strong>. I built this project to learn more about APIs, automation, and how to integrate messaging platforms with real-time data. I love working with Python and exploring full-stack development.</p>

<hr>

<h2>📌 Project Overview</h2>

<p>This bot sends <strong>10 random India-based news headlines</strong> directly to your WhatsApp whenever you run the script. It uses the <a href="https://newsapi.org">NewsAPI</a> for fetching news, and the <a href="https://www.twilio.com/whatsapp">Twilio WhatsApp API</a> to send messages. The backend is powered by <strong>Python + Flask</strong>.</p>

<hr>

<h2>🔧 Dependencies</h2>

<p>You can install dependencies using the following command:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<p>Or manually:</p>

<pre><code>
pip install flask
pip install requests
pip install twilio
pip install python-dotenv
</code></pre>

<hr>

<h2>🛠 Tech Stack</h2>

<table>
  <tr><th>Component</th><th>Purpose</th></tr>
  <tr><td>Python 3</td><td>Programming Language</td></tr>
  <tr><td>Flask</td><td>Minimal web server (optional browser trigger)</td></tr>
  <tr><td>Twilio API</td><td>Send WhatsApp messages</td></tr>
  <tr><td>NewsAPI</td><td>Fetch India news headlines</td></tr>
  <tr><td>dotenv</td><td>Manage config securely</td></tr>
  <tr><td>requests</td><td>HTTP requests to NewsAPI</td></tr>
</table>

<hr>

<h2>🔐 .env File Setup</h2>

<p>Create a file named <code>.env</code> in your project folder with the following values:</p>

<pre><code>
NEWS_API_KEY=your_newsapi_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
MY_WHATSAPP_NUMBER=whatsapp:+91xxxxxxxxxx
</code></pre>

<p>
<strong>Note:</strong> You must join the Twilio Sandbox by sending the join code (e.g., <code>join sunny-cat</code>) to <code>+14155238886</code> from your WhatsApp number.
</p>

<hr>

<h2>🚀 How to Run the Project</h2>

<ol>
  <li>Clone or download this repository</li>
  <li>Create your <code>.env</code> file as shown above</li>
  <li>Install the dependencies</li>
  <li>Run the script:</li>
</ol>

<pre><code>python app.py</code></pre>

<p>You will instantly receive a WhatsApp message with <strong>10 random India news headlines</strong> 📱</p>

<hr>

<h2>🌐 Optional: Run With Flask Server</h2>

<ol>
  <li>Uncomment <code>app.run()</code> at the bottom of <code>app.py</code></li>
  <li>Start the server:
    <pre><code>python app.py</code></pre>
  </li>
  <li>Open in your browser:
    <ul>
      <li><a href="http://localhost:5000/">http://localhost:5000/</a></li>
      <li><a href="http://localhost:5000/send-news">http://localhost:5000/send-news</a></li>
    </ul>
  </li>
</ol>

<hr>

<h2>💬 What This Project Does</h2>

<ul>
  <li>Fetches news about "India" using NewsAPI</li>
  <li>Randomly selects 10 articles</li>
  <li>Sends them as a WhatsApp message via Twilio</li>
  <li>Can be triggered automatically or via URL</li>
</ul>

<hr>

<h2>📄 License</h2>

<p>This project is open-source and free for educational or personal use.</p>

<hr>

<h2>⭐ Support</h2>

<p>If you liked this project, please <strong>star it ⭐</strong> and share it with your friends!</p>
