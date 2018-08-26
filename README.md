# YT-share

### Description
YT-share is a tool that syncs the playback of youtube videos across different computers.

### Installation
1. Clone the repo
```bash
git clone https://github.com/gauthamk97/YT-share
```

2. (Recommended) Use a virtual environment
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

3. Install the required python libraries
```bash
pip install -r requirements.txt
```

### Usage
1. Run the server for the backend
```bash
python server.py
```

2. Run the server for the frontend
```bash
python -m "SimpleHTTPServer"
```

3. Open Chrome and hit **localhost:8000** (For users on other systems, find your IP, and tell them to hit **<your_IP>:8000**)

##### Note : All users must be on the same network

### Supported Functionality
- Playing
- Pausing
- Seeking

### Coming Soon
- Support for playback rate
- Choose a video given the video ID
- Multiple sessions
- Chat functionality

### Supported Browsers
#### Google Chrome
Tried and tested. Works with 100% functionality.

#### Safari
Works completely from user's perspective. However, duplicate messages are being sent due to a _buffering_ state. While this doesn't hinder user experience, it could become noticable if there are a large number of users in the same session.

#### Mozilla Firefox
Not tested yet.

#### Microsoft Edge
Why are you using Edge?