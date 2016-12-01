import numpy as np
import random

class Network():

     def __init__(self, weights=None):
         self.inner = 2
         self.hidden = 2
         self.outer = 1
         if not weights:
            self.weights = [np.random.randn(x,y) for x, y in zip([self.inner,self.hidden], [self.hidden, self.outer])]
         else: self.weights = weights


     def feedforward(self, a):
         for w in self.weights:
             a = sigmoid(np.dot(a,w))
         return a


def sigmoid(n):
    return 1 / (1 + np.exp(-n))

nn = Network()
n1 = Network()

# print(zip(nn.weights[1],n1.weights[0]))
# print(nn.weights)
#
# print('toooo je to',nn.feedforward(np.array([4,6])))
# print(nn.weights)
# # print(n1.weights)
# #
# r1, r2 = [],[]
# for l1,l2 in zip(nn.weights, n1.weights):
#     # half = len(w1) / 2
#
#     for w1,w2 in zip(l1,l2):
#         print(w1)
#         print(w2)
#         for c1,c2 in zip(w1,w2):
#             r1.append(c1)
#             r2.append(c2)
#
# print(r1)
# print(r2)


   #print(layer1,layer2)
#     #layer1.shape = (1)
#     #print(layer1)
#     # for w2, w1 in layer1,layer2:
#     #     w1 = w1[:len(w1) // 2].append(w2[len(w1) // 2:])
#     #     print(w1)
#         # for w1,w2 in neuron1,neuron2:
#
# print(nn.weights)
# shuffeled = [i if i % 3 == 0 else j for i,j in zip(nn.weights[0],n1.weights[0])]
# print(shuffeled)
# print(nn.weights)
# in_data = np.array([[0,1],[1,1],[1,0],[0,0],[0,1],[0,0]])
# out_data = np.array([[1],[1],[1],[0],[1],[0]])
#
#
#
# for epoch in range(1000):
#
#     #feed forward
#     in_layer = in_data
#     print(nn.weights[0])
#     print(in_layer)
#     hid_layer = sigmoid(np.dot(in_layer,nn.weights[0]))
#     print(hid_layer)
#     print(nn.weights[1])
#     out_layer = sigmoid(np.dot(hid_layer,nn.weights[1]))
#     print(out_layer)
#     #epoch errror
#     out_error = out_data - out_layer
#
#     print('error: {}'.format(np.mean(np.abs(out_error))))
#
#     d_out_layer = out_error * sigmoid_deriv(out_layer)
#     hid_error = d_out_layer.dot(nn.weights[1].T)
#
#     d_hid = hid_error * sigmoid_deriv(hid_layer)
#
#     nn.weights[1] += hid_layer.T.dot(d_out_layer)
#     nn.weights[0] += in_layer.T.dot(d_hid)
#



