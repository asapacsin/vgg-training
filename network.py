import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import pickle

class simple_neural_network():
    def __init__(self,middle_network_size = 3):
        network = {}
        self.middle_network_size = middle_network_size
        first_layer_size = middle_network_size
        self.middle_size = middle_network_size
        #input has a n size, the network would has mxn size and output m size, m = 3
        #initize random  network size
        m = first_layer_size
        #n = input_size
        #here the m equal n 
        n = 3
        #network = np.random.rand(m,n)
        network['w1'] = np.random.rand(m,n)
        last_layer_size = 1
        n = m
        m = last_layer_size
        network['w2'] = np.random.rand(m,n)
        self.network = network
    def set_weight(self,w1,w2):
        self.network['w1'] = w1
        self.network['w2'] = w2

    def get_output(self,input):
        get_network = self.network['w1']
        output = np.dot(get_network,input)
        get_network = self.network['w2']
        output = np.dot(get_network,output)
        return output
    def get_result_network(self,input):
        result = {}
        result['input'] = input
        result['w1'] = self.relu(np.dot(self.network['w1'],input))
        result['end'] = self.relu(np.dot(self.network['w2'],result['w1']))
        return result
    def update_network(self,result_network,s):
        gradient = {}
        epi0 = s*self.relu_gradient(result_network['end'])
        epi1 = result_network['w1']*epi0
        gradient['w2'] =epi1

        result_vec1 = result_network['input'].T
        result_vec2 = np.array([result_vec1 for i in range(self.middle_network_size)])
        grad1 = gradient['w2']
        grad2 = grad1*self.relu_gradient(result_network['w1'])
        grad2 = np.array([[grad2[i]] for i in range(len(grad2))])
        gradient['w1'] = result_vec2*grad2
        #update w
        self.network['w1'] = self.network['w1'] - gradient['w1']
        self.network['w2'] = self.network['w2'] - gradient['w2']

    def train(self,input,output):
        result_network = self.get_result_network(input)
        s = result_network['end'] - output
        loss = pow(s,2)
        self.loss = loss
        self.update_network(result_network,s)
        print('loss is:',loss)
    def relu(self,input):
        return np.maximum(input,0)
    def relu_gradient(self,x):
        #return the numpy array with same size 1 if x > 0 else 0
        return np.where(x>0,1,0)
    def getloss(self):
        return self.loss


def main():
    net = simple_neural_network(100)
    #create random 3x1 vector
    workbook = openpyxl.load_workbook('test_case.xlsx')
    worksheet = workbook.active
    #read input and output
    #input = np.array([])
    #output = np.array([])
    loss_arr = []
    for i in range(1000):
        print(f'epoch {i+1}')
        #input = np.append(input,[[worksheet['A'+str(i+2)].value,worksheet['B'+str(i+2)].value,worksheet['C'+str(i+2)].value]])
        get_input = np.array([worksheet['A'+str(i+2)].value,worksheet['B'+str(i+2)].value,worksheet['C'+str(i+2)].value])
        #output = np.append(output,[[worksheet['D'+str(i+2)].value]])
        get_output = np.array([worksheet['D'+str(i+2)].value])
        net.train(get_input,get_output)
        loss = net.getloss()
        loss_arr.append(loss)

    #plot loss
    plt.plot(loss_arr)
    plt.show()

    #save weight in weight.xlsx
    w1 = net.network['w1']
    w2 = net.network['w2']
    #save weight in weight.xlsx
    with open('weight.pickle','rb') as f:
        pickle.dump([w1,w2],f)
    f.close()
    

main()
