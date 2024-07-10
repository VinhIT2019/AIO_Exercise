#1. Viết function thực hiện đánh giá classification model bằng F1-Score.
def exercise1(tp,fp,fn):
  if type(tp)!=int:
    return print(f"tp must be int")
  if type(fp)!=int:
    return print(f"fp must be int")
  if type(fn)!=int:
    return print(f"fn must be int")
  if tp<=0 or fp<=0 or fn<=0:
    return print(f"tp and fp and fn must be greater than zero")

  precision = tp/(tp+fp)
  recall = tp/(tp+fn)
  f1 = 2*precision*recall/(precision+recall)
  print(f"precision is {precision}")
  print(f"recall is {recall}")
  print(f"f1 - score is {f1}")

exercise1(tp=2, fp=3 , fn=4)
exercise1(tp ='a', fp =3 , fn =4)
exercise1(tp =2 , fp ='a', fn =4)
exercise1(tp =2 , fp =3 , fn ='a')
exercise1(tp =2 , fp =3 , fn =0)
exercise1(tp =2.1 , fp =3 , fn =0)