# Instructions for Running AI Health Agent Demo in Google Colab

Follow these step-by-step instructions to set up and run the AI Health Agent demo in Google Colab.

## Step 1: Create a new Google Colab notebook

1. Go to [Google Colab](https://colab.research.google.com/)
2. Click on "New Notebook" to create a fresh notebook

## Step 2: Set up the files

Copy and paste each of the following code cells into your Colab notebook. Execute them one by one.

### Cell 1: Save the HTML demo file

```python
# Save the HTML demo file
with open('AI_Health_Agent_Demo.html', 'w') as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Health Agent - Simplified Demo</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }
        
        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        
        header {
            background-color: #3498db;
            color: white;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        header h1 {
            font-size: 24px;
        }
        
        .user-info {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .user-select {
            padding: 8px;
            border-radius: 4px;
            border: none;
        }
        
        .main-section {
            display: flex;
            height: 600px;
        }
        
        .sidebar {
            width: 300px;
            padding: 20px;
            border-right: 1px solid #eee;
            overflow-y: auto;
        }
        
        .chat-section {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }
        
        .section-title {
            font-size: 18px;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 1px solid #eee;
            color: #3498db;
        }
        
        .info-group {
            margin-bottom: 20px;
        }
        
        .info-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
        }
        
        .info-label {
            font-weight: bold;
            color: #666;
        }
        
        .health-item {
            padding: 8px 0;
            border-bottom: 1px solid #eee;
            display: flex;
            justify-content: space-between;
        }
        
        .chat-messages {
            flex-grow: 1;
            padding: 20px;
            overflow-y: auto;
        }
        
        .message {
            margin-bottom: 15px;
            max-width: 80%;
            padding: 10px 15px;
            border-radius: 8px;
        }
        
        .agent-message {
            background-color: #f1f1f1;
            margin-right: auto;
        }
        
        .user-message {
            background-color: #3498db;
            color: white;
            margin-left: auto;
        }
        
        .message-time {
            font-size: 12px;
            opacity: 0.7;
            margin-top: 5px;
        }
        
        .source-info {
            font-size: 12px;
            font-style: italic;
            color: #3498db;
            margin-top: 5px;
        }
        
        .chat-input {
            display: flex;
            padding: 10px;
            border-top: 1px solid #eee;
        }
        
        .chat-input input {
            flex-grow: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            margin-right: 10px;
        }
        
        .chat-input button {
            padding: 10px 20px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        
        .suggestions {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            padding: 10px;
            border-top: 1px solid #eee;
        }
        
        .suggestion-btn {
            background-color: #f1f1f1;
            border: 1px solid #ddd;
            border-radius: 20px;
            padding: 8px 12px;
            font-size: 14px;
            cursor: pointer;
        }
        
        .actions {
            display: flex;
            justify-content: space-between;
            padding: 10px 20px;
            border-top: 1px solid #eee;
        }
        
        .action-btn {
            padding: 8px 16px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: #f9f9f9;
            cursor: pointer;
        }
        
        .visualization {
            margin-top: 15px;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 8px;
        }
        
        .chart-container {
            margin-top: 10px;
            height: 200px;
            position: relative;
        }
        
        .chart-bar {
            position: absolute;
            bottom: 0;
            width: 30px;
            background-color: #3498db;
            border-radius: 3px 3px 0 0;
        }
        
        .chart-date {
            position: absolute;
            bottom: -25px;
            font-size: 12px;
            text-align: center;
            width: 40px;
            margin-left: -5px;
        }
        
        .chart-value {
            position: absolute;
            bottom: -40px;
            font-size: 12px;
            text-align: center;
            width: 40px;
            margin-left: -5px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>AI Health Agent for Personalized Health Management</h1>
            <div class="user-info">
                <select class="user-select" id="userSelect">
                    <option value="user123">User123</option>
                    <option value="demo_user">Demo User</option>
                    <option value="test_user">Test User</option>
                </select>
            </div>
        </header>
        
        <div class="main-section">
            <aside class="sidebar">
                <div class="info-group">
                    <h2 class="section-title">Personal Information</h2>
                    <div class="info-row">
                        <span class="info-label">Age:</span>
                        <span>42</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">Gender:</span>
                        <span>Female</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">Height:</span>
                        <span>165 cm</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">Weight:</span>
                        <span>68 kg</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">Activity Level:</span>
                        <span>Moderate</span>
                    </div>
                </div>
                
                <div class="info-group">
                    <h2 class="section-title">Health Conditions</h2>
                    <div class="health-item">
                        <span>Mild hypertension</span>
                        <span>June 2023</span>
                    </div>
                    <div class="health-item">
                        <span>Seasonal allergies</span>
                        <span>March 2020</span>
                    </div>
                </div>
                
                <div class="info-group">
                    <h2 class="section-title">Medications</h2>
                    <div class="health-item">
                        <span>Lisinopril</span>
                        <span>10mg, daily</span>
                    </div>
                    <div class="health-item">
                        <span>Loratadine</span>
                        <span>10mg, as needed</span>
                    </div>
                </div>
                
                <div class="info-group">
                    <h2 class="section-title">Recent Health Metrics</h2>
                    <div class="info-row">
                        <span class="info-label">Sleep (Apr 17):</span>
                        <span>6.5 hrs, fair quality</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">Activity (Apr 17):</span>
                        <span>8,750 steps, 42 min</span>
                    </div>
                    <div class="info-row">
                        <span class="info-label">Vitals (Apr 17):</span>
                        <span>BP: 132/84, HR: 72</span>
                    </div>
                </div>
            </aside>
            
            <div class="chat-section">
                <div class="chat-messages" id="chatMessages">
                    <div class="message agent-message">
                        <div>Welcome to your AI Health Agent! I'm here to provide personalized health recommendations based on your profile and needs. How can I assist you today?</div>
                        <div class="message-time">10:30 AM</div>
                    </div>
                </div>
                
                <div class="suggestions" id="suggestionArea">
                    <button class="suggestion-btn">How can I improve my sleep quality?</button>
                    <button class="suggestion-btn">What might be causing my fatigue lately?</button>
                    <button class="suggestion-btn">How can I better manage my hypertension?</button>
                    <button class="suggestion-btn">Should I adjust my exercise routine?</button>
                </div>
                
                <div class="chat-input">
                    <input type="text" id="messageInput" placeholder="Type your health question here...">
                    <button id="sendButton">Send</button>
                </div>
                
                <div class="actions">
                    <button class="action-btn" id="healthDataBtn">Add Health Data</button>
                    <button class="action-btn" id="visualizeBtn">Show Health Trends</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Get DOM elements
        const chatMessages = document.getElementById('chatMessages');
        const messageInput = document.getElementById('messageInput');
        const sendButton = document.getElementById('sendButton');
        const suggestionButtons = document.querySelectorAll('.suggestion-btn');
        const visualizeBtn = document.getElementById('visualizeBtn');
        const healthDataBtn = document.getElementById('healthDataBtn');
        
        // Add event listeners
        sendButton.addEventListener('click', sendMessage);
        messageInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
        
        suggestionButtons.forEach(button => {
            button.addEventListener('click', function() {
                messageInput.value = this.textContent;
                sendMessage();
            });
        });
        
        visualizeBtn.addEventListener('click', showVisualization);
        healthDataBtn.addEventListener('click', function() {
            alert("In a full implementation, this would open a form to add new health metrics like sleep, activity, and vital signs.");
        });
        
        // Functions
        function sendMessage() {
            const message = messageInput.value.trim();
            if (message === '') return;
            
            // Add user message
            const userMessageElement = document.createElement('div');
            userMessageElement.className = 'message user-message';
            
            const messageText = document.createElement('div');
            messageText.textContent = message;
            userMessageElement.appendChild(messageText);
            
            const messageTime = document.createElement('div');
            messageTime.className = 'message-time';
            const now = new Date();
            messageTime.textContent = `${now.getHours()}:${now.getMinutes().toString().padStart(2, '0')}`;
            userMessageElement.appendChild(messageTime);
            
            chatMessages.appendChild(userMessageElement);
            
            // Clear input
            messageInput.value = '';
            
            // Scroll to bottom
            chatMessages.scrollTop = chatMessages.scrollHeight;
            
            // Generate response after short delay
            setTimeout(function() {
                generateResponse(message);
            }, 1000);
        }
        
        function generateResponse(userMessage) {
            // Simple keyword-based responses
            let response = '';
            let source = '';
            
            if (userMessage.toLowerCase().includes('sleep') || userMessage.toLowerCase().includes('tired') || userMessage.toLowerCase().includes('fatigue')) {
                response = "Looking at your sleep patterns, I see you've been averaging about 6.5 hours with 'fair' quality. For someone with mild hypertension, quality sleep is particularly important.\n\nSome personalized recommendations:\n1. Maintain a consistent sleep schedule (even on weekends)\n2. Consider taking your Lisinopril in the morning rather than evening, as it can sometimes affect sleep\n3. Your activity level is good (8,750 steps yesterday), but try to complete exercise at least 3-4 hours before bedtime\n4. Create a calming pre-sleep routine without screens\n5. Your low sodium dietary preference is excellent for hypertension and can also help reduce nighttime awakenings";
                source = "National Sleep Foundation, 2024; American Heart Association, 2023";
            }
            else if (userMessage.toLowerCase().includes('blood pressure') || userMessage.toLowerCase().includes('hypertension')) {
                response = "Your recent blood pressure reading of 132/84 shows mild elevation. For someone with your profile, here are targeted recommendations:\n\n1. Continue your prescribed Lisinopril (10mg daily)\n2. Maintain your low-sodium diet approach - this is excellent for managing hypertension\n3. Your current activity level (moderate with ~8,750 steps) is beneficial; aim for consistency with 30+ minutes of activity daily\n4. Consider incorporating stress management techniques like deep breathing or meditation\n5. Work on improving sleep quality, as your recent average of 6.5 hours is below optimal and can impact blood pressure";
                source = "American Heart Association Guidelines, 2023; American College of Cardiology, 2024";
            }
            else if (userMessage.toLowerCase().includes('exercise') || userMessage.toLowerCase().includes('activity')) {
                response = "Based on your profile showing moderate activity level and recent logs averaging 8,750 steps and 42 active minutes daily, you're doing well with physical activity.\n\nFor someone with mild hypertension, your current activity pattern is beneficial. Some personalized suggestions:\n\n1. Maintain your current step count while gradually working toward 10,000 steps\n2. Consider adding 2 days of strength training weekly, which has specific benefits for blood pressure management\n3. Your walking routine is excellent - adding brief intervals of increased pace can enhance cardiovascular benefits\n4. Monitor your blood pressure before and after exercise occasionally to understand your body's response";
                source = "World Health Organization Physical Activity Guidelines, 2023; American Heart Association, 2023";
            }
            else {
                response = "Based on your health profile with mild hypertension and seasonal allergies, I can provide personalized guidance on several aspects of your health:\n\n- Managing your blood pressure (currently 132/84)\n- Improving your sleep quality (currently averaging 6.5 hours)\n- Optimizing your exercise routine\n- Addressing seasonal allergies\n\nIs there a specific area you'd like me to focus on?";
                source = "";
            }
            
            // Add agent message
            const agentMessageElement = document.createElement('div');
            agentMessageElement.className = 'message agent-message';
            
            const messageText = document.createElement('div');
            messageText.textContent = response;
            agentMessageElement.appendChild(messageText);
            
            if (source) {
                const sourceInfo = document.createElement('div');
                sourceInfo.className = 'source-info';
                sourceInfo.textContent = `Source: ${source}`;
                agentMessageElement.appendChild(sourceInfo);
            }
            
            const messageTime = document.createElement('div');
            messageTime.className = 'message-time';
            const now = new Date();
            messageTime.textContent = `${now.getHours()}:${now.getMinutes().toString().padStart(2, '0')}`;
            agentMessageElement.appendChild(messageTime);
            
            chatMessages.appendChild(agentMessageElement);
            
            // Scroll to bottom
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
        
        function showVisualization() {
            // Create visualization message
            const visualizationMsg = document.createElement('div');
            visualizationMsg.className = 'message agent-message';
            
            const messageContent = document.createElement('div');
            
            // Add title and explanation
            messageContent.innerHTML = '<div>Here\'s a visualization of your recent blood pressure readings:</div>';
            
            // Create visualization
            const visualization = document.createElement('div');
            visualization.className = 'visualization';
            
            // BP chart
            const chartTitle = document.createElement('h3');
            chartTitle.textContent = 'Blood Pressure Trend';
            chartTitle.style.marginBottom = '10px';
            visualization.appendChild(chartTitle);
            
            const chartContainer = document.createElement('div');
            chartContainer.className = 'chart-container';
            chartContainer.style.marginBottom = '40px';
            
            // BP data
            const bpData = [
                { date: 'Apr 13', value: 135, height: 85 },
                { date: 'Apr 15', value: 128, height: 78 },
                { date: 'Apr 17', value: 132, height: 82 }
            ];
            
            // Create bars
            bpData.forEach((data, index) => {
                const position = 15 + (index * 80);
                
                const bar = document.createElement('div');
                bar.className = 'chart-bar';
                bar.style.left = `${position}px`;
                bar.style.height = `${data.height}px`;
                bar.style.backgroundColor = data.value > 130 ? '#ff9f80' : '#80b1ff';
                
                const dateLabel = document.createElement('div');
                dateLabel.className = 'chart-date';
                dateLabel.textContent = data.date;
                dateLabel.style.left = `${position}px`;
                
                const valueLabel = document.createElement('div');
                valueLabel.className = 'chart-value';
                valueLabel.textContent = `${data.value}/` + (data.value - 50);
                valueLabel.style.left = `${position}px`;
                
                chartContainer.appendChild(bar);
                chartContainer.appendChild(dateLabel);
                chartContainer.appendChild(valueLabel);
            });
            
            visualization.appendChild(chartContainer);
            
            // Analysis
            const analysis = document.createElement('div');
            analysis.innerHTML = '<strong>Analysis:</strong> Your blood pressure has been fluctuating slightly, but remains in the mildly elevated range. The 132/84 reading on Apr 17 is an improvement from Apr 13, suggesting your medication and lifestyle adjustments are having a positive effect. Continue monitoring regularly and maintaining your current treatment plan.';
            analysis.style.marginTop = '20px';
            analysis.style.fontSize = '14px';
            
            visualization.appendChild(analysis);
            messageContent.appendChild(visualization);
            
            // Source citation
            const sourceInfo = document.createElement('div');
            sourceInfo.className = 'source-info';
            sourceInfo.textContent = 'Source: American Heart Association Guidelines, 2023';
            
            // Timestamp
            const messageTime = document.createElement('div');
            messageTime.className = 'message-time';
            const now = new Date();
            messageTime.textContent = `${now.getHours()}:${now.getMinutes().toString().padStart(2, '0')}`;
            
            // Add all elements to message
            visualizationMsg.appendChild(messageContent);
            visualizationMsg.appendChild(sourceInfo);
            visualizationMsg.appendChild(messageTime);
            
            // Add to chat and scroll
            chatMessages.appendChild(visualizationMsg);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    </script>
</body>
</html>""")
```

### Cell 2: Save the SVG architecture diagram

```python
# Save the SVG architecture diagram
with open('AI_Health_Agent_RAG_Architecture.svg', 'w') as f:
    f.write("""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="900" height="600" viewBox="0 0 900 600" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="900" height="600" fill="#f8fafc" rx="10" ry="10"/>
  
  <!-- Title -->
  <text x="450" y="40" font-family="Arial" font-size="24" text-anchor="middle" font-weight="bold" fill="#1e293b">AI Health Agent: RAG-based Architecture</text>
  
  <!-- User Representation -->
  <circle cx="100" cy="150" r="30" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/>
  <circle cx="100" cy="130" r="10" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/>
  <path d="M80,155 C90,180 110,180 120,155" fill="none" stroke="#64748b" stroke-width="2"/>
  <text x="100" y="200" font-family="Arial" font-size="14" text-anchor="middle" fill="#475569">User</text>
  
  <!-- Interface Layer Component -->
  <rect x="200" y="120" width="150" height="100" rx="5" ry="5" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="275" y="145" font-family="Arial" font-size="16" text-anchor="middle" font-weight="bold" fill="#0284c7">Interface Layer</text>
  <line x1="210" y1="155" x2="340" y2="155" stroke="#0284c7" stroke-width="1"/>
  <text x="275" y="175" font-family="Arial" font-size="12" text-anchor="middle" fill="#0369a1">Conversational UI</text>
  <text x="275" y="195" font-family="Arial" font-size="12" text-anchor="middle" fill="#0369a1">Data Visualization</text>
  
  <!-- Health Recommendation Engine Component -->
  <rect x="400" y="250" width="240" height="180" rx="5" ry="5" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="520" y="275" font-family="Arial" font-size="16" text-anchor="middle" font-weight="bold" fill="#4f46e5">Health Recommendation Engine</text>
  <line x1="420" y1="285" x2="620" y2="285" stroke="#4f46e5" stroke-width="1"/>
  
  <!-- LLM Component inside Recommendation Engine -->
  <rect x="430" y="295" width="180" height="55" rx="5" ry="5" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
  <text x="520" y="315" font-family="Arial" font-size="14" text-anchor="middle" fill="#334155">Large Language Model</text>
  <text x="520" y="335" font-family="Arial" font-size="12" text-anchor="middle" fill="#64748b">(GPT-4, Llama 3)</text>
  
  <!-- Prompt Engineering Component inside Recommendation Engine -->
  <rect x="430" y="355" width="180" height="55" rx="5" ry="5" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
  <text x="520" y="375" font-family="Arial" font-size="14" text-anchor="middle" fill="#334155">Context-Aware</text>
  <text x="520" y="395" font-family="Arial" font-size="14" text-anchor="middle" fill="#334155">Prompt Engineering</text>
  
  <!-- Health Knowledge Base Component -->
  <rect x="400" y="80" width="240" height="120" rx="5" ry="5" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="520" y="105" font-family="Arial" font-size="16" text-anchor="middle" font-weight="bold" fill="#16a34a">Health Knowledge Base</text>
  <line x1="420" y1="115" x2="620" y2="115" stroke="#16a34a" stroke-width="1"/>
  
  <!-- Vector DB Component inside Knowledge Base -->
  <rect x="430" y="125" width="180" height="55" rx="5" ry="5" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
  <text x="520" y="145" font-family="Arial" font-size="14" text-anchor="middle" fill="#334155">Vector Database</text>
  <text x="520" y="165" font-family="Arial" font-size="12" text-anchor="middle" fill="#64748b">(Embeddings & Retrieval)</text>
  
  <!-- User Profile Manager Component -->
  <rect x="680" y="250" width="180" height="180" rx="5" ry="5" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="770" y="275" font-family="Arial" font-size="16" text-anchor="middle" font-weight="bold" fill="#dc2626">User Profile Manager</text>
  <line x1="690" y1="285" x2="850" y2="285" stroke="#dc2626" stroke-width="1"/>
  
  <!-- FHIR Resources inside Profile Manager -->
  <rect x="700" y="295" width="140" height="120" rx="3" ry="3" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
  <text x="770" y="310" font-family="Arial" font-size="12" text-anchor="middle" fill="#334155">FHIR-Inspired Resources</text>
  <line x1="710" y1="315" x2="830" y2="315" stroke="#94a3b8" stroke-width="1"/>
  <text x="770" y="330" font-family="Arial" font-size="11" text-anchor="middle" fill="#334155">• Patient</text>
  <text x="770" y="350" font-family="Arial" font-size="11" text-anchor="middle" fill="#334155">• Condition</text>
  <text x="770" y="370" font-family="Arial" font-size="11" text-anchor="middle" fill="#334155">• MedicationStatement</text>
  <text x="770" y="390" font-family="Arial" font-size="11" text-anchor="middle" fill="#334155">• Observation</text>
  
  <!-- Safety Mechanisms Component -->
  <rect x="400" y="460" width="240" height="100" rx="5" ry="5" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
  <text x="520" y="485" font-family="Arial" font-size="16" text-anchor="middle" font-weight="bold" fill="#ca8a04">Safety Mechanisms</text>
  <line x1="420" y1="495" x2="620" y2="495" stroke="#ca8a04" stroke-width="1"/>
  <text x="520" y="515" font-family="Arial" font-size="12" text-anchor="middle" fill="#854d0e">• Emergency Detection</text>
  <text x="520" y="535" font-family="Arial" font-size="12" text-anchor="middle" fill="#854d0e">• Scope Limitations</text>
  <text x="520" y="555" font-family="Arial" font-size="12" text-anchor="middle" fill="#854d0e">• Source Attribution</text>
  
  <!-- Connection Arrows -->
  <!-- User to Interface -->
  <path d="M140,150 L190,150" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="5,3"/>
  <polygon points="195,150 185,146 185,154" fill="#64748b"/>
  
  <!-- Interface to Recommendation Engine -->
  <path d="M275,220 L275,340 L390,340" fill="none" stroke="#0284c7" stroke-width="2"/>
  <polygon points="395,340 385,336 385,344" fill="#0284c7"/>
  <text x="300" y="300" font-family="Arial" font-size="10" fill="#0284c7">User Query</text>
  
  <!-- Recommendation Engine to Interface -->
  <path d="M400,310 L275,310 L275,230" fill="none" stroke="#4f46e5" stroke-width="2"/>
  <polygon points="275,225 271,235 279,235" fill="#4f46e5"/>
  <text x="320" y="330" font-family="Arial" font-size="10" fill="#4f46e5">Response</text>
  
  <!-- Knowledge Base to Recommendation Engine -->
  <path d="M520,200 L520,240" fill="none" stroke="#16a34a" stroke-width="2"/>
  <polygon points="520,245 516,235 524,235" fill="#16a34a"/>
  <text x="540" y="225" font-family="Arial" font-size="10" fill="#16a34a">Retrieved Knowledge</text>
  
  <!-- Recommendation Engine to Knowledge Base -->
  <path d="M490,250 L490,210" fill="none" stroke="#4f46e5" stroke-width="2"/>
  <polygon points="490,205 486,215 494,215" fill="#4f46e5"/>
  <text x="450" y="225" font-family="Arial" font-size="10" fill="#4f46e5">Query</text>
  
  <!-- Profile Manager to Recommendation Engine -->
  <path d="M680,310 L650,310" fill="none" stroke="#dc2626" stroke-width="2"/>
  <polygon points="645,310 655,306 655,314" fill="#dc2626"/>
  <text x="660" y="300" font-family="Arial" font-size="10" fill="#dc2626">Profile Data</text>
  
  <!-- Recommendation Engine to Profile Manager -->
  <path d="M650,340 L670,340" fill="none" stroke="#4f46e5" stroke-width="2"/>
  <polygon points="675,340 665,336 665,344" fill="#4f46e5"/>
  <text x="660" y="360" font-family="Arial" font-size="10" fill="#4f46e5">Query</text>
  
  <!-- Safety Mechanisms to Recommendation Engine -->
  <path d="M520,460 L520,440" fill="none" stroke="#ca8a04" stroke-width="2"/>
  <polygon points="520,435 516,445 524,445" fill="#ca8a04"/>
  <text x="550" y="450" font-family="Arial" font-size="10" fill="#ca8a04">Safety Filters</text>
  
  <!-- RAG Workflow -->
  <path d="M100,80 C200,10 700,10 750,70 C800,130 800,350 750,400 C700,450 200,450 150,400 C100,350 30,150 100,80" fill="none" stroke="#475569" stroke-width="1" stroke-dasharray="5,3"/>
  <text x="450" y="70" font-family="Arial" font-size="14" text-anchor="middle" font-style="italic" fill="#475569">RAG Workflow</text>
  
  <!-- Data Flow Legend -->
  <rect x="640" y="490" width="240" height="90" rx="5" ry="5" fill="white" stroke="#94a3b8" stroke-width="1"/>
  <text x="760" y="510" font-family="Arial" font-size="14" text-anchor="middle" font-weight="bold" fill="#475569">Data Flow Legend</text>
  
  <!-- Legend Items -->
  <line x1="660" y1="530" x2="690" y2="530" stroke="#0284c7" stroke-width="2"/>
  <text x="770" y="535" font-family="Arial" font-size="12" fill="#475569">User Interaction</text>
  
  <line x1="660" y1="550" x2="690" y2="550" stroke="#4f46e5" stroke-width="2"/>
  <text x="770" y="555" font-family="Arial" font-size="12" fill="#475569">Query & Response Flow</text>
  
  <line x1="660" y1="570" x2="690" y2="570" stroke="#16a34a" stroke-width="2"/>
  <text x="770" y="575" font-family="Arial" font-size="12" fill="#475569">Knowledge Retrieval</text>
</svg>""")
```

### Cell 3: Create the AI Health Agent Python implementation

```python
# Create the AI Health Agent Python implementation
with open('ai_health_agent.py', 'w') as f:
    f.write("""
import os
import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from IPython.display import display, HTML

# Mock vector database and embeddings (in a real implementation, this would use a proper vector DB)
class HealthKnowledgeBase:
    def __init__(self):
        # Mock health knowledge
        self.health_knowledge = {
            "hypertension": {
                "recommendations": [
                    "Maintain a low-sodium diet with less than 2,300mg per day",
                    "Regular physical activity of at least 150 minutes per week",
                    "Maintain a healthy weight (BMI between 18.5-24.9)",
                    "Limit alcohol consumption",
                    "Take medications as prescribed"
                ],
                "sources": ["American Heart Association Guidelines, 2024", "CDC Hypertension Guidelines, 2023"]
            },
            "sleep_quality": {
                "recommendations": [
                    "Maintain a consistent sleep schedule",
                    "Create a restful environment (dark, quiet, comfortable temperature)",
                    "Limit exposure to screens before bedtime",
                    "Avoid caffeine and large meals before bedtime",
                    "Exercise regularly, but not too close to bedtime"
                ],
                "sources": ["National Sleep Foundation, 2024", "American Academy of Sleep Medicine, 2023"]
            },
            "exercise": {
                "recommendations": [
                    "Aim for at least 150 minutes of moderate-intensity activity per week",
                    "Include strength training at least twice per week",
                    "Start slowly and gradually increase intensity",
                    "Choose activities you enjoy to maintain consistency",
                    "Include flexibility and balance exercises"
                ],
                "sources": ["World Health Organization Physical Activity Guidelines, 2023", "American College of Sports Medicine, 2024"]
            },
            "allergies": {
                "recommendations": [
                    "Identify and avoid triggers",
                    "Keep windows closed during high pollen seasons",
                    "Use air purifiers with HEPA filters",
                    "Take medications as prescribed",
                    "Consider immunotherapy for severe allergies"
                ],
                "sources": ["American Academy of Allergy, Asthma & Immunology, 2023", "CDC Allergy Management, 2024"]
            }
        }
    
    def retrieve(self, query, top_k=2):
        # Simple keyword matching (in a real implementation, this would use vector similarity)
        scores = {}
        for topic, data in self.health_knowledge.items():
            if topic in query.lower():
                scores[topic] = 1.0
            else:
                # Assign some relevance based on keyword presence
                scores[topic] = 0.1
        
        # Sort by relevance and return top_k
        sorted_topics = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
        results = []
        
        for topic, score in sorted_topics:
            results.append({
                "topic": topic,
                "score": score,
                "data": self.health_knowledge[topic]
            })
        
        return results

# User Profile Management
class UserProfileManager:
    def __init__(self):
        # Default user profile (FHIR-inspired format)
        self.user_profile = {
            "resourceType": "Patient",
            "id": "user123",
            "active": True,
            "name": {
                "given": ["Demo"],
                "family": "User"
            },
            "gender": "female",
            "birthDate": "1981-07-15",
            "extension": [
                {
                    "url": "height",
                    "valueQuantity": {
                        "value": 165,
                        "unit": "cm"
                    }
                },
                {
                    "url": "weight",
                    "valueQuantity": {
                        "value": 68,
                        "unit": "kg"
                    }
                },
                {
                    "url": "activityLevel",
                    "valueString": "moderate"
                }
            ]
        }
        
        # Health conditions
        self.conditions = [
            {
                "resourceType": "Condition",
                "id": "cond1",
                "subject": {"reference": "Patient/user123"},
                "code": {
                    "text": "Mild hypertension"
                },
                "onsetDateTime": "2023-06-10"
            },
            {
                "resourceType": "Condition",
                "id": "cond2",
                "subject": {"reference": "Patient/user123"},
                "code": {
                    "text": "Seasonal allergies"
                },
                "onsetDateTime": "2020-03-15"
            }
        ]
        
        # Medications
        self.medications = [
            {
                "resourceType": "MedicationStatement",
                "id": "med1",
                "subject": {"reference": "Patient/user123"},
                "status": "active",
                "medicationCodeableConcept": {
                    "text": "Lisinopril"
                },
                "dosage": [
                    {
                        "text": "10mg, daily"
                    }
                ]
            },
            {
                "resourceType": "MedicationStatement",
                "id": "med2",
                "subject": {"reference": "Patient/user123"},
                "status": "active",
                "medicationCodeableConcept": {
                    "text": "Loratadine"
                },
                "dosage": [
                    {
                        "text": "10mg, as needed"
                    }
                ]
            }
        ]
        
        # Recent observations
        self.observations = [
            {
                "resourceType": "Observation",
                "id": "obs1",
                "subject": {"reference": "Patient/user123"},
                "code": {
                    "text": "Blood Pressure"
                },
                "valueString": "132/84",
                "effectiveDateTime": "2024-04-17"
            },
            {
                "resourceType": "Observation",
                "id": "obs2",
                "subject": {"reference": "Patient/user123"},
                "code": {
                    "text": "Heart Rate"
                },
                "valueQuantity": {
                    "value": 72,
                    "unit": "bpm"
                },
                "effectiveDateTime": "2024-04-17"
            },
            {
                "resourceType": "Observation",
                "id": "obs3",
                "subject": {"reference": "Patient/user123"},
                "code": {
                    "text": "Sleep"
                },
                "valueString": "6.5 hrs, fair quality",
                "effectiveDateTime": "2024-04-17"
            },
            {
                "resourceType": "Observation",
                "id": "obs4",
                "subject": {"reference": "Patient/user123"},
                "code": {
                    "text": "Activity"
                },
                "valueString": "8,750 steps, 42 min",
                "effectiveDateTime": "2024-04-17"
            }
        ]
        
        # Historical blood pressure readings
        self.bp_history = [
            {"date": "2024-04-13", "value": "135/85"},
            {"date": "2024-04-15", "value": "128/78"},
            {"date": "2024-04-17", "value": "132/84"}
        ]
    
    def get_user_summary(self):
        # Calculate age from birthdate
        birthdate = datetime.strptime(self.user_profile["birthDate"], "%Y-%m-%d")
        today = datetime.now()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        
        # Get height and weight
        height = None
        weight = None
        for ext in self.user_profile["extension"]:
            if ext["url"] == "height":
                height = ext["valueQuantity"]["value"]
            elif ext["url"] == "weight":
                weight = ext["valueQuantity"]["value"]
        
        # Calculate BMI if height and weight are available
        bmi = None
        if height and weight:
            # Convert height from cm to m
            height_m = height / 100
            bmi = round(weight / (height_m * height_m), 1)
        
        # Get latest observations
        latest_bp = None
        latest_sleep = None
        latest_activity = None
        
        for obs in self.observations:
            if obs["code"]["text"] == "Blood Pressure":
                latest_bp = obs["valueString"]
            elif obs["code"]["text"] == "Sleep":
                latest_sleep = obs["valueString"]
            elif obs["code"]["text"] == "Activity":
                latest_activity = obs["valueString"]
        
        # Compile user summary
        summary = {
            "demographics": {
                "age": age,
                "gender": self.user_profile["gender"],
                "bmi": bmi
            },
            "conditions": [cond["code"]["text"] for cond in self.conditions],
            "medications": [
                {
                    "name": med["medicationCodeableConcept"]["text"],
                    "dosage": med["dosage"][0]["text"]
                } for med in self.medications
            ],
            "recent_metrics": {
                "blood_pressure": latest_bp,
                "sleep": latest_sleep,
                "activity": latest_activity
            }
        }
        
        return summary

# Recommendation Engine
class HealthRecommendationEngine:
    def __init__(self):
        self.knowledge_base = HealthKnowledgeBase()
        self.profile_manager = UserProfileManager()
        
    def generate_response(self, user_query):
        # Get user profile summary
        user_summary = self.profile_manager.get_user_summary()
        
        # Retrieve relevant knowledge
        retrieved_knowledge = self.knowledge_base.retrieve(user_query)
        
        # Simple keyword-based response generation
        response = ""
        sources = []
        
        # Detect query type based on keywords
        if "sleep" in user_query.lower() or "tired" in user_query.lower() or "fatigue" in user_query.lower():
            response = f"Looking at your sleep patterns, I see you've been averaging about 6.5 hours with 'fair' quality. For someone with mild hypertension, quality sleep is particularly important.\\n\\nSome personalized recommendations:\\n"
            
            # Add recommendations from knowledge base
            sleep_data = next((item for item in retrieved_knowledge if item["topic"] == "sleep_quality"), None)
            if sleep_data:
                for i, rec in enumerate(sleep_data["data"]["recommendations"], 1):
                    response += f"{i}. {rec}\\n"
                sources.extend(sleep_data["data"]["sources"])
            
            # Add personalized notes based on user profile
            response += "\\nYour activity level is good (8,750 steps), but try to complete exercise at least 3-4 hours before bedtime."
                
        elif "blood pressure" in user_query.lower() or "hypertension" in user_query.lower():
            response = f"Your recent blood pressure reading of {user_summary['recent_metrics']['blood_pressure']} shows mild elevation. For someone with your profile, here are targeted recommendations:\\n\\n"
            
            # Add recommendations from knowledge base
            bp_data = next((item for item in retrieved_knowledge if item["topic"] == "hypertension"), None)
            if bp_data:
                for i, rec in enumerate(bp_data["data"]["recommendations"], 1):
                    response += f"{i}. {rec}\\n"
                sources.extend(bp_data["data"]["sources"])
            
            # Add personalized notes based on user profile
            response += "\\nYour current activity level (moderate with ~8,750 steps) is beneficial; work on improving sleep quality, as your recent average of 6.5 hours is below optimal and can impact blood pressure."
                
        elif "exercise" in user_query.lower() or "activity" in user_query.lower():
            response = f"Based on your profile showing moderate activity level and recent logs averaging {user_summary['recent_metrics']['activity']}, you're doing well with physical activity.\\n\\nFor someone with mild hypertension, your current activity pattern is beneficial. Some personalized suggestions:\\n\\n"
            
            # Add recommendations from knowledge base
            exercise_data = next((item for item in retrieved_knowledge if item["topic"] == "exercise"), None)
            if exercise_data:
                for i, rec in enumerate(exercise_data["data"]["recommendations"][:4], 1):  # Limit to 4 recommendations
                    response += f"{i}. {rec}\\n"
                sources.extend(exercise_data["data"]["sources"])
            
            # Add personalized note based on user profile
            response += "\\nMonitor your blood pressure before and after exercise occasionally to understand your body's response."
            
        elif "allerg" in user_query.lower():
            response = f"Based on your history of seasonal allergies (since March 2020), here are some personalized recommendations:\\n\\n"
            
            # Add recommendations from knowledge base
            allergy_data = next((item for item in retrieved_knowledge if item["topic"] == "allergies"), None)
            if allergy_data:
                for i, rec in enumerate(allergy_data["data"]["recommendations"], 1):
                    response += f"{i}. {rec}\\n"
                sources.extend(allergy_data["data"]["sources"])
            
            # Add medication reminder based on user profile
            response += "\\nContinue taking Loratadine (10mg) as needed during allergy season."
            
        else:
            # General response if no specific topic is detected
            response = f"Based on your health profile with mild hypertension and seasonal allergies, I can provide personalized guidance on several aspects of your health:\\n\\n"
            response += f"- Managing your blood pressure (currently {user_summary['recent_metrics']['blood_pressure']})\\n"
            response += f"- Improving your sleep quality (currently averaging {user_summary['recent_metrics']['sleep']})\\n"
            response += f"- Optimizing your exercise routine\\n"
            response += f"- Addressing seasonal allergies\\n\\n"
            response += f"Is there a specific area you'd like me to focus on?"
        
        # Format sources if available
        source_text = "; ".join(sources) if sources else ""
        
        return {
            "response": response,
            "sources": source_text
        }
    
    def visualize_blood_pressure(self):
        # Get BP history from profile manager
        bp_history = self.profile_manager.bp_history
        
        # Extract dates and systolic/diastolic values
        dates = [item["date"][-5:] for item in bp_history]  # Just month/day
        systolic = []
        diastolic = []
        
        for item in bp_history:
            bp_parts = item["value"].split("/")
            systolic.append(int(bp_parts[0]))
            diastolic.append(int(bp_parts[1]))
        
        # Create visualization
        plt.figure(figsize=(10, 6))
        
        # Plot systolic
        plt.plot(dates, systolic, 'o-', color='#ff9f80', linewidth=2, markersize=8, label='Systolic')
        
        # Plot diastolic
        plt.plot(dates, diastolic, 'o-', color='#80b1ff', linewidth=2, markersize=8, label='Diastolic')
        
        # Add reference lines for normal ranges
        plt.axhspan(120, 130, color='#e6ffe6', alpha=0.3, label='Normal Systolic Range')
        plt.axhspan(80, 85, color='#e6f2ff', alpha=0.3, label='Normal Diastolic Range')
        
        # Customize the plot
        plt.title('Blood Pressure Trend', fontsize=16)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Blood Pressure (mmHg)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        
        # Add value labels
        for i, (sys, dia) in enumerate(zip(systolic, diastolic)):
            plt.text(i, sys+2, str(sys), ha='center')
            plt.text(i, dia-4, str(dia), ha='center')
        
        # Set y-axis limits with some padding
        plt.ylim(min(diastolic)-10, max(systolic)+10)
        
        # Add analysis text
        analysis = "Analysis: Your blood pressure has been fluctuating slightly, but remains in the mildly elevated range. "
        analysis += "The 132/84 reading on Apr 17 is an improvement from Apr 13, suggesting your medication and lifestyle "
        analysis += "adjustments are having a positive effect. Continue monitoring regularly and maintaining your current treatment plan."
        
        plt.figtext(0.5, 0.01, analysis, ha='center', fontsize=10, wrap=True)
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.2)  # Make room for the analysis text
        plt.savefig('bp_trend.png')
        
        # Display the source
        source = "Source: American Heart Association Guidelines, 2023"
        return source

# User Interface
class HealthAgentUI:
    def __init__(self):
        self.recommendation_engine = HealthRecommendationEngine()
        self.conversation_history = []
        
        # Add initial greeting
        self.add_message("agent", "Welcome to your AI Health Agent! I'm here to provide personalized health recommendations based on your profile and needs. How can I assist you today?")
    
    def add_message(self, sender, text, source=None):
        # Add a message to the conversation history
        now = datetime.now().strftime("%H:%M")
        message = {
            "sender": sender,
            "text": text,
            "time": now,
            "source": source
        }
        self.conversation_history.append(message)
        return message
    
    def process_user_message(self, message_text):
        # Add user message to history
        self.add_message("user", message_text)
        
        # Generate response from recommendation engine
        response_data = self.recommendation_engine.generate_response(message_text)
        
        # Add agent response to history
        self.add_message("agent", response_data["response"], response_data["sources"])
        
        # Return the latest message for display
        return self.conversation_history[-1]
    
    def generate_visualization(self):
        # Generate blood pressure visualization
        source = self.recommendation_engine.visualize_blood_pressure()
        
        # Add visualization message to history
        self.add_message(
            "agent", 
            "Here's a visualization of your recent blood pressure readings. The chart shows your systolic and diastolic values over time, with reference ranges for normal blood pressure.", 
            source
        )
        
        # Return the latest message for display
        return self.conversation_history[-1]
    
    def render_conversation(self):
        # Create HTML output for the conversation
        html = """
        <div style="max-width: 800px; margin: 0 auto; font-family: Arial, sans-serif;">
            <div style="background-color: #3498db; color: white; padding: 15px; border-radius: 8px 8px 0 0;">
                <h2 style="margin: 0;">AI Health Agent</h2>
            </div>
            <div style="height: 400px; overflow-y: auto; padding: 15px; background-color: #f9f9f9; border-left: 1px solid #ddd; border-right: 1px solid #ddd;">
        """
        
        # Add messages
        for message in self.conversation_history:
            if message["sender"] == "agent":
                html += f"""
                <div style="margin-bottom: 15px; max-width: 80%; background-color: #f1f1f1; padding: 10px 15px; border-radius: 8px; margin-right: auto;">
                    <div style="white-space: pre-line;">{message["text"]}</div>
                """
                
                if message["source"]:
                    html += f"""
                    <div style="font-size: 12px; font-style: italic; color: #3498db; margin-top: 5px;">Source: {message["source"]}</div>
                    """
                
                html += f"""
                    <div style="font-size: 12px; opacity: 0.7; margin-top: 5px;">{message["time"]}</div>
                </div>
                """
            else:
                html += f"""
                <div style="margin-bottom: 15px; max-width: 80%; background-color: #3498db; color: white; padding: 10px 15px; border-radius: 8px; margin-left: auto;">
                    <div>{message["text"]}</div>
                    <div style="font-size: 12px; opacity: 0.7; margin-top: 5px;">{message["time"]}</div>
                </div>
                """
        
        # Close message container
        html += """
            </div>
        """
        
        # Add BP visualization if available
        if os.path.exists('bp_trend.png'):
            html += """
            <div style="padding: 15px; background-color: white; border-left: 1px solid #ddd; border-right: 1px solid #ddd;">
                <h3 style="margin-top: 0; color: #3498db;">Blood Pressure Visualization</h3>
                <img src="bp_trend.png" style="max-width: 100%; margin-top: 10px;" />
            </div>
            """
        
        # Add input field and buttons
        html += """
            <div style="padding: 15px; background-color: white; border-radius: 0 0 8px 8px; border: 1px solid #ddd;">
                <div style="display: flex; margin-bottom: 15px;">
                    <input type="text" id="messageInput" placeholder="Type your health question here..." style="flex-grow: 1; padding: 10px; border: 1px solid #ddd; border-radius: 4px; margin-right: 10px;">
                    <button id="sendButton" style="padding: 10px 20px; background-color: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer;">Send</button>
                </div>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 15px;">
                    <button class="suggestion-btn" style="background-color: #f1f1f1; border: 1px solid #ddd; border-radius: 20px; padding: 8px 12px; font-size: 14px; cursor: pointer;">How can I improve my sleep quality?</button>
                    <button class="suggestion-btn" style="background-color: #f1f1f1; border: 1px solid #ddd; border-radius: 20px; padding: 8px 12px; font-size: 14px; cursor: pointer;">What might be causing my fatigue lately?</button>
                    <button class="suggestion-btn" style="background-color: #f1f1f1; border: 1px solid #ddd; border-radius: 20px; padding: 8px 12px; font-size: 14px; cursor: pointer;">How can I better manage my hypertension?</button>
                    <button class="suggestion-btn" style="background-color: #f1f1f1; border: 1px solid #ddd; border-radius: 20px; padding: 8px 12px; font-size: 14px; cursor: pointer;">Should I adjust my exercise routine?</button>
                </div>
                <div style="display: flex; justify-content: space-between;">
                    <button id="healthDataBtn" style="padding: 8px 16px; border: 1px solid #ddd; border-radius: 4px; background-color: #f9f9f9; cursor: pointer;">Add Health Data</button>
                    <button id="visualizeBtn" style="padding: 8px 16px; border: 1px solid #ddd; border-radius: 4px; background-color: #f9f9f9; cursor: pointer;">Show Health Trends</button>
                </div>
            </div>
        </div>
        """
        
        return HTML(html)
    
    def render_dashboard(self):
        # Create a dashboard with user profile and chat interface
        html = """
        <div style="max-width: 1000px; margin: 0 auto; font-family: Arial, sans-serif; display: flex; flex-direction: column;">
            <div style="background-color: #3498db; color: white; padding: 15px; border-radius: 8px 8px 0 0; display: flex; justify-content: space-between; align-items: center;">
                <h2 style="margin: 0;">AI Health Agent for Personalized Health Management</h2>
                <div style="display: flex; align-items: center; gap: 10px;">
                    <select style="padding: 8px; border-radius: 4px; border: none;">
                        <option>User123</option>
                        <option>Demo User</option>
                        <option>Test User</option>
                    </select>
                </div>
            </div>
            <div style="display: flex; height: 600px; background-color: white; border-left: 1px solid #ddd; border-right: 1px solid #ddd;">
                <!-- Sidebar with user profile -->
                <div style="width: 300px; padding: 20px; border-right: 1px solid #eee; overflow-y: auto;">
                    <div style="margin-bottom: 20px;">
                        <h3 style="font-size: 18px; margin-bottom: 15px; padding-bottom: 8px; border-bottom: 1px solid #eee; color: #3498db;">Personal Information</h3>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                            <span style="font-weight: bold; color: #666;">Age:</span>
                            <span>42</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                            <span style="font-weight: bold; color: #666;">Gender:</span>
                            <span>Female</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                            <span style="font-weight: bold; color: #666;">Height:</span>
                            <span>165 cm</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                            <span style="font-weight: bold; color: #666;">Weight:</span>
                            <span>68 kg</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                            <span style="font-weight: bold; color: #666;">Activity Level:</span>
                            <span>Moderate</span>
                        </div>
                    </div>
                    
                    <div style="margin-bottom: 20px;">
                        <h3 style="font-size: 18px; margin-bottom: 15px; padding-bottom: 8px; border-bottom: 1px solid #eee; color: #3498db;">Health Conditions</h3>
                        <div style="padding: 8px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between;">
                            <span>Mild hypertension</span>
                            <span>June 2023</span>
                        </div>
                        <div style="padding: 8px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between;">
                            <span>Seasonal allergies</span>
                            <span>March 2020</span>
                        </div>
                    </div>
                    
                    <div style="margin-bottom: 20px;">
                        <h3 style="font-size: 18px; margin-bottom: 15px; padding-bottom: 8px; border-bottom: 1px solid #eee; color: #3498db;">Medications</h3>
                        <div style="padding: 8px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between;">
                            <span>Lisinopril</span>
                            <span>10mg, daily</span>
                        </div>
                        <div style="padding: 8px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between;">
                            <span>Loratadine</span>
                            <span>10mg, as needed</span>
                        </div>
                    </div>
                    
                    <div style="margin-bottom: 20px;">
                        <h3 style="font-size: 18px; margin-bottom: 15px; padding-bottom: 8px; border-bottom: 1px solid #eee; color: #3498db;">Recent Health Metrics</h3>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                            <span style="font-weight: bold; color: #666;">Sleep (Apr 17):</span>
                            <span>6.5 hrs, fair quality</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                            <span style="font-weight: bold; color: #666;">Activity (Apr 17):</span>
                            <span>8,750 steps, 42 min</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                            <span style="font-weight: bold; color: #666;">Vitals (Apr 17):</span>
                            <span>BP: 132/84, HR: 72</span>
                        </div>
                    </div>
                </div>
                
                <!-- Chat section -->
                <div style="flex-grow: 1; display: flex; flex-direction: column;">
                    <div id="chatMessages" style="flex-grow: 1; padding: 20px; overflow-y: auto;">
        """
        
        # Add messages
        for message in self.conversation_history:
            if message["sender"] == "agent":
                html += f"""
                <div style="margin-bottom: 15px; max-width: 80%; background-color: #f1f1f1; padding: 10px 15px; border-radius: 8px; margin-right: auto;">
                    <div style="white-space: pre-line;">{message["text"]}</div>
                """
                
                if message["source"]:
                    html += f"""
                    <div style="font-size: 12px; font-style: italic; color: #3498db; margin-top: 5px;">Source: {message["source"]}</div>
                    """
                
                html += f"""
                    <div style="font-size: 12px; opacity: 0.7; margin-top: 5px;">{message["time"]}</div>
                </div>
                """
            else:
                html += f"""
                <div style="margin-bottom: 15px; max-width: 80%; background-color: #3498db; color: white; padding: 10px 15px; border-radius: 8px; margin-left: auto;">
                    <div>{message["text"]}</div>
                    <div style="font-size: 12px; opacity: 0.7; margin-top: 5px;">{message["time"]}                    </div>
                </div>
                """
        
        # Add the rest of the dashboard
        html += """
                    </div>
                    
                    <div style="display: flex; flex-wrap: wrap; gap: 8px; padding: 10px; border-top: 1px solid #eee;">
                        <button class="suggestion-btn" style="background-color: #f1f1f1; border: 1px solid #ddd; border-radius: 20px; padding: 8px 12px; font-size: 14px; cursor: pointer;">How can I improve my sleep quality?</button>
                        <button class="suggestion-btn" style="background-color: #f1f1f1; border: 1px solid #ddd; border-radius: 20px; padding: 8px 12px; font-size: 14px; cursor: pointer;">What might be causing my fatigue lately?</button>
                        <button class="suggestion-btn" style="background-color: #f1f1f1; border: 1px solid #ddd; border-radius: 20px; padding: 8px 12px; font-size: 14px; cursor: pointer;">How can I better manage my hypertension?</button>
                        <button class="suggestion-btn" style="background-color: #f1f1f1; border: 1px solid #ddd; border-radius: 20px; padding: 8px 12px; font-size: 14px; cursor: pointer;">Should I adjust my exercise routine?</button>
                    </div>
                    
                    <div style="display: flex; padding: 10px; border-top: 1px solid #eee;">
                        <input type="text" id="messageInput" placeholder="Type your health question here..." style="flex-grow: 1; padding: 10px; border: 1px solid #ddd; border-radius: 4px; margin-right: 10px;">
                        <button id="sendButton" style="padding: 10px 20px; background-color: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer;">Send</button>
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; padding: 10px 20px; border-top: 1px solid #eee;">
                        <button id="healthDataBtn" style="padding: 8px 16px; border: 1px solid #ddd; border-radius: 4px; background-color: #f9f9f9; cursor: pointer;">Add Health Data</button>
                        <button id="visualizeBtn" style="padding: 8px 16px; border: 1px solid #ddd; border-radius: 4px; background-color: #f9f9f9; cursor: pointer;">Show Health Trends</button>
                    </div>
                </div>
            </div>
        </div>
        """
        
        return HTML(html)
""")
```

### Cell 4: Create the demo execution script

```python
# Create a demo script that runs everything
with open('run_health_agent_demo.py', 'w') as f:
    f.write("""
# Import required libraries
import os
import sys
import matplotlib.pyplot as plt
from IPython.display import display, HTML, IFrame, SVG

# Check if we're in Colab
try:
    import google.colab
    IN_COLAB = True
except:
    IN_COLAB = False

if IN_COLAB:
    print("Setting up the AI Health Agent demo in Google Colab...")
else:
    print("This script is designed to run in Google Colab. Some features may not work correctly.")

# Import the health agent module
from ai_health_agent import HealthAgentUI

def run_demo():
    # Create the agent UI
    ui = HealthAgentUI()
    
    # Display the architecture diagram
    print("\\n== AI Health Agent Architecture ==")
    try:
        with open('AI_Health_Agent_RAG_Architecture.svg', 'r') as f:
            svg_content = f.read()
        display(SVG(data=svg_content))
    except Exception as e:
        print(f"Could not display architecture diagram: {e}")
    
    # Display the static HTML demo
    print("\\n== Static HTML Demo ==")
    try:
        display(IFrame(src='AI_Health_Agent_Demo.html', width=1000, height=700))
    except Exception as e:
        print(f"Could not display HTML demo: {e}")
    
    # Display the interactive Python demo
    print("\\n== Interactive Python Demo ==")
    display(ui.render_dashboard())
    
    # Process a few example queries
    example_queries = [
        "How can I improve my sleep quality?",
        "I'm concerned about my blood pressure readings",
        "What kind of exercise would be best for me?"
    ]
    
    for query in example_queries:
        print(f"\\n== Processing query: {query} ==")
        ui.process_user_message(query)
        display(ui.render_dashboard())
    
    # Generate and show visualization
    print("\\n== Generating blood pressure visualization ==")
    ui.generate_visualization()
    display(ui.render_dashboard())
    
    print("\\nDemo completed! You can now interact with the AI Health Agent by modifying the code.")

if __name__ == "__main__":
    run_demo()
""")
```

## Step 3: Run the demo

After creating all the necessary files, you can run the demo with the following code cell:

```python
# Install any required libraries (if needed)
!pip install matplotlib

# Execute the demo
%run run_health_agent_demo.py
```

## Step 4: Experiment with the Health Agent

Now that the demo is running, you can experiment with the AI Health Agent by trying different inputs:

```python
# Import the health agent module
from ai_health_agent import HealthAgentUI

# Create a fresh instance or use the existing one
ui = HealthAgentUI()

# Example: Ask about allergies
ui.process_user_message("What can I do to manage my seasonal allergies better?")
display(ui.render_dashboard())

# Example: Generate blood pressure visualization
ui.generate_visualization()
display(ui.render_dashboard())
```

## Understanding the Implementation

This implementation demonstrates a simplified RAG-based AI Health Agent with these key components:

1. **Knowledge Base**: Stores health recommendations and their sources
2. **User Profile Manager**: Contains FHIR-inspired health records
3. **Recommendation Engine**: Combines user data with health knowledge
4. **Visualization**: Creates data visualizations for health metrics
5. **UI Components**: Provides dashboard and chat interfaces

In a production implementation, you would enhance this with:
- A real vector database for knowledge retrieval
- Integration with an actual LLM API (like Claude or GPT-4)
- Secure user authentication and data storage
- More sophisticated retrieval algorithms
- Additional health metrics and visualization options

## Notes About Colab Implementation

1. The interactive HTML features (buttons, input) are for demonstration purposes only, as Colab's security model prevents direct JavaScript execution in displayed HTML.

2. Instead, we use Python functions to simulate user interactions with the agent.

3. The data visualization uses matplotlib which works well in Colab notebooks.

4. This setup allows you to understand the architecture and modify it for your own health agent implementation.
                    "