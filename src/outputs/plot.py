import matplotlib.pyplot as plt

loss_train, loss_val = [], []
EPOCHS = 0

for i in range(1, 3):
	with open(f'./run{i}/out{i}.txt', 'r') as f:
		for line in f:
			sp = line.split(' ')
			loss_train.append(float(sp[5]))
			loss_val.append(float(sp[9]))
			EPOCHS += 1

epochs = range(1, EPOCHS + 1)
plt.plot(epochs, loss_train, 'g', label='Training loss')
plt.plot(epochs, loss_val, 'b', label='validation loss')
plt.title('Training and Validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig('Model.png')
