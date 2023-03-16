import cv2
src = cv2.imread('Lenna.png')

b,g,r = cv2.split(src) #영상 3채널로 분리 한 다음에
dst = cv2.merge([b, g, r]) # 다시 하나로 병합. merge함수.

print(type(dst)) # 타입은 아까랑 똑같이 ndarray
print(dst.shape) # 512, 512, 3배열

cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()