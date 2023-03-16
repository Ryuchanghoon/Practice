import cv2

src = cv2.imread('Lenna.png')

dst = cv2.split(src) # 단일 채널을 분리

print(type(dst)) # tuple 
print(type(dst[0])) # ndarray -> Blue
print(type(dst[1])) # ndarray -> Green
print(type(dst[2])) # ndarray -> Red

cv2.imshow('blue', dst[0]) ## blue
cv2.imshow('green', dst[1]) ## green
cv2.imshow('red', dst[2]) ## red

cv2.waitKey()
cv2.destroyAllWindows()