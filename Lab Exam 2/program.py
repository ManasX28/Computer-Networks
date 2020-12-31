queue = list(map(int, input("Enter the packet sizes as space separated numbers: ").split(" ")))

out_rate = 42

storage = 0

max_storage = 400

i = 0

while queue:

    print("Packet number "+str(i)+", Packet size = "+str(queue[-1]))

    storage = queue[-1]

    if storage > max_storage:

	    print("Overflowed")

	    break

    if queue[-1] < out_rate:

        storage = 0

        x = queue.pop()

        print("Bucket output successfull")

        i += 1

        print("Last "+str(x)+" bytes sent")

    elif queue[-1] > out_rate:

        storage -= out_rate

        print("Bucket output successfull")

        print("Last "+str(out_rate)+" bytes sent")

        queue[-1] -= out_rate

    else:

        queue.pop()

        print("Bucket output successfull")

        print("Last "+str(out_rate)+" bytes sent")

        i+=1