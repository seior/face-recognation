from subprocess import call

print("[1] initialize project")
call(['python', 'init.py'])

print("[2] take image sample")
call(['python', 'take_sample.py'])

print("[3] train model")
print("[3] waiting for train model...")
call(['python', 'train_image.py'])

print("[4] start to recognize")
print("[4] recognize")
call(['python', 'face_recognation.py'])

print("done")