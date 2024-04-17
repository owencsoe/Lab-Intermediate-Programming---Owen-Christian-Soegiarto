temp=40
message_toohot= "weather is too hot, better stay home"
message_hot= "keep in mind of weather hot"
message_good= "let's go out and enjoy the good weather!"
if temp > 40:
    print(message_toohot)
else:
    if temp < 33:
        print (message_good)
    else:
        print(message_hot)

