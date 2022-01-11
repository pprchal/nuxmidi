import mido
import time
from collections import deque

print(mido.get_output_names()) # To list the output ports
print(mido.get_input_names()) # To list the input ports

inport = mido.open_input('NUX MIGHTY LITE MIDI:NUX MIGHTY LITE MIDI Bluetooth 128:0')
outport = mido.open_output('NUX MIGHTY LITE MIDI:NUX MIGHTY LITE MIDI Bluetooth 128:0')


msglog = deque()
echo_delay = 2

drumOn = mido.Message('control_change', channel=0, control=122, value=127, time=0)
styleOD = mido.Message('control_change', channel=0, control=75, value=1, time=0)
drumSamba = mido.Message('control_change', channel=0, control=123, value=9, time=0)


outport.send(styleOD)
outport.send(drumOn)
outport.send(drumSamba)
## control_change channel=0 control=122 value=127 time=0

while True:
    msg = inport.receive()
    if msg.type != "clock":
        print(msg)
        msglog.append({"msg": msg, "due": time.time() + echo_delay})
    # while len(msglog) > 0 and msglog[0]["due"] <= time.time():
    #     outport.send(msglog.popleft()["msg"])