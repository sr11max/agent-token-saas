import urllib.request, json, os
url = 'https://api.deepseek.com/v1/chat/completions'
key = os.environ.get('DEEPSEEK_API_KEY', '')
body = {
    'model': 'deepseek-chat',
    'messages': [{'role': 'user', 'content': '1+1=?'}],
    'max_tokens': 50
}
req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'),
    headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        result = json.loads(r.read())
        print('OK:', result['choices'][0]['message']['content'])
        print('Tokens:', result['usage'])
except Exception as e:
    print('FAIL:', e)