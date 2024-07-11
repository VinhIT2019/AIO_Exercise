#3. Viết function lựa chọn regression loss function để tính loss:
import math
import random
def exercise3():
  num_samples = input("Input number of samples ( integer number ) which are generated :")
  if not num_samples.isnumeric():
    print("number of samples must be an integer number")
    return
  num_samples = int(num_samples)
  if num_samples<=0:
    print("number of samples must be greater than zero")
    return

  loss_name = input("Input loss name :")
  if loss_name not in "MSE|MAE|RMSE".split("|"):
    print(f"{loss_name} is not supportted")
    return
  total_loss=0
  for i in range(num_samples):
    predict = random.uniform(0,10)
    target = random.uniform(0,10)
    if loss_name=="mse":
      loss = (predict-target)**2
    elif loss_name=="mae":
      loss = abs(predict-target)
    else:
      loss = math.sqrt((predict-target)**2)

    print(f"loss name : {loss_name} , sample : {i} , pred : {predict} , target : {target}, loss: {loss}")
    total_loss+=loss
  print(f"final {loss_name} : {total_loss/num_samples}")

exercise3()