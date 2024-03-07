a=input()
if a[0] != '"' or a[-1] != '"' or len(a)<3:
    print('CE')
else:
  try:exec(f'print({a})')
  except:print('CE')