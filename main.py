from subprocess import call

print("[ Initialize Project ] Intialize project")
call(['python', 'init.py'])

print("[ Take Sample ] Take image sample")
call(['python', 'take_sample.py'])

print("[ Train Image ] Train models")
print("[ Train Image ] Waiting for train model")
call(['python', 'train_image.py'])
print("[ Train IMage ] Finish train model")

print("[ Face Recognation ] start to recognize")
print("[ Face Recognation ] recognize")
call(['python', 'face_recognation.py'])

print("[ Face Recognation ] Finish recognize")