'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('2d_img.png')
img = img[:,:,0] # to grayscale
'''
import numpy as np
import matplotlib.pyplot as plt

for frame_size in list(range(50))+list(range(48,0,-1)):

    size = 100
    img = np.zeros( (size, size) )
    # frame_size = 10
    img[frame_size:size-frame_size, frame_size:size-frame_size] = 1
    '''
    print('img.shape =', img.shape)
    plt.imshow(img)
    plt.title('original img')
    plt.show()
    '''
    # fft2 with img

    img_fft = np.fft.fft2(img)
    img_fft = np.fft.fftshift(img_fft)
    # Add 1e-6 to avoid divide by zero problems.
    img_fft = np.log( np.abs(img_fft) + 1e-12 )
    img_fft -= np.min(img_fft)

    plt.clf() # clean old frame
    plt.imshow(img_fft)
    plt.title('fft img with frame_size = '+str(frame_size))
    # plt.show()
    plt.pause(0.1)
