from chunitizer import chunitize


man = 'おじいさん'
woman = 'おばあさん'
houseworks = [
    {'place': '山', 'task': '芝刈り'},
    {'place': '川', 'task': '洗濯'},
]

f_str = f'''
むかしむかしあるところに、{man}と{woman}が暮らしていました。
{man}は{houseworks[0]['place']}へ{houseworks[0]['task']}に、{woman}は{houseworks[1]['place']}へ{houseworks[1]['task']}に行きました。
'''

t_str = t'''
むかしむかしあるところに、{man}と{woman}が暮らしていました。
{man}は{houseworks[0]['place']}へ{houseworks[0]['task']}に、{woman}は{houseworks[1]['place']}へ{houseworks[1]['task']}に行きました。
'''

if __name__ == '__main__':
    print("f-string: ")
    print(f_str)

    print("t-string: ")
    print(chunitize(t_str))
