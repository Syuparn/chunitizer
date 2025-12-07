import subprocess

prompt = '''
以下の単語を厨二病っぽく言い換えてください。
なるべくスケールの大きいカッコ良い言葉が理想です。
ただし、回答として該当する単語だけを答えてください。
---
'''

def to_chuni(value: str):
    result = subprocess.run(
        ['gemini', '-p', prompt + value, '-m', 'gemini-2.5-flash'],
        capture_output=True, text=True)
    return result.stdout.replace('\n', '')
